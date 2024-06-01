x = 5
print(5+1)

name = input()
print(name)

x=2
y=3
z=4
print(x,y,z, sep=",")

print("Hello", end=" ")
print("World", end=" ")


def tushar1():
    print("Hello World")

# Keyword arguments
def tushar2( name, age, skill):
    print(name, "age is", age , "Who have a skill as of", skill )


tushar2(name ="tushar", age = 99 , skill = "software developer")

#  In keyword arguments can only be passed when all the arguments should have a keyword.

# Position Arguments
def tushar3(X,Y):
    print(X,Y)

tushar3(6,5)


def add_num(*args):
    print(type(args))

    sum = 0 
    for num in args:
        sum +=num
        return sum

add_num(3,4,5)

# **Kwargs --> Dictionary

def display(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key, "->", value)

display(name="tushar",age=23,city = "Mumbai")

def func(a,b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

func(5, 6,7,8,9,10,11, name = "tushar", age = 23, city = "Mumbai")

# Implicit conversion 
def add_num1(a : int, b:int)-> int:
    return a+b;
print(add_num1(5.5,7.7))


def outer():
    print("Hello im the Outer")

    def inner():
        print("Hello im the Inner")
        return inner

        # outer()()

    

