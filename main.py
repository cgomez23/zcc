# TODOs: 
# - Error pages for auth failure --GOOD
# - Unit testing
# - Make README
# - Comment! --GOOD
# - Fix Pagimation --GOOD

from flask.helpers import url_for
from utils import *

from flask import Flask, render_template, redirect, request
from flask_paginate import Pagination, get_page_args
from zenpy import Zenpy
import json

# Start
app = Flask(__name__)

creds_pass = True
creds = json.load(open('creds.json'))

# try connecting to Zendesk API
try:
    # conntect to Zendesk API
    zenpy_client = Zenpy(**creds)

    # get api ticket objects
    tickets_objs = zenpy_client.tickets()
    tickets = [t for t in tickets_objs]

    # get api user objects
    users_objs = zenpy_client.users()
    users = [u for u in users_objs]

# if credentials login fails, set flag to False
except Exception:
    creds_pass = False
    pass



# Controller

# Displays home page with list of tickets, 25 tickets per page.
@app.route('/', methods=["GET"])
def home():

    # if cedentials do not work, redirect to error page
    if creds_pass == False:
        return redirect(url_for('api_error'))

    headers = ['', 'Ticket Number', 'Subject']

    # get page pagination args
    page = int(request.args.get('page', 1))
    per_page = 25
    offset = (page - 1) * per_page

    # calls for api ticket objects and diplays list on page
    ticket_view_list = get_ticket_list(tickets)
    total = len(ticket_view_list)
    pagination_users = get_tickets_pagination(ticket_view_list, offset=offset, per_page=per_page)
    pagination = Pagination(page=page, 
                            per_page=per_page, 
                            total=total,
                            css_framework='bootstrap4')
    
    return render_template('home.html', 
                            list=pagination_users, 
                            headers=headers, 
                            page=page,
                            per_page=per_page,
                            pagination=pagination)

# Page to display if api error occurs
@app.route('/api_error')
def api_error():
    return render_template('api_error.html', code=302)

# Page that displays unique ticket details.
@app.route('/ticket', methods=["GET"])
def ticket():

    # get ticket id from URL
    id = request.args.get('id', None)

    # gets the ticket view and renders it
    ticket_view = get_ticket_view(id, tickets, users)
    return render_template('ticket.html', ticket=ticket_view)

# Starts the site.
if __name__ == "__main__":
    app.run(debug=True)
