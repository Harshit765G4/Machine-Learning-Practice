import json
import random
import string
from pathlib import Path


class Bank:
    database = "data.json"
    data = []

    # Load existing data
    try:
        if Path(database).exists():
            with open(database, "r") as fs:
                data = json.load(fs)
        else:
            print("No database file exists. A new one will be created.")

    except Exception as err:
        print(f"An exception occurred: {err}")

    @classmethod
    def __update(cls):
        """Save current bank data to JSON file."""
        with open(cls.database, "w") as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def __accountgenerate(cls):
        """Generate a random account number."""
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)

        account_id = alpha + num + spchar
        random.shuffle(account_id)

        return "".join(account_id)

    @classmethod
    def __findaccount(cls, accNum, accPin):
        """Find an account using account number and PIN."""

        for account in cls.data:
            if account["accountNo."] == accNum and account["pin"] == accPin:
                return account

        return None

    # --------------------------------------------------
    # CREATE ACCOUNT
    # --------------------------------------------------

    def createaccount(self):
        try:
            name = input("Tell your name: ")
            age = int(input("Tell your age: "))
            email = input("Tell your email: ")
            pin = int(input("Tell your 4 digit PIN: "))

            if age < 18:
                print("Sorry, you must be 18 or above to create an account.")
                return

            if len(str(pin)) != 4:
                print("PIN must contain exactly 4 digits.")
                return

            info = {
                "name": name,
                "age": age,
                "email": email,
                "pin": pin,
                "accountNo.": Bank.__accountgenerate(),
                "balance": 0
            }

            Bank.data.append(info)
            Bank.__update()

            print("\nAccount has been created successfully.")
            print("-" * 30)

            for key, value in info.items():
                print(f"{key}: {value}")

            print("-" * 30)
            print("Please note down your account number.")

        except ValueError:
            print("Please enter valid numeric values.")

    # --------------------------------------------------
    # DEPOSIT MONEY
    # --------------------------------------------------

    def depositmoney(self):
        accNum = input("Please enter your Account Number: ")

        try:
            accPin = int(input("Please enter your PIN: "))
        except ValueError:
            print("PIN must be numeric.")
            return

        userdata = Bank.__findaccount(accNum, accPin)

        if not userdata:
            print("Sorry, no account found.")
            return

        try:
            amount = int(input("Enter amount to deposit: "))
        except ValueError:
            print("Please enter a valid amount.")
            return

        if amount <= 0 or amount > 10000:
            print("You can deposit an amount between 1 and 10000.")
            return

        userdata["balance"] += amount

        Bank.__update()

        print(f"₹{amount} deposited successfully.")
        print(f"Current balance: ₹{userdata['balance']}")

    # --------------------------------------------------
    # WITHDRAW MONEY
    # --------------------------------------------------

    def withdrawmoney(self):
        accNum = input("Please enter your Account Number: ")

        try:
            accPin = int(input("Please enter your PIN: "))
        except ValueError:
            print("PIN must be numeric.")
            return

        userdata = Bank.__findaccount(accNum, accPin)

        if not userdata:
            print("Sorry, no account found.")
            return

        try:
            amount = int(input("Enter amount to withdraw: "))
        except ValueError:
            print("Please enter a valid amount.")
            return

        if amount <= 0 or amount > 10000:
            print("You can withdraw an amount between 1 and 10000.")
            return

        if userdata["balance"] < amount:
            print("Sorry, you have insufficient balance.")
            return

        userdata["balance"] -= amount

        Bank.__update()

        print(f"₹{amount} withdrawn successfully.")
        print(f"Current balance: ₹{userdata['balance']}")

    # --------------------------------------------------
    # SHOW DETAILS
    # --------------------------------------------------

    def showdetails(self):
        accNum = input("Please enter your Account Number: ")

        try:
            accPin = int(input("Please enter your PIN: "))
        except ValueError:
            print("PIN must be numeric.")
            return

        userdata = Bank.__findaccount(accNum, accPin)

        if not userdata:
            print("Sorry, no account found.")
            return

        print("\nYour Account Details")
        print("-" * 30)

        for key, value in userdata.items():
            print(f"{key}: {value}")

    # --------------------------------------------------
    # UPDATE DETAILS
    # --------------------------------------------------

    def updatedetails(self):
        accNum = input("Please enter your Account Number: ")

        try:
            accPin = int(input("Please enter your PIN: "))
        except ValueError:
            print("PIN must be numeric.")
            return

        userdata = Bank.__findaccount(accNum, accPin)

        if not userdata:
            print("Sorry, no account found.")
            return

        print("\nYou cannot change:")
        print("- Age")
        print("- Account Number")
        print("- Balance")

        print("\nLeave a field empty if you don't want to change it.")

        new_name = input("Enter new name: ")
        new_email = input("Enter new email: ")
        new_pin = input("Enter new 4 digit PIN: ")

        if new_name:
            userdata["name"] = new_name

        if new_email:
            userdata["email"] = new_email

        if new_pin:
            if not new_pin.isdigit() or len(new_pin) != 4:
                print("PIN must contain exactly 4 digits.")
                return

            userdata["pin"] = int(new_pin)

        Bank.__update()

        print("Details updated successfully.")

    # --------------------------------------------------
    # DELETE ACCOUNT
    # --------------------------------------------------

    def accdelete(self):
        accNum = input("Please enter your Account Number: ")

        try:
            accPin = int(input("Please enter your PIN: "))
        except ValueError:
            print("PIN must be numeric.")
            return

        userdata = Bank.__findaccount(accNum, accPin)

        if not userdata:
            print("Sorry, no account found.")
            return

        check = input(
            "Press Y if you want to delete the account "
            "or N if you want to cancel: "
        )

        if check.lower() == "n":
            print("Request bypassed.")
            return

        elif check.lower() == "y":
            Bank.data.remove(userdata)
            Bank.__update()

            print("Account deleted successfully.")

        else:
            print("Invalid input.")


# ======================================================
# MAIN PROGRAM
# ======================================================

user = Bank()

print("\n========== BANKING SYSTEM ==========")
print("1. Create an Account")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Show Account Details")
print("5. Update Account Details")
print("6. Delete Account")
print("=====================================")

try:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        user.createaccount()

    elif choice == 2:
        user.depositmoney()

    elif choice == 3:
        user.withdrawmoney()

    elif choice == 4:
        user.showdetails()

    elif choice == 5:
        user.updatedetails()

    elif choice == 6:
        user.accdelete()

    else:
        print("Invalid choice. Please select 1-6.")

except ValueError:
    print("Please enter a valid number.")