class Master:
    def __init__(self, master):
        self.__master = master
    def get_master(self):
        return self.__master
mast = Master("Soll")
print(mast.get_master())