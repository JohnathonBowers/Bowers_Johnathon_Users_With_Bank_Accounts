class BankAccount:
    all_account_info = []
    
    def __init__(self, int_rate, balance):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        BankAccount.all_account_info.append(self.balance)
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self
    
    @classmethod
    def all_instances(cls):
        print(BankAccount.all_account_info)

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.checking = BankAccount(0.01, 0)
        self.savings = BankAccount(0.01, 0)

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print ("Insufficient points to spend this amount.")
            return False
        else:
            self.gold_card_points -= amount

    def make_deposit(self, account, amount):
        if account == "checking":
            self.checking.deposit(amount)
        elif account == "savings":
            self.savings.deposit(amount)
        return self

    def make_withdrawal(self, account, amount):
        if account == "checking":
            self.checking.withdraw(amount)
        elif account == "savings":
            self.savings.withdraw(amount)
        return self
    
    def transfer_money(self, amount, from_account, other_user, to_account):
        if from_account == "checking":
            self.checking.withdraw(amount)
        if from_account == "savings":
            self.savings.withdraw(amount)
        if other_user == "lebron":
            if to_account == "checking":
                lebron.checking.deposit(amount)
            if to_account == "savings":
                lebron.savings.deposit(amount)
        if other_user == "stephen":
            if to_account == "checking":
                stephen.checking.deposit(amount)
            if to_account == "savings":
                stephen.savings.deposit(amount)
        if other_user == "giannis":
            if to_account == "checking":
                giannis.checking.deposit(amount)
            if to_account == "savings":
                giannis.savings.deposit(amount)

    def display_user_balance(self):
        print(f"User: {self.first_name}, Checking Balance: ${self.checking.balance}")
        print(f"User: {self.first_name}, Savings Balance: ${self.savings.balance}")

lebron = User("LeBron", "James", "ljames@email.com", 37)

stephen = User("Stephen", "Curry", "scurry@email.com", 34)

giannis = User("Giannis", "Antetokounmpo", "gantetokounmpo@email.com", 27)

lebron.make_deposit("checking", 1000)

lebron.transfer_money(200, "checking", "giannis", "savings")

lebron.display_user_balance()

giannis.display_user_balance()