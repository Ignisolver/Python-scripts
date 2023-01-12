class Meta:
    def __new__(cls, class_name, bases, attrs):
        print(f"meta new run for: {class_name}")
        return type(class_name, bases, attrs)

class Dog(metaclass=Meta):
    pass

class Cat(metaclass=Meta):
    pass

Dog()
Dog()

class Test:
    def __new__(cls, *args, **kwargs):
        print("new in Test")
        cls.__init__(cls)

    def __init__(self):
        print("init in Test")

import dis
dis.dis(Meta.__new__)
