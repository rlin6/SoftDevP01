from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    print(app)
    return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

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

