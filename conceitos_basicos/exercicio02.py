# Faça um programa que peça a quantidade de quilômetros. Transforme em metros, centímetros e milímetros.

quilometros = int(input("Quilômetros: "))

metros = quilometros * 1000
centimetros = metros * 100
milimetros = centimetros * 10

print(f"{quilometros}km são {metros} metros")
print(f"{quilometros}km são {centimetros} centímetros")
print(f"{quilometros}km são {milimetros} milímetros")
