import requests
from flask import Flask, request, redirect, session
from flask_session import Session
from env import CONFIG


app = Flask(__name__)
app.config.from_object(__name__)
Session(app)

@app.route("/")
def hello():
    if session.get('access_token'):
        return "Hello {}".format(session.get('access_token'))
    else:
        return "Hello World!"


@app.route("/callback")
def callback():
    client_id = CONFIG.get('wunderlist', 'client_id')

    if request.args.get('code'):
        access_url = CONFIG.get('wunderlist', 'auth_access_url')
        code = request.args.get('code')
        client_secret = CONFIG.get('wunderlist', 'client_secret')
        r = requests.post(access_url, data={'code':code, 'client_id':client_id, 'client_secret':client_secret})
        json_res = r.json()

        if 'access_token' in json_res:
            session['access_token'] = json_res['access_token']
        else:
            return "error:{}".format(r.json())

        return redirect("/")

    else:
        client_id = CONFIG.get('wunderlist', 'client_id')
        redirect_url = CONFIG.get('wunderlist', 'app_callback_url')
        state = CONFIG.get('wunderlist', 'state')
        auth_url = CONFIG.get('wunderlist', 'auth_url')
        url = "{}?client_id={}&redirect_uri={}&state={}".format(auth_url, client_id, redirect_url, state)

        return redirect(url)


if __name__ == "__main__":
    app.run('127.0.0.1')
