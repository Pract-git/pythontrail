class Fclass:
    def __init__(self, a2):
        self.a2 = a2

    def somemethod(self):
        print("firstclass", format(self.a2))
        #return self.a2


class Sclass(Fclass):
    def __init__(self, a3):
        self.a3 = a3


        Fclass.__init__(self, a3)

    def somemethond2(self):
        print(self.a3)
        return self.a3


v = Sclass(5)

print('The value is', v.somemethod())
print('The value is', v.somemethond2())

