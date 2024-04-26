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
`echo 'export PATH="<your-directory-path>:$PATH"' >> ~/.zshrc` - Replace <your-directory-path> with the path from previous step  
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
We can go inside that virtual environment directory to explore the `bin` directory (optional, if curious):    
`cd /home/sbocanci/.local/share/virtualenvs/django_tuto-SIq5Ifcc`  

Also in the project directory, we can see the `Pipfile` and `Pipfile.lock` files.  

5)  
Now we activate the virtual environment specific to the project, not the global one:  
`pipenv shell` - to activate the virtual environment in the project directory (normally ther will be a `(project_name)` prefix in the terminal before the prompt).  
`deactivate` - to deactivate the virtual environment (if/when needed).  

6)  
`django-admin` - to see the django-admin commands.  
`django-admin startproject <project_name> .` - to create a new django project in the current directory.
`django-admin startproject <project_name>` - to create a new project in the child directory `<project_name>`.  
This will be the core project directory.  

All other `.py` files inside the project dicectory are the django files, considered as modules.   

Created `manage.py` file inside the `<project_name>` directory is the entry point to the project. It is used to run the server, create migrations, etc.  
The following commands shall be run in the project directory and with the virtual environment activated (step 5).

7)  
`python manage.py runserver` - to start the server. Also we can specify the port: `python manage.py runserver 8080`, by default it will run on port 8000.    
First run will show the warning about unapplied migrations.. to fix this we run:  
`python manage.py migrate` - to apply the migrations.
!! Migrations are necessary component to manage changes to the database. Making changes to the `models` module will require to use `python manage.py makemigrations` and `python manage.py migrate` commands every time change is made to ensure the database is functioning properly.  

Also the second to the last line will show the link to our webapp page: `http://127.0.0.1:8000/`  

## Creating a new app in the project directory  

in `settings.py` file, in the `INSTALLED_APPS` list, we can add new apps. Each app provides a certain functionality. Below is the short explanation of the existing lines in the `INSTALLED_APPS` section of the `<project_name>/<project_name>/settings.py` file:      
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
1) 
We can create a new app in the project directory with the following command:  
`python manage.py startapp new_app` - to create a new app in the project.  

Note that every django app has exact same structure. Usually it is a directory with the same name as the app. Inside there is another directory `migration` (used for generating databes tbles) and a files:  
`__init__.py` - is an empty file that tells python that this directory is a package.   
`admin.py` - this is where the admin panel is configured. Defines how the admin panel will look like.     
`apps.py` - this is where the app configuration is stored. The name `apps` is a bit misleading, it could be named `config.py`.  
`models.py` - this is where the database models are defined. Created classes will be used to pull out data from the database to present to users.    
`tests.py` - this is where the tests are defined. Unit tests, integration tests, etc.  
`views.py` - this is where the views are defined. Views are the functions that take a web request and return a web response. This file controls the requests and responses.  

2) 
Once the app is created it is necessary to add it to `settings.py` module/file in the `INSTALLED_APPS` list.  
```python
INSTALLED_APPS = [
    ...
    '<new_app>',
]
```

## ABOUT `views.py` & `urls.py`

1) 
This is where the views are defined. Views are the functions that take a web request and return a web response.  
This file controls the requests and responses, `<project_name>/new_app/views.py` e.g.:    

```python
from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return HttpResponse('Hello, World!')
```

2)
Next I would like to create the link / reference from `<project_name>/<project_name>/urls.py` file in `urlpatterns` --> to the <new_app> `<project_name>/new_app/urls.py` file (which doesn't exist just yet) also in `urlpatterns`.   
So `<project_name>/<project_name>/urls.py` e.g.:
  
```python
from django.contrib import admin
from django.urls import path, include # adding `include` function as well

urlpatterns = [
    path('admin/', admin.site.urls),
    # adding the following:
    path('new_app/', include('new_app.urls'))
]
```
...first argument to the `path()` function is the URL pattern, second is the app urls that shall handle the request  
...we add `include` function as well to import from `django.urls`
...so by declaring `path('new_app/, include('new_app.urls'))` we add a link to `urls.py` file in `new_app`.    

3) 
In the APP DIRECTORY `new_app` we create the `urls.py`. This file will define the URL patterns. This is where we map the URL to the views in `<project_name>/new_app/views.py`.  

`<project_name>/new_app/urls.py` e.g.:  

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.say_hello), # this is optional
    path('hello/', views.say_hello)
]
```
...to demnstrate the concept I have added two fundtion declarations, so that by visiting either `http://127.0.0.1/new_app/hello/` or `http://127.0.0.1/new_app/` both will render the logic from `say_hello` function in `<project_name>/new_app/views.py`.   

Now we shall see the `Hello, World!` message when navigating to `http://127.0.0.1/new_app/hello/` or `<project_name>/new_app/`.  

## Templates

Templates are the HTML files that are rendered by the `views.py` file. In the those files we can use django templating syntax to take advantage of simple programming concepts from Python.  

The following file will demonsrate how it works.  

1) 
First we create directory `templates` in `new_app`, and also create `hello.html` file inside `<project_name>/new_app/templates/hello.html` with the following content, e.g:

```html
{% if name %}
	<h1>Hello {{ name }} !</h1>
{% else %}
	<h1>Hello World !</h1>
{% endif %}

```
..with this simple html file we can pass the `name` variable from the `views.py` file.  

2) 
Then we need to change the `say_hello` function in `views.py` which shall return `render()` function.
`<project_name>/new_app/views.py` e.g.:  

```python
from django.shortcuts import render

def say_hello(request):
	return render(request, 'hello.html', { 'name': 'Django' })
```
herer the 3rd argument is a dictionary that contains the variable `name` that is passed to the html file using templating syntax.  

#### Today the templates are NOT typically used to render the HTML files. Django, as a backend framework, is used mostly to manage and pull out the necessary data from the database and present it to the user.  

## Debugging

To debug Django app in vscode we can create `launch.json` file in the `.vscode` directory in the root of the project or in the root of the repository, in case the project directory is a child directory in the root of the repository.  

This file is created automatically when the `Run and Debug` option is selected on the side panel.  
The first time (when the `launch.json` file does not exist) we click on the `create a launch.json file` link and select `Python` (or `Python Debugger`) and then `Django ..` options from the dropdown.  
You might also be prmpted to choose the path to `manage.py` (on Linux).  

Here is the example of the generated `launch.json` file:  

```json
{
	"version": "0.2.0",
	"configurations": [
		{
			"name": "Python: Django",
			"type": "python",
			"request": "launch",
			"program": "${workspaceFolder}/manage.py",
			"args": [
				"runserver",
				"9000" // specify the port different from the default 8000 to avoid conflicts
			],
			"django": true
		}
	]
}
```
Once this is saved we can start the debug session by first putting the breakpoints in the code and then clicking on the green play button on the side panel.    

##  django-debug-toolbar

This toolbar is easy to use and it offers good visibility of wahat is going on with the project.  
`https://django-debug-toolbar.readthedocs.io/en/latest/`  

1) 
Installation:  
`https://django-debug-toolbar.readthedocs.io/en/latest/installation.html`  
`pipenv install django-debug-toolbar`  

2) 
Adding the following to `settings.py` file in `<project_name>`:
  
```python
INSTALLED_APPS = [
	...
	'debug_toolbar',
]
```

3) 
Add to the `<project_name>/urls.py` file new lines:  

```python
...
import debug_toolbar

urlpatterns = [
	...
	path('__debug__/', include(debug_toolbar.urls)),
]
```

4) 
Add to the `settings.py` file in `MIDDLEWARE` list:  
```python
MIDDLEWARE = [
	'debug_toolbar.middleware.DebugToolbarMiddleware',
	...
]
```

5) 
Add to the `settings.py` file `INTERNAL_IPS` list:  
```python
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
```  

#### Once the server is started, the debug toolbar will be visible on the right side of the page. The debug toolbar is very useful, especially for analizing the SQL queries to the database.  

## Models (database models)

Models are used to store and retrieve data from the database.  
- Introduction to data modeling.  
- Example of an e-commerce data model.  
- Organizing models in apps.   
- Coding model classes.  

Models are defined in the `models.py` file of the app directory.  
```python
```
...


