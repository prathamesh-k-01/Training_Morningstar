# try:
#     result = 10/0

# except ZeroDivisionError:
#     print("Cannot divide by zero")


# try:
#     result = 10/ int("string")

# except (ZeroDivisionError, ValueError) as e:
#     print(f"Eror occured as {e}")

def check_positive(age):
    if age <=0:
        raise ValueError("Number should be greater than 0")
    return age

try:
    check_positive(-10)
except ValueError as e:
    print(e)