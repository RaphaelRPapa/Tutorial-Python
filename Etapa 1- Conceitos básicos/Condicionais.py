# Exemplo de condicionais em Python

# Verificar se um número é positivo, negativo ou zero
num = int(input("Digite um número: "))

if num > 0:
    print("O número é positivo.")
elif num < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

num = int(input("Digite um dia da semana: "))

match num:
    case 1:
        print("segunda.")
    case 2:
        print("terça.")
    case 3:
        print("quarta.")
    case 4:
        print("quinta.")
    case 5:
        print("sexta.")
    case 6:
        print("sabado.")
    case 7:
        print("domingo.")
    case _:
        print("Digite um numero de 1 a 7.")

