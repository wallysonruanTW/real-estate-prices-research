import datetime


class RealState:
    def __init__(self, address, price, date_of_creation=datetime.date.today()):
        self.address = address
        self.price = price
        self.dateOfCreation = date_of_creation
