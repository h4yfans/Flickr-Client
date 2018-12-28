# Flickr Client App | Hipo Backend Ödevi

The application allows you to search photos by tag.

You have to **logged in** if you want to save your favorite photos and previous search history.

# Installation
Clone the repository and create a virtual environment with **pipenv**

    $ git clone git@github.com:h4yfans/Flickr-Client.git
	$ cd Flickr-Client
	$ pipenv install
	$ pipenv shell
	
If you are not using **pipenv**, type:

    $ pip install -r requirements.txt
	
After installed all packages, you have to migrations and create superuser
		

    python manage.py migrate
    python manage.py createsuperuser
    

### Project settings

You don't have to set `API` keys or `EMAIL HOST`. Because `settings` has separate environment folder as `dev.py` and `prod.py`

You just need to set `DJANGO_SETTINGS_MODULE`, see:

`export DJANGO_SETTINGS_MODULE=flickrproject.settings.dev`

Run project

    python manage.py runserver

   
