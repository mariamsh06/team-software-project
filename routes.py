from . import app
import requests
from flask import render_template, request, flash, redirect, url_for

@app.route('/')  # This is our main page that's gonna open when you first click on the link. It's set to be the homepage.
def home():
    return render_template('homepage.html')

@app.route('/events')  # This is page 2 for events where we added a filtering feature
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
        "Authorization": "Bearer tBK21eyBEA9wpCoMwM5_NIaXgNodRa3A1tZewlLh"  # THIS IS THE NEW API KEY VALID TIL MAY 2ND  
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        events = data.get("results", [])
        return render_template("events.html", events=events)
    else:
        return f"Error: Unable to fetch events. Status Code: {response.status_code}", 500

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('message')  

        
        import re
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        phone_pattern = r'^\+?\d{10,15}$'

        if not re.match(email_pattern, email):
            flash('Please enter a valid email address.', 'error')
            return redirect(url_for('contact'))

        if not re.match(phone_pattern, phone):
            flash('Please enter a valid phone number (10-15 digits).', 'error')
            return redirect(url_for('contact'))

        if not name.strip():
            flash('Name cannot be empty.', 'error')
            return redirect(url_for('contact'))

       
        flash("Your message has been received! We'll get back to you soon.", 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')



