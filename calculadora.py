# -*- coding: utf-8 -*-
"""
calculadora
Autor: Cesar Soares
Função: fazer contas soma, subtração, mutiplicação e divisão
"""
"""
print("----- CALCULADORA V2.0----")
sair = False

while sair == False:
	
	valor1 = input("Digite o primeiro numero: ")
	valor1=int(valor1)
	operador = input("Digite o operador (+-/*):")
	valor2 = input("Digite o segundo numero ")
	valor2=int(valor2)

	# + soma
	if operador =="+":
		operacao = valor1 + valor2

	# - subtração
	if operador =="-":
		operacao = valor1 - valor2

	# / divisão
	if operador =="/":
		operacao = valor1/valor2

	# * mutiplicação
	if operador == "*":
		operacao = valor1 * valor2

	print("Resultado: " )
	print(operacao)

	teste = input("Deseja Sair (n/s): ")
	if teste == "s":
		sair=true


"""
sair = False

while sair == False:
	valor1=input("Digite o valor1: ")
	valor1=int(valor1)
	valor2=input("Digite o valor2: ")
	valor2=int(valor2)
	operacao=valor1 / valor2

	print("resultado: ")
	print(operacao)

	teste = input("Deseja Sair (s/n): ")
	if teste == "s":
		sair=true

