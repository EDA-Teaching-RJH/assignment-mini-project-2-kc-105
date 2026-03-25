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
    
    def get_price(self):
        return self.price * 0.9#if customer is employee 10% discount
        
        
class electronics(product):
    def __init__(self,product_name,description,price,review,stock,warranty):
        super().__init__(product_name,description,price,review,stock)
        self.warranty = warranty

    def displayinfo(self):# will display the warranty as well
        return f"[{super().displayinfo()} size:{self.warranty}]"
    
    def detailed_view(self):
        return f"[{super().displayinfo()} size:{self.warranty}]"

class cart:
    def __init__(self):
        self.cart_contents = []

    def cartquantity(self):
        total = 0 
        for item in self.cart_contents:
            total = total + item["quantity"]
        return total

    
    def add_item(self, product, quantity):#will add items to the cart
        if product.reducestock(quantity):
            self.cart_contents.append({"product": product, "quantity":quantity})
        else:
            print("Item not added to cart")

    def remove_item(self):
    def total_price(self):
        total = 0 
        for item in self.cart_contents:
            total = total + item["product"].get_price * item["quantity"]
        return total

    def view_cart(self):
        if not self.cart_contents:
            print("No items in Cart")
            return 
        print("Shopping Cart")
        print("    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("    ⣿⣷⣤⣄⣉⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("    ⣿⣿⣿⣿⣿⣷⡄⠹⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿")
        print("    ⣿⣿⣿⣿⣿⣿⣿⡄⢰⣶⣶⣶⣶⡆⢰⣶⣶⣶⣶⠀⣶⣶⣶⣶⣶⠆⣸⣿⣿⣿")
        print("    ⣿⣿⣿⣿⣿⣿⣿⣷⠀⠿⠿⠿⠿⠇⠘⠿⠿⠿⠿⠀⠻⠿⠿⠿⠟⢀⣿⣿⣿⣿")
        print("    ⣿⣿⣿⣿⣿⣿⣿⣿⣇⠘⣿⣿⣿⡇⢸⣿⣿⣿⣿⠀⣾⣿⣿⣿⠀⣼⣿⣿⣿⣿")
        print("    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠘⠛⠛⠃⠘⠛⠛⠛⠛⠀⠛⠛⠛⠃⢰⣿⣿⣿⣿⣿")
        print("    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⣿⣿⡇⢸⣿⣿⣿⣿⠀⣿⣿⡟⢀⣿⣿⣿⣿⣿⣿")
        print("    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠈⣛⣃⣈⣛⣛⣛⣛⣀⣙⣛⣁⣼⣿⣿⣿⣿⣿⣿")
        print("    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⠈⡉⠉⣉⣉⣉⣉⣉⣉⠉⣉⠉⢉⣿⣿⣿⣿⣿⣿⣿")
        print("    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠘⠟⢀⣿⣿⣿⣿⣿⣿⡈⠻⠃⣸⣿⣿⣿⣿⣿⣿⣿")
        print("    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        for item in self.cart_contents:
            i = item.["product"]
            print(f"{i.product_name}:- Quantity:{item["quantity"]}")
        print(f"Full Price: £{self.total_price():.2f}")

def main():
    inventory = [product_id,product_name,description,price,review,stock
        electronics("E000","Laptop","windows Hp laptop 2015",1000.00,"",10)
        clothes("C000","Hoodie","Cotton zip up hoodie",15.00,"",30)
        product("P000","carrot cake","crunchy crunchy carrot cake",5.00,"",5)
    ]
    my_cart = cart()
    user_login()
    while True:
        print(f"--------MAIN SHOP PAGE--------cart({my_cart.cartquantity()})")
        print("")
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")#main menu
        print(f"this is a placeholder for a random item display as an ad")
        print("1. Catalogue") 
        print("2. Search For Item")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")
        



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