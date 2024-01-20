# Peça ao usuário para informar o ano de nascimento. Em seguida, calcule e imprima a idade atual.

from datetime import datetime

print("\nVamos descobrir a sua idade?\n")

ano_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = datetime.now().year
idade_atual = ano_atual - ano_nascimento

print(f"Você tem ou fará {idade_atual} anos em {ano_atual}.")
