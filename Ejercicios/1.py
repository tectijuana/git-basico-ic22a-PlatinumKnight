numero = 1
while numero <= 400:
    contador =1
    x=0
    while contador <= numero:
        if numero % contador == 0:
            x=x+1
        contador = contador + 1
    if x == 2:
        print(numero)
    numero = numero + 1

#CAP 7 EJ 1 