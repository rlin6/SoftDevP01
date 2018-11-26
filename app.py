#BooStRadley - Ricky Lin, Matthew Ming, Mohammed Uddin, Sophia Xia

from flask import Flask, render_template, session, redirect
#import os 

app = Flask(__name__)

#app.secret_key = os.urandom(32)

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
def auth():

    message = ''

    if request.method == 'GET' or not ('user' in request.form.keys()):
        return redirect('/')

    if "conf" in request.form.keys():
        message = auth.register(request.form['user'], request.form['pwd'], request.form['conf'])

    else: message = auth.CheckInfo(request.form['user'], request.form['pwd'])

    if message in ["Account creation successful", "Login Successful"]:
        session['user'] = re

@app.route("/track")
def track():
    return render_template("track.html")

@app.route("/weather")
def weather():
    return render_template("weather.html")

@app.route("/account")
def account():
    return render_template("account.html")

@app.route("/places")
def places():
    return render_template("places.html")

if __name__ == '__main__':
    app.run(debug=True)
