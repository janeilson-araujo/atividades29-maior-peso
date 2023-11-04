# Exercício Python 29: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

peso = []

print("de uma lista de 5 pessoas sábia quem pesa mais e quem pesa menos")

for i in range(1 , 6):
    kg = float(input(f"digite o peso da {i}° pessoa:"))
    peso.append(kg)
    
maior = peso[0]
menor = peso[0]     

for I in range(len(peso)):
    if peso[I] > maior :
        maior = peso[I]
    if peso[I] < menor :
        menor = peso[I]
        
print(f"maior peso:{maior}kg")        
print(f"menor peso:{menor}kg")