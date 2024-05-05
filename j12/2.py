n = int(input("enter the number of serie: "))


def mul_serie(n):
    m1 = 1
    print(m1, end=" ")
    for i in range(2, n + 1):
        m1 *= i
        print(m1, end=" ")


mul_serie(n)