from . import app
import requests
from flask import render_template, request

@app.route('/') # this is out main page thats gonna open when u first click on link i set it to be homepage
def home():
    return render_template('homepage.html')

@app.route('/events') # this is my page 2 for events i added a filtering feature 
def events():
    category = request.args.get('category', '')

    base_url = "https://api.predicthq.com/v1/events/"
    location = "within=30km@30.0444,31.2357"
    country = "country=EG"
    limit = "limit=20"

    
    if category:
        category_param = f"category={category}"
        url = f"{base_url}?{location}&{country}&{limit}&{category_param}"
    else:
        url = f"{base_url}?{location}&{country}&{limit}"

    headers = {
        "Authorization": "Bearer 5b52pFPahJmUK2XRA4kuH_Yrr8Y9Rjklovb1zhbb"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        events = data.get("results", [])
        return render_template("events.html", events=events)
    else:
        return f"Error: Unable to fetch events. Status Code: {response.status_code}", 500






