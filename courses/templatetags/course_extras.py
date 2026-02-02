"""Template filters for courses/lessons."""
import re
from django import template

register = template.Library()


@register.filter
def youtube_embed_url(url):
    """Convert YouTube watch URL to embed URL, or return as-is for other URLs."""
    if not url:
        return ''
    # youtu.be/VIDEO_ID
    m = re.search(r'youtu\.be/([a-zA-Z0-9_-]+)', url)
    if m:
        return f'https://www.youtube.com/embed/{m.group(1)}'
    # youtube.com/watch?v=VIDEO_ID
    m = re.search(r'(?:youtube\.com/watch\?v=)([a-zA-Z0-9_-]+)', url)
    if m:
        return f'https://www.youtube.com/embed/{m.group(1)}'
    # Already embed or other URL
    if 'embed' in url:
        return url
    return url
