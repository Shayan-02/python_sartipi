def sums(a, b):
    global c
    c = a + b
    d = a * b
    e = {d, c}
    return e


sums(10, 15)
print(f"c : {c}")