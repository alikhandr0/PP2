#_1_Variables

# Creating Variables

'''
x = 5
y = "John"
print(x)
print(y)

x = 4  # x is of type int
x = "Sally" # x is now of type str
print(x)

'''


# Casting

'''
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)
'''


# Get the Type

'''
x = 5
y = "John"
print(type(x))
print(type(y))



# Single or Double Quotes?

x = "Hello"
# is the same as
x = 'World'



# Case-Sensitive

a = 4
A = "Sally"
# A will not overwrite a
'''

#------------------------------------------------------------------------------------------------------------


#_2_Variable Names

#correct
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#wrong
#2myvar = "John"
#my-var = "John"
#my var = "John"



#Multi Words Variable Names

#Camel Case
myVariableName = "John"

#Pascal Case
MyVariableName = "John"

#Snake Case
my_variable_name = "John"


#------------------------------------------------------------------------------------------------------------


#_3_Assign Multiple Values

#Many Values to Multiple Variables

'''
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
'''


#One Value to Multiple Variables

'''
x = y = z = "Orange"
print(x)
print(y)
print(z)
'''

#Unpack a Collection

'''
fruits = ["Apple", "Banana", "Cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
'''

#------------------------------------------------------------------------------------------------------------

#_4_Output Variables

# Output Variables

'''
x = "Python is awesome"
print(x)


x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


x = 5
y = 10
print(x + y)


x = 5
y = "John"
print(x + y) # This will produce an error
'''


#------------------------------------------------------------------------------------------------------------

#_5_Global Variables

# Global Variables

'''
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()
'''

# create a global variable inside a function
'''
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)
'''

# Global Keyword 

#we can use the global keyword to create a global variable inside a function
'''
def myfunc():
    global x
    x = "fantastic"

myfunc()

print ("Python is " + x)
'''


'''
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)
'''


#------------------------------------------------------------------------------------------------------------


#_6_Variable Exercises


