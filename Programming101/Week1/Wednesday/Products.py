class Product():
    def __init__(self, name, stock, final):
        self.name = name
        self.stock = stock
        self.final = final

    def profit(self):
        return self.final - self.stock

    def __str__(self):
        return "{}".format(self.name)


class Laptop(Product):
    def __init__(self, name, stock, final, HDD, RAM):
        super().__init__(name, stock, final)
        self.HDD = HDD
        self.RAM = RAM


class Smartphone(Product):
    def __init__(self, name, stock, final, displaySize, megaPixels):
        super().__init__(name, stock, final)
        self.displaySize = displaySize
        self.megaPixels = megaPixels


class Store():
    warehouse = {}
    income = 0

    def __init__(self, name):
        self.name = name

    def load_new_products(self, product, count):
        self.warehouse[product] = count

    def list_products(self, prodClass):
        for item in self.warehouse:
            if isinstance(item, prodClass):
                print (item, " - ", self.warehouse[item])

    def sell_product(self, product):
        if product not in self.warehouse:
            return False
        elif self.warehouse[product] > 0:
            self.warehouse[product] -= 1
            self.income += product.profit()
            return True
        else:
            return False

    def total_income(self):
        return self.income
