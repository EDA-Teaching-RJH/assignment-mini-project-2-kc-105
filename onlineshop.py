import sys
import re
class Customer:
    def __init__(self,username,password,wallet,email):
        self.username = username
        self.password = password
        self.wallet = wallet
        self.email = email

    def getuser(self):

class product:
    def __init__(self,product_id,product_name,description,price,review,stock):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.__price = price
        self.review = review
        self.stock = stock

    def reducestock(self, quantity):
        if quantity <= self.stock:
            self.stock = self.stock - 1
            return True
        else:
            print(f"Not enough stock left of {self.name}")
            return False
        
    def get_price(self): #can create employee discounts using polymorphism
        return self.price
        

    def displayinfo(self):
        return f"[{self.product_name}({self.product_id}): {self.price:.2f} (stock:{self.stock})]"
    
    def detailed_view(self):
        return f"[{self.product_name}({self.product_id}): {self.price:.2f} (stock:{self.stock}) {self.description} {self.review}]"
    
    def product_search(self):
    #allow the user to search for certain items 


class clothes(product):
    def __init__(self,product_name,description,price,review,stock,size):
        super().__init__(product_name,description,price,review,stock)
        self.size = size

    def displayinfo(self):# will display the size as well
        return f"[{super().displayinfo()} size:{self.size}]"
    
    def detailed_view(self):
        return f"[{super().displayinfo()} size:{self.size}]"
        
class electronics(product):
    def __init__(self,product_name,description,price,review,stock,warranty):
        super().__init__(product_name,description,price,review,stock)
        self.warranty = warranty

    def displayinfo(self):# will display the warranty as well
        return f"[{super().displayinfo()} size:{self.warranty}]"
    
    def detailed_view(self):
        return f"[{super().displayinfo()} size:{self.warranty}]"

class cart:
    def __init__(self,cart_contents):
        self.cart_contents = []
    
    def add_item():
    def remove_item():
    def total_price():
    def total_items():
            

class order:
    def __init__(self,order_id,address,date,customer):
        self.order_id = order_id
        self.address = address
        self.date = date
        self.customer = customer

    def order_summary():

def main():
    user_login()
    print("---MAIN SHOP PAGE---")
    print("")
    print("")
    print ("~~~~~~~~~~~~~~~~~~")#main menu

def new_user():
    newuser = input("please enter a new unique username:")   
    while True:
        newemail= input("please enter a new unique email")
        validemailtest(newemail)        
    newpassword = input("please enter a new unique password:")

def validemailtest(newemail):
    validemailtest = r'[^a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9-.]+$'
    if re.fullmatch(newemail, validemailtest)
        return False
    else
        print ("please enter a valid email")

def user_login():#let the user login with their username and password
    while True:
        print("Welcome ")
        print("Please Login")
        currentuser = input("username:")#if usernot found offer to create new user
        currentpassword = input("password")
        if usernotfound:
            input("would you like to make a new user(y/n)")
            new_user    
    
def product_browsing():
    #allow the user to scroll through different items nad pages

def product_search(self):
    #allow the user to search for certain items