# Django settings for webapp project.
import sys
import platform

                   
if platform.node() == "ELIJOT":
    APPLICATION_URL = 'http://localhost:8000'
    APPLICATION_ROOT = 'F:\\www\\i2a_2\\webapp'
    DEBUG = True
else:
    APPLICATION_URL = 'http://web.i2asolutions.com'
    APPLICATION_ROOT = '/var/sites/i2awebsite-dev/webapp'
    DEBUG = False

TEMPLATE_DEBUG = DEBUG

sys.path.append('%s/apps' % APPLICATION_ROOT)
sys.path.append('%s/libs' % APPLICATION_ROOT)

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '%s/database.db' % APPLICATION_ROOT,          # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'America/Los_Angeles'

LANGUAGE_CODE = 'en'

gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
    ('pl', gettext('Polski')),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

MEDIA_ROOT = '%s/site_media' % APPLICATION_ROOT
MEDIA_URL = '/site_media/'
ADMIN_MEDIA_PREFIX = '/media/'
APPEND_SLASH = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'o@(yg%(-mdf@rph0-3sy&q&r2!+n%qrlu*jr$47302+9w!z6+2'

CMS_TEMPLATES = (
        ('base_home.html', gettext('home')),
        ('base_simple.html', gettext('simple')),
        ('base_twocolumns.html', gettext('twocolumns')),
        ('base_contact.html', gettext('contact_form')),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
        "django.contrib.auth.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.request",
        "cms.context_processors.media",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
)

ROOT_URLCONF = 'webapp.urls'

TEMPLATE_DIRS = ( "%s/templates" % APPLICATION_ROOT )


CMS_SOFTROOT = True
CMS_CONTENT_CACHE_DURATION = 1
CMS_USE_TINYMCE = True
#TINYMCE_FILEBROWSER = False

TINYMCE_DEFAULT_CONFIG = {
    'mode': "textareas",
    'theme': "advanced",
    'language': "en",
    'skin': "o2k7",
    'browsers': "gecko",
    'dialog_type': "modal",
    'object_resizing': True,
    'cleanup_on_startup': True,
    'forced_root_block': "p",
    'remove_trailing_nbsp': True,
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_statusbar_location': "none",
    'theme_advanced_buttons1': "formatselect,bold,italic,underline,bullist,numlist,undo,redo,link,unlink,image,code,fullscreen,pasteword,media,charmap",
    'theme_advanced_buttons2': "",
    'theme_advanced_buttons3': "",
    'theme_advanced_path': False,
    'theme_advanced_blockformats': "p,h1,h2,h3,h4,h5,h6",
    'width': '100%',
    'height': '200',
    'plugins': "advimage,advlink,fullscreen,visualchars,paste,media,template,searchreplace",
    'advlink_styles': "internal (sehmaschine.net)=internal;external (link to an external site)=external",
    'advimage_update_dimensions_onchange': True,
    'relative_urls': False,
    'valid_elements': "" +
    "-p," +
    "a[href|target=_blank|class]," +
    "-strong/-b," +
    "-em/-i," +
    "-u," +
    "-ol," +
    "-ul," +
    "-li," +
    "br," +
    "img[class|src|alt=|width|height]," +
    "-h1,-h2,-h3,-h4," +
    "-pre," +
    "-code," +
    "-div",
    'extended_valid_elements': "" +
    "a[name|class|href|target|title|onclick]," +
    "img[class|src|border=0|alt|title|hspace|vspace|width|height|align|onmouseover|onmouseout|name]," +
    "br[clearfix]," +
    "-p[class<clearfix?summary?code]," +
    "h1[class<clearfix],h2[class<clearfix],h3[class<clearfix],h4[class<clearfix]," +
    "ul[class<clearfix],ol[class<clearfix]," +
    "div[class],"
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    #'django.contrib.messages',
    'django.contrib.sitemaps',
    'tinymce',
    'cms',
    'cms.plugins.text',
    'cms.plugins.picture',
    'cms.plugins.link',
    'cms.plugins.file',
    'cms.plugins.snippet',
    'cms.plugins.googlemap',
    'cms.plugins.teaser',
    'mptt',
    'publisher',
    'reversion'
)

CACHE_BACKEND = 'locmem://'
GOOGLE_MAPS_API_KEY = 'ABQIAAAAeYdkrvcHC7_L2VlgMmesdBSCosKOIM1bMMBAEnWIcBy4h0fBrxRoBlJW_DcVkFub1AfgGJkj7XXipQ'
