# Faça um programa que peça a quantidade de quilômetros. Transforme em metros, centímetros e milímetros.

km = int(input("Quilômetros: "))

m = km * 1000
cm = m * 100
mm = cm * 10

print(f"{km}km são {m} metros")
print(f"{km}km são {cm} centímetros")
print(f"{km}km são {mm} milímetros")
