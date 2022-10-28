class Garage:
    def __init__(self):
        self.tickets = []
        self.parkingSpaces = []
        self.currentTicket = {}

    def takeTicket(self):
        if self.tickets == []:
            print("Parking lot is full")
        else:
            for ticket in self.tickets:
                self.tickets.pop(ticket)

    def run(self):