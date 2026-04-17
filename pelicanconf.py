AUTHOR = 'Kian Wee Chen'
SITENAME = 'Designing with Computers'
SITEURL = ""

THEME = 'themes/dwc_bootstrap5' # default was 'notmyidea'

PATH = "content"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = True  # default was False
SLUGIFY_SOURCE = 'basename'  # default was 'title'

INDEX_SAVE_AS = '/blogs/index.html'  # default was 'index.html'
ARTICLE_PATHS = ['blogs']  # default was ['']
PAGE_PATHS = ['pages', 'cv', 'research', 'educational', 'pelican_tutorial']  # default was ['pages']

USE_FOLDER_AS_CATEGORY = False  # default was True
PATH_METADATA = r'(?P<path_no_ext>.*)\..*'  # default was ''
ARTICLE_URL = '{path_no_ext}.html'  # default was '{slug}.html'
PAGE_URL = '{path_no_ext}.html'  # default was 'pages/{slug}.html'
ARTICLE_SAVE_AS = '{path_no_ext}.html'  # default was '{slug}.html'
PAGE_SAVE_AS = '{path_no_ext}.html'  # default was 'pages/{slug}.html'

ARCHIVES_SAVE_AS = False
DISPLAY_CATEGORIES_ON_MENU = False

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

MENUITEMS = (
    ("Home", f"{SITEURL}/", "item"),
    ("Blog", f"{SITEURL}/blogs/", "item"),
    ("Research", f"{SITEURL}/research/", "dropdown"),
    ("Educational", f"{SITEURL}/educational/", "dropdown"),
    ("About", f"{SITEURL}/pages/about.html", "item"),
)

# pelican-seo variable
SEO_REPORT = True  # SEO report is enabled by default
SEO_ENHANCER = True  # SEO enhancer is disabled by default
SEO_ENHANCER_OPEN_GRAPH = True # Subfeature of SEO enhancer
SEO_ENHANCER_TWITTER_CARDS = False # Subfeature of SEO enhancer

# variable specific to this theme
NAVBAR_BRAND_IMAGE = 'images/logo.svg' # the logo used for the index.html landing page
NAVBAR_BRAND_IMAGE_NON_LANDING = 'images/logo_non_landing.svg' # the logo used for other pages
NAVBAR_LOGO_WIDTH = 300 # theme solo_proto_workshop_bootstrap5 specific variable
PAGEFIND = True
GOATCOUNTER_URL = '<script data-goatcounter="https://designingwithcomputers.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>'