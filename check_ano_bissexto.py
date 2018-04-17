#Autor: Jucio Gabriel
#Versao: 1.0
#Formas de Contato: Gmail: juciogabriel@gmail.com
#Whats app: 085985427699
#Gmail secundario: juciogabriel01@gmail.com
#Tentei melhorar ao maximo cada script.
#coding: utf-8
from datetime import datetime
print("""Escolha uma opcao:
    [1] Ano Atual
    [2] Ano eacolhido""")
opcao = int(input("Opcao:"))
if opcao == 1:
    ano_atual = datetime.today().year
    if ano_atual % 4 == 0 or ano_atual<2000 and ano_atual % 400 == 0:
        print("o ano",ano_atual,"e bissexto")
    else:
        print("o ano",ano_atual,"nao e bissexto")
elif opcao == 2:
    ano = int(input("Ano:"))
    if ano % 4 == 0 or ano<2000 and ano % 400 ==0:
        print("o ano",ano,"e bissexto")
    else:
        print("o ano",ano,"nao e bissexto")

