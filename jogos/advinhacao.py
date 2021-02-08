import random

def jogar():

    print("**********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("**********************************")


    numero_secreto = random.randrange(1,101) # 0.0 1.0
    tota_de_tentativas = 0
    pontos = 1000

    print("Qual  nivel de dificuldade?", )
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nivel: "))


    if(nivel == 1):
        tota_de_tentativas = 20
    elif(nivel == 2):
        tota_de_tentativas = 10
    else:
        tota_de_tentativas = 5





    ## devemos converter a str por int




    for rodada in range(1,  tota_de_tentativas + 1):

        print("Tentativas {} de {}".format(rodada, tota_de_tentativas))
        chute_str = input("Digite um numero entre 1 e 100!: ")

        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if(chute <1 or chute>100):
            print("você deve digitar um numero entre 1 e 100!")
            continue



        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto


        if(acertou):

            print("Você acertou e fez {} pontos".format(pontos))
            # para para sair do laço:
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o numero secreto")
            elif(menor):
                print("VocÊ errou! O seu chute foi menor que o numero secreto ")
            pontos_perdidos = abs(numero_secreto - chute)  #40-20 obs: pode ficar negativo. Então usamos a função de valor absoluto
            pontos = pontos - pontos_perdidos
        rodada = rodada + 1


        print("Fim de jogo")

    print("O numero sorteado foi: {}".format(numero_secreto))

if(__name__ == "__main__"):
    jogar()

"""\ nome = "Nico"
sobrenome = "Steppat"
print(nome, sobrenome, sep="_") 



numero3 = 30 * "*"
print(numero3)




idade_str = input("Digite sua idade: ")
idade = int(idade_str)

if (idade > 18):
    print("Você é maior de idade.")
else:
    if (idade < 12):
        print("Você é uma criança.")
    elif (idade > 12):
        print("Você é um adolescente.") 


idade_str = input("Digite sua idade: ")
idade = int(idade_str)

maior_idade = idade > 18
crianca     = idade < 12
adolescente = idade > 12





usuario = input("Informe o usuário do sistema!")

if(usuario == "Flávio"):
    print("Seja bem-vindo Flávio!")
elif(usuario == "Douglas"):
    print("Seja bem-vindo Douglas!")
elif(usuario == "Nico"):
    print("Seja bem-vindo Nico")
else:
    print("Usuário não identificado!") 

contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 2
    if(contador == 5):
        contador = contador + 2


for rodada in range(0, 10):
    print(rodada)



for rodada in range(1,10, 2):
    print(rodada)


for i in range(1,8):
    if(i == 5):
        continue # pula a contagem do n 5. Não imprime ele so 1-4 e 6-
    print(i)

"""