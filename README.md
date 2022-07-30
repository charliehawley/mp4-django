# Wisecrack

Wisecrack is a place for friends to meet and compete for upvotes. In this quirky quiz-style game, prompts are given and the users are encouraged to go wild. 
Wisecrack requires a broad imagination and is sure to test your wit. <br>
See how many votes you can garner on [Wisecrack](https://wisecrack-django.herokuapp.com/).
![responsive design on a variety of screens](/doc_media/amiresponsive.jpg)

## Index

- 	[title](#header)
- 	[User Stories](#user-stories)
- 	[Features](#features)

## UI / UX
### User Stories

- As a user, I want to play a word game against other users.
- As a user, I want to vote on my favourite submissions and contribute to the leaderboards.
- As a user, I want to have a profile on the website so that my submissions will be associated with me.
- As a user, I want to be able to manage my submissions, to edit and delete them as well as submit them. I want these changes reflected to me immediately.

- As an admin, I need access to an admin panel to create and edit prompts for users to respond to.
- As an admin, I want to restrict core functions, like submitting and voting, to authenticated users only.
- As an admin, I want to restrict the number of upvotes a user can give to each submission.
- As an admin, I want to restrict users from voting on their own submissions.

### Design
#### Typography

IM Fell DW Pica - This font was used as the default font style for the site. The printed serif look gave an impression of permanence and authority whilst retaining an air of levity in it's uncanny representation of written prompts.

Kalam - This font was used explicitly for user submissions. The cursive nature lends itself to content created by users by virtue of a contrast with the authoritative IM Fell DW Pica, as if the user had scribbled it themselves.

#### Colours

The background for all pages of the website was provided by https://csshero.org/mesher/<br>
This soft but vibrant gradient with randomly placed origins is intended to give the site a feeling of levity and nebulous possibility, representing the site's intended function: to encourage users to address prompts with responses plucked from the ether.

## Features

- ### Collapsible Nav Bar
The responsive nav bar appears consistent across the site and collapses on smaller screens into a hamburger menu.
Authenticated users will find the navigation list populated with 'Home, My Subs, and Logout.' 
Users who haven't yet logged in or registered will find the list populated with 'Home, Login, and Register.'
![navbar not authorised](/doc_media/nav1.jpg)
![navbar authorised](/doc_media/nav2.jpg)
![navbar mobile](/doc_media/nav_mob.jpg)

- ### Landing page
Immediately, visitors are made aware of the purpose and function of the website through copy text. 
This is accompanied by a number of cards which represent the active prompts available to browse.

![landing page](/doc_media/landing.jpg)

- ### Prompt Details page
Users who follow the links in the prompt cards will be presented with a prompt card followed by a list of submissions.
Only authenticated users will have the opportunity to vote on submissions that they like and will also be able to submit a response of their own through a form.

![prompt detail page authorised](/doc_media/prompt_detail_auth.jpg)
<br><br>
Users who aren't authenticated will not see upvote buttons or a submissions form and will instead be urged to login or register.

![prompt detail page not authorised](/doc_media/prompt_detail_noauth.jpg)

- ### My Subs page
Authenticated users can navigate to a page hosting all of their submissions, where they are presented with the opportunity to edit or delete their submissions.

![user submissions page](/doc_media/my_subs.jpg)

- ### Login/Register pages
Users can register using forms with validation on usernames and matching passwords.
Messages are thrown for success and failure.

## Future Features
- Message for attempt at upvoting user's own submission.
- Restrict user from submitting multiple submissions per prompt to avoid user's monopolising a prompt.
- More intuitive link content. Prompts should have titles in their models to give context to users.
- It would be more engaging to have timers implemented on prompts so that submission state can finish at a set date/time.
- Submissions on prompt details page could be ordered by upvotes, creating a leaderboard-style layout. Users can see 'the one to beat.'
- Email notifications for when your submission is knocked off a 'Top 3' podium.
- Avatars to more easily associate submissions to users and embolden rivalries.
- Badges applied to account for holding the top of the leaderboard at deadline.

## Testing
Python tests were set up but configured incorrectly per the following error:
``` django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.```
As a result, all testing was manual on this site. A TDD approach was adopted but undocumented.

## Prompt properties:
- Date: documents creation date to calculate active prompt's age. Future feature would remove ability to submit after predetermined deadline.
- Prompt: the content of the prompt for the users to respond to.
- Slug: auto-generated from the prompt to serve to the url hosting the prompt and relevant submissions.
- Subs list: a many to many field that records users who have submitted. Future feature would restrict submission form if current user's username features on this list.

## Submission properties: 
- Sub: the content of the submission for user's to read and vote on.
- User: a foreign key referencing the ownership of the submission.
- Upvotes: a many to many field that records the users who have upvoted this submission.
- Created on: a date field that records creation date.

## Known bugs

- Submission field remains populated after post method returns page.

## Languages
- HTML5
- CSS3
- Python

## Frameworks and Libraries
- Git
- Github
- Django
- dj_database_url
- dj allauth
- dj crispy forms
- Bootstrap
- Gunicorn
- Cloudinary

## Deployment
### Heroku
This project was deployed using Heroku, a cloud-based platform that manages apps and databases and links to your github repository for automatic deployment every time you push your code after setup.<br><br>
To create an app on Heroku, login/signup and navigate to your Heroku dashboard. Click 'New' > 'Create new app.' Define an app name, select your region and click 'Create app.'<br><br>
Now that your app is provisioned, navigate to the 'Resources' tab in the app overview. Searching 'postgres' in the resources search bar will present you with a list of results including 'Heroku Postgres.' Select 'Heroku Postgres' and select 'Hobby dev - free' from the 'Plan name' dropdown menu. Confirming these options will add Heroku Postgres management to your app.<br><br>
In the 'Settings' tab, click 'Reveal Config Vars.' You will now see a list of key/value pairs that represent your config vars in the deployed environment. Copy the url in the value field for DATABASE_URL and assign this to `os.environ["DATABASE_URL"]` in an env.py file that should be created at the top level in your virtual environment. This env.py file should be included in your gitignore file to protect your database from malicious entities.<br><br>
You will also need to set up a secret key and add this to both your env.py and your config vars in Heroku.<br>
In the env.py: `os.environ["SECRET_KEY"] = "someSecretKey"`<br><br>
In Heroku config vars: SECRET_KEY, someSecretKey<br><br>
You will now want to write some code to tell the browser where to find these environment variables depending on the current method of deployment.<br><br>
In settings.py: 
```
import os
import dj_database_url
if os.path.isfile('env.py'):
    import env
```
<br><br>
Currently your SECRET_KEY, as assigned automatically in your settings.py, is insecure. You should replace the value of SECRET_KEY thusly: `SECRET_KEY = os.environ.get('SECRET_KEY')`
<br><br>
You will then need to set up your database to use Heroku's postgres database when in the deployed environment and sqlite when running locally. In the settings.py file, replace your current database configuration with the following:
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```
Add Heroku to your list of allowed hosts as well as localhost so you can continue running your app in the dev environment:
`ALLOWED_HOSTS = ['appname.herokuapp.com', 'localhost']`<br>
Now add a Procfile to your project and include `web: gunicorn appname.wsgi` to tell Heroku to expect http traffic and allow python to integrate with Heroku.
Finally, remember to set DEBUG to False in your settings.py to protect your app from malicious entities and hide data you do not wish to share.

### CDN
Django is not configured to serve static files. Your media and stylesheets will need to be stored on a content delivery network. Here we have used Cloudinary.<br><br>
Login/signup to Cloudinary and navigate to your dashboard and copy your API Environment Variable (a url assignment).<br><br>
Return to your env.py file and assign `os.environ["CLOUDINARY_URL"] = "your cloudinary API Environment Variable"` remembering to remove the assignment and leave only the url.<br><br>
Again, you will need to reflect this in your deployed environment by adding CLOUDINARY_URL and the url you've copied to the config vars in the Heroku settings panel. If you have disabled COLLECTSTATIC in your Heroku environment, remember to remove this when you deploy your app.<br><br>
You will then need to update your settings.py to include configuration for cloudinary by adding the following:
```
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```
And then adding 'cloudinary_storage' and 'cloudinary' (either side of 'django.contrib.staticfiles' respectively) to the list of installed apps.

You are now deployed.

## Resources

- Getbootstrap documentation
- Stack Overflow:
    - Return only digits from variables
    - Endless resources on how to manage views and return reverse statemnets in particular
- Django documentation