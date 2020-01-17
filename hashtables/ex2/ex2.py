#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    for i in range(length):
        if i == 0:
            route[i] = hash_table_retrieve(hashtable, "NONE")
            # GET NONE
        else:
            # Get the route before and check i - 1, shows destination/value of last used source/key
            print("Hashtable: ", hash_table_retrieve(hashtable, route[i - 1]))
            route[i] = hash_table_retrieve(hashtable, route[i - 1])

    # Used to get rid of NONE at end of list, fails on tests, tests look for NONE 

    # if route[len(route) -1] == "NONE":
    #     route.remove(route[len(route) -1])
    # print("route", route)
    return route


     # OLD CODE< NEEDED TO RESTART
    # def reconstruct_trip(tickets, length):
    #     hashtable = HashTable(length)
    #     route = [None] * length
    #     position = 0
    #     for i in range(length):
    #         hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
    #     if hash_table_retrieve(hashtable, tickets[i].source) == 'None':
    #         route[0] = hash_table_retrieve(hashtable, tickets[i].source)
    #         position +=1
    #     else:
    #         while position <= length:
    #             if hash_table_retrieve(hashtable, route[0]) == hash_table_retrieve(hashtable, tickets[i].source):
    #                 route[position] = hashtable.storage[tickets[i].destination]
    #                 position += 1
    #             elif hash_table_retrieve(hashtable, route[position]) == hash_table_retreive(hashtable, tickets[i].source):
    #                 route[position] = hashtable.storage[tickets[i].destination]
    #                 position += 1
    #             elif hash_table_retrieve(hashtable, route[position]) == 'None':
    #                 route[len(route)-1] = hashtable.storage[route[position]]
    #                 position += 1
    #     print(route)
    #     return route 
        


# ticket_1 = Ticket("PIT", "ORD")
# ticket_2 = Ticket("XNA", "SAP")
# ticket_3 = Ticket("SFO", "BHM")
# ticket_4 = Ticket("FLG", "XNA")
# ticket_5 = Ticket("NONE", "LAX")
# ticket_6 = Ticket("LAX", "SFO")
# ticket_7 = Ticket("SAP", "SLC")
# ticket_8 = Ticket("ORD", "NONE")
# ticket_9 = Ticket("SLC", "PIT")
# ticket_10 = Ticket("BHM", "FLG")

# tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
#             ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]


# reconstruct_trip(tickets, 10)
