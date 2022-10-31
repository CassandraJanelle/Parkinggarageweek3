import time
from tkinter import N

# ParkingGarage class definition
class ParkingGarage():

    # ParkingGarage constructor definition
    def __init__(self):
        self.tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.parkingSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.currentTicket = {}

    # takeTicket function definition
    def takeTicket(self):
        # Check if any tickets/spots are available
        time.sleep(.5)
        print("\n------ Checking for Available Spots ------")
        time.sleep(.5)
        if self.tickets == []:
            print("\nIf only you knew the power of the Park Side.... but you won't since the garage is full!")
        else:
            # set printed ticket to unpaid
            self.currentTicket[self.tickets[0]] = False
            time.sleep(.5)
            print("\n------ Fetching Ticket ------")
            time.sleep(.5)
            print(f'\nYour ticket number is {self.tickets[0]}')
            # decrease the amount of tickets available by 1
            del self.tickets[0]
            # decrease the amount of parkingSpaces available by 1
            del self.parkingSpaces[0]

    def payForParking(self):
        ticket_num = int(input("\nEnter your ticket number: "))
        time.sleep(.5)
        print("\n------ Checking Ticket ------")
        time.sleep(.5)
        # Check if ticket number has been taken
        if ticket_num in self.currentTicket:
            # Any payment amount suffices as long as integer value is over 0
            payment = 0
            while payment <= 0:
                payment = int(input("\nPlease enter payment amount: "))
                time.sleep(0.5)
                print("\n------ Processing Payment ------")
                time.sleep(.5)
                print("\n------ Payment Successful ------")
                time.sleep(.5)
                print("\n------ You have 15 min to exit garage ------")
                if payment <= 0:
                    print("Invalid amount")
        else:
            print("Ticket number not valid!")
            return
        self.currentTicket[ticket_num] = True
    
    def leaveGarage(self):
    # userTalk = int(input('What is your ticket number? '))
    
    # if userTalk not in self.currentTicket:
    #     print('Please enter a valid ticket number.')
        ticket_num = int(input("Enter your ticket number: "))
        time.sleep(.5)
        print("\n------ Checking Ticket ------")
        time.sleep(.5)
        # Check if ticket has been pulled then check if it has been paid
        if ticket_num in self.currentTicket.keys():
            # If paid then return ticket number into pool and update parking spaces
            if self.currentTicket[ticket_num] == True:
                print("\nThanks for parking at 'Park Side of the Moon', where if you don't pay there will be tyre consequences!")
                self.tickets.append(ticket_num)
                self.parkingSpaces.append(ticket_num)
                # Remove ticket from currentTickets
                del self.currentTicket[ticket_num]
                self.tickets.sort()
                self.parkingSpaces.sort()
            # If ticket has not been paid, remind them to pay
            elif self.currentTicket[ticket_num] == False:
                print("\nYou're parking up the wrong tree, Please pay before leaving.")
        else:
            print("\nInvalid response!")


    def run(self):
        # Prompt when entering garage
        print("Welcome to 'Park side of the Moon")
        print("""
        What would you like to do?
        1 - Take Ticket
        2 - Pay for Parking
        3 - Leave Garage
        4 - Quit
        """)

        while True:
            # Print number of available spots whenever returning to menu
            print(f"\nCurrently there are {len(self.parkingSpaces)} available spots.")
            response = input("\nChoose a numbered option from list (1, 2, 3, 4): ")

            if response == '1':
                self.takeTicket()
            elif response == '2':
                self.payForParking()
            elif response == '3':
                self.leaveGarage()
            elif response == '4':
                print("\nThanks for coming to 'Park Side of the Moon', where if you don't pay there will be tyre consequences!\n")
                break
            else:

                print("Invalid response, please choose numbered option from list!")

park = ParkingGarage()
park.run()