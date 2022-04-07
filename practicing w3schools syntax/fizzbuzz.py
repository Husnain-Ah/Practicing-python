# if input is divisible by 3 output fizz, if it is divisible by 5 output buzz, if divisible by both output fizzbuzz

def fizzbuzz(input):

    if input % 3  == 0 and input % 5 == 0: # I had to move this statement to the top as the value of 15 was being caught on the first statement of 'divisible by 3'
        output = "fizzbuzz"
    elif input % 3 == 0:
        output = "fizz"
    elif input % 5 == 0:
        output = "buzz"
    return output
    
print(fizzbuzz(15))