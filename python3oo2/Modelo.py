class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.__ano = ano
        self.__duracao = duracao
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def ano(self):
        return self.__ano

    @property
    def duracao(self):
        return self.__duracao

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @ano.setter
    def ano(self):
        self.__ano = self.__ano

    @duracao.setter
    def duracao(self):
        self.duracao = self.duracao


    @property
    def likes(self):
        return self.__likes

    @likes.setter
    def likes(self):
        self.__likes = self.__likes



    def dar_like(self):
        self.__likes += 1


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.__ano = ano
        self.__temporada = temporadas
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def ano(self):
        return self.__ano

    @property
    def temporada(self):
        return self.__temporada

    @property
    def duracao(self):
        return self.__duracao



    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @ano.setter
    def ano(self):
        self.__ano = self.__ano

    @temporada.setter
    def temporada(self):
        self.temporada = self.temporada

    @duracao.setter
    def duracao(self):
        self.duracao = self.duracao

    @property
    def likes(self):
        return self.__likes

    @likes.setter
    def likes(self):
        self.__likes = self.__likes


    def dar_like(self):
        self.__likes += 1





vingadores = Filme("Vingadores - Guerra infinita", 2018, 180)

vingadores.dar_like()


print(f'Nome: {vingadores.nome} - Ano:{vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')





vis_a_vis = Serie("Vis a Vis ", 2017, 3)

vis_a_vis.dar_like()
vis_a_vis.dar_like()
vis_a_vis.dar_like()
vis_a_vis.dar_like()
print(f"Nome: {vis_a_vis.nome} - Ano:{vis_a_vis.ano} - Temporadas: {vis_a_vis.temporada} - Likes: {vis_a_vis.likes}")


