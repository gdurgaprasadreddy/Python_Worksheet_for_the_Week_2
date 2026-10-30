class BankAccount:

    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
            print("Updated Balance:", self.balance)
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")

        elif amount > self.balance:
            print("Insufficient balance.")

        else:
            self.balance -= amount
            print("Withdrawal successful.")
            print("Remaining Balance:", self.balance)

    def check_balance(self):
        print("Account Number:", self.account_number)
        print("Account Holder:", self.account_holder_name)
        print("Available Balance:", self.balance)

account = BankAccount(12345, "Durga", 50000)

while True:
    print("\n===== BANK MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        elif choice == 2:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif choice == 3:
            account.check_balance()

        elif choice == 4:
            print("Thank you for using our banking system!")
            break

        else:
            print("Invalid choice! Please select 1 to 4.")

    except ValueError:
        print("Invalid input! Please enter a valid number.")
