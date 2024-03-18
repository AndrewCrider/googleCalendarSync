# googleCalendarSync
 
 Find out more at https://medium.com/technology-hits/create-an-automated-database-of-your-google-calendar-events-e3edb75e681e.

## Prerequisites
 This repository is designed to be used as a Google Cloud Function.  It uses the following capabilities:
 1. Google Cloud - Pub Sub, Google HTTP Functions, and the Google Calendar API
 2. Firebase - Firebase Database
 3. Google Calendar

## Configuration
 As described in the above article, you will want to generate a Service Account JSON file for both Google Cloud and Firebase.  They should be placed in config/googleJSON/
 * cloudServices.json (GCP Service Account)
 * firebase.json (Firebase Service Account)

 You will also want to secure the calendarID (or Calender IDs) from the Google Calendars that you want to sync and place.  An example file is located in config/helperFiles/example_calendarsToSync.py.  A simple array is being used.

## Possible Enhancements
 * Add the ability to call the Firebase Import from the main function
 * Add the ability to read Microsoft Outlook Calendars
 * Add a GenAI ability to Summarize the events
 * Add filters to events coming in

## Further Information
 This project was a module for a Generative AI based Assistant that I'm working on.  Some other information that you might find useful:
 * Personality and AI — Create an AI Assistant Team(https://medium.com/datadriveninvestor/personality-and-ai-create-an-ai-assistant-team-0faf01f82a44)
   GitHub(https://github.com/AndrewCrider/Generate-Jarvis)
 * You Need to Build Your own Personal Corpus before the Singularity(https://medium.com/@andrewcrider/you-need-to-build-your-own-personal-corpus-before-the-singularity-bf13c8c10925)
