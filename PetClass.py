class Foo:
    def __init__(self, val):
        self.val = val
    def printVal(self):
        return self.val
obj1 = Foo('1')
# obj2 = Foo('2')
obj1.printVal()
# obj2.printVAl()
print(obj1)
# print(obj2)