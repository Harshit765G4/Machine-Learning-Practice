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
        """Save bank data to JSON."""
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
    def __findaccount(cls, acc_num, acc_pin):
        """Find account using account number and PIN."""

        for account in cls.data:
            if (
                account["accountNo."] == acc_num
                and account["pin"] == acc_pin
            ):
                return account

        return None

    @classmethod
    def create_account(cls, name, age, email, pin):

        if age < 18:
            return False, "You must be 18 or above."

        if len(str(pin)) != 4:
            return False, "PIN must contain exactly 4 digits."

        account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo.": cls.__accountgenerate(),
            "balance": 0
        }

        cls.data.append(account)
        cls.__update()

        return True, account

    @classmethod
    def deposit_money(cls, acc_num, acc_pin, amount):

        account = cls.__findaccount(acc_num, acc_pin)

        if not account:
            return False, "Invalid account number or PIN."

        if amount <= 0:
            return False, "Amount must be greater than 0."

        if amount > 10000:
            return False, "Maximum deposit is ₹10,000."

        account["balance"] += amount

        cls.__update()

        return True, account["balance"]

    @classmethod
    def withdraw_money(cls, acc_num, acc_pin, amount):

        account = cls.__findaccount(acc_num, acc_pin)

        if not account:
            return False, "Invalid account number or PIN."

        if amount <= 0:
            return False, "Amount must be greater than 0."

        if amount > 10000:
            return False, "Maximum withdrawal is ₹10,000."

        if account["balance"] < amount:
            return False, "Insufficient balance."

        account["balance"] -= amount

        cls.__update()

        return True, account["balance"]

    @classmethod
    def get_details(cls, acc_num, acc_pin):

        account = cls.__findaccount(acc_num, acc_pin)

        if not account:
            return None

        return account

    @classmethod
    def update_details(
        cls,
        acc_num,
        acc_pin,
        name=None,
        email=None,
        pin=None
    ):

        account = cls.__findaccount(acc_num, acc_pin)

        if not account:
            return False, "Invalid account number or PIN."

        if name:
            account["name"] = name

        if email:
            account["email"] = email

        if pin:

            if not pin.isdigit() or len(pin) != 4:
                return False, "PIN must contain exactly 4 digits."

            account["pin"] = int(pin)

        cls.__update()

        return True, "Account details updated successfully."

    @classmethod
    def delete_account(cls, acc_num, acc_pin):

        account = cls.__findaccount(acc_num, acc_pin)

        if not account:
            return False, "Invalid account number or PIN."

        cls.data.remove(account)

        cls.__update()

        return True, "Account deleted successfully."