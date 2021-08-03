# Zendesk Coding Challenge!

This project is for the Zendesk 2021 Co-Op coding challenge.
- Created using Zenpy and Flask in Python

Install Instructions:
- Install Python 3.8 or later
- Make sure pip is installed
- Clone repository to local drive
- In a terminal, Navigate to the "zendesk-coding-challenge" git folder in your local drive using cd
- Create Json file called "creds.json" with the necessary keys: email, password or token, and subdomain
- Add this file to the project
- Install necessary python packages using the "pip install -r requirements.txt" script
- Finally, type "python main.py" in the same directory
- Open http://127.0.0.1:5000/ (if not port 5000, or a different URL, check the output in the terminal for the correct URL)
- Run the unit tests with "python -m unittest unit_tests"

Note: 
- The Setup folder contains code for uploading the test tickets.
- Error handling:
    - If you change the creds.json file to unrecognizable credentials, an error page will display.
    - If you pass an unrecognized id or non-integer value in for the id variable in the ticket URL (e.g. /ticket=True or /ticket=3.4), it will redirect to a user-friendly error page.