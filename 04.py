#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

a = float(input('Digite o primeiro lado: '))
b = float(input('Digite o segundo lado: '))
c = float(input('Digite o terceiro lado: '))
x = str
status = 'Não é triângulo'

#Verificando a existência de triângulo
if a + b > c and a + c > b and b + c > a:
    x = 'Positivo'
else:
    x = 'Negativo'

#Classificando o tipo de triângulo
if x == 'Positivo':
    if a == b and b == c:
        status = "Equilátero"
    elif a == b or a == c or b == c:
        status = 'Isósceles'
    else:
        status = 'Escaleno'

print('+=' * 12)

if x == 'Positivo':
    print(f'Estas medidas {a, b, c} podem formar um triângulo? : {x}')
    print(f'Este triângulo é classificado como {status}')
else:
    print('Com estas medidas não é possível formar um triângulo')



