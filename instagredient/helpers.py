import ConfigParser, requests
from flask import redirect

def read_config(config_file="./config.cfg"):
    config = ConfigParser.ConfigParser()
    config.read(config_file)

    return config

def token(session, from_url):
    name = 'access_token'
    if session.get(name):
        return session.get(name)
    else:
        return redirect('/callback?redirect_url={}'.format(from_url))

def exchange_code(request, session):

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

