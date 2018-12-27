# Flickr Client App | Hipo Backend Ödevi

The application allows you to search photos by tag.

You have to **logged in** if you want to save your favorite photos and previous search history.

# Installation
Clone the repository and create a virtual environment with **pipenv**

    $ git clone git@github.com:h4yfans/Hipo-Flickr-Client.git
	$ cd Hipo-Flickr-Client
	$ pipenv install
	$ pipenv shell
	
If you are not using **pipenv**, type:

    $ pip install -r requirements.txt
	
After installed all packages, you have to create migrations and superuser
		

    python manage.py migrate
    python manage.py createsuperuser
    

And then follow the steps for initialize the `FLICKR_API_KEY` and `MAIL` 

 - Go to settings.py
 - Change `FLICKR_API_KEY` to *Hipo's Public Key* `1ddb7df62cbdc4e07f6ec75ca78e2960` or change your `os.environ`
 - Once you change you API key for Flickr, next you should add your `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` for password reset.

Run project

    python manage.py runserver

   
