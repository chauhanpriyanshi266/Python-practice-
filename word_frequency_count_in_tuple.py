# Program to count the frequency of each word in a tuple

tup = tuple(input("Enter sentence: ").split())

dic = {}

# Count the frequency of each word
for word in tup:
    frequency = tup.count(word)
    dic[word] = frequency

# Display word frequencies
print("Word frequencies:", tuple(dic.items()))