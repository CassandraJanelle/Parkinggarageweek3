# ParkingGarage class definition
class ParkingGarage():

    # ParkingGarage constructor definition
    def __init__(self):
        self.tickets = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.parkingSpaces = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.currentTicket = {}

    # takeTicket function definition
    def takeTicket(self):

         # decrease the amount of tickets available by 1
        self.tickets.remove(self.tickets[-1])
         # decrease the amount of parkingSpaces available by 1
        self.parkingSpaces.remove(self.parkingSpaces[-1])

# function definition for payForParking
def payForParking(self):

    amount = input('Enter 1 to pay now: ')

    if amount == '1':

            # update the "currentTicket" dictionary key "paid" to True
            self.currentTicket['Paid'] = True
            print('ticket has been paid, you have 15 minutes to leave')