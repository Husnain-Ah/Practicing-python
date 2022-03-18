a = ['apple', 'ant', 'antlion', 'archies']
for x in a:
    print(x)
    #print every value in the list 'a'

for x in "bob":
    print(x)
    #print every letter in the specified word 

for x in a:
    print(x)
    if x == 'ant':
        break
    # break out of the loop if x = ant
    #can break before the print if print(x) is moved to after the break
        