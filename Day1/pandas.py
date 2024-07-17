d = {'a':1,'b':2, 'c':3}
new_d = {}
for k, v in d.items():
    new_d[v] = k
print(new_d)


students = {'Alice':{'age':25,'grade':'A'}, 'Bob':{'age':22, 'grade':'B'}}

print(students['Alice']['grade'])

for i in range(1,11):
    print(f'2*{i} =',2*i)

i = 1
while i<11:
    print(f'2*{i} =',2*i)
    i += 1


#prime number 

def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
        
    return True


a = int(input())
if a%2:
    print("It is odd")
else:
    print("It is even")
if is_prime(a):
    print("It is a prime number")

else:
    print("not prime")


escape = "this is a  newline\and this is a tab \ch"
print(escape)