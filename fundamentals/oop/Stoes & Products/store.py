### Things to work on ###
#1 - How to print values, and not memory locations. Everytime I try to print the list of products from the store, I get a memory location
#2 - Change the inflation method and set_clearance method to the Store CLass 
#3 - Update product class to give each product a unique id. Update the sell_product method to accept the unique id. 


import product

class Store:
    def __init__(self, name, products = []):
        self.name = name
        self.products = products

    def __str__(self):
        return self.products

    def inventory(self): ### Not chainable ###
            inventory = self.products
            return inventory

    def add_product(self, new_product):
        for i in range(len(self.products)):
            if new_product == self.products[i]:
                print(f"Item is already for sale. Please choose a different product to add.")
                return self
        self.products.append(new_product)
        print(Store.inventory(self))
        return self

    def sell_product(self, id):
        self.products.remove(id)
        print(self.products)
        return self
    
    def inflation(self, percent_increase):
        for i in range(len(self.products)):
            product.Product.update_price(self.products[i], percent_increase, True)
        return self
    
    def clearance(self, percent_discount):  ## How can I do an iterave if statement that compares the cost of each product in my store to see if it is $0.00?
        for i in range(len(self.products)):
            product.Product.update_price(self.products[i], percent_discount, False)
        return self

Heritage = Store("heritage")
Espresso = product.Product("Espresso", 3.50, "Drink")
Halie_Awesome = product.Product("Halie Awesome", 8.00, 'Food')
Coffee_Beans = product.Product("Coffee Beans", 18.00, "Goods")

Heritage.add_product(Espresso).add_product(Halie_Awesome).inflation(.1).clearance(.1)
print(Store.inventory(Heritage))
