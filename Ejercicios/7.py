def numeroPrimoRecursivo(n,c):
    
    if(n % c == 0 and n != 2):
        return False
    elif(c > int(n/2)):
        return True
    else:
        return numeroPrimoRecursivo(n, c+1)
for i in range (2, 998, 1):
    if( numeroPrimoRecursivo(i,2) and numeroPrimoRecursivo(i+2, 2)):
        print("Pareja de primos gemelos:" +str(i)+ "," + str(i+2))

#CAP 7 EJ 6 
