t = "ali", "reza", "mohammad"
print(type(t))
print(t, sep=" ")

b = list(t)
# b[1] = "taha"
t = list(t)
t[1] = "taha"
print(t[1])

fruits = ("apple", "banana", "cherry", "cheese", "pineapple")
g = fruits[2:]
f = ("orange")
fruits[:1] += f
fruits = list(fruits)
fruits.remove("cherry")
fruits = tuple(fruits)
red, *yellow, green, black, white = fruits
print(red)
print(yellow)
print(green)
print(black)
print(white)

