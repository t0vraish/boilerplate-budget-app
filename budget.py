class Category:
    def __init__(self, name, funds=0) -> None:
        self.ledger = list()
        self.name = name
        self.funds = funds

    def check_funds(self, amount):
        return amount <= self.funds

    def get_balance(self):
        # entry_txt="The current balance is:"
        return f"Total: {'{:.2f}'.format(self.funds)}"

    def deposit(self, amount, description="Deposit"):
        self.ledger.append({"amount": amount, "description": description})
        self.funds += amount

    def withdraw(self, amount, description="Withdraw"):
        if not self.check_funds(amount):
            return False
        self.deposit(-amount, description)
        return True

    def transfer(self, amount, dest_categ):
        self.withdraw(amount, description=f"Transfer to {dest_categ.name}")
        dest_categ.deposit(amount=amount, description=f"Transfer from {self.name}")
        return True

    def __str__(self) -> str:
        def format_amount(amount):
            return f"{amount:.2f}"

        title = self.name.center(30, "*")  # ****Food*** 30 chars centered
        main_lst = list()
        for (
            record
        ) in (
            self.ledger
        ):  # printing records and name of transaction left aligned, amount right aligned
            dscrptn_prntd = record["description"]
            scr_prntd = str("{:.2f}".format(record["amount"]))
            main_lst.append(f"{dscrptn_prntd.ljust(23)}{scr_prntd.rjust(7)}")
        main_txt = "\n".join(main_lst)
        total = self.get_balance()

        return "\n".join([title, main_txt, total])


def create_spend_chart(categories):
    for category in categories:
        pass


##SOME INITIAL TESTING FOR THE CLASS##
# food = Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and dessert")

# clothing = Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)

# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.transfer(400, food)
# auto.withdraw(15)

# print(f"{food}\n")
# print(clothing)
# print(f"\n{auto}")
