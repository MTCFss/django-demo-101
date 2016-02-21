common commands on django project develoement:

```sh
django-admin startproject PROJECT_NAME . # create a django project on current dir
python manage.py migrate                 # create database used by django
python manage.py startapp APP_NAME       # create an app
python manage.py makemigrations          # generate app migration files
python manage.py migrate                 # apply app migration files
python manage.py createsuperuser         # create superuser account
python manage.py runserver [IP:PORT]     # run server on address http://IP:PORT or http://0.0.0.0:8000
```

dejango app developement steps:

- add app name to `INSTALLED_APPS` array on `PROJECT_NAME/settings.py` file.
- add url pattern to `urlpatterns` array on `PROJECT_NAME/urls.py` file to include APP_NAME `urls.py` file.
- define view function (or class) on `APP_NAME/views.py`
- define url pattern releated to the view function on `APP_NAME/urls.py` and add `name`
- define our Databese models on `APP_NAME/models.py` based on `models.Model` class
- define `__str__` fnct for every model to have a better name
- register our models to the admin site on `APP_NAME/admin.py`
- add our templates files under `APP_NAME/templates/APP_NAME/TEMPLATE.html`

git common commands:

```sh
git add FILE_NAME1 FILE_NAME2...      # add files to staged (history tracking)
git commit -m 'message'               # save changes with message as title
git push                              # send changes to the repo (GitHub)
```