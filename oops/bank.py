
class Account:
    bankName="SBI"
    AccountNumbers=1000
    def __init__(self,name,mob,initailBalance):
        if initailBalance<=100:
            raise Exception("Your initial balance shoud be greterthen 100")
        self.initailBalance=initailBalance
        self.name=name
        self.mob=mob
        Account.AccountNumbers += 1
        self.AccountNumbers=Account.AccountNumbers
    def showInfo(self):
        print("="*30)
        print("Bank Name :",self.bankName)
        print("Account Number : ",self.AccountNumbers)
        print("Name: ",self.name)
        print("Mob : ",self.mob)
        print("Balance : ",self.initailBalance)

ac1=None
ac2=None
ac3=None
try:
   
    ac2=Account("Lalit",223,10000)
    ac3=Account("Krapansh",54365,10000)
    ac1=Account("Rakesh ",9876,1)
    
except Exception as e:
    print(e)

try:
    ac2.showInfo()
    ac3.showInfo()
    ac1.showInfo()
except Exception as e:
    print(e)




# class Account:
#     bankName = "SBI"
#     AccountNumbers = 1000

#     def __init__(self, name, mob, initialBalance):
#         if initialBalance < 100:
#             raise ValueError("Your initial balance should be at least 100")

#         self.initialBalance = initialBalance
#         self.name = name
#         self.mob = mob

#         Account.AccountNumbers += 1
#         self.AccountNumbers = Account.AccountNumbers

#     def showInfo(self):
#         print("=" * 30)
#         print("Bank Name:", self.bankName)
#         print("Account Number:", self.AccountNumbers)
#         print("Name:", self.name)
#         print("Mob:", self.mob)
#         print("Balance:", self.initialBalance)


# ac2 = Account("Lalit", 223, 10000)
# ac3 = Account("Krapansh", 54365, 500)
# ac1 = Account("Rakesh", 9876, 10)

# ac2.showInfo()
# ac3.showInfo()
# ac1.showInfo()
