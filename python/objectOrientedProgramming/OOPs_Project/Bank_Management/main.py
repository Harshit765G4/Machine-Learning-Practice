import json 
import random
import string 
from pathlib import Path 


class Bank:
    database = 'data.json'
    data = []
    
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exist ")
    except Exception as err:
        print(f"an exception occured as {err}")
    
    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k = 3)
        num = random.choices(string.digits,k= 3)
        spchar = random.choices("!@#$%^&*",k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)



    def createaccount(self):
        info = {
            "name": input("Tell your name :- "),
            "age" : int(input("tell your age :- ")),
            "email": input("tell your email :- "),
            "pin": int(input("tell your 4 number pin :- ")),
            "accountNo." : Bank.__accountgenerate(),
            "balance" : 0
        }
        if info['age'] < 18  or len(str(info['pin'])) != 4:
            print("sorry you cannot create your account")
        else:
            print("account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account number")

            Bank.data.append(info)

            Bank.__update()

    def depositmoney(self):
        accNum = input("Please Enter your Account Number: ")
        accPin = int(input("Please Enter your PIN: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accNum and i['pin'] == accPin]

        if userdata == False:
            print("Sorry No Data Found")
        else:
            amount = int(input("Enter how much amount you want to Deposit: "))
            if amount > 10000 or amount < 0:
                print("Sorry you can only Deposit the amount below 10000")
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("your amount get Deposit successfully.")

    def withdrawmoney(self):
        accNum = input("Please Enter your Account Number: ")
        accPin = int(input("Please Enter your PIN: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accNum and i['pin'] == accPin]

        if userdata == False:
            print("Sorry No Data Found")
        else:
            withdrawamount = int(input("Enter how much amount you want to withdraw: "))
            if withdrawamount > 10000 or withdrawamount < 0:
                print("Sorry you can only withdraw the amount below 10000")
            elif userdata[0]['balance'] < withdrawamount:
                print("Sorry you have low balance.")
            else:
                userdata[0]['balance'] -= withdrawamount
                Bank.__update()
                print("your amount is withdrawn successfully.")

user = Bank()

print("Press 1 for Creating an Account")
print("Press 2 for Depositing Money in the bank")
print("Print 3 for Withdrawing the money")
print("Press 4 for Details")
print("Press 5 for updating the details")
print("press 6 for deleting your Account")

check = int(input("tel your respone:- "))

if check == 1:
    user.createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()