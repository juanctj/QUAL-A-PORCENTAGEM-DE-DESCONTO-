#CALCULO DESCONTO DE PRODUTOS

valor1 = input('Digite o valor do produto SEM desconto em R$: ')
valor1 = float(valor1)
valor2 = input('Digite o valor do produto COM desconto em R$: ')
valor2 = float(valor2)

if valor1 <= 0:
    print('O valor do produto SEM desconto NÂO pode ser ZERO')
elif valor1 < valor2:
    print('O valor do produto SEM desconto, deve ser maior que o valor COM desconto')
else:
    calc = (1 - (valor2/valor1))*100
    calc = float(calc)
    print(f'A porcentagem de desconto do produto é: {calc}%')


            