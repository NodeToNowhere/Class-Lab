class Customer:
    def __init__(self, name, wallet, age):
        self.drunkeness = 0
        self.name = name
        self.wallet = wallet
        self.age = age

    def reduce_wallet(self, price):
        self.wallet -= price
