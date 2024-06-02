# Pass by value

num = 5

def modify_num(num):
    num +=1
    print(num)

modify_num(num)

print("Original num", num)

# immutable datatypes : numbers, String, tuple - Passed by values


# Pass by Refrence : -> Mutable Datatypes :list, Dictionary

My_list =[1,2,3,4]

def modify_list(li):
    li.append(5)
    print(li)

print("Before Calling Func", My_list)

modify_list(My_list)
print("After calling Func", My_list)


# Lambda Function

func = lambda x : x+10 

print(func(5))

add = lambda a,b : a +b

print(add(10,2))

def myfunct():
    # return a new func
    return lambda msg : print(msg)

myfunct()("Hello World")

