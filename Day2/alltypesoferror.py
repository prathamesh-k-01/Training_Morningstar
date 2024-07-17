class NegiveNumberError(Exception):
    def __init__(self, number, message="Number must be positive!!!"):
        self.number = number
        self.message = message
        super().__init__(self.message)


def divide(a, b):
    try:
        if a < 0 or b<0:
            raise NegiveNumberError(a if a <0 else b)
        result = a/b

    except ZeroDivisionError:
        print("cannot divide by zero")

    except NegiveNumberError as ne:
        print(f"Exception: {ne}")

    except Exception as e:
        print(f"Unexpected Error: {e}")

    else:
        print(f"Result is {result}")
    finally:
        print("Program Excuted successfully")


divide(10,0)
divide(-10,5)
divide(2,5)