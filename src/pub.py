class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, price):
        self.till += price

    def check_age(self, customer):
        return customer.age >= 18

    def add_drink(self, drink):
        self.drinks.append(drink)

    def sell_drink(self, customer, drink):
        if self.check_age(customer):
            customer.reduce_wallet(drink.price)
            self.increase_till(drink.price)
        
