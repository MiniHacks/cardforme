import heapq


class Transactions:

    def __init__(self):
        self.flights = 0.0  # 'Airlines and Aviation Services'
        self.groceries = 0.0
        self.gas = 0.0  # 'Taxi'
        self.dining = 0.0  # 'Restaurants'
        self.entertainment = 0.0
        self.car_rental = 0.0
        self.hotel = 0.0
        self.retail = 0.0

        self.digital_wallet = False
        self.total = 0.0

    #         for transaction in response:
    #             if transaction.category == "Flights":
    #                 self.flights += transaction.amount
    #             elif transaction.category == "Groceries":
    #                 self.groceries += transaction.amount
    #             elif transaction.category == "Gas":
    #                 self.gas += transaction.amount
    #             elif transaction.category == "Dining":
    #                 self.dining += transaction.amount
    #             elif transaction.category == "Entertainment":
    #                 self.entertainment += transaction.amount
    #             elif transaction.category == "Car Rental":
    #                 self.car_rental += transaction.amount
    #             elif transaction.category == "Hotel":
    #                 self.hotel += transaction.amount
    #
    #             self.total += transaction.amount

    def set_benefits(self, benefits):
        self.benefits = benefits

    def extract_max_values(self, k):
        # Create a max heap (negate the values to simulate a max heap)
        max_heap = []

        heapq.heappush(max_heap, (-self.flights, "Flights"))
        heapq.heappush(max_heap, (-self.groceries, "Groceries"))
        heapq.heappush(max_heap, (-self.gas, "Gas"))
        heapq.heappush(max_heap, (-self.dining, "Dining"))
        heapq.heappush(max_heap, (-self.entertainment, "Entertainment"))
        heapq.heappush(max_heap, (-self.car_rental, "Car Rental"))
        heapq.heappush(max_heap, (-self.hotel, "Hotel"))
        heapq.heappush(max_heap, (-self.retail, "Retail"))

        max_values = []
        for i in range(k):
            if max_heap:
                _, category = heapq.heappop(max_heap)  # Negate back to get the actual max value
                max_values.append(category)
            else:
                break

        return max_values

    def add_transaction(self, category, amount):
        self.total += amount
        if category == "Airlines and Aviation Services":
            self.flights += amount
        elif category == "Groceries":
            self.groceries += amount
        elif category == "Gas":
            self.gas += amount
        elif category == "Restaurants":
            self.dining += amount
        elif category == "Entertainment":
            self.entertainment += amount
        elif category == "Car Rental":
            self.car_rental += amount
        elif category == "Hotel":
            self.hotel += amount
        elif category == "Retail":
            self.retail += amount
