# Internathon- A simple Geotag Photo Application



This is a django application powered by geocoder and geopy python module which has features like posting images and it automatically detects your location using your ip adress.

## Table of Contents
* [Introduction](#introduction)
* [link to deployed application](#link-to-deployed-application)
* [Features](#features)
  * [Current features](#current-features)
  * [Features to add](#features-to-add)
  * [Feature request](#feature-request)
* [Technologies and tools used](#technologies-and-tools-used)
* [Installation and Setup(Optional)](#)
* [Running in the local server(Optional)](#)
* [Deploying the app to heroku(Optional)](#)
* [Bug Reporting](#)
* [License](License)


## Introduction
I made this project for hackathon in which i participated.It is a geotag photo application.We can check more about the website [here](https://thejourneyapp.herokuapp.com/).



## link to deployed application
The application is deployed in heroku platform. This is the link to the deployed application <b>:</b>
 [https://thejourneyapp.herokuapp.com/](https://thejourneyapp.herokuapp.com/)


## 🚀 Features
### Current features
* Users can create account and upload photos.
* The photo will automatically show the location from where user posted using ip adress.
### Features to add
* Looking to develop the UI/UX more.
* Looking to detect locations on more detailed basis.

### ⭐ Feature request

* Any other feature you would like to suggest ,then please [open an issue]() for that.😊
* Connect with me in [LinkedIn](www.linkedin.com/in/debraj-bhal-7597861b2). I did 💖 to hear how you feel using this app.
## Technologies and tools used
* [Django-python](https://www.djangoproject.com/)
* [Geocoder](https://pypi.org/project/geocoder/)
* [Geopy](https://pypi.org/project/geopy/)
* [Django-ipware](https://pypi.org/project/django-ipware/)
* [Django Google Drive Storage](https://github.com/torre76/django-googledrive-storage/blob/master/docs/index.rst)
* [Html](https://www.w3schools.com/html/)
* [CSS](https://www.w3schools.com/Css/)
* [JavaScript](https://www.w3schools.com/js/DEFAULT.asp)
* [Python](https://www.python.org/doc/)
* [Bootstrap](https://getbootstrap.com/)

## Installation and Setup(Optional)
First clone this repository to your local machine using the following command in git bash<b>:</b>
```
$ git clone https://github.com/krishna-vasudev/Internathon
```
Now open git bash in the root directory of the repository and enter the following command to install the required dependencies<b>:</b>
```
$ pip install -r requirements.txt
``` 


## Running in the local server(Optional)
Open the git bash inside the root directory present in the root directory of the repository.
Run the following commands in order one by one:
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
Follow the link generated after last command and Hurrah!🎉 the app is running.

## Deploying the app to heroku(Optional)
Now although it's running good in local server but to deploy to heroku we have to make few more changes. Refer to [this](https://www.youtube.com/watch?v=UkokhawLKDU&list=WL&index=39) tutorial for detailed step by step deployment to heroku.

## 🐛 Bug Reporting
Feel free to [open an issue](https://github.com/krishna-vasudev/internathon/issues) on github if you find any bug.
## 📜 License
This software is open source, licensed under the [MIT License](/LICENSE).
