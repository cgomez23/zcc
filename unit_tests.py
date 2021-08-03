import unittest
import utils
import json
from zenpy import Zenpy

creds = json.load(open('creds.json'))
zenpy_client = Zenpy(**creds)

# get api ticket objects
tickets_objs = zenpy_client.tickets()
tickets = [t for t in tickets_objs]
tickets_dict = {}
# maps ids to ticket objects
for t in tickets:
    tickets_dict[t.id] = t

# get api user objects
users_objs = zenpy_client.users()
users = [u for u in users_objs]
users_dict = {}
for u in users_objs:
    users_dict[u.id] = u

# class to check the get_ticket() function
class TestGetTicketFunction(unittest.TestCase):
    # checks to see if the output is correct
    def test_ticket_return(self):
        id = '1'
        self.assertEqual(utils.get_ticket(id, tickets), tickets_dict[int(id)])
        id2 = '2'
        self.assertEqual(utils.get_ticket(id2, tickets), tickets_dict[int(id2)])
        id3 = '3'
        self.assertEqual(utils.get_ticket(id3, tickets), tickets_dict[int(id3)])
    
    # checks to see if the id value is recognized in the list of tickete ids
    def test_ticket_arg_value(self):
        args = ['204', tickets] # ids so far: 1 to 203
        self.assertRaises(ValueError, utils.get_ticket, *args)
        args = ['1000', tickets]
        self.assertRaises(ValueError, utils.get_ticket, *args)
    
    # checks to see if the id string contains a numeric value
    def test_ticket_arg_string_contents(self):
        args = ['str', tickets]
        self.assertRaises(TypeError, utils.get_ticket, *args)
        args = ['True', tickets]
        self.assertRaises(TypeError, utils.get_ticket, *args)
        args = ['2.1', tickets]
        self.assertRaises(TypeError, utils.get_ticket, *args)
    
    # checks to see if the id type is a string
    def test_ticket_arg_type(self):
        args = [True, tickets]
        self.assertRaises(TypeError, utils.get_ticket, *args)
        args = [1, tickets]
        self.assertRaises(TypeError, utils.get_ticket, *args)

# class to check the get_requester() function
class TestGetRequesterFunction(unittest.TestCase):
    # checks for correct return
    def test_get_requester_return(self):
        self.assertEqual(utils.get_requester_name(tickets[0], users), 'The Customer')
        self.assertEqual(utils.get_requester_name(tickets[4], users), 'Carlos Gomez')

# class to check the get_tickets() function
class TestGetTicketsFunction(unittest.TestCase):
    # checks to see if the ticket list for the home page UI is correct
    def test_get_tickets(self):
        self.assertEqual(utils.get_ticket_list(tickets), [(t.id, t.subject) for t in list(tickets_dict.values())])

# print(utils.get_ticket(418740978252, tickets))