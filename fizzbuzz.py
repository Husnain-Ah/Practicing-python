# if input is divisible by 3 output fizz, if it is divisible by 5 output buzz, if divisible by both output fizzbuzz

def fizz_buzz(input):

    if input % 3  == 0 and input % 5 == 0:
        output = "fizzbuzz"
    elif input % 3 == 0:
        output = "fizz"
    elif input % 5 == 0:
        output = "buzz"
    
    return output


print(fizz_buzz(5))