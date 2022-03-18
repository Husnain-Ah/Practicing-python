#str x = ("string") dont initialise variables with a  datatype

x = ("string")
print (str(x))

y = ("7")
print (int(y))
print (float(y))

z = 1j # Complex numbers are written with a "j" as the imaginary part:
print (z)
print (type(z))

print ((x,y)) # this is a list

a = ['hi', 'no', 'yes']
print (a)
print (type(a))

b = {'hi', 'no', 'yes'}
print (b)
print (type(b))
print (len(b)) # get length of the set

c = set(('a', 6, 'b')) # alternate way of initialising a set, just use curly brackets for ease

