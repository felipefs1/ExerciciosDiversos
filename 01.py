# Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input('Digite um número:  '))
num2 = int(input('Digite um número:  '))
num3 = int(input('Digite um número:  '))
lista = [num1, num2, num3]
lista.sort(reverse=True)

print(lista)
