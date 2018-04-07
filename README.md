# djrfw_social_oauth2_demo
Example for using djangorestframework and Social Oauth2

This demo uses [Django rest-framework Social Oauth2](https://github.com/RealmTeam/django-rest-framework-social-oauth2) for social authentication with [Django-Rest-Framework](http://www.django-rest-framework.org/).
Detailed explaination can be found in those two links.

# To use this demo
install packages
```pip install django djangorestframework django-rest-framework-social-oauth2 django-cors-middleware```

# Configuration
in ```_app/settings.py```
```
# Facebook configuration
SOCIAL_AUTH_FACEBOOK_KEY = '<your app id goes here>'
SOCIAL_AUTH_FACEBOOK_SECRET = '<your app secret goes here>'
# Gmail configuration
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '<your app id goes here>'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '<your app secret goes here>'
````
Replace ```<...>``` with your app id and secret.

Change the IP address in 
```
CORS_ORIGIN_WHITELIST = (
    'localhost:3000',
    '127.0.0.1:3000'
)
```
appropriately.

# Runserver
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

You can now POST your token to this django server to get the access token as shown [here](https://github.com/RealmTeam/django-rest-framework-social-oauth2#facebook-example)
