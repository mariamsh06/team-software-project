import requests
from flask import jsonify
from . import app

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
        return jsonify(events["results"][:5])  # just return first 5 events
    else:
        return f"Error: Unable to fetch events, Status Code: {response.status_code}", 500



