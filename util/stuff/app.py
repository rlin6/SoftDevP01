from flask import Flask, render_template
from urllib import request, parse
import json
app=Flask(__name__)
key="kRAtgnsgZTOsTguZs5C7s5rw3wnAM1Mi"
amount=10#change this in root if amount of results changes
@app.route("/")
def root():
    #get ISS coordinates
    ISS="http://api.open-notify.org/iss-now.json"
    response = request.urlopen(ISS)
    obj = json.loads(response.read())
    long=obj['iss_position']['longitude']
    lat=obj['iss_position']['latitude']
    #long =str(-74.005973)#placeholder
    #lat= str(40.712775)
    #find attractions near ISS(max is 50)(default is 10)
    text="https://www.mapquestapi.com/search/v4/place?sort=distance&feedback=false&key="+ key+"&circle="+long+"%2C"+lat+"%2C1000"
    response =request.urlopen(text)
    info =json.loads(response.read())
    description = info["results"]
    #generates image of ISS location
    base="https://www.mapquestapi.com/staticmap/v5/map?key="+key+"&center="+lat+","+long
    return render_template("index.html",text=description,image=base)
if __name__ == "__main__":
  app.debug = True
  app.run()
