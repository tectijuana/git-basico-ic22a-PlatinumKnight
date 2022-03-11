def decimal_a_octal(decimal):
    octal = ""
    while decimal > 0:
        residuo = decimal % 8
        octal = str(residuo) + octal
        decimal = int(decimal / 8)
    return octal


decimal = int(input("Ingresa un número decimal: "))
octal = decimal_a_octal(decimal)
print(f"El decimal {decimal} es {octal} en octal")

#CAP 6 EJ 1 
