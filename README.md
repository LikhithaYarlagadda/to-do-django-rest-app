# To-Do List Application
It is a To-Do Application developed with Django Rest Framework in Linux environment and postgresql database is used.


## End Points

* `GET /api/task_list/`
* `GET /api/task_detail/{pk}`
* `POST /api/task_create/`
* `POST /api/task_update/{pk}`
* `DELETE /api/task_delete/{pk}`


## Get the code
* Clone the repository
`git clone https://github.com/LikhithaYarlagadda/to-do-django-rest-app.git`

## Install the project dependencies

First create virtualenv, then enter the following command.

`pip install -r requirements.txt`

## Run the commands to generate the database
`python manage.py makemigrations`

`python manage.py migrate`

## Generate super user
`python manage.py createsuperuser`

## Run the server
`python manage.py runserver` the application will be running on port 8000 **http://0.0.0.0:8000/**

## Run the test
`python manage.py test`
