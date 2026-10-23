class Vehicle:

    def __init__(self, fares, total_price):
        self.fares = fares
        self.total_price = total_price

Bus = Vehicle(1000, 2000)

print("Bus fares:", Bus.fares)
print("Total price of the bus costs including fares and maintenance:", Bus.total_price)