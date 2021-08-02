from logging import raiseExceptions
from Models.ticket import Ticket_View

# Functions

# Function to get the list of tickets from desired client.
# args: none
# return: list of api ticket objects
def get_ticket_list(tickets):
    ticket_view_list = [(t.id, t.subject) for t in tickets]
    return ticket_view_list

# Function to get specific ticket by id number.
# args: int
# return: api ticket object
def get_ticket(id, tickets):
    if type(id) != int:  
        raise TypeError("Not a valid ID")

    for t in tickets:
        if t.id == id:
            # print(t)
            return t

    raise ValueError("ID is not recognized.")

# Function to get the requester name for unique ticket.
# args: ticket api object
# return: string
def get_requester_name(ticket, users):
    users_names_and_ids = [(u.id, u.name) for u in users]
    for u in users_names_and_ids:
        if u[0] == ticket.requester_id:
            return u[1]

# Function to get a unique ticket and create a ticket view for the UI.
# args: int
# return: Ticket_View object 
def get_ticket_view(id, tickets, users):
    ticket = get_ticket(id, tickets)
    # print(ticket)
    requestor_name = get_requester_name(ticket, users)
    view = Ticket_View(ticket.id, requestor_name, ticket.subject, ticket.description)
    return view

# Function to get list of tickets per page
# args: api ticket objects, int (optional), int (optional) 
# return: list of 
def get_tickets_pagination(tickets, offset=0, per_page=25):
    return tickets[offset: offset + per_page]