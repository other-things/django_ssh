# django_ssh

### Overview
A webtool to access remote ssh server and display server's basic information in table format.


### Pre-request
- Python 3.7


### Install & run app locally
- Clone this repo and cd to root of this project directory
- Install dependencies
```pip install -r requirements.txt```
- Database migration
```python manage.py migrate```
- Run app on [http://localhost:8080][0]
```python manage.py runserver 8080```

### Deploy app on heroku
Files for deloy via [Heroku Cli][1] are configured.

[0]: http://localhost:8080
[1]: https://devcenter.heroku.com/articles/git