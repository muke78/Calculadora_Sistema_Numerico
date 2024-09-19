# Funciones de conversion manual

def binario_a_decimal(binario):
    decimal = 0
    for i, bit in enumerate(reversed(binario)):
        if bit == "1":
            decimal += 2**i
    return decimal


def decimal_a_binario(decimal):
    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal //= 2
    return binario if binario else "0"


def decimal_a_octal(decimal):
    octal = ""
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal //= 8
    return octal if octal else "0"


def decimal_a_hexadecimal(decimal):
    hexadecimal = ""
    hexa_digits = "0123456789ABCDEF"
    while decimal > 0:
        hexadecimal = hexa_digits[decimal % 16] + hexadecimal
        decimal //= 16
    return hexadecimal if hexadecimal else "0"