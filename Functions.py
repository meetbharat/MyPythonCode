# series of square numbers
def fibo(n):
    a = 0
    b = 1
    for x in range(n):
        a = b
        b = a+b
        print(a,'\n')
    return b

num = int(input("Enter a value  of n:"))
print(fibo(num))

# For Prime number
def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

n = 6
if isprime(n):
    print("Yes")
else:
    print("NO")
