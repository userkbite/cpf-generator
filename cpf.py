#!/usr/bin/env python3

from requests import post
import sys

amount = int(sys.argv[1])

for i in range(0, amount):
    url = post('https://www.4devs.com.br/ferramentas_online.php',{"acao":"gerar_cpf","pontuacao":"S"})
    response = url.text
    print(response)
