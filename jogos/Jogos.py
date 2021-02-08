import forca
import advinhacao


#def escolhe_jogo():
print("**********************************")
print("********Escolha seu jogo**********")
print("**********************************")

print("(1) Forca (2) Advinhação")

jogo = int(input("Qual o jogo \n"))

if (jogo == 1):
    print("jogando Forca")
    forca.jogar()
elif (jogo == 2):
    print("Jogando advinhação")
    advinhacao.jogar()

"""\if(__name__ == "main__"):
    escolhe_jogo()"""