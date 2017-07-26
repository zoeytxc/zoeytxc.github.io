#initialisation
print("Welcome to the number game")
n = input('Lower limit:(integer inclusive) ')  #input lower limit
m = input('Upper limit:(integer inclusive) ')   #input higher limit

#list for the binary form for all numbers from n to m
binary = []  
for i in range(int(n),int(m)+1):
    s = ''
    j = i
    while j != 0:   #transform into binary 
        s = s + str(j%2)
        j = j >> 1
    binary.append(s)   
b = 0
j = int(m)

#claculate the number of tables needed
number = 0
while j != 0:   
    b += 1
    j = j >> 1
    
for i in range(b):
    for j in range(int(n),int(m)+1):
        if i < len(binary[j-int(n)]) and binary[j-int(n)][i] == '1':   #decide whether the number should be displayed in the table based on the binary form
            print(j, end = ' ')
    f = input('Is your number here?(Y/N)')
    if f == 'Y':   #calculate the number based on the binary form
        number += 2**i
        print(number)
print('Your number is: ', number)
