# Wisecrack

Wisecrack is a place for friends to meet and compete for upvotes. In this quirky quiz-style game, prompts are given and the users are encouraged to go wild. 
Wisecrack requires a broad imagination and is sure to test your wit. <br>
See how many votes you can garner on [Wisecrack](https://wisecrack-django.herokuapp.com/).

## Index

- 	[title](#header)
- 	[User Stories](#user-stories)
- 	[Features](#features)

## User stories

- As a user, I want to play a word game against other users.
- As a user, I want to vote on my favourite submissions and contribute to the leaderboards.
- As a user, I want to have a profile on the website so that my submissions will be associated with me.
- As a user, I want to be able to manage my submissions, to edit and delete them as well as submit them. I want these changes reflected to me immediately.

- As an admin, I need access to an admin panel to create and edit prompts for users to respond to.
- As an admin, I want to restrict core functions, like submitting and voting, to authenticated users only.
- As an admin, I want to restrict the number of upvotes a user can give to each submission.
- As an admin, I want to restrict users from voting on their own submissions.

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
Authenticated users will have the opportunity to vote on submissions that they like and will also be able to submit a response of their own through a form.

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
- Badges applied to account for holding the top of the leaderboard at deadline.#

## Testing
All testing was manual on this site. A TDD approach was adopted but undocumented.

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

## Resources

- Getbootstrap documentation
- Stack Overflow:
    - Return only digits from variables
    - Endless resources on how to manage views and return reverse statemnets in particular
- Django documentation