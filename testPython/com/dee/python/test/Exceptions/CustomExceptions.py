class BaseExceptionClass(Exception):
    pass


class ValueSmallException(BaseExceptionClass):
    pass


class ValueLargeException(BaseExceptionClass):
    pass


while True:
    try:
        apt_value = 10
        guess_value = int(input("Enter a Number:"))
        if (guess_value > apt_value):
            raise ValueLargeException
        elif (guess_value < apt_value):
            raise ValueSmallException
        else:
            print("Correct Value")
        break
    except ValueSmallException:
        print("Value is smaller")
    
    except ValueLargeException:
        print("Value is larger")
