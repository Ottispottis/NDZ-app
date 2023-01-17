# Web app for Reaktor's summer developer trainee position 2023

The pre-assignment for Reaktor's summer trainee position was a web application that would display the information of pilots who violated the "No drone zone" set around 
the nest of a rare bird breed "Monadikuikka".

Link to assignment description: https://assignments.reaktor.com/birdnest/

# Requirements

- Persist the pilot information for 10 minutes since their drone was last seen by the equipment

- Display the closest confirmed distance to the nest

- Contain the pilot name, email address and phone number

- Immediately show the information from the last 10 minutes to anyone opening the application

- Not require the user to manually refresh the view to see up-to-date information
# Function
This Python program gathers and parses all the required information and renders it as a web page using Flask.

All the information is automatically collected, updated, and displayed to the user as a chart.

After 10 minutes from the last violation, pilot gets removed from the list. 

If a pilot violates the NDZ again before 10 minutes has passed from the last recorded violation, the time of the violation gets updated.

Position only gets updated when the new position is closer than the previous one.
# Running locally
Prerequisites:

- Python 3.8 or newer

- Install packages listed in requirements.txt

- a Modern browser that supports Fetch

NOTE: requirements.txt is configured so that it is compatible with Google Cloud, for running locally NumPy 1.24.0 is recommended

Running:

1. Prerequisites
2. Open CLI and navigate to web_app directory
3. Run Flask --app main.py in your CLI
4. Navigate to http://127.0.0.1:5000 on your browser
5. Chart should start filling up with pilot information :)

# Live version
At the time of writing a functional version of this app has been deployed on Google Cloud: https://reaktor-ndz-app.ew.r.appspot.com/

Due to free hosting, the chart won't be populated unless someone has recently viewed the web app.

# Improvements that I would do to increase performance and improve UX:

- Using a database for storing the pilot information - currently reading and writing is done from a JSON file which works fine for demonstrating, but using something like SQL would be preferable as this current method is computationally expensive and slow. Unfortunately I didn't have the time to implement that yet.
- Modern UI
- Allow sorting of the chart in different orders: time, position etc.

