x = int(input("Enter the Number"))

if x > 15:
    print("Number is Greater than 15")

elif x == 15:
    print("The number is equal to 15")

else :
    print("The number is Smaller than 15")  


# more compatibility 
# Truly Values

# Sequence data type i.e Non-Empty
# [1] , 'a', (1,2)

# Any Non Zero numerical value - - > 3 , -7 -- - - > also means true

# Falsly Values
# Sequence data type i.e NEmpty
# [] , '', ()

# Any Zero numerical value - - > 0 -- - - > also means False

if 5 :
    print("the Inider is if") # Truly Values

if 0 :
    print("The insider is if")

else: 
    print("The insider is else")


# Nested condition
x = 4 

if x > 5:
    print("the Number is Greater than 5")

    if x%2 == 0:
        print("The number is Even number")
    else: 
        print("The number is Odd Numbers")
else:
    print("the Number is Smaller than 5")


# Ternary Conditions

num = 5
result  = "Positive" if num > 0 else "Negative"
print("The number is ",result)


