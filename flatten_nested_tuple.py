# Program to flatten a nested tuple

import ast

tup = ast.literal_eval(input("Enter a nested tuple: "))

result = []

def flatten(tup):
    for i in tup:

        # Check whether the element is a nested tuple
        if isinstance(i, tuple):
            flatten(i)

        else:
            result.append(i)

# Flatten the nested tuple
flatten(tup)

# Display the flattened tuple
print("Flattened tuple:", tuple(result))