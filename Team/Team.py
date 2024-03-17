x = int(input())
y = 0
for i in range(0,x):
    valoracion = input()
    if int(valoracion[0])+int(valoracion[2])+int(valoracion[4])>1:
        y+=1
print(y)