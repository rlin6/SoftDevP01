# SoftDevP01
Project 01 for Software Development: ISS World Tour

BooStRadley Roster:

Ricky Lin 

Matthew Ming 

Mohammed Uddin  

Sophia Xia

Period 6 Software Development

## Overview 

ISS World Tour uses the coordinates of the International Space Station to display its location on a map. The website also shows you the weather conditions in the area and nearby attractions. As the user, you can save the location, weather, or attractions to try to earn achievements. You are able to use the site without signing up, but you would not be able to save anything. 

## Site Guide 

After going on the site, you have the option to signup, sign in, or go straight to the site. Signup lets you create an account and sign in logs you in. If you are not logged in, you can view the tracking page where you can see the ISS location, view the weather there, and look at the attractions. If you are logged in, you can do all of this in addition to saving the details to your account page. 

## API Keys

You do not need a key for the ISS API; you only need the url: http://open-notify.org/Open-Notify-API/ISS-Location-Now/ 

For DarkSky API, you have to sign up with an email. Then, click the link that is sent to your email. The quota is 1000 requests per day for free: https://darksky.net/dev/

For MapQuest API, you have to sign up for an account on the website. Afte making your account, you get an unique key for that account. The quota is 15000 requests per month: https://developer.mapquest.com/documentation/traffic-api/

## Dependencies

Note:

Python 3 is used

On a Linux, sudo access is required to install packages and dependencies  

You need to create a virtual environment and then install Wheel and Flask.

Wheel archives the requirements and dependencies installed.  

Flask is required to create and run flask apps. 

Note: angle brackets(<>) are simply used to denote a field you should fill out, do not include them.

Installing a virtual environment:

```
sudo apt install python3 -venv
python3 -m venv <name of venv>
```

Activate the virtual environment

```
.<name of venv>/bin/activate
```

Installing Wheel:

```
pip3 install wheel
```

Installing Flask:

```
pip3 install flask
```

## Running the app

After cloning the repository from github, activate your virtual environment. Move into the repository and then run the program by using the following command:

```
python app.py
```

Then head to localhost:5000 or the given ip link in the terminal 
