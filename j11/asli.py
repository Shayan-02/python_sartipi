from lib import *

print(sum(5, 6))


a = "hello world"
print(len(a))


b = [1, "ali", 2, "reza", 3, "mohammad"]
print(len(b))

c = {1:"ali", "ali":["name", "family", "student", "employee", "manager"], "ali" : "ali", 2:"reza", "reza":"name", 3:"familly", "mohammad":4}

c["reza"] = "mohammadi"
print(c.items())
for i in c:
    print(i, end = " ")
    
print(len(c))