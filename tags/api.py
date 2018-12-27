import requests
from django.conf import settings


# https://www.flickr.com/services/api/misc.urls.html
class FlickrAPI(object):
    API_KEY = settings.FLICKR_PUBLIC_KEY
    URL = "https://api.flickr.com/services/rest/"
    METHOD = "flickr.photos.search"
    images_info = []
    per_page = 6

    def __init__(self, tag, current_page):
        try:
            r = requests.get(
                f'{self.URL}?method={self.METHOD}&api_key={self.API_KEY}&tags={tag}&per_page={self.per_page}&page={current_page}&format=json&nojsoncallback=1')
            self.images_info = r.json()
        except TypeError:
            self.images_info = []

    # https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg
    def constructed_urls(self):
        images = [f"https://farm{image.get('farm')}.staticflickr.com/{image.get('server')}/{image.get('id')}_{image.get('secret')}.jpg"for image in self.images_info.get('photos')['photo']]

        return images