import requests
from flask import Flask, request, redirect, session
from flask_session import Session
from env import CONFIG
from instagredient import helpers


app = Flask(__name__)
app.secret_key = CONFIG.get('general', 'app_secret')
sess = Session()


@app.before_request
def exchange():
    if request.args.get('code'):
        access_url = CONFIG.get('wunderlist', 'auth_access_url')
        code = request.args.get('code')
        client_id = CONFIG.get('wunderlist', 'client_id')
        client_secret = CONFIG.get('wunderlist', 'client_secret')
        r = requests.post(access_url, data={'code':code, 'client_id':client_id, 'client_secret':client_secret})
        json_res = r.json()

        if 'access_token' in json_res:
            session['access_token'] = json_res['access_token']
        else:
            return "error:{}".format(json_res)

@app.before_request
def get_token():
    name = 'access_token'
    if (not session.get(name) or session.get(name) == '') and request.path!= '/callback':
        return redirect('/callback?redirect_url={}'.format(request.path))

@app.route("/")
def hello():
    if session.get('access_token'):
        return "Hello {}".format(session.get('access_token'))
    else:
        return "Hello World!"

@app.route("/clearsession")
def clear():
    session.clear()
    return redirect("/")

@app.route("/callback")
def callback():
    if not request.args.get('code'):
        client_id = CONFIG.get('wunderlist', 'client_id')
        redirect_url = "{}{}".format(CONFIG.get('wunderlist', 'app_url'), request.args.get('redirect_url'))
        state = CONFIG.get('wunderlist', 'state')
        auth_url = CONFIG.get('wunderlist', 'auth_url')
        url = "{}?client_id={}&redirect_uri={}&state={}".format(auth_url, client_id, redirect_url, state)

        return redirect(url)

@app.route("/add")
def add():
    w = Wunderlist(session.get('access_token')
    w.check_list()
    # check if list exists
    # parse url
    # add items to list
    return "test"


if __name__ == "__main__":
    app.config['SESSION_TYPE'] = 'filesystem'

    sess.init_app(app)
    app.run('127.0.0.1')
