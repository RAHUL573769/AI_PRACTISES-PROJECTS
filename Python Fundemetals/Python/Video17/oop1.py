# class ATM:
#     # constructor
#     def __init__(self):
#         self.pin = ''
#         self.balance = 0
#         self.menu()

#     def menu(self):
#         userInput = input("""
# Welcome to ATM

# 1. Create PIN
# 2. Deposit
# 3. Withdraw
# 4. Check Balance
# 5. Exit

# Enter your choice: """)

#         if userInput == '1':
#             self.create_pin()

#         elif userInput == '2':
#             self.deposit()

#         elif userInput == '3':
#             self.withdraw()

#         elif userInput == '4':
#             self.check_balance()

#         elif userInput == '5':
#             print("Thank you for using ATM")

#         else:
#             print("Invalid choice")

#     def create_pin(self):
#         self.pin = input("Create your PIN: ")
#         print("PIN created successfully")

#     def deposit(self):
#         temp = input("Enter your PIN: ")

#         if temp == self.pin:
#             amount = int(input("Enter amount to deposit: "))
#             self.balance += amount
#             print("Deposit successful")
#         else:
#             print("Incorrect PIN")

#     def withdraw(self):
#         temp = input("Enter your PIN: ")

#         if temp == self.pin:
#             amount = int(input("Enter amount to withdraw: "))

#             if amount <= self.balance:
#                 self.balance -= amount
#                 print("Withdrawal successful")
#             else:
#                 print("Insufficient balance")
#         else:
#             print("Incorrect PIN")

#     def check_balance(self):
#         temp = input("Enter your PIN: ")

#         if temp == self.pin:
#             print("Your balance is:", self.balance)
#         else:
#             print("Incorrect PIN")


# # object creation
# obj = ATM()

class ATM_NEW:

    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()   # calling menu

    def menu(self):

        userInput = input("""
Welcome to ATM

1. Create PIN
2. Deposit
3. Withdraw
4. Check Balance
5. Exit

Enter your choice: """)

        if(userInput == "1"):
            print("Create Pin")
            self.create_pin()

    def create_pin(self):

        self.pin = input("Create your PIN: ")
        print("PIN created successfully")


obj = ATM_NEW()

# What is constructor?
# constructor is a special method which is automically called whwn instance of class created

# class Fraction:
#     def __add__(self,x,y):
#         self.num1=x
#         self.num2=y
#     def __str__(self):
#         number= '{}/{}'.format(self.num1,self.num2)
#         return number


# result=Fraction(23,43)
# print(result)



class   Fraction1:
    def __init__(self,x,y):
        self.num=x
        self.den=y
    def __str__(self):
        result2="{}/{}".format(self.num,self.den)
        print(result2)

fraction=Fraction1(12,45)
print(fraction)