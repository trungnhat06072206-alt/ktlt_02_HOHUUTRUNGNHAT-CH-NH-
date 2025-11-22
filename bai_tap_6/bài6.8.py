print("ho huu trung nhat")
print("mssv 245752021610023")

class Bank:
    Account_type = "Savings"
    location = "Guntur"

    def __init__(self, name, Account_Number, balance):
        self.name = name
        self.Account_Number = Account_Number
        self.balance = balance
        self.self_Account_type = Bank.Account_type
        self.self_location = Bank.location

    def __repr__(self):
        print("Welcome to the SBI ATM Machine")
        print("--------------------------------")
        account_pin = int(input("Please enter your pin number: "))

        if account_pin == 123:
            self.Account()
        else:
            print("Pin Incorrect. Please try again")
            self.Error()

        return ' '.join([self.name, str(self.Account_Number)])

    def Error(self):
        account_pin = int(input("Please enter your pin number: "))
        if account_pin == 123:
            self.Account()
        else:
            print("Pin Incorrect. Please try again")
            self.Error()

    def Account(self):
        print("Your Card Number is: XXXX XXXX XXXX 1337")
        print("Would you like to deposit/withdraw/check balance?")
        print("""
1) Balance
2) Withdraw
3) Deposit
4) Quit
""")
        option = int(input("Please enter your choice: "))

        if option == 1:
            self.Balance()
        elif option == 2:
            self.Withdraw()
        elif option == 3:
            self.Deposit()
        elif option == 4:
            self.Exit()
        else:
            print("Invalid choice.")
            self.Account()

    def Balance(self):
        print("Balance:", self.balance)
        self.Account()

    def Withdraw(self):
        w = int(input("Please enter withdraw amount: "))
        if self.balance >= w:
            self.balance -= w
            print("Your transaction is successful.")
            print("Your Balance:", self.balance)
        else:
            print("Transaction cancelled.")
            print("Amount not sufficient.")
        self.Account()

    def Deposit(self):
        d = int(input("Please enter deposit amount: "))
        self.balance += d
        print("Your transaction is successful.")
        print("Balance:", self.balance)
        self.Account()

    def Exit(self):
        print("Exit")

# Test
t1 = Bank("mahesh", 1453210145, 5000)
print(t1)
