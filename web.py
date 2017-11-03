import requests
from flask import Flask, request, redirect
from env import CONFIG


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/callback")
def callback():
    if request.args.get('code'):
        access_url = CONFIG.get('wunderlist', 'auth_access_url')
        code = request.args.get('code')
        client_id = CONFIG.get('wunderlist', 'client_id')
        client_secret = CONFIG.get('wunderlist', 'client_secret')
        r = requests.post(access_url, data={'code':code, 'client_id':client_id, 'client_secret':client_secret})

        app.logger.debug("stuff  {}".format(r.json()))
	return "success {}".format(r.json())

    else:
        client_id = CONFIG.get('wunderlist', 'client_id')
        redirect_url = CONFIG.get('wunderlist', 'app_callback_url')
        state = CONFIG.get('wunderlist', 'state')
        auth_url = CONFIG.get('wunderlist', 'auth_url')
        url = "{}?client_id={}&redirect_uri={}&state={}".format(auth_url, client_id, redirect_url, state)

        return redirect(url)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "do_the_login"
    else:
        return "show_the_login_form"

if __name__ == "__main__":
    app.run('127.0.0.1')
