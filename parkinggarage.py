
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

    def payForParking(self):
        payment = 0
        while payment <=0:
            payment = input("Please enter payment amount: ")
            if payment <= 0:
                print("Invalid amount")
        
        self.curentTicket['paid'] = True
    

    def run(self):
        print("""
        What would you like to do?
        1 - Take Ticket
        2 - Pay for Parking
        3 - Leave Garage
        4 - Quit
        """)

        while True:
            response = input("Choose a numbered option from list: ")

            if response == '1':
                self.takeTicket()
            elif response == '2':
                self.payForParking
            elif response == '3':
                self.leaveGarage()
            elif response == '4':
                print("Thanks for coming to 'Parking up the wrong tree', where if you don't pay there will be tyre consequences!")
                break
            else:
                print("Invalid response, please choose numbered option from list!")