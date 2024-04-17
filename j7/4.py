num1 = int(input("enter a number: "))
op = input("enter a operator: ")
num2 = int(input("enter a number: "))

if op == "/":
    if ZeroDivisionError:
        print("division by zero")
    else:
        print(num1 / num2)
elif op == "*":
    print(num1 * num2)
elif op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
else:
    print("invalid operator")

a = 1
b = "1"
c = 1

print(a is c)

