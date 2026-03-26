import sys
import re
import datetime
import json
class Customer:
    def __init__(self,username,password,wallet,email):
        self.username = username
        self.password = password
        self.wallet = wallet
        self.email = email

    def getuser(self):
        return f"User:{self.username}, Email: {self.email}, wallet {self.wallet}"

class product:
    def __init__(self,product_id,product_name,description,price,review,stock):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price
        self.review = review
        self.stock = stock

    def reducestock(self, quantity):
        if quantity <= self.stock:
            self.stock = self.stock - quantity
            return True
        else:
            print(f"Not enough stock left of {self.name}")
            return False
        
    def get_price(self): #can create employee discounts using polymorphism
        return self.price
        

    def displayinfo(self):
        return f"{self.product_name}({self.product_id}): £{self.price:.2f} stock:{self.stock}"
    
    def detailed_view(self):
        return f"{self.product_name}({self.product_id}): £{self.price:.2f} stock:{self.stock} {self.description} {self.review}"
    
    def product_search(self):#allow the user to search for certain items
        return f""


class clothes(product):
    def __init__(self,product_id,product_name,description,price,review,stock,size):
        super().__init__(product_id,product_name,description,price,review,stock)
        self.size = size

    def displayinfo(self):# will display the size as well
        return f"[{super().displayinfo()} size:{self.size}]"
    
    def detailed_view(self):
        return f"[{super().detailed_view()} size:{self.size}]"
    
    def getproductname(self):
        return self.product_name
    
    def get_price(self):
        return self.price * 0.9#if customer is employee 10% discount
        
        
class electronics(product):
    def __init__(self,product_id,product_name,description,price,review,stock,warranty):
        super().__init__(product_id,product_name,description,price,review,stock)
        self.warranty = warranty

    def displayinfo(self):# will display the warranty as well
        return f"[{super().displayinfo()} Warranty:{self.warranty}]"
    
    def detailed_view(self):
        return f"[{super().detailed_view()} Warranty:{self.warranty}]"

class cart:
    def __init__(self):
        self.cart_contents = []

    def cartquantity(self):
        total = 0
        for item in self.cart_contents:
            total = total + item["quantity"]
        return total
    
    def add_item(self, products, quantity):
        seeker = products.reducestock(quantity) 
        if seeker:
            self.cart_contents.append({"product": products, "quantity": quantity})
            print("added to cart")
        else:
            print("Item not added to cart")

    def receipt_generator(self, user):
        transactiontime = datetime.datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"receipt-{user.username}-{transactiontime}.txt"

        try:
            with open(filename, "w") as file:
                file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                file.write("~~~~~~~~~~~~Receipt~~~~~~~~~~~~~~~~~")
                file.write(f"Customer:{user.username}\n")
                file.write(f"Email   :{user.email}\n")
                file.write(f"Date    :{datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S\n")}")
                file.write(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                i = 0
                for item in self.cart_contents:
                    i = i + 1
                    prod = item["product"]
                    qty = item["quantity"]
                    itemprice = prod.get_price() * qty
                    file.write(f"{i} :{prod.productname:<20} £{itemprice:>8.2f}\n")
                    file.write(f"x{qty:<3}\n")
                file.write(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                file.write(f"Total price:    £{self.total_price:>8.2f}\n")
            print ("Receipt {filename} printed")
        except IOError as e:
            print(f"Error printing Receipt ({e})")

    
    def total_price(self):
        total = 0 
        for item in self.cart_contents:
            total = total + item["product"].get_price() * item["quantity"]
        return total

    def view_cart(self):
        if len(self.cart_contents) == 0:
            print("No items in Cart")
            return 
        else:
            print("Shopping Cart")
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
            for item in self.cart_contents:
                i = item["product"]
                print(f"{i.product_name}:- Quantity:{item["quantity"]}")
            print(f"Full Price: £{self.total_price():.2f}")

def main():
    inventory = load_inventory("products.json")
    my_cart = cart()
    currentuser = user_login()
    print(f"Welcome to the shoppe {currentuser.username}")
    print("loading...")
    print("loading...")
    print("loading...")
    while True:
        print(f"--------MAIN SHOP PAGE--------cart({my_cart.cartquantity()})")
        print("SALE!!! 10% OFF ALL CLOTHES")
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")#main menu
        print(f"this is a placeholder for a random item display as an ad")
        print("1. Catalogue") 
        print("2. Search For Item by ID")
        print("3. Search by Name")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")
        opt = input("Select option:")
        
        match opt:
            case "1":
                #product_browsing(inventory)
                print("~~~~~~~~Catalogue~~~~~~~~~~~")
                for item in inventory:
                    print(item.displayinfo()) 
            case "2":
                #product_search(inventory)
                searchterm = input("Please Enter product ID").strip().upper()
                for item in inventory:
                    if item.product_id == searchterm: 
                        print(item.displayinfo()) 
                search_item = next ((p for p in inventory if p.product_id == searchterm))
                if search_item:
                    cartconfirm = input("would you like to add to cart(y/n)?")
                    if cartconfirm == "y":
                        quty = int(input(f"how many {search_item.product_name}s?"))
                        my_cart.add_item(search_item, quty)
                else:
                    print("product not found")
            case "3":
                searchterm = input("Please Enter Search Term").lower()

                for item in inventory:
                    if item.product_name == searchterm: 
                        print(item.displayinfo()) 
                search_item = next ((p for p in inventory if searchterm in p.product_name.lower()))
                if search_item:
                    cartconfirm = input("would you like to add to cart(y/n)?")
                    if cartconfirm == "y":
                        quty = int(input(f"how many {search_item.product_name}s?"))
                        my_cart.add_item(search_item, quty)
                else:
                    print("product not found")
            case "4":
                my_cart.view_cart()
            case "5":
                if not my_cart.cart_contents:
                    print ("cart empty no items purchased")
                else:
                    print("Finalising order")
                    print (f"Amount due:£{my_cart.total_price():.2f}")
                    my_cart.receipt_generator(currentuser)
                    print ("Shop with us again!")
                    break
            case "6":
                print("Thank you come again!")
                break
            case _:
               print("please enter a valid option") 

    if __name__ == "__main__":
        main()



def new_user():
    newuser = input("please enter a new unique username:")   
    while True:
        newemail= input("please enter a new unique email")
        validemailtester = r'[^a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9-.]+$'
        if re.fullmatch(validemailtester, newemail):
            break
        else:
            print ("please enter a valid email")       
    newpassword = input("please enter a new unique password:")

def user_login():#let the user login with their username and password
    while True:
        print("Welcome ")
        print("Please Login")
        currentuser = input("username:")#if usernot found offer to create new user
        currentpassword = input("password")
        if currentuser not in Customer:
            input("would you like to make a new user(y/n)")
            new_user()

def load_inventory(filename):
    inventory = []
    try:
        with open(filename, "r")as file:
            data = json.load(file)
            for item in data:
                if item["type"] == "electronics":
                    obj = electronics(item["product_id"],item["product_name"],item["description"],item["price"],item["review"],item["stock"],item["warranty"])
                elif item["type"] == "clothes":
                    obj = electronics(item["product_id"],item["product_name"],item["description"],item["price"],item["review"],item["stock"],item["size"])
                else:
                    obj = electronics(item["product_id"],item["product_name"],item["description"],item["price"],item["review"],item["stock"],)
                inventory.append(obj)
        print(f"Loaded {len(inventory)} items")
    except FileNotFoundError:
        print ("No inventory found shop empty")
    return inventory



#def product_search(inventory):#allow the user to search for certain items
#    searchterm = input("Please Enter Item ID")
#    search_item = next ((p for p in inventory if p.product_id == searchterm))
#    if search_item:
#        quantity = int(input(f"how many {search_item.product_name}s?"))
#        my_cart.add_item(search_item, quantity)
    #for i in inventory:
    #    if searchterm in i.inventory() or in i.

#def product_browsing(inventory):#allow the user to scroll through different items nad pages
#    print("~~~~~~~~Catalogue~~~~~~~~~~~")
#    for item in inventory:
#        print(item.displayinfo()) 

main()