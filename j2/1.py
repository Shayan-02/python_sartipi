math = int(input("math: "))
science = int(input("science: "))
geometry = int(input("geometry: "))
chmestry = int(input("chmestry: "))
avg = (math + science + geometry + chmestry)/4

# if avg > 16:
#     print("a")
# elif avg < 16 and avg > 14:
#     print("b")
# elif avg < 14 and avg > 12:
#     print("c")
# elif avg < 12 and avg > 10:
#     print("d")
# elif avg < 10:
#     print("fail")

if math >= 0 and math <= 20 and geometry >= 0 and geometry <= 20 and science >= 0 and science <= 20 and chmestry >= 0 and chmestry <= 20:
    if avg >= 16:
        print("your average is", avg, "so your grade is A")
    elif avg >= 14:
        print(f"your average is {avg} so your grade is B")
    elif avg >= 12:
        print("your average is {} so your grade is C".format(avg))
    elif avg >= 10:
        print(f"your average is {avg} so your grade is D")
    else:
        print("fail...")
else:
    print("average is false...")