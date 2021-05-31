#!/usr/bin/env python3

from requests import post
import sys

try:
    amount = int(sys.argv[1])
    for i in range(0, amount):
        url = post('https://www.4devs.com.br/ferramentas_online.php',{"acao":"gerar_cpf","pontuacao":"S"})
	response = url.text
	print(response)
except IndexError:
    print('Utilize: python3 cpf.py (quantidade de cpfs a ser gerado)')

except ValueError:
    print('É Necessário passar um valor inteiro ex: 1, 2, 3')
