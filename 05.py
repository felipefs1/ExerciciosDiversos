"""O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                   Até 5 Kg              Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar."""
import time

nome = str(input('Olá, qual seu nome?:  ')).upper().strip()
tipo = str(input(' 1 - File Duplo \n'
                 ' 2 - Alcatra \n'
                 ' 3 - Picanha \n'
                 'Qual o tipo de carne?: '))
qtd = float(input('Quantos Quilos?:  '))
price = float(0)
payment = str(input(' 1 - Dinheiro \n'
                    ' 2 - Cartão externo \n'
                    ' 3 - Cartão Tabajara \n'
                    ' 4 - Pix \n'
                    'Forma de pagamento? ')).upper().strip()
cardTabajara = 0
priceTotal = price - cardTabajara

if tipo == ('1' or 'FILE DUPLO') and qtd <= 5:
    price = qtd * 4.90
    tipo = 'FILE DUPLO'
elif tipo == ('1' or 'FILE DUPLO') and qtd > 5:
    price = qtd * 5.80
    tipo = 'FILE DUPLO'
elif tipo == ('2' or 'ALCATRA') and qtd <= 5:
    price = qtd * 5.90
    tipo = 'ALCATRA'
elif tipo == ('2' or 'ALCATRA') and qtd > 5:
    price = qtd * 6.80
    tipo = 'ALCATRA'
elif tipo == ('3' or 'PICANHA') and qtd <= 5:
    price = qtd * 6.90
    tipo = 'PICANHA'
elif tipo == ('3' or 'PICANHA') or '3' and qtd > 5:
    price = qtd * 7.80
    tipo = 'PICANHA'
else:
    print('Escolha errada, reinicie o programa!')

if payment == ('1' or 'DINHEIRO'):
    payment = 'DINHEIRO'
elif payment == ('2' or 'CARTÃO EXTERNO'):
    payment = 'CARTÃO EXTERNO'
elif payment == ('3' or 'CARTÃO TABAJARA'):
    cardTabajara = (price * 5) / 100
    payment = 'CARTÃO TABAJARA'
elif payment == ('4' or 'PIX'):
    payment = 'PIX'


print('\n')
print('\n')
print('\n')
print('\n')
print('\n')

print('Gerando Cupom...')
time.sleep(2)

print('\n')
print('\n')
print('\n')
print('\n')
print('\n')

print('--' * 20)
print('CUPOM FISCAL - DANFE')
print('--' * 20)

print(f'Prezado {nome.capitalize()}, abaixo o resumo da sua compra!')
print(f'A carne escolhida foi *{tipo.capitalize()}*')
print(f'A quantidade escolhida foi *{qtd:.0f}Kg*')
print(f'Com valor total de *R${price:.2f}*')
print(f'O tipo de pagamento escolhido foi *{payment.capitalize()}*')
print(f'Você recebeu um desconto de *R${cardTabajara:.2f} reais*')
print(f'Com desconto você irá pagar *R${price - cardTabajara:.2f}*')