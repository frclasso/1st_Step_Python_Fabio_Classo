
peso = float(input('Digite seu peso: '))
altura = float(input("Digite sua altura: "))
imc = peso /altura ** 2

imc = round(imc, 2)

if imc < 17:
    print(f'Seu peso está muita abaixo do ideal. Seu IMC {imc}')
elif 17 <= imc < 18.5:
    print(f'Seu peso está  abaixo do ideal. Seu IMC {imc}')
elif 18.5 <= imc < 25:
    print(f'Seu peso está dentro da faixa ideal. Seu IMC {imc}')
elif 25 <= imc < 30:
    print(f'Seu peso está acima do ideal. Seu IMC {imc}')
elif 30 <= imc < 35:
    print(f'Seu peso está acima do ideal (Obesidade I). Seu IMC {imc}')
elif 35 <= imc < 40:
    print(f'Seu peso está acima do ideal (Obesidade II - Severa). Seu IMC {imc}')
else:
    print(f'Seu peso está acima do ideal (Obesidade III - Móbida). Seu IMC {imc}')
