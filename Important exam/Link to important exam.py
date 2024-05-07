n,m = [int(x) for x in input().split()] #n:Estudiantes m:Preguntas
respuestas = []
total = 0
for i in range (n):
    respuestas.append(input())
puntos = [int(x) for x in input().split()]



#print(respuestas)
#print(puntos)

for j in range (m):
    ocurrencias = {}
    _max = 0
    for i in range (n):
#        print(respuestas[i][j])
        letra = respuestas[i][j]
        if letra in ocurrencias:
            ocurrencias[letra] += 1
        else:
            ocurrencias[letra] = 1
        
        if ocurrencias[letra] > _max:
            _max = ocurrencias[letra]
    total+= puntos[j]*_max
print(total)
#    print(ocurrencias)

