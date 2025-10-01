#!/usr/bin/env python3
"""
Generate MRSS (Media RSS) feed from catalog.json
Based on Yahoo Media RSS specification: https://www.rssboard.org/media-rss
"""
import json
import sys
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

def generate_mrss(catalog_path, base_url=""):
    with open(catalog_path) as f:
        catalog = json.load(f)
    
    # Create RSS root with Media RSS namespace
    rss = Element("rss", version="2.0")
    rss.set("xmlns:media", "http://search.yahoo.com/mrss/")
    rss.set("xmlns:dcterms", "http://purl.org/dc/terms/")
    
    channel = SubElement(rss, "channel")
    SubElement(channel, "title").text = "Scrap TV Feed"
    SubElement(channel, "description").text = "Sample TV content for developers"
    SubElement(channel, "link").text = "https://github.com/chris-trag/scrap-tv-feed"
    SubElement(channel, "lastBuildDate").text = datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
    
    for item_data in catalog["items"]:
        item = SubElement(channel, "item")
        
        # Basic RSS fields
        SubElement(item, "title").text = item_data["title"]
        SubElement(item, "description").text = item_data["description"]
        SubElement(item, "guid").text = item_data["id"]
        SubElement(item, "category").text = item_data["category"]
        
        # Media RSS extensions
        video_url = item_data["sources"][0]["url"].replace("${base_path}", base_url)
        poster_url = item_data["images"]["poster_16x9"].replace("${base_path}", base_url)
        
        # media:content - main video
        media_content = SubElement(item, "media:content")
        media_content.set("url", video_url)
        media_content.set("type", "video/mp4")
        media_content.set("duration", str(item_data["duration_sec"]))
        
        # media:thumbnail - poster image
        SubElement(item, "media:thumbnail", url=poster_url)
        
        # media:title and media:description
        SubElement(item, "media:title").text = item_data["title"]
        SubElement(item, "media:description").text = item_data["description"]
        
        # media:category
        SubElement(item, "media:category", scheme="urn:scrap-tv:category").text = item_data["category"]
        
        # media:keywords (genres)
        if item_data["genres"]:
            SubElement(item, "media:keywords").text = ", ".join(item_data["genres"])
        
        # media:rating
        media_rating = SubElement(item, "media:rating")
        media_rating.set("scheme", "urn:simple")
        media_rating.text = str(item_data["rating_stars"])
        
        # media:credit (for content rating)
        if item_data.get("content_rating"):
            media_credit = SubElement(item, "media:credit")
            media_credit.set("role", "rating")
            media_credit.text = item_data["content_rating"]
        
        # Additional metadata
        SubElement(item, "media:copyright").text = f"© {item_data['release_year']} Scrap TV"
        
        # Trending indicator as media:restriction
        if item_data.get("trending"):
            media_restriction = SubElement(item, "media:restriction")
            media_restriction.set("type", "trending")
            media_restriction.text = "allow"
    
    # Pretty print XML
    rough_string = tostring(rss, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

if __name__ == "__main__":
    catalog_path = sys.argv[1] if len(sys.argv) > 1 else "../catalog.json"
    base_url = sys.argv[2] if len(sys.argv) > 2 else "https://raw.githubusercontent.com/chris-trag/scrap-tv-feed/main"
    
    mrss_xml = generate_mrss(catalog_path, base_url)
    print(mrss_xml)
