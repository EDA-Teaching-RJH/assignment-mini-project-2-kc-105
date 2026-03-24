import sys
class Customer:
    def __init__(self,username,password,wallet,email):
        self.username = username
        self.password = password
        self.wallet = wallet
        self.email = email


class product:
    def __init__(self,product_name,description,price,review,stock):
        self.product_name = product_name
        self.description = description
        self.price = price
        self.review = review
        self.stock = stock

    def reducestock(stock):
        stock = stock - 1

    def getinformation(product_name,description,price,stock):
        

class clothes(product):
    def __init__(self,product_name,description,price,review,stock,size):
        super().__init__(product_name,description,price,review)
        self.size = size

    def getclothesinformation(product_name, description, price, stock, size):
        
class electronice(product):
    def __init__(self,product_name,description,price,review,stock,warranty):
        super().__init__(product_name,description,price,review)
        self.warranty = warranty

    def getelectronicsinformation(product_name, description, price, stock, warranty):

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

    def invoice():

def main():
    
    while True:
        print("Welcome ")
        print("Please Login")
        currentuser = input("username:")#if usernot found offer to create new user
        currentpassword = input("password")
        if usernotfound:

        print("---MAIN SHOP PAGE---")
        print("")
        print("")

    print ("~~~~~~~~~~~~~~~~~~")#main menu


def user_login():
    #let the user login with their username and password

def cart():
    #store the users items saved to cart
    
def product_browsing():
    #allow the user to scroll through different items nad pages

def product_search():
    #allow the user to search for certain items

def order_summary():
    #when the user wants to check out give a summary of all items

def 