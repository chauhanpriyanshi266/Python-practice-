# Program to convert all elements to uppercase in a tuple

tup = tuple(input("Enter elements: "))

result = ()

# Convert each element to uppercase
for ch in tup:
    result = result + (ch.upper(),)

print("Uppercase tuple:", result)