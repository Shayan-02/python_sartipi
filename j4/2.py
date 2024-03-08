s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3, 10, 11, "ali"}
s1 = s1.union(s2)
print(s1)


s3 = s1.difference(s2)
s4 = s1 - s2
print(s3) # s1 - s2
print(s4)

l1 = []
for i in s3:
    l1.append(i)

print(l1[1])