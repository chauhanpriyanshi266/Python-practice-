# Program to create a tuple containing the squares of all elements 

tup = tuple(int(x) for x in input("Enter elements : ").split())
square = []

for i in tup:
    sq = i**2
    square.append(sq)

print("Square tuple : ",tuple(square))