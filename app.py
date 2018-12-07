#BooStRadley - Ricky Lin, Matthew Ming, Mohammed Uddin, Sophia Xia

import json
import os
import urllib

from flask import Flask, render_template, session, redirect, request, url_for, flash

from util import auth, adders, getters

app = Flask(__name__)

app.secret_key = os.urandom(32)
with open("data/keys.json") as f:
    data = json.loads(f.read())
    key=data['map_key']
    secondkey=data['weather_key']

#key = "kRAtgnsgZTOsTguZs5C7s5rw3wnAM1Mi"
amount = 10 #number of places to return
currLat = ''
currLong = ''
firstTrack = True

def loggedIn():

    if 'user' in session:
        return True
    return False

def refresh():

    #get ISS latitude
    ISS = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(ISS)
    obj = json.loads(response.read())

    lat=obj['iss_position']['latitude']
    #lat= str(40.712775)

    #get ISS longtitude
    ISS = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(ISS)
    obj = json.loads(response.read())

    long=obj['iss_position']['longitude']
    #long =str(-74.005973)#placeholder

    global currLat
    global currLong
    
    #print( currLat)
    currLat = lat
    #print(currLat)
    
    #print(currLong)
    currLong = long
    #print(currLong)
    
@app.route("/")
def index():

    if 'user' in session:
        return redirect('/track')

    return render_template("index.html", SESSION = loggedIn())

@app.route("/logout")
def logout():

    global firstTrack

    firstTrack = True

    if 'user' in session:
        session.pop('user')
    return redirect('/')

@app.route("/signup")
def signup():

    if 'user' in session:
        return redirect('/track')

    return render_template("signup.html", SESSION = loggedIn())

@app.route("/auth", methods = ['POST','GET'])
def authen():

    global currLat
    global currLong

    message = ''

    if request.method == 'GET' or not ('user' in request.form.keys()):
        return redirect('/')

    if "conf" in request.form.keys():
        message = auth.register(request.form['user'], request.form['pwd'], request.form['conf'])
        
    else: message = auth.login(request.form['user'], request.form['pwd'])

    if message in ["Account creation successful", "Login Successful"]:
        refresh()
        session['user'] = request.form['user']
        return redirect('/track')

    else:
        flash(message)
        print(message)
        return redirect(request.referrer or '/')

@app.route("/track")
def track():

    global firstTrack

    if (not loggedIn()) and firstTrack:
        refresh()
        firstTrack = False

    global currLong
    global currLat

    base = "https://www.mapquestapi.com/staticmap/v5/map?key=" + key + "&center=" + currLat + "," + currLong +"&locations="+ currLat + "," + currLong +"&zoom=6&size=760,310@2x"

    return render_template("track.html", lat = currLat, lon = currLong, image = base, SESSION = loggedIn())

@app.route("/info")
def info():

    global currLat
    global currLong
    global firstTrack

    if firstTrack:
        return redirect('/track')

    data = "https://www.mapquestapi.com/search/v4/place?sort=distance&feedback=false&key=" + key + "&circle=" + currLong + "%2C" + currLat + "%2C1000"
    response = urllib.request.urlopen(data)
    info = json.loads(response.read())
    description = info["results"]
    #secondkey="647d4c51b198137da2da622c301ce39d"
    weather = "https://api.darksky.net/forecast/"+secondkey+"/"+currLat+","+currLong
    response = urllib.request.urlopen(weather)
    obj = json.loads(response.read())
    print(weather)
    if description == []:
        description=["There are no registered attractions at this current location."]
    summary=obj['hourly']['summary']
    data = obj['daily']['data'][0]
    low = data['temperatureMin']
    high = data['temperatureMax']
    
    return render_template("info.html",text = description,day=summary, SESSION = loggedIn())

@app.route("/account")
def account():

    if 'user' not in session:
        return redirect('/track')
    
    user = session['user']
    saves = getters.get_saves(user)
    return render_template("account.html", SESSION = loggedIn(), saves = saves, user = session['user'])

@app.route("/save")
def save():
    info = request.args
    if 'user' not in session:
        return redirect('/')
    user = session['user']
    times = info['times']
    lat = info['lat']
    lon = info['long']
    address = info['address']
    summary = info['summary']
    high = info['high']
    low = info['low']
    alerts = info['alerts']
    place = info['place']
    adders.add_save(user,times,lat,lon,address,summary,high,low,alerts,place)
    return redirect("/account")

@app.route("/update")
def update():
    
    global currLat
    global currLong

    refresh()

    return redirect("/track")

@app.route("/demo")
def demo():

    global currLat
    global currLong

    if currLat != str(40.712775) and currLong != str(-74.005973):
        currLat = str(40.712775) 
        currLong = str(-74.005973)

    else: 

        refresh()

    return redirect("/track")

if __name__ == '__main__':
    app.run(debug=True)
