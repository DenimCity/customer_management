
1. Create a folder using mkdir
#create django project

2. django-admin startproject "name of folder"
## create virtual environemnt
3. python -m venv venv
## activate virutal environment
4. source ./venv/bin/activate
# Test that your django app works
5. python manage.py runserver
# create app
6. python manage.py startapp "name of app"
ex: python manage.py startapp accounts


after you make changes to the database
you have to do a migrate
    ```python manage.py makemigrations```
then run ```python manage.py migrate ```
