from TelefonesBr import TelefonesBr
from Datas_br import DatasBr
import datetime

from datetime import datetime, timedelta



#importando a biblioteca TelefonesBr


import re


"""\
padrao = "[0-9][a-z][0-9]"

texto = "123 1a2 1cc aa1"


resposta = re.search(padrao, texto)


padrao = "\w{0,8}@\w{3,10}.\w{2,3}.\w{2,3}"
texto = "aaabbbcccesar123@gmail.com.br sygtdustuydtsyudtuys dsiydyusudsuyds"

resposta = re.search(padrao, texto)

print(resposta.group())



print(resposta.group())

#---------------********************-------------------
# TELEFONE


padrao_molde ="(xx)aaaa-wwww"

padrao1 = "[0-9]{2}[0-9]{4,5}[0-9]{4}"

texto1 = "eu gosto do numero de telefone 2126556797 e tambem 21999814857"


resposta1 = re.findall(padrao1, texto1)

print(resposta1)

padrao_molde2 ="55(xx)aaaa-wwww"


telefone = "552126559550"


telefone_objeto = TelefonesBr(telefone)


print(telefone)

#------------********-----------
# Criando a mascara

telefone2 = "2126559550"
padrao_molde3 ="55(xx)aaaa-wwww"

#telefone_objeto = TelefonesBr(telefone2)

padrao2 = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"

resposta2 = re.search(padrao2, telefone2)

# com o search podemos com o metodo group, escolher qual parte printar
print(resposta2.group())


telefone = "552126559550"

telefone_objeto = TelefonesBr(telefone)

#telefone_objeto.format_numero()

print(telefone_objeto)




import datetime

from datetime import datetime, timedelta

# o metodo da classe datetime que é a today() mostra data e hora do dia
print(datetime.today())

#---------------*-------------



from Datas_br import DatasBr

cadastro = DatasBr()
print(cadastro.mes_cadastro())

print(cadastro.dia_semana())


as expressões regulares ou regex.

%A retorna os dias da semana por extenso, como Sunday;

%d exibe os dias do mês com números de 01 a 31;

%m retorna meses em números de 01 a 12;

%y mostra o ano com apenas dois dígitos;

%Y apresenta o ano em formato de quatro números;

%H retorna o horário no formato decimal, como 00, 001 e etc;

%M exibe os minutos de forma decimal;

%S apresenta os segundos em decimal.

"""

'''
hoje = datetime.today()

hoje_formatado = hoje.strftime("%d/%m/%Y %H:%M:%S")

print(hoje_formatado)



cadastro = DatasBr()
print(cadastro)



hoje = DatasBr()

print(hoje.tempo_cadastro())

'''


import requests

from acesso_cep import BuscaEndereco

cep = "25525750"

objeto_cep = BuscaEndereco(cep)


#print(objeto_cep)



#r =requests.get("https://viacep.com.br/ws/01001000/json/")

#print(type(r.text))
#<Response [200]>

#a = objeto_cep.acessa_via_cep()


#print(type(a))

#print(dir(a))

bairro, localidade, uf = objeto_cep.acessa_via_cep()

print(bairro, localidade, uf)
