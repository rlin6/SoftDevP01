import json
from flask import Flask
with open('file.json', 'w') as f:
        json.dump({"map_key" :"kRAtgnsgZTOsTguZs5C7s5rw3wnAM1Mi","weather_key":"647d4c51b198137da2da622c301ce39d"}, f)