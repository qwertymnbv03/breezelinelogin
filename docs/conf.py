project = 'spypoint-login'
author = 'spypoint-login'
release = '1.0'

# Extensions
extensions = [
    'sphinx_sitemap',
]

# Paths
templates_path = ['_templates']
exclude_patterns = []

# Theme
html_theme = 'alabaster'
html_static_path = ['_static']

# Custom JS & Favicon
html_js_files = ['chatbot.js']  # chatbot widget
html_favicon = '_static/favicon.png'

# Google & Bing Verification Meta Tags
html_context = {
    "meta_tags": """
    <meta name="google-site-verification" content="YOUR_GOOGLE_CODE" />
    <meta name="msvalidate.01" content="YOUR_BING_CODE" />
    """
}

# Base URL for sitemap
html_baseurl = 'https://breezelinelogin.readthedocs.io/'


# Ensure robots.txt is copied to root
html_extra_path = ['_static/robots.txt']
