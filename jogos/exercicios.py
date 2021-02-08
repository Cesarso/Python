""""\

# coding: utf-8
frutas = ['Banana', 'Maca', 'Pera', 'Uva', 'Melancia', 'Jamelão']

fruta_pedida = input('Qual é a fruta que deseja consultar ?')

if(fruta_pedida in frutas):
    print ('Sim, temos a fruta.')
else:
    print ('Não temos a fruta.')


## função count
valores = [ 0, 0, 0, 1, 2, 3, 4]
print(valores.count(0))

letras_acertadas = ['_','_','_','_','_','_']
letras_faltando = str(letras_acertadas.count('_'))
print( 'Ainda faltam acertar {} letras'.format(letras_faltando))


### --------------**---------- função index

frutas = ['Banana', 'Morango', 'Maçã', 'Uva', 'Maçã', 'Uva']
print(frutas.index('Uva'))

frutas = ['Banana', 'Morango', 'Maçã', 'Uva']
print(frutas.index('Melancia'))

frutas = ['Banana', 'Morango', 'Maçã', 'Uva']

fruta_buscada = 'Melancia'
if fruta_buscada in frutas:
    print(frutas.index(fruta_buscada))
else:
    print('Desculpe, a {} não está na lista frutas'.format(fruta_buscada))



## --------------***---------


frutas = ["maçã", "banana", "laranja", "melancia"]


lista = [fruta.upper() for fruta in frutas]


### TUPLAS: dias("s","t","q","q","s","s","d") -> dias da semana. OBS. listas[] tuplas () É uma lista que não se pode alterar



def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "maça".upper()
    letras_acertadas = ["_", "_", "_", "_"]


    erros = 0
    print(len(palavra_secreta))
    print(letras_acertadas)

    while(True):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        if (erros == 6):
            break
        if ("_" not in letras_acertadas):
            break
        print(letras_acertadas)


    if("_" not in letras_acertadas):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print("Fim do jogo")

### lendo arquivos externos

arquivo = open("palavras.txt", "w") # 1º abre conexão

### arquivo
### <_io.TextIOWrapper name='palavras.txt' mode='w' encoding='cp1252'> ## chama o arquivo


arquivo.write("melancia") ## escre no arquivo

arquivo.write("maça\n") ## pulando linhas

arquivo.close() ## é preciso fechar a conexão

 ###Funções em str:
    ###palavra.capitalize() *gera uma copia da str com a 1º letra Maiuscula



#arquivo copia.py
logo = open("Downloads\IMG_0095.JPG", 'rb')
data = logo.read()
logo.close()

logo2 = open('python-logo2.png', 'wb')
logo2.write(data)
logo2.close()"""



