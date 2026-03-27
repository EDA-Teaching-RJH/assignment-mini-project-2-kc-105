Project Development Online shop
the goal was to create a system that has object oriented programming at its foundation and can handle different types of products
I made a base product class and shred its data using inheritance to make the subclasses clothes and electronics 
I also implemented polymorphism to this by making the price calculated on clothes to be 10% off or in the display of products in subclasses it would show extra items like the size of the clothes or warranty of the electronics.
later i focused on user validation andsecurity with the loop that ensures a correct email has been entered which uses regular expressions to check if its correct.using the match function
File I/O i made json files so that the data for the products and users could be stored in a file which is read from or written to if a new user is added 
I also added a receipt that gets output as a .txt file 
Libraries i used a few libraries in my code most notably the json library which i used to read and write to the json files. I also used datetime so that i could make unique receipts using the time stamp.
Search feature i added the features to search using the product ID or Product name so its easier. the .upper() function helped ensure the product id that was entered would always be in the correct format - uppercase. i also addedstock management with reducestock() to prevent overselling or items having negative values when sold links the cart and the product classes together well.

the biggest challenge was managing the relationship between cart and products objects. by using composition and having a list of products within the cart this made things easier.

