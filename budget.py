class Category:
    def __init__(self, name, funds=0) -> None:
        self.ledger = list()
        self.funds = funds
        self.name = name

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.funds += amount

    def check_funds(self, amount):
        if amount > self.funds:
            return False
        else:
            return True

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount=amount):
            return False
        else:
            self.ledger.append({"amount": -amount, "description": description})
            self.funds += -amount
            return True

    def get_balance(self):
        print(f"The current balance is: {self.funds}")

    def transfer(self, amount, dest_categ):
        if not self.check_funds(amount=amount):
            return False
        else:
            self.withdraw(amount=amount, description=f"Transfer to {self.dest_categ}")
            try:
                dest_categ.deposit(
                    amount=amount, description=f"Transfer from {self.name}"
                )
                return True
            except:
                print("The destination category should be an object of the same class")
                return False

    def __repr__(self) -> str:
        print(self.name.center(30, "*"))  # ****Food*** 30 chars centered
        for (
            record
        ) in (
            self.ledger
        ):  # printing records and name of transaction left aligned, amount right aligned
            print(self.name.center(30, "*"))

            dscrptn_prntd = record["description"]
            scr_prntd = str("{:.2f}".format(record["amount"]))

            print(f"{dscrptn_prntd.ljust(23)}{scr_prntd.rjust(7)}")


def create_spend_chart(self, categories):
    pass
