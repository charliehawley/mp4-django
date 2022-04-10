# Wisecrack

Wisecrack is a place for friends to meet and compete for upvotes. In this quirky quiz-style game, prompts are given and the users are encouraged to go wild. Wisecrack requires a broad imagination and is sure to test your wit. <br>
See how many votes you can garner on [Wisecrack](https://wisecrack-django.herokuapp.com/).

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