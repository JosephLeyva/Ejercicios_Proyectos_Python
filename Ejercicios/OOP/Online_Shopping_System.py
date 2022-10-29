'''
EXERCISE: Using OOP, create Customer, Shopping Cart and Product Classes

Customer
------
ATTRIBUTES
   * name
   * address
METHODS
   * login()
   * logout()
   * selectProduct()

========================
Shopping Cart
------
ATTRIBUTES
   * items
METHODS
   * add()
   * remove()

========================
Product
------
ATTRIBUTES
   * name
   * price
   * quantityAvailable
METHODS
   * order()
   * changePrice()
'''


class Customer:

    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address

    def login(self):
        pass

    def logout(self):
        pass

    def selectProduct(self, product):
        self.product = product


class ShoppingCart:

    def __init__(self, items) -> None:
        self.items = items

    def add(self, item):
        pass

    def remove(self, item):
        pass


class Product:

    def __init__(self, name, price, quantityAvailable) -> None:
        self.name = name
        self.price = price
        self.quantityAvailable = quantityAvailable

    def order(self):
        pass

    def changePrice(self):
        pass
