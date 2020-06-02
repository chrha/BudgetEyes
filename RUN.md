# How to setup the app:

## Install python >3.6
## Install nodejs@latest

## Install pipenv:

> `pip install pipenv`

## Install dependencies:

> `cd path/to/tddd27`  
> `pipenv install --dev`
> `cd frontend`
> `npm install`

## Add stocks to database:

> `cd Budgeteyes/scripts`
> `python stock_to_json.py`
> `cd ..`
> `./manage.py loaddata stocks.json`
 

# How to run the app:

## In one terminal:

> `cd BudgetEyes`  
> `pipenv run python manage.py runserver`

## In another terminal: 

> `cd frontend` 
> `npm run serve`
