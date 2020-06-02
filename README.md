# Project for the course TDDD27 - Advanced Web Programming

# [Link to mid course screencast](https://youtu.be/nrZc5Tm-Kvg) 

# [Link to Project Screencast 06/02](https://www.youtube.com/watch?v=gxZi5-Kc6ic)

## Individual screencasts:

### [Viktor Blidh](https://youtu.be/DZAeoaPYg4I)
### [Ilian Ayoub](https://youtu.be/C5cjWka9uQg)
### [Chris Habib]()


# Specifications

## Functional specification
The vision with this project is to design a website for personal finance and budgeting.

Core functions will be the provision of budget management so that the user can have an overview of their own income and spendings.

We have also considered some form of communication between users so that tips and help can be shared.
The website will also provide stock investment features as to when to buy or sell depending on strategies that the user chooses. 

Currently the desired functionalities of this website are the following:

*  Give a logged in user a good overview of his/her economy.
*  Give an aesthetically pleasing yet easy to understand view of the stock market.
*  Provide the user with tips on when to buy/sell using currently existing algorithms.
*  Let logged in users discuss different strategies in a forum

## Technical specification

### Backend
The backend framework that the project will be built on is Django. 
We researched the differences between Flask and Django and opted for Django due to several reasons:

* Django comes with a lot of built in security measures, and since this app will handle sensitive data such as a users money security was deemed to be an important attribute. 
* The "batteries included" approach of Django means that we as developers won't have to use third-party libraries (that may not work as intended) to the same extent as if we used Flask.
* Unlike Flask, django allows developers to divide the project into multiple applications, thus making it easier to divide work between developers.  
* Although the scope of the project isn't that big, which makes a better case for flask, the developers in this project had a desire to learn Django for future use.  

To manage data we are initially going to use a sqlite database, but if the application moves from development to an actual product this may very well change. 
Other options are then PostgreSQL, MariaDB or MySQL. Django supports all of these databases. Django also comes with a built in ORM which makes it easy to send queries to the
database, and it also means that changing to another database will not require any change to our code. 


### Frontend
For the frontend we will be using Vue.js. We discussed the possibility of using React however we felt that Vue.js was more modular compared to react. 
Vue is a lightweight library and thus takes very short time to load upon rendering pages compared to other frameworks. This gives a better user experience, 
especially for users running the application on a less powerful machine like a phone. Vue still gives us the functionality we desire, more specifically it 
is very reactive, i.e it will automatically update data on a page when it changes. This will be relevant to our application since it will continuously request
stock data from external API:s, and this data must always be up to date on the webpage. Another reason for choosing Vue is the possibility to divide a page into 
several different components. Since this application will be developed by three developers work can easier be divided; one developer can work on one component while another
works on a second component. 

