def my_name(myname):
    # This will print the given name
    print('The given name is', myname)
    return
my_name('Nazmul')



def addition(a,b):
    sum=a+b
    print(sum)
addition(10,5)


def add(a,b,c):
    return 1+2+3
temp=add(1,2,3)
print(temp)

'''
## Required_Arguements
def add(a, b, c):
    return a+b+c
temp = add(1, 2)
print(temp)
'''


## Keyword Argument
def add(a, b, c):
    return a+b+c
temp = add(b=2, c=3, a=1)
print(temp)
