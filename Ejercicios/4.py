numero = "" 
baseActual = 0 
base10 = 0
a=[] 

print("Ingresa el número a convertir a base 10")
numero = input() 
print("Ingresa la base actual")
baseActual = int(input()) # 6

tam = len(numero)

for k in range(len(numero)):
   a.append(numero[k])


cont = tam - 1

temporal = 0
for i in range(tam):
    temporal = int(a[i]) * pow(baseActual, cont)
    cont = cont - 1
    base10 = base10 + temporal 

print("El numero en base 10 = {} " .format(base10))

#CAP 6 EJ 2 