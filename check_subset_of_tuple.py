# Program to check whether one tuple is a subset of another

tup1 = tuple(input("Enter elements for tuple 1: ").split())
tup2 = tuple(input("Enter elements for tuple 2: ").split())

# Check whether tup1 is a subset of tup2
for i in tup1:
    if i not in tup2:
        print("tup1 is not a subset of tup2")
        break
else:
    print("tup1 is a subset of tup2")