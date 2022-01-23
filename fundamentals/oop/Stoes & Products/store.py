


import re
import product

class Store:
    @classmethod
    def inflation(cls, percent_increase):
        for i in range(len(cls.products)):
            product.Product.update_price(cls.products[i], percent_increase, True)
        
    @classmethod
    def clearance(cls, percent_discount):  
        for i in range(len(cls.products)):
            if cls.products[i].price <= 0:
                print(f"{cls.products[i].name} item is already free.")
                continue
            product.Product.update_price(cls.products[i], percent_discount, False)
        return

    def __init__(self, name, products = []):
        self.name = name
        self.products = products

    def __str__(self):
        return str(self.products)

    def inventory(self):
            print(self.products)
            return self
    
    def inventory1(self):
        for i in range(len(self.products)):
            product.Product.print_info(self.products[i])
        return self

    def add_product(self, new_product):
        for i in range(len(self.products)):
            if new_product == self.products[i]:
                print(f"Item is already for sale. Please choose a different product to add.")
                return self
        self.products.append(new_product)
        # print(Store.inventory(self))
        return self

    def sell_product(self, id):
        for i in range(len(self.products)-1):
             if id == self.products[i].id:
                print("found it")
                self.products.pop(i)
        print(self.products)
        return self
    
    def inflation(self, percent_increase):
        for i in range(len(self.products)):
            product.Product.update_price(self.products[i], percent_increase, True)
        return self
    
    def clearance(self, percent_discount):  
        for i in range(len(self.products)):
            if self.products[i].price <= 0:
                print(f"{self.products[i].name} item is already free.")
                continue
            product.Product.update_price(self.products[i], percent_discount, False)
        return self

Heritage = Store("heritage")
Espresso = product.Product("Espresso", 3, "Drink")
Halie_Awesome = product.Product("Halie Awesome", 8.00, 'Food')
Coffee_Beans = product.Product("Coffee Beans", 18.00, "Goods")
Sticker = product.Product("Sticker", 0, "Goods")

Heritage.add_product(Espresso).add_product(Halie_Awesome).add_product(Coffee_Beans).add_product(product.Product("Test", .00, "Goods")).inventory1().sell_product(1)
Heritage.inflation(.5)
Heritage.clearance(.5)
