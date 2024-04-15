## How I learned Django

##### Steps to start a new project
1)  
`python3 --version` - to check python version (update if necessary)   
`pip3 --version` - to check pip version (update if necessary)  

2)  
`pip3 install pipenv` - to install pipenv (for dependency packages management)  

3)  
`mkdir project_name` - to create a new project directory  
`cd project_name` - to navigate to the project directory  

4)  
`pipenv install django` - to install django in the project directory  

..if `pipenv` is not found, add the following to the `~/.zshrc` file:  
`python3 -m site --user-base` - this will output a path. Append /bin to this path.
`echo 'export PATH="<your-directory-path>:$PATH"' >> ~/.zshrc` - Replace <your-directory-path> with the path from precious step  
`source ~/.zshrc` - to update the shell  

`pipenv install django` will output the path to the virtual environment created:  
```bash
...
✔ Successfully created virtual environment!
Virtualenv location: /home/sbocanci/.local/share/virtualenvs/django_tuto-SIq5Ifcc
...
```
This path can also be retrieved by running `pipenv --venv`.  

If working in vscode it is recommended to use the `pipenv` virtual environment created above..  
In `command palette` (Ctrl+Shift+P) type `Python: Select Interpreter` and select the environment with the path from above.. or use the `Add Interpreter` option to add a new one with the path from above + `/bin/python` in the end: `/home/sbocanci/.local/share/virtualenvs/django_tuto-SIq5Ifcc/bin/python`.  

At this point `pipenv` created a virtual environment and installed django in it.  
We can go inside that virtual environment directory to explore the `bin` directory:    
`cd /home/sbocanci/.local/share/virtualenvs/django_tuto-SIq5Ifcc`  

Also in the project directory, we can see the `Pipfile` and `Pipfile.lock` files.  
All other `.py` are the django files, considered as modules.  

5)  
Now we activate the virtual environment specific to the project, not the global one:  
`pipenv shell` - to activate the virtual environment in the project directory (normally ther will be a `(project_name)` prefix in the terminal before the prompt).  
`deactivate` - to deactivate the virtual environment.  

6)  
`django-admin` - to see the django-admin commands.  
`django-admin startproject project_name .` - to create a new django project in the current directory. This will be the core project directory.    

Created `manage.py` file is the entry point to the project. It is used to run the server, create migrations, etc.  
The following commands shall be run in the project directory and with the virtual environment activated (step 5).

7)  
`python manage.py runserver` - to start the server. Also we can specify the port: `python manage.py runserver 8080`, by default it will run on port 8000.    
First run will show the warning about unapplied migrations.. to fix this we run:  
`python manage.py migrate` - to apply the migrations.  
Also the second to the last line will show the link to our webapp page: `http://127.0.0.1:8000/`  

##### Creating a new app in the project directory  

in `settings.py` file, in the `INSTALLED_APPS` list, we can add new apps. Each app provides a certain functionality.    
```python
INSTALLED_APPS = [
	'django.contrib.admin', # for admin panel, managing data, users, groups, etc.
	'django.contrib.auth', # for authentication of users
	'django.contrib.contenttypes', # for content types
	'django.contrib.sessions', # for session management, managing users' data. Not used anymore, can be removed.
	'django.contrib.messages', # for displaying one time messages to users
	'django.contrib.staticfiles', # for static files (img, css, js) ets.
]
```
We can create a new app in the project directory with the following command:  
`python manage.py startapp app_name` - to create a new app in the project.  

Note that every django app has exact same structure. Usually it is a directory with the same name as the app. Inside there is another directory `migration` (used for generating databes tbles) and a files:  
`__init__.py` - is an empty file that tells python that this directory is a package.   
`admin.py` - this is where the admin panel is configured. Defines how the admin panel will look like.     
`apps.py` - this is where the app configuration is stored. The name `apps` is a bit misleading, it could be named `config.py`.  
`models.py` - this is where the database models are defined. Created classes will be used to pull out data from the database to present to users.    
`tests.py` - this is where the tests are defined. Unit tests, integration tests, etc.  
`views.py` - this is where the views are defined. Views are the functions that take a web request and return a web response. This file controls the requests and responses.  

Once the app is created it is necessary to add it to `settings.py` module/file in the `INSTALLED_APPS` list.  
```python
INSTALLED_APPS = [
	...
	'<app_name>',
]
```

##### views.py & urls.py
This is where the views are defined. Views are the functions that take a web request and return a web response. This file controls the requests and responses. e.g.:    
```python
from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
	return HttpResponse('Hello, World!')
```

In the APP DIRECTORY `<app_name>` we create the `urls.py`. This file will define the URL patterns. This is where we map the URL to the views. e.g.:  
```python
from django.urls import path
from . import views

urlpatterns = [
	path('app_name_test/hello/', views.say_hello)
]
```  
..this also needs to be added to the main `urls.py` configuration file of the project directory `<project_name>`.  
That `urls.py` file exsit in the project directory once the project is created. Inside there are some guides on how to add the app urls as well.  
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
	path('app_name_test/', include('app_name.urls')) # first argument is the URL pattern, second is the app urls that shall handle the request 
]
```  
..once ths is done, it is not necessary to indicate the `app_name` in the `urls.py` file of the app directory. Also the `/` shall be always added at the end of the URL pattern.  
```python
from django.urls import path
from . import views

urlpatterns = [
	path('hello/', views.say_hello)
]
```  
The client shall see the `Hello, World!` message when navigating to `http://127.0.0.1/app_name/hello/`.  







