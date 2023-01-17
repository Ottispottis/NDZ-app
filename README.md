# Web app for Reaktor's summer developer trainee position 2023

The pre-assignment for Reaktor's summer trainee position was a web application that would display the information of pilots who violated the "No drone zone" set around 
the nest of a rare bird breed "Monadikuikka".

Requirements:

- Persist the pilot information for 10 minutes since their drone was last seen by the equipment

- Display the closest confirmed distance to the nest

- Contain the pilot name, email address and phone number

- Immediately show the information from the last 10 minutes to anyone opening the application

- Not require the user to manually refresh the view to see up-to-date information

This Python program gathers and parses all the required information and renders it as a web page using Flask.

All the information is automatically collected, updated, and displayed to the user as a chart.

I recommend using Python 3.8 => if you want to try running this locally on your own machine.

At the time of writing a functional version of this app has been deployed on Google Cloud: https://reaktor-ndz-app.ew.r.appspot.com/

Due to free hosting, the chart won't be populated unless someone has recently viewed the web app.