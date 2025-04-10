from . import app
import requests
from flask import render_template, request
from datetime import datetime



from flask import render_template
from . import app  

@app.route('/') # THIS IS OUR ROOOT DIRECTORYYY!! RESERVED FOR OUR HOMEPAGE
def home():
    
    return render_template('homepage.html') # here this just displays our front end for homepage





@app.route('/events')  # THIS IS PAGE TWO!! THE EVENTS PAGE
def events_page():
    
    url = "https://api.predicthq.com/v1/events/?within=30km@30.0444,31.2357&country=EG"
    headers = {
        "Authorization": "Bearer 5b52pFPahJmUK2XRA4kuH_Yrr8Y9Rjklovb1zhbb"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        events = response.json()["results"]
        
       
        for event in events:
            
            event['start'] = datetime.strptime(event['start'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d/%m/%Y')
            
            
            event['location'] = "Cairo"  

        return render_template("events.html", events=events)
    else:
        return f"Error: Unable to fetch events, Status Code: {response.status_code}", 500





