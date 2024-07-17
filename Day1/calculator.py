def add(a,b):
    return a+b

def sub(a,b):
    return a-b
def mul(a,b):
    return a*b

def div(a,b):
    return a//b


i = int(input("input the operation as 1 to add,2 to substract,3 to multiply,4 to divide: "))
a = int(input("input 1st number: "))
b = int(input("Input second number: "))

if i ==1:
    ans = add(a,b)
    print(ans)
elif i ==2:
    ans = sub(a,b)
    print(ans)
elif i ==3:
    ans = mul(a,b)
    print(ans)
elif i ==4:
    ans = div(a,b)
    print(ans)







def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
        
    return True


a = int(input("Enter a number"))
if a%2:
    print("It is odd")
else:
    print("It is even")
if is_prime(a):
    print("It is a prime number")

else:
    print("not prime")
