n = int(input("enter number of serie: "))


def fibo(n):
    if n < 1:
        raise ValueError("n must be greater than 1")
    f1 = 1
    f2 = 1
    print(f1, end = " ")
    print(f2, end = " ")

    for i in range(3, n + 1):
        f3 = f1 + f2
        print(f3, end = " ")
        f1 = f2
        f2 = f3
        # print(f3)
    # return f3


fibo(n)
