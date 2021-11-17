class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, amount):
        self.till += amount

    def sell_drink(self, customer, drink):
        if self.check_age(customer):
            customer.reduce_wallet(drink.price)
            self.increase_till(drink.price)

    def check_age(self, customer):
        return customer.age >= 18

    def add_drink(self, drink):
        self.drinks.append(drink)
