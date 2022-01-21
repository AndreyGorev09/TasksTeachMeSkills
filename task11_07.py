class Adr:
    def __init__(self, adress):
        self.__adress = adress
    def get_adr(self):
        return self.__adress
    def set_adr(self, adress):
        self.__adress = adress
adr = Adr('Minsk')
print(adr.get_adr())
adr.set_adr('Grodno')
print(adr.get_adr())