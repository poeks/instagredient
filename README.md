# instagredient
Convert a recipe URL to Wunderlist shopping list

## Install 

### Server

#### Install and run NGINX and UWSGI

https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-16-04

#### Configure

* Copy config.ini.sample to config.ini
* Create Wunderlist app
* Edit config.ini to reflect wunderlist app config

#### Run locally

`FLASK_APP=instagredient.py flask run`

### Client
