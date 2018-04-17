#Autor: Jucio Gabriel
#Versao: 1.0
#Formas de Contato: Gmail: juciogabriel@gmail.com
#Whats app: 085985427699
#Gmail secundario: juciogabriel01@gmail.com
#Tentei melhorar ao maximo cada script.
#coding: utf-8

aluno = str(input("Nome Do Aluno:")).strip().title()
n1 = float(input("Primeira Nota do aluno:"))
n2 = float(input("Segunda Nota Do Aluno:"))
n3 = float(input("Terceira Nota Do Aluno:"))
media = (n1+n2+n3)/3
print("Seu Nome é",aluno)
print(f"Seu Nome é: {aluno} Sua Media Foi De: {media:.1f}")

if media >= 7.0:
    print("Aluno Aprovado")
elif media <= 4.0:
    print("Aluno em Recuperacao")



