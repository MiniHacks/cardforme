import heapq
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

def extract_max_values(k):
    # Create a max heap (negate the values to simulate a max heap)

    heapq.heappush(max_heap, (-self.card.flights, "Flights"))
    heapq.heappush(max_heap, (-self.card.groceries, "Groceries"))
    heapq.heappush(max_heap, (-self.card.gas, "Gas"))
    heapq.heappush(max_heap, (-self.card.dining, "Dining"))
    heapq.heappush(max_heap, (-self.card.entertainment, "Entertainment"))
    heapq.heappush(max_heap, (-self.card.car_rental, "Car Rental"))
    heapq.heappush(max_heap, (-self.card.hotel, "Hotel"))
    heapq.heappush(max_heap, (-self.card.retail, "Retail"))


    max_values = []
    for _ in range(k):
        if max_heap:
            max_value = -heapq.heappop(max_heap)  # Negate back to get the actual max value
            max_values.append(max_value)
        else:
            break

    return max_values

# Example usage:
my_list = [3, 1, 7, 2, 8, 5]
k = 2  # Number of max values to extract
max_vals = extract_max_values(my_list, k)
print("Max Values:", max_vals)
