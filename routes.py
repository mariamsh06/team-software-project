from . import app
import requests
from flask import render_template, request

@app.route('/')
def index():
    url = "https://api.predicthq.com/v1/events/?within=30km@30.0444,31.2357&country=EG"
    headers = {
        "Authorization": "Bearer 5b52pFPahJmUK2XRA4kuH_Yrr8Y9Rjklovb1zhbb"
    }

    response = requests.get(url, headers=headers)

    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    if response.status_code == 200:
        events = response.json()
        return render_template("index.html", events=events["results"])
 
    else:
        return f"Error: Unable to fetch events, Status Code: {response.status_code}", 500



