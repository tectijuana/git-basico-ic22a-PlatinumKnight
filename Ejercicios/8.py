Y = int(input("ingrese los años:" ))
def lightyear(Y):

   rate=3*100000000   

   seconds=(365*24*60*60)*(Y)

   return str((rate*seconds)/1000)+ "km"

print(lightyear(Y))

#CAP 8 EJ 2 
