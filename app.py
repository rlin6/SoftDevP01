#BooStRadley - Ricky Lin, Matthew Ming, Mohammed Uddin, Sophia Xia

import json
import os
import urllib

from flask import Flask, render_template, session, redirect, request, url_for, flash

from util import auth, adders, getters

app = Flask(__name__)

app.secret_key = os.urandom(32)

key = "kRAtgnsgZTOsTguZs5C7s5rw3wnAM1Mi"
amount = 10 #number of places to return

def getLat():

    #get ISS latitude
    ISS = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(ISS)
    obj = json.loads(response.read())

    lat=obj['iss_position']['latitude']
    #lat= str(40.712775)

    return lat

def getLong():

    #get ISS longtitude
    ISS="http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(ISS)
    obj = json.loads(response.read())

    long=obj['iss_position']['longitude']
    #long =str(-74.005973)#placeholder

    return long

@app.route("/")
def index():

    if 'user' in session:
        return redirect('/track')

    return render_template("index.html")

@app.route("/signup")
def signup():

    if 'user' in session:
        return redirect('/track')

    return render_template("signup.html")

@app.route("/auth", methods = ['POST','GET'])
def authen():

    message = ''

    if request.method == 'GET' or not ('user' in request.form.keys()):
        return redirect('/')

    if "conf" in request.form.keys():
        message = auth.register(request.form['user'], request.form['pwd'], request.form['conf'])

    else: message = auth.login(request.form['user'], request.form['pwd'])

    if message in ["Account creation successful", "Login Successful"]:
        session['user'] = request.form['user']
        return redirect('/track')

    else:
        flash(message)
        return redirect(request.referrer or '/')

@app.route("/track")
def track():

    base = "https://www.mapquestapi.com/staticmap/v5/map?key=" + key + "&center=" + getLat() + "," + getLong()

    return render_template("track.html", image = base)

@app.route("/places")
def places():

    data = "https://www.mapquestapi.com/search/v4/place?sort=distance&feedback=false&key=" + key + "&circle=" + getLong() + "%2C" + getLat() + "%2C1000"
    response = urllib.request.urlopen(data)
    info = json.loads(response.read())
    description = info["results"]

    return render_template("places.html", text = description)

@app.route("/weather")
def weather():
    return render_template("weather.html")

@app.route("/account")
def account():
    return render_template("account.html")

if __name__ == '__main__':
    app.run(debug=True)
