
class Product:

    def __init__(self, name, price, category, quantity = 1):
        self.name = name
        self.price = price
        self.category = category
        self.quantity = quantity

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += (self.price * percent_change)
            print(f"New Price is {self.price}.")
            return self

        if is_increased == False:
            self.price -= (self.price * percent_change)
            print(f"New Price is {self.price}.")
            return self
    
    def print_info(self):
        print(f"Name: {self.name} \n Price: {self.price} \n Category: {self.category} \n Quantity: {self.quantity}")
        return self
