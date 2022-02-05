class SaleItem:
    def __init__(self, price):
        self.price = price

class Fruit:
    
    def __init__(self, color):
        self.color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

class YellowBanana(Fruit, SaleItem):
    
    def __init__(self, price):
        Fruit.__init__(self, 'yellow')
        SaleItem.__init__(self, price)

banana1 = YellowBanana(10.00)
print(banana1.color) # calls the getter
banana1._color # doesn't call getter or setter
