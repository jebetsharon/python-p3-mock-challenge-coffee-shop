class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, "_name"):
            self._name = name
        else:
            raise Exception("Name must be a string with at least 3 characters")

    def orders(self):
        return [order for order in Order.all if order.coffee is self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        prices = [order.price for order in self.orders()]  
        if prices:
            total = sum(prices)
            return total / len(prices)
        return 0  


class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception("Name must be 1 to 15 characters long")

    def orders(self):
        return [order for order in Order.all if order.customer is self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, new_coffee, new_price):
        return Order(self, new_coffee, new_price)

    @classmethod
    def most_aficionado(cls, coffee):
        coffee_orders = [order for order in Order.all if order.coffee is coffee]
        if coffee_orders:
            return max(
                cls.all,
                key=lambda customer: sum(
                    order.price for order in coffee_orders if order.customer is customer
                ),
            )
        return None


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception("Invalid customer")

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise Exception("Invalid coffee")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if (isinstance(price, float) and 1.0 <= price <= 10.0 and not hasattr(self, "_price")):
            self._price = price
        else:
            raise Exception("Price must be a float between 1.0 and 10.0")
