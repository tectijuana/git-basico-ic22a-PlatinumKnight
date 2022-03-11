numero = 1973
while numero <= 2000:
    contador =1
    x=0
    while contador <= numero:
        if numero % contador == 0:
            x=x+1
        contador = contador + 1
    if x == 2:
        print(numero)
    numero = numero + 1

#CAP 7-5