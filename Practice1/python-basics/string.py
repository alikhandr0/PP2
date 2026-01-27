#_1_String 

#string

'''
print("Hello")
print('Hello')
'''

#quotes inside quotes

'''
print("It's alright")
print("he is called 'john'")
print('He is called "john"')
'''

#assign string to variable

'''
a = "Hello"
print(a)
'''

#multiline string

#in the result, the line breaks are inserted at the same position as in the code
'''
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
'''

"""
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
"""

#strings are arrays

'''
a = "Hello, World!"
print(a[0])
'''

#looping through a string

'''
for x in "banana":
    print(x)
'''

#string length

'''
a = "Hello, World!"
print(len(a))
'''

#check string
'''
txt = "The best things in life are free!"
print("free" in txt)
'''

'''
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
'''

#check if NOT

'''
txt = "The best things in life are free!"
print("expensive" not in txt)
'''

'''
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")    
'''

#------------------------------------------------------------------------------------------------------------

#_2_Slicing Strings

#slicing

'''
b = "Hello, World!"
print(b[2:5])  #first index is included, last index is excluded
'''

#slice from the start

'''
b = "Hello, World!"
print(b[:5])
'''

#slice to the end

'''
b = "Hello, World!"
print(b[2:]) #if we omit the last index, the slice will go to the end
'''

#negative indexing

'''
b = "Hello, World!"
print(b[-5:-2])  #если первый индекс отрицательный, то отсчет идет с конца строки
'''


#------------------------------------------------------------------------------------------------------------

#_3_Modifying Strings

#upper case

'''
a = "hello, world!"
print(a.upper())
'''

#lower case

'''
a = "HELLO, WORLD!"
print(a.lower())
'''

#remove whitespace

'''
a = " Hello, World! "
print(a.strip()) #returns "Hello, World!"
'''

#replace string

'''
a = "Hello, World!"
print(a.replace("H", "J")) #заменяет все вхождения H на J
'''

#split string

'''
a = "Hello, World!"
print(a.split(","))  #заменяет строку на список по разделителю ","
'''


#------------------------------------------------------------------------------------------------------------

#_4_String Concatenation

#concatenate strings

'''
a = "Hello"
b = "World"
c = a + b
print(c)
'''

'''
a = "Hello"
b = "World"
c = a + " " + b
print(c)
'''


#------------------------------------------------------------------------------------------------------------

#_5_Format Strings

#format strings

#это пример неправильного кода, который вызовет ошибку
'''
age = 36
txt = "My name is John, and I am " + age
print(txt)
'''

#f-strings

#это пример правильного кода
#как оно работает: перед строкой ставится буква f,
#а внутри строки в фигурных скобках указывается переменная, значение которой нужно вставить в строку

'''
age = 36
txt = f"My name is John, and I am {age}"
print(txt)
'''

#placeholder and modifiers

'''
price = 49
txt = f"The price is {price} dollars"
print(txt)  
'''

'''
price = 59
txt = f"The price is {price:.2f} dollars" #".2f" - формат с двумя знаками после запятой,
print(txt) # а знак ":" перед price означает, что это модификатор для переменной price
'''

'''
txt = f"The price is {20 * 59} dollars"
print(txt)   #можно использовать выражения внутри фигурных скобок
'''

#--------------------------------------------------------------------------------------------

#_6_Escape Characters

#escape characters

'''
txt = "We are the so-called "Vikings" from the north." #это пример неправильного кода, который вызовет ошибку
'''

'''
#чтобы исправить ошибку, нужно использовать обратный слеш \ перед внутренними кавычками,
# для того чтобы они воспринимались как часть строки, а не как конец строки
txt = "We are the so-called \"Vikings\" from the north." 
print(txt)
'''

#other escape characters

'''
    Code	                    Result

    \'	                        Single Quote	
    \\	                        Backslash	
    \n	                        New Line	
    \r	                        Carriage Return	
    \t	                        Tab	
    \b	                        Backspace	
    \f	                        Form Feed	
    \ooo	                    Octal value	
    \xhh	                    Hex value
'''


#--------------------------------------------------------------------------------------------

#_7_String Methods

#string methods

'''
    Method	                                    Description
capitalize()	                            конвертирует первый символ строки в верхний регистр
casefold()	                                конвертирует строку в нижний регистр
center()	                                возвращает отцентрированную строку
count()	                                    Returns the number of times a specified value occurs in a string
encode()	                                Returns an encoded version of the string
endswith()	                                Returns true if the string ends with the specified value
expandtabs()	                            Sets the tab size of the string
find()	                                    Searches the string for a specified value and returns the position of where it was foundformat()	    Formats specified values in a string
format()	                                Formats specified values in a string
format_map()	                            Formats specified values in a string
index()	                                    Searches the string for a specified value and returns the position of where it was found
isalnum()	                                Returns True if all characters in the string are alphanumeric
isalpha()	                                Returns True if all characters in the string are in the alphabet
isascii()	                                Returns True if all characters in the string are ascii characters
isdecimal()	                                Returns True if all characters in the string are decimals
isdigit()	                                Returns True if all characters in the string are digits
isidentifier()	                            Returns True if the string is an identifier
islower()	                                Returns True if all characters in the string are lower case
isnumeric()	                                Returns True if all characters in the string are numeric
isprintable()	                            Returns True if all characters in the string are printable
isspace()	                                Returns True if all characters in the string are whitespaces
istitle()                               	Returns True if the string follows the rules of a title
isupper()                               	Returns True if all characters in the string are upper case
join()	                                    Joins the elements of an iterable to the end of the string
ljust()	                                    Returns a left justified version of the string
lower()	                                    Converts a string into lower case
lstrip()	                                Returns a left trim version of the string
maketrans()	                                Returns a translation table to be used in translations
partition()	                                Returns a tuple where the string is parted into three parts
replace()	                                Returns a string where a specified value is replaced with a specified value
rfind()	                                    Searches the string for a specified value and returns the last position of where it was found
rindex()	                                Searches the string for a specified value and returns the last position of where it was found
rjust()	                                    Returns a right justified version of the string
rpartition()	                            Returns a tuple where the string is parted into three parts
rsplit()	                                Splits the string at the specified separator, and returns a list
rstrip()	                                Returns a right trim version of the string
split()	                                    Splits the string at the specified separator, and returns a list
splitlines()	                            Splits the string at line breaks and returns a list
startswith()	                            Returns true if the string starts with the specified value
strip()	                                    Returns a trimmed version of the string
swapcase()	                                Swaps cases, lower case becomes upper case and vice versa
title()	                                    Converts the first character of each word to upper case
translate()	                                Returns a translated string
upper()	                                    Converts a string into upper case
zfill()	                                    Fills the string with a specified number of 0 values at the beginning
''' 

#--------------------------------------------------------------------------------------------

