Y = int(input("ingrese los minutos:" ))
def lightminutes(Y):

   rate=3*100000000   

   seconds=(60)*(Y)

   return str((rate*seconds)/1000)+ "km"

print(lightminutes(Y))

#CAP 8 EJ 3 
