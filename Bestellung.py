class produkt:
    def __init__(self, name, price, number):
        self.name = name
        self.price = float(price)
        self.number = int(number)
    def give_number(self):
        return self.number
    def give_name(self):
        return self.name
    def give_price(self):
        return self.price
    def deduct(self, Number):
        if Number > self.number:
            print("Too many products")
            return False
        elif self.number == 0:
            print("product not available")
            return False
        else:
            self.number -= number
            return True

class customer:
    def __init__(self, name, shop):
        self.name = name
        self.wk = {} 
        self.shop = shop
    def buy(self, product, amount):
        found = False
        for object in self.wk:
            if object.give_name() == product:
                found = True
                break
        if not found:
             for object in self.shop.pl:
                if product == objekt.give_name():
                    success = objekt.deduct(amount)
                    if success:
                        self.wk[object] = amount
                    else:
                        print("Process not possible")
                else:
                    print("Product not found")
        if found:
            print("Prodct already in you shopping list")
    def shopping_list(self):
        D = {}
        for objekt, amount in self.wk.items():
            D[objekt.geb_name()] = menge
        return D
    def change(self, product):
        for object in self.shop.pl:
            if product == objekt.give_name():
                del self.wk[object]
    def more(self, product, Amount): 
        for object, amount in self.wk.items():
            if product == object.give_name():
                success = object.deduct(Amount)
                if success:
                    self.wk[object] += Amount
    def pay(self):
        Total = 0 
        for objekt, amount in self.wk.items():
            Add = objekt.geb_preis() * amount
            Total += Add
        return Total

class shop:
    def __init__(self):
        self.cl = [] 
        self.pl = [] 
    def new_prod(self, name, price, number):
        self.pl.append(Produkt(name, price, number))
        return self.pl
    def check_avail(self, product):
        found = False
        for object in self.pl:
            if product == object.give_name():
                found = True
                print(object.give_number())
        if not found:
            print("Product not found")
    def show_prod(self):
        if self.pl:
            L = []
            for object in self.pl:
                L.append(object.give_name())
            print(L) 
        else:
            print("No products available")


