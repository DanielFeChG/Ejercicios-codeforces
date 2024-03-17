x = input().split(" ")
puntos = input().split(" ")
ganadores = 0
for i in range(0,len(puntos)):
    if int(puntos[i])>=  int(puntos[int(x[1])-1]) and int(puntos[i])!=0:
        ganadores+=1
print(ganadores)