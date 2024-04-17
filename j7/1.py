# 1
# num = input("enter a number: ")
# print("reverse number:", num[::-1])

# 2
num2 = int(input("enter a number: "))
for i in range(1, num2+1):
    for j in range(1, num2+1):
        print(i*j, end="\t")
    print("\n")

# 3
# height = float(input("enter your height(in meter): "))
# weight = float(input("enter your weight(in kg): "))
# bmi = weight / (height * height)
# print("bmi: ", round(bmi, 2))

# 4
# while True:
#     num1 = int(input("Enter the first number: "))
#     operator = input("Enter the operator (+, -, *, /): ")
#     num2 = int(input("Enter the second number: "))

#     if operator == "+":
#         result = num1 + num2
#     elif operator == "-":
#         result = num1 - num2
#     elif operator == "*":
#         result = num1 * num2
#     elif operator == "/":
#         result = num1 / num2
#     else:
#         print("Invalid operator")

#     print("Result: ", result)


#     choice = input("Do you want to perform another calculation? (y/n): ")
#     if choice.lower() != "y":
#         break
# functions
# def sum_numbers(a, b):
#     return a + b


# def sub_numbers(a, b):
#     return a - b


# def mul_numbers(a, b):
#     return a * b


# def div_numbers(a, b):
#     return a / b


# i = 1
# loop = True

# num1 = int(input(f"enter number{i}: "))
# i += 1
# op = input("enter operator: ")
# num2 = int(input(f"enter a number{i}: "))
# if op == "+":
#     result = sum_numbers(num1, num2)
# elif op == "-":
#     result = sub_numbers(num1, num2)
# elif op == "*":
#     result = mul_numbers(num1, num2)
# elif op == "/":
#     result = div_numbers(num1, num2)
# else:
#     print("invalid operator")
# i += 1
# while loop:
#     again = input("do you want to continue calc?(y/n): ")
#     if again.lower() == "n":
#         break
#     elif again.lower() == "y":
#         op2 = input("enter operator: ")
#         num3 = int(input(f"enter a number{i}: "))
#         if op2 == "+":
#             result = sum_numbers(result, num3)
#         elif op2 == "-":
#             result = sub_numbers(result, num3)
#         elif op2 == "*":
#             result = mul_numbers(result, num3)
#         elif op2 == "/":
#             result = div_numbers(result, num3)
#         else:
#             print("invalid operator")
#         i += 1

# print("result:", result)


# 5
# def sum_of_series(m, n):
#     """
#     Calculates the sum of an arithmetic series with initial term m and n terms, where m and n are input by the user.

#     Args:
#         m (int): initial term
#         n (int): number of terms

#     Returns:
#         int: The sum of the arithmetic series.
#     """
#     total = 0
#     for i in range(n + 1):
#         total += m + (i * m)
#     return total


# m = int(input("Enter the initial term(m): "))
# n = int(input("Enter the number of terms(n): "))
# result = sum_of_series(m, n)
# print(f"The sum of the series for m={m} and n={n} is {result}")


# 6


def get_inputs(n):
    """
    Gets n inputs from the user and returns them as a list.

    :param n: The number of inputs to get from the user.
    :return: A list of n inputs.
    """

    inputs = []

    if n < 1:
        raise ValueError("n must be greater than or equal to 1.")
    for i in range(n):
        input_value = float(input(f"Enter input #{i+1}: "))
        inputs.append(input_value)

    return inputs


count = int(input("how many inputs you want: "))
print("your inputs are: ", get_inputs(count))
