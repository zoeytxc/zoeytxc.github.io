#initialisation
print("Welcome to the number convertor")
n = input('Original number base: ')  #input original base
m = input('Number base that you want to change to: ')   #input new base
original = input("Number you want to change: ")   #input original number
decimal=0   
n=int(n)
m=int(m)
forwardmap={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
backwardmap={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
#convert form n to 10
for i in range(len(original)):   # convert the original number to decimal bu weighed sum
    if original[len(original)-1-i]>='0' and original[len(original)-1-i]<='9':
        decimal += int(original[len(original)-1-i])*(n**i)
    else:
        decimal += forwardmap[original[len(original)-1-i]]*(n**i)
decimal=int(decimal)

#convert from 10 to m
results=''
while decimal != 0:   #transform into new base by division
    if (decimal % m)>=0 and (decimal % m)<=9:
        results = results + str(decimal % m)
    else:
        results = results + backwardmap[decimal % m]
    decimal = decimal // m
for i in range(len(results)):
    print(results[len(results)-1-i],end='')
