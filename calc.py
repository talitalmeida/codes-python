soma = lambda x,y: x+y
divide = lambda x,y: x/y
subtrai = lambda x,y: x-y
multiplica = lambda x,y: x*y

def switch(op, x, y):
 if op == "+":
    return soma(x,y)
 elif op == "-":
    return subtrai(x,y)
 elif op == "*":
    return multiplica(x,y)
 elif op == "/":
    return divide(x,y)

def default(op):
 while op != "+" and op != "-" and op != "*" and op != "/":
    print("\nSorry, something went wrong, try again!")
    print("+\t-\t*\t/")
    op = input("Digite uma operação: ")
    return op

#main_py
x = float(input("Digite o 1º valor: "))
op = input("Digite a operação: ")
op = default(op)
y = float(input("Digite o 2º valor: "))
print(f"\n{x} {op} {y} = {switch(op, x, y)}")