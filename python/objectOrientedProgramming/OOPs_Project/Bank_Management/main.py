import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database,'r') as fs:
                data = json.load(fs)
        else:
            print("No such file exists")
    except Exception as err:
        print(f"An Exception occured as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(cls.data))

    @classmethod
    def __accountNoGenerator(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spchar = random.choices("!@#$%^&*",k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return  "".join(id)
    

    def createAccount(self):
        info = {
            "name": input("Enter You Full Name in Capital:- "),
            "age": int(input("Enter You age:- ")),
            "email": input("Enter your Email:- "),
            "pin": int(input("Enter a 4 Digit PIN to create Account:- "))
            ,"accountNo.": Bank.__accountNoGenerator(),
            "balance": 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry You cannot create your Account.")
        else:
            print("Account has been Created Successfully.")
            for i in info:
                print(f"{i}:{info[i]}")
            print("Please Note Down Your Account Number.")
            Bank.data.append(info)


            Bank.__update()



user = Bank()

print("Press 1 for Creating an Account")
print("Press 2 for Depositing Money in the bank")
print("Print 3 for Withdrawing the money")
print("Press 4 for Details")
print("Press 5 for updating the details")
print("press 6 for deleting your Account")

check = int(input("tel your respone:- "))

if check == 1:
    user.createAccount()