class Cliente:
    def __init__(self,nome):
        self.nome = nome
    def get__nome(self):
        return self.nome.title()

    @property
    def nome(self):
        print("chamando @property nome()")
        return self.__nome.title()


    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome
