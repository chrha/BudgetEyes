# Project for the course TDDD27 - Advanced Web Programming

## Functional specification
The vision with this project is to design a website for personal finance and budgeting.

Core functions will be the provision of budget management so that the user can have an overview of their own income and spendings.

We have also considered some form of communication between users so that tips and help can be shared.
The website will also provide stock investment features as to when to buy or sell depending on strategies that the user chooses. 

## Technical specification
The backend framework that the project will be built on is django. 
We researched the differences between Flask and django and considering
the scope of the project we felt that django would be a better fit, 
django being a full-stack framework while flask being a lightweight library. 
Django will not however be used for the frontend.

For the frontend we will be using Vue.js. We discussed the possibility of using React however we felt that Vue.js was more modular compared to react. 
Vue is more of a library where you import the things that you need and react requires a whole environment to develop a react app.

To manage data we decided to use a sqlite database,  where our server communicates with it using an ORM  already available to us in django.
