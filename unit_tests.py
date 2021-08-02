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


class TestGetTicketFunction(unittest.TestCase):
    def test_ticket_return(self):
        id = 1
        self.assertEqual(utils.get_ticket(id, tickets), tickets_dict[id])
        id2 = 2
        self.assertEqual(utils.get_ticket(id2, tickets), tickets_dict[id2])
        id3 = 3
        self.assertEqual(utils.get_ticket(id3, tickets), tickets_dict[id3])
    
    def test_ticket_arg_value(self):
        args = [204, tickets] # ids so far: 1 to 203
        self.assertRaises(ValueError, utils.get_ticket, *args)
        args = [1000, tickets]
        self.assertRaises(ValueError, utils.get_ticket, *args)
    
    def test_ticket_arg_type(self):
        args = ['str', tickets]
        self.assertRaises(TypeError, utils.get_ticket, *args)
        args = [True, tickets]
        self.assertRaises(TypeError, utils.get_ticket, *args)
        args = [2.1, tickets]
        self.assertRaises(TypeError, utils.get_ticket, *args)

class TestGetRequesterFunction(unittest.TestCase):
    def test_ticket_return(self):
        self.assertEqual(utils.get_requester_name(tickets[0], users), 'The Customer')
        self.assertEqual(utils.get_requester_name(tickets[4], users), 'Carlos Gomez')
    

# print(utils.get_ticket(418740978252, tickets))