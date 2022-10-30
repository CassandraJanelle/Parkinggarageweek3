
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


class parkingGarage():
    def __init__(self, tickets, parkingSpaces, currentTicket, licensePlate):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
        self.licensePlate = licensePlate 
        
    
    def takeTicket(self):
        userTalk = str(input('What is your license plate number? '))
        if self.tickets == []:
            print('Sorry, the garage is at capacity.')
        else:
            self.currentTicket[self.tickets[0]] = 'not paid'
            print(f'Your ticket number is {self.tickets[0]}')
            del self.tickets[0]
            del self.parkingSpaces[0]
            
         
    def payForParking(self):
        userTalk = int(input('What is your ticket number? '))
        
        if userTalk < 1 or userTalk > 5:              
            print('This is not a ticket.')
        
        elif userTalk not in self.currentTicket:
            print('Please enter a valid ticket number.')
        
        else:
            if self.currentTicket[userTalk] == 'not paid':
                payment = input('Type "pay" to pay. ')
                self.currentTicket[userTalk] = 'paid'
                print(self.currentTicket)        
            
                       
    def leaveGarage(self):
        userTalk = int(input('What is your ticket number? '))
        
        if userTalk not in self.currentTicket:
            print('Please enter a valid ticket number.')
        
        elif self.currentTicket[userTalk] == 'Paid. You have 15 minutes to leave!':
            print('Come again soon!')
            self.tickets.insert(0, userTalk)
            self.parkingSpaces.insert(0, userTalk)
            del self.currentTicket[userTalk]                
            self.tickets.sort()
            self.parkingSpaces.sort()
        
        elif self.currentTicket[userTalk] == 'not paid':
            print('Please pay before leaving.')
      
        else:
            print('Please pay before leaving.')

def park():
        parking = parkingGarage([1,2,3,4,5], [1,2,3,4,5], {}, {})
        while True:
            userTalk = input('Welcome. Would you like to park, pay, or leave? ')
            
            if userTalk.lower() == 'park':
                parking.takeTicket()
                        
            elif userTalk.lower() == 'pay':
                parking.payForParking()
                
            elif userTalk.lower() == 'leave':
                parking.leaveGarage()
            
            elif userTalk.lower() == 'quit':
                break
            
            else:
                print('Type a valid command.')

park()
