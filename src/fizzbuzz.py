# Pseudocode:
#  number / 3 = "Fizz"
#  number / 5 = "Buzz"
#  number / 3 and / 5 = "FizzBuzz"
# else return strin "7"

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 != 0:
        return "Fizz"
    elif number % 5 == 0 and number % 3 != 0:
        return "Buzz"
    else:
        return "error"