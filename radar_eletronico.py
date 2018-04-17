#Autor: Jucio Gabriel
#Versao: 1.0
#Formas de Contato: Gmail: juciogabriel@gmail.com
#Whats app: 085985427699
#Gmail secundario: juciogabriel01@gmail.com
#Tentei melhorar ao maximo cada script.
#coding: utf-8

vel = int(input("Velocidade:"))
if vel > 80:
    print(f"Voce Excedeu o Limite de Velocidade Sua Multa e De R$ {(vel - 80) * 7.00:.1f}")
