# Faça um programa que peça dois números e realize as principais operações: soma, subtração, multiplicação e divisão.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print(f"\nO resultado da soma é: {soma}")
print(f"O resultado da substração é: {subtracao}")
print(f"O resultado da multiplicação é: {multiplicacao}")
print(f"O resultado da divisão é: {divisao:.2f}")
