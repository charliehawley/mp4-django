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

## submission properties: 
- datetime class properties which are used to restrict multiple submissions in a single day 
- number of subs for a given prompt must be converted to a list, then length of list used to show how many subs per prompt in index.html

## upvote properties:
- upvote user id list boolean check user id presence in list to restrict user from upvoting a submission more than once.
- upvote appends user id to list[], number of upvotes = user_upvote.length()

## Known bugs

- sub field remains populated after submission

## Resources

- https://getbootstrap.com/docs/