from flickrproject.settings.base import *

# Override base.py settings here
SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = ['h4yfans.pythonanywhere.com']
DEBUG = False
FLICKR_KEY = os.environ['PUBLIC_KEY']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
