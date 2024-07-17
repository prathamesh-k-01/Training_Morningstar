# take inputs from the user
# sum 3 >10000-> 10 percent discount >5k 5 percent discount else no discount 
object_a = int(input("Print the price of first "))
object_b = int(input("Print the price of second "))
object_c = int(input("Print the price of Third "))


sum_of_objects = object_a + object_b + object_c

if sum_of_objects>=10000:
    print(f"The total bill is: {sum_of_objects}")
    discount = sum_of_objects / 10
    print(f"The discount is:{discount}")
    print (f"The final price is:{sum_of_objects-discount}")


elif sum_of_objects>=5000 and sum_of_objects<10000:
    print(f"The total bill is: {sum_of_objects}")
    discount = sum_of_objects / 20
    print(f"The discount is:{discount}")
    print (f"The final price is:{sum_of_objects-discount}")
    
else:
    print(f"The final price is: {sum_of_objects}")



l = ['physics', 'chem', 'biology',55.5,43]
a = l[1] + l[0][0:3] +  l[2][0:3]
print(a)



# import random
# greet = ['', '','','','','']
# choice = random.choice(greet)
