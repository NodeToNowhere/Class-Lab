class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
        self.max_drunkeness = 10

    def increase_till(self, price):
        self.till += price

    def check_age(self, customer):
        return customer.age >= 18

    def add_drink(self, drink):
        self.drinks.append(drink)

    def sell_drink(self, customer, drink):
        if self.check_age(customer) and customer.wallet >= drink.price and customer.drunkeness < self.max_drunkeness:
            customer.reduce_wallet(drink.price)
            self.increase_till(drink.price)
            customer.drunkeness += drink.alcohol_level
        
