# Este é um programa que calcula o imc - Índice de Massa Corporal

print('----------------------')

peso = float(input("Insira o seu peso:"))
altura =  float(input('Insira a sua altura:'))
imc = peso/(altura**2)

print(f'O seu imc é: {imc:.2f}')

if imc <= 16.9 :
    print('Você está muito abaixo do peso.')
elif 16.9 < imc < 18.4:
    print('Você está abaixo do peso.')
elif 18.4 < imc <= 24.9:
    print('Você tem o peso ideal.')
elif 24.9 < imc < 29.9:
    print('Você está acima do peso.')
elif 29.9 < imc < 34.9:
    print('Você possui Obesidade Grau I !')
elif 34.9 < imc < 40.0:
    print('Você possui Obesidade Grau II !!')
elif imc > 40.0:
    print('Você possui Obesidade Grau III !!!') 

print('----------------------')