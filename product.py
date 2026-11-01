class Product:
    def __init__(self, product_id, name, price, stock):
        # Double underscore = private by convention (encapsulation)
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    # Getters: let other code READ the values safely
    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    # The Product controls how its own stock is changed
    def update_stock(self, quantity):
        if quantity < 0:
            print("Stock cannot be negative. Stock not changed.")
            return False
        self.__stock = quantity
        return True

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | "
              f"Price: ${self.__price:.2f} | Stock: {self.__stock}")

    # Turns the product into a dictionary so it can be saved to JSON
    def to_dict(self):
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }
