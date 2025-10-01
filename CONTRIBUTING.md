# Contributing to scrap-tv-feed 🎬

Thanks for your interest in contributing! This project aims to provide realistic sample data for app development.

## 🎯 What We're Looking For

- **Bug fixes** in the catalog structure or metadata
- **New platform examples** (additional frameworks, etc.)
- **Documentation improvements**
- **Tooling enhancements** for catalog generation
- **More absurd content ideas** (with proper implementation)

## 🚫 What We're NOT Looking For

- Real copyrighted content
- Offensive or inappropriate material
- Breaking changes to the catalog schema without discussion
- Large binary files without proper justification

## 📝 How to Contribute

### Reporting Issues
1. Check existing issues first
2. Use the issue templates when available
3. Include platform/framework details if relevant
4. Provide sample code when reporting integration problems

### Adding Platform Examples
1. Create a new file in `/examples/`
2. Follow the naming pattern: `platform-language-example.ext`
3. Include comprehensive comments
4. Show both basic usage and advanced filtering
5. Test your example before submitting

### Improving Documentation
- Fix typos and unclear explanations
- Add missing platform instructions
- Improve code examples
- Update badges and links

## 🔧 Development Setup

### Prerequisites
- Python 3.7+ (for catalog generation tools)
- `exiftool` (for metadata management)
- `ffprobe` (for video duration extraction)

### Local Development
```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/scrap-tv-feed.git
cd scrap-tv-feed

# Install Python dependencies (if modifying tools)
pip install -r requirements.txt

# Validate catalog structure
python tools/validate_catalog.py

# Test catalog generation
python tools/organize_tv_feed.py --help
```

## 📋 Submission Guidelines

### Pull Request Process
1. **Fork** the repository
2. **Create a feature branch** from `main`
3. **Make your changes** with clear, descriptive commits
4. **Test thoroughly** - ensure catalog.json remains valid
5. **Update documentation** if you're changing functionality
6. **Submit a pull request** with a clear description

### Commit Message Format
```
type(scope): brief description

Longer explanation if needed

- Bullet points for multiple changes
- Reference issues with #123
```

**Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

**Examples:**
- `feat(examples): add React Native integration example`
- `fix(catalog): correct duration for cereal-streamz`
- `docs(readme): improve Android setup instructions`

### Code Style
- **JavaScript/TypeScript**: Follow Prettier defaults
- **Python**: Follow PEP 8
- **Kotlin**: Follow Android Kotlin style guide
- **Comments**: Explain the "why", not the "what"

## 🧪 Testing

### Catalog Validation
Before submitting changes to `catalog.json`:
```bash
# Validate JSON structure
python -m json.tool catalog.json > /dev/null

# Check required fields
python tools/validate_catalog.py

# Test with your platform
# (include test results in PR description)
```

### Example Testing
- Ensure all code examples compile/run
- Test with the actual catalog URL
- Verify error handling works
- Check performance with full dataset

## 📚 Adding New Content

### Content Guidelines
- Keep it **family-friendly** but absurd
- **Original concepts only** - no copyrighted material
- Maintain the **silly/satirical tone**
- Ensure **metadata consistency**

### Content Creation Process
1. **Propose the concept** in an issue first
2. **Create placeholder assets** (can be simple/generated)
3. **Write compelling descriptions**
4. **Add appropriate metadata** (ratings, genres, etc.)
5. **Update catalog generation tools** if needed

### Metadata Requirements
- Realistic but not real ratings/view counts
- Appropriate content ratings for the concept
- Consistent release years (2018-2024)
- Proper genre classification
- Engaging descriptions without copyright issues

## 🎨 Asset Guidelines

### Video Requirements
- **Format**: MP4 (H.264)
- **Resolution**: 1920x1080 preferred
- **Duration**: 5-15 seconds for samples
- **Size**: Keep under 10MB per file
- **Content**: Original, non-copyrighted material only

### Image Requirements
- **Format**: JPG
- **Dimensions**: 1920x1080 (16:9 aspect ratio)
- **Size**: Keep under 500KB
- **Quality**: High enough for app previews

## 🏷️ Metadata Standards

### Required Fields
All shows must include:
- Unique `id` (slug format)
- Descriptive `title` and `description`
- Appropriate `content_rating`
- Realistic `rating_stars` (3.0-5.0)
- Valid `genres` array
- Proper `category` assignment

### Optional Enhancements
- Season/episode information for series
- Cast/crew details (fictional)
- Awards or recognition (fictional)
- Related content suggestions

## 🤝 Community Guidelines

### Be Respectful
- Constructive feedback only
- Help newcomers learn
- Celebrate creative contributions
- Keep discussions on-topic

### Stay Professional
- No spam or self-promotion
- Respect maintainer decisions
- Follow GitHub's community guidelines
- Keep content appropriate for all audiences

## 📞 Getting Help

- **Questions**: Open a GitHub Discussion
- **Bugs**: Create an issue with the bug template
- **Features**: Propose in GitHub Discussions first
- **Security**: Email maintainers directly

## 🎉 Recognition

Contributors will be:
- Listed in the README acknowledgments
- Credited in release notes for significant contributions
- Invited to help maintain the project (for regular contributors)

---

**Remember**: This project exists to help developers build amazing experiences. Every contribution, no matter how small, helps the community! 🚀
