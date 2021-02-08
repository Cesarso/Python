from Cpf_cnpj import Documento

from validate_docbr import CNPJ
#35379838000112





#print(cnpj.validate(exemplo_cnpj))


#documento = CpfCnpj(exemplo_cnpj, 'cnpj') # precisa passar o tipo de documento


#cnpj = CNPJ()

exemplo_cnpj = "35379838000112"


exemplo_cpf = "11954784708"


documento = Documento.cria_documento(exemplo_cnpj)

print(documento)


"""\
cpf_um = Cpf("11954784708")

print(cpf_um)

---------------***********-----------------



# JOGAR O IMPORTE PRA DENTRO DO ARQUIVO DA CLASSE


from validate_docbr import CPF


cpf = CPF()

print(cpf.validate("11954784708"))
# Assim já funciona dizendo ser valido ou não




cpf = 11954784708
cpf = str(cpf)
objeto_cpf = Cpf(cpf)


#cpf = input("Digite seu cpf: \n")

# É preciso fatiar os digitos do cpf em pedaços
fatia_um = cpf[:3]

fatia_dois = cpf[3:6]

fatia_tres = cpf[6:9]

fatia_quatro = cpf[9:]

# Agora é preciso juntar os pedaços

cpf_formatado = "{}.{}.{}-{}".format(
    fatia_um,
    fatia_dois,
    fatia_tres,
    fatia_quatro
)


print(objeto_cpf)
"""
