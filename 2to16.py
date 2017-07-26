#initialisation
original = input('number in binary')
i = len(original)-1
map = {'0000':'0','0001':'1','0010':'2','0011':'3','0100':'4','0101':'5','0110':'6','0111':'7','1000':'8','1001':'9','1010':'A','1011':'B','1100':'C','1101':'D','1110':'E','1111':'F'}
result = ''

#regroup the numbers in 4 and map
while i >= 0:
    j = 0
    inverse = ''
    while i >= 0 and j < 4:
        inverse = inverse + original[i]
        i -= 1
        j += 1
    real = ''
    for k in range(j):
        real = real + inverse[j-1-k]
    result = result + map[real]

#the result is inversed
for k in range(len(result)):
    print(result[len(result)-1-k],end = '')
