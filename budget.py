class Category:
    ledger = list()
    fund = 0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.fund += amount

    def withdraw(self, amount, description=""):
        if self.fund < amount:
            return False
        else:
            self.ledger.append({"amount": -amount, "description": description})
            return True

    def get_balance(self):
        print(self.fund)

    def transfer(amount, dest_categ):
        pass

    def check_funds():
        pass

    pass


def create_spend_chart(categories):
    pass
