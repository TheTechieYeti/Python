
class Product:
    id = 1
    def __init__(self, name, price, category, quantity = 1):
        self.name = name
        self.price = price
        self.category = category
        self.quantity = quantity
        self.id = Product.id
        Product.id += 1
    def __repr__(self):
        return self.name
    
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += (self.price * percent_change)
            print(f"{self.name}'s new price is {self.price}.")
            return self

        if is_increased == False:
            self.price -= (self.price * percent_change)
            print(f"{self.name}'s new price is {self.price}.")
            return self
    
    def print_info(self):
        print(f" Id: {self.id} Name: {self.name} Price: {self.price} Category: {self.category} Quantity: {self.quantity}")
        return self



