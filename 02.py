""" Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,0ndo) : aumento de 20%
salários entre R$ 280,00 e R$700 (inclui 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante: aumento de 5%
Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento."""


sal = float(input('Qual o valor do seu salário? :  '))
novoSal = 0
perc = 0

if sal <= 280:
    perc = 20
    novoSal = sal + (sal * perc / 100)
elif 280 < sal <= 700:
    perc = 15
    novoSal = sal + (sal * perc / 100)
elif 700 < sal <= 1500:
    perc = 10
    novoSal = sal + (sal * perc / 100)
else:
    perc = 5
    novoSal = ((sal * perc)/100) + sal

print('-=-=' * 10)
print(f'O salário era de R${sal:.2f} reais')
print(f'O percentual de aumento foi de {perc}%')
print(f'O valor do aumento foi de aproximadamente R${novoSal-sal:.2f} reais')
print(f'O salário após aumento ficou em R${novoSal} reais')
print('-=-=' * 10)
