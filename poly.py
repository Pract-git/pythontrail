class Fruits:
    #color1 = red
    #color2 = orange

    def __init__(self, shape, taste):
        self.shape = shape
        self.taste = taste

    print("This is fruits base class")

    def color(self):
        print("color of the fruit from base class")


class Apple(Fruits):
    def __init__(self, price):
        self.price = price
        super().__init__("round","sweet")

    def color(self):
        print("color of the fruit from child class")
        return 0


x = Apple(10)
y = Fruits("round", "sweet")

#print(x)
print(x.color())
print(x.shape)
print(y.color())






