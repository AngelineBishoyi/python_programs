class animal:
    def __init__(self,type):
        print('Animal Type',type)
class mammal(animal):
    def __init__(self):
        super().__init__('Mammal')
        print('mammal give birth directly')
        super().__init__('tiger')
        print('mammal give birth directly')
dog=mammal()
        