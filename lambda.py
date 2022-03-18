x = lambda a : a + 10
print(x(50))

x = lambda a : a * 10
print(x(10))

x = lambda a, b, c : a + b - c
print(x(1,2,3))

def triple(j): # define a function with a placeholder variable j
    return lambda a : a * j # return a value that is both place holders multiplied by eachother

dotriple = triple(3) # set the value of j
print(dotriple(10))  # set the value of a  -- then output the value of the function

def double(g):
    return lambda a : a * g

dodouble = double(2)

print (dodouble(10))