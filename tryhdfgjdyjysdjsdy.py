class ParentClass1:
    def __init__(self, attribute1):
        self.attribute1 = attribute1

    def method1(self):
        print("This is method 1 from Parent Class 1")


class ParentClass2:
    def __init__(self, attribute2):
        self.attribute2 = attribute2

    def method2(self):
        print("This is method 2 from Parent Class 2")


class ChildClass(ParentClass1, ParentClass2):
    def __init__(self, attribute1, attribute2, attribute3):
        ParentClass1.__init__(self, attribute1)
        ParentClass2.__init__(self, attribute2)
        self.attribute3 = attribute3

    def method3(self):
        print("This is an exclusive method in Child Class")