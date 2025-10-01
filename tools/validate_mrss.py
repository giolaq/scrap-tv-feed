#!/usr/bin/env python3
"""
Validate MRSS feed structure and required elements
"""
import xml.etree.ElementTree as ET
import sys

def validate_mrss(feed_path):
    try:
        tree = ET.parse(feed_path)
        root = tree.getroot()
        
        print("🔍 MRSS Feed Validation")
        print("=" * 40)
        
        # Check RSS structure
        if root.tag != "rss":
            print("❌ Root element should be <rss>")
            return False
        print("✅ Valid RSS root element")
        
        # Check version
        version = root.get("version")
        if version != "2.0":
            print(f"⚠️  RSS version is {version}, expected 2.0")
        else:
            print("✅ RSS version 2.0")
        
        # Check Media RSS namespace
        namespaces = root.attrib
        media_ns = None
        for attr, value in namespaces.items():
            if "media" in attr and value == "http://search.yahoo.com/mrss/":
                media_ns = value
                break
        
        if media_ns:
            print("✅ Media RSS namespace declared")
        else:
            print("❌ Missing Media RSS namespace")
            return False
        
        # Check channel
        channel = root.find("channel")
        if channel is None:
            print("❌ Missing <channel> element")
            return False
        print("✅ Channel element found")
        
        # Check required channel elements
        required_channel = ["title", "description", "link"]
        for elem in required_channel:
            if channel.find(elem) is None:
                print(f"❌ Missing required channel element: {elem}")
                return False
        print("✅ Required channel elements present")
        
        # Check items
        items = channel.findall("item")
        print(f"✅ Found {len(items)} feed items")
        
        if len(items) == 0:
            print("❌ No items found in feed")
            return False
        
        # Validate first few items
        media_elements_found = 0
        for i, item in enumerate(items[:3]):  # Check first 3 items
            print(f"\n📺 Validating item {i+1}:")
            
            # Check basic item elements
            title = item.find("title")
            desc = item.find("description")
            guid = item.find("guid")
            
            if title is not None:
                print(f"  ✅ Title: {title.text[:50]}...")
            else:
                print("  ❌ Missing title")
            
            if desc is not None:
                print(f"  ✅ Description present ({len(desc.text)} chars)")
            else:
                print("  ❌ Missing description")
            
            if guid is not None:
                print(f"  ✅ GUID: {guid.text}")
            else:
                print("  ❌ Missing GUID")
            
            # Check media elements (need to handle namespace)
            media_content = None
            media_thumbnail = None
            media_title = None
            
            for child in item:
                if child.tag.startswith("{http://search.yahoo.com/mrss/}") or "media:" in child.tag:
                    media_elements_found += 1
                    if "content" in child.tag:
                        media_content = child
                    elif "thumbnail" in child.tag:
                        media_thumbnail = child
                    elif "title" in child.tag:
                        media_title = child
            
            if media_content is not None:
                url = media_content.get("url")
                content_type = media_content.get("type")
                duration = media_content.get("duration")
                print(f"  ✅ Media content: {content_type}, {duration}s")
            else:
                print("  ❌ Missing media:content")
            
            if media_thumbnail is not None:
                thumb_url = media_thumbnail.get("url")
                print("  ✅ Media thumbnail present")
            else:
                print("  ❌ Missing media:thumbnail")
        
        print(f"\n📊 Summary:")
        print(f"  • Total items: {len(items)}")
        print(f"  • Media elements found: {media_elements_found}")
        print(f"  • Average media elements per item: {media_elements_found/len(items):.1f}")
        
        if media_elements_found > 0:
            print("✅ MRSS feed validation passed!")
            return True
        else:
            print("❌ No media elements found - not a valid MRSS feed")
            return False
            
    except ET.ParseError as e:
        print(f"❌ XML Parse Error: {e}")
        return False
    except Exception as e:
        print(f"❌ Validation Error: {e}")
        return False

if __name__ == "__main__":
    feed_path = sys.argv[1] if len(sys.argv) > 1 else "feed.xml"
    success = validate_mrss(feed_path)
    sys.exit(0 if success else 1)
