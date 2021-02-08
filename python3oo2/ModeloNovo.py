class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'Nome: {self.nome} Likes: {self.likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

## __getitem__ faz com que programas seja do tipo interavel. Para percorrer como um list
    def __getitem__(self, item):
        return self._programas[item]


    @property
    def listagem(self):
        return self._programas


    def __len__(self):
        return len(self._programas)




vingadores = Filme('vingadores - guerra infinita', 2018, 160)

tmep = Filme('Todo mundo em pânico', 1999, 100)

demolidor = Serie('Demolidor', 2016, 2)


atlanta = Serie('atlanta', 2018, 2)




vingadores.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

filmes_e_series = [atlanta, tmep, demolidor, vingadores]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)


print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)






"""\
for programa in filmes_e_series:
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    ###                            hasattr é uma funçao que compara se tem algum objeto na lista
    print(f'{programa.nome} - {detalhes}  - {programa.likes}')




from abc import ABCMeta, abstractmethod 
class Programa(metaclass = ABCMeta): 
    @abstractmethod 
    def __str__(self): 
        pass
"""
