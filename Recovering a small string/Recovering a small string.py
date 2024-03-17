alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
x = int(input())
for z in range (0,x):
    code = int(input())-3
    l1 = 0
    l2 = 0
    l3 = 0
    if l1 +  l2 + l3 != code:
        for i in range(0,25):
            l3 += 1
            if l1 +  l2 + l3 == code:
                break 

    if l1 +  l2 + l3 != code:
        for j in range(0,25):
            l2 += 1
            if l1 +  l2 + l3 == code:
                break 

    if l1 +  l2 + l3 != code:    
        for k in range(0,25):
            l1 += 1
            if l1 +  l2 + l3 == code:
                break 

    print(alphabet[l1] + alphabet[l2] + alphabet[l3])

           