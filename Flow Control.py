# if elif else for Marksheet
marks = 75
if (marks > 80):
    print("Grade A")
elif (marks > 60) and (marks <= 80):
    print("Grade B")
elif (marks > 40) and (marks <= 60):
    print(("Grade C"))
else:
    print("Grade D")


########## while Loops #################

words = ['One','Two','Three','Four','Five','Six','Seven']

n = 0

while (n < 5):
    print(words[n])
    n +=1


# While Loops for getting a sum upto given number
num = int(input("Enter the value of n="))
if num <= 0:
    print("Enter a valid number")
else:
    sum = 0
    while (num>0):
        sum+=num
        num-=1
print(sum)

# Fibonacci series

a,b = 0, 1
while b < 1000:
    print(b,end=" ",flush=True)
    a,b = b, a+b

print()

########## For Loops #################


words = ['One','Two','Three','Four','Five','Six','Seven']

for i in words:
    print(i)

# For Loop Beer Song
for quant in range(99,0,-1):
    if quant > 1:
        print(quant,' Bottles of beer on wall,', quant,' bottles of beer')
        if quant > 2:
            suffix = str(quant)+' bottles of beer on wall'
        else:
            suffix = '1 bottles of beer on wall'
    elif quant == 1:
        print('1 bottles of beer on wall, 1 bottles of beer')
        suffix = 'NO more beer on the wall'

    print('Take one down and pass it around', suffix)
    print("---")

# Break example for limiting infinite loop at 10 number only

count = 0
while True:
    print(count)
    count +=1
    if (count > 10):
        break

# continue example for odd number
for x in range(20):
    if (x%2)==0:
        continue
    print(x)

















