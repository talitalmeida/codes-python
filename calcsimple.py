num1 = int(input("Digite o 1º valor: "))
num2 = int(input("Digite o 2º valor: "))
oper = str(input("Escolha uma operação: \n+\n-\n*\n/"))
print("O resultado é", end ="")
if oper == '+':
    print(num1+num2)
elif oper == '-':
    print(num1-num2)
elif oper == '*':
    print(num1*num2)
else:
    print(num1/num2)