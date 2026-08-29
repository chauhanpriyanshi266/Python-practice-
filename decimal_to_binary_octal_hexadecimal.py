# Program to convert decimal into binary, octal and hexadecimal

dec = int(input("Enter decimal: "))
num = dec

if num == 0:
    binary = "0"
    octal = "0"
    hexa_dec = "0"

else:
    # Convert decimal to binary
    dec = num
    binary = ""

    while dec > 0:
        rem = dec % 2
        binary = str(rem) + binary
        dec = dec // 2

    # Convert decimal to octal
    dec = num
    octal = ""

    while dec > 0:
        rem = dec % 8
        octal = str(rem) + octal
        dec = dec // 8

    # Convert decimal to hexadecimal
    dec = num
    hexa_dec = ""
    digits = "0123456789ABCDEF"

    while dec > 0:
        rem = dec % 16
        hexa_dec = digits[rem] + hexa_dec
        dec = dec // 16

print("Binary:", binary)
print("Octal:", octal)
print("Hexadecimal:", hexa_dec)