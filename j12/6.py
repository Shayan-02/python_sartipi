a = 3243453465467
b = str(a)

max = 0
min = 9
for i in b:
    if int(i) > max:
        max = int(i)
    if int(i) < min:
        min = int(i)
print(max)
print(min)