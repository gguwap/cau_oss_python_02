def add(a, b): return a + b
def sub(a, b): return a - b


def arithmetic_ops(op):
    num1 = int(input("input 1st number:"))
    num2 = int(input("input 2nd number:"))
    return num1, num2, op(num1, num2)

while True:
    op = input("input operation: ")
    if op == "end":
        break
    elif op == "+":
        num1, num2, ret = arithmetic_ops(add)
    elif op == "-":
        num1, num2, ret = arithmetic_ops(sub)
    elif op == "*":
        num1, num2, ret = arithmetic_ops(lambda a,b: a * b)
    elif op == "/":
        num1, num2, ret = arithmetic_ops(lambda a,b: a / b)
    elif op == "%":
        num1, num2, ret = arithmetic_ops(lambda a,b: a % b)
    else:
        print("Invalid operation")
        continue
    print(f"{num1}{op}{num2} = {ret}")
print("Exit program")
    
        