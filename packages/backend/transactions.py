class Transactions:

    def __init__(self, response):
        self.flights = 0.0
        self.groceries = 0.0
        self.gas = 0.0
        self.dining = 0.0
        self.entertainment = 0.0
        self.car_rental = 0.0
        self.hotel = 0.0
        self.retail = 0.0

        self.digital_wallet = False
        self.total = 0.0

        for transaction in response:
            if transaction.category == "Flights":
                self.flights += transaction.amount
            elif transaction.category == "Groceries":
                self.groceries += transaction.amount
            elif transaction.category == "Gas":
                self.gas += transaction.amount
            elif transaction.category == "Dining":
                self.dining += transaction.amount
            elif transaction.category == "Entertainment":
                self.entertainment += transaction.amount
            elif transaction.category == "Car Rental":
                self.car_rental += transaction.amount
            elif transaction.category == "Hotel":
                self.hotel += transaction.amount

            self.total += transaction.amount

    def set_benefits(self, benefits):
        self.benefits = benefits
