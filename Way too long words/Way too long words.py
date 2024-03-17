x = int(input())
for i in range(0,x):
    palabra = input()
    if len(palabra) >10:
        print(palabra[0]+ str(len(palabra)-2) + palabra[len(palabra)-1])
    else:
        print(palabra)