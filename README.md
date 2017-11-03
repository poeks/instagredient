# instagredient
Convert a recipe URL to Wunderlist shopping list

## Install 

### Server

#### Install and run NGINX and UWSGI

https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-16-04

#### Configure

* Copy config.ini.sample to config.ini
* Create Wunderlist app: https://developer.wunderlist.com
* Edit config.ini to reflect wunderlist app config

#### Run locally

```bash
. venv/bin/activate
pip install -r requirements.txt
python web.py
```

