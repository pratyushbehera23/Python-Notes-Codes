# Python roadmap

```py

'''Roadmap{
    
basics condition loop 
function recursion lambda 
error-exception file-handling 
oop-class 
dsa : (array: linearList,stack,queue,circularQueue,) (sort: bubble,insertion,)

modules : 
[os sys time math random calendar turtle colorama  
json numpy matplotlib pandas scikitLearn 
beautifulSoup pyttx3 PyQt5 Tk  sympy scipy 
multimedia[graphics(imghdr colorsys imageop rgbimg) audio(sndhdr aifc audioop chunk sunau wave)] ]

Libraries for Information processing, file system manipulation, data management, network communication, multimedia,
WebD: python web script, CGI interface, 

Creating modules and packages.

Python as RAD tool for rapid application development
Work with SGML,HTML,XML for advanced web development
Build GUI based applications using Tk interface
Extend and embed python using C.
}'''

# 

''' NOTE
Programming languages: 
    Low-level(Machine(01) Assembly) High-level((C BASIC FORTRAN PASCAL)(C++ Java)(JavaScript Python Ruby)) 
    Logic Procedure-oriented Functional-oriented Object-oriented Functional-objected-oriented 
    Declarative Imperative 
Python: 
    High-level (programmer-friendly)
    Object-oriented (Technique focusing real-world objects)
    Interpreted (line by line execution)
    REPL(read,eval,print,loop)
    PROs: free, open-source, portable, flexibility, versatile, neat, easy, powerful, extensible, fast to develope. 
        General-purpose: CompetitiveProgramming WebDev WebScraping DataScience MachineLearning ...
    CONs: slow, memory-consumption, threading-problems, not-native-to-mobile-env, 
Used:
    mathematics, data-analysis, AI-ML, 
IDEs and Code-Editors:
    PyCharm(IDE) VScode(editor) repl.it(online) Jupyter(notebook)
Package managers:
    PyPl-pip, Anaconda-conda
Roadmap:
    Basic-Syntax Variables Data-types Built-in-Functions
    Statements Expressions Block Comments Token{Keywords Identifiers Literals} [Modules Libraries Packages]
    Display output (print command)
    Take user input (input command)
    Conditionals (if elif else)
    Loop (for while)
    List Tuple Sets Dictionary (+methods)
    Functions (def arguments/parameters)
    Errors and Exception handling
    File handling
    Lambda, Decorators
    Import use and create-your-own : Modules Libraries Packages
    Data-Structure:
        Array and Linked-lists
        Stack Queue Heaps Hash-Tables
    Algorithms:
        Searching algorithms (Binary search)
        Sorting algorithms (Bubble sort, Selection sort)
        Recursion
    OOP:
        Object Class Inheritance
        Method and Constructor, Dunder
    Package Managers: PyPl pip conda
    Framework
    Testing applications
Simple coding problems:
    Conversion miles-m-Km, $-₹-₿-⟠, speed, ...
    odd-even Prime-composite
    Coin-toss, Dice, ArmstrongNo, RandomNo-guess, 
    Sum of all digits in a number
    Reverse string (+ check palindrome)
    Simple-Interest, Compound-Interest
    Sum/largest/smallest/average in list
    Calculate age
    Build a simple calculator
    User login using dictionary
Projects:
    Build a Web-Crawler
    News Aggregator
    Simple games using PyGame
    Data analysis using numpy,pandas,matplotlib,scikit-learn
    WebDev using Django
'''

# BASICS
print("Hello World")

a = 'Hello world'
s = "string"    #string
n = 23      #integer
f = 11.02       #float
b = True    #boolean
c = 1.5 + 4j    #complex
ls = [1, 2.0, '3', False]      #list
ls = [1, 2, 3, 4]      #array; list of same data types
t = (1, 2, 3, 4)       #tuple
d = {a:1, b:2, c:3}     #dictionary
s = {1, 2, 3.5, 'hi'}   #set

#   + - * / ** // % == != > < >= <= 
#   and or 

a = input("Enter : ")
s = str(input("Enter : "))
n = int(input("Enter : "))
f = float(input("Enter : "))
b = bool(input("Enter : "))
c = complex(input("Enter : "))

bool(0) #False
bool(1) #True

#complex
c.real  # to check the real part of complex no
c.imag  # to check the imaginary part of complex no

l = len()   # length (built-in function to calculate length of any sequence data types like string,list,etc.)
i = id()    # returns memory address to which a variable is referencing
type()      # check the data-type of any variable/value

eval()  # it's awesome; 

print("Output :",)

# Number systems:
# Decimal to
bin(22)
oct(24)
hex(29)
# getting Decimal from
0b11010
0o17
0x3b

# Keywords are word with some meaning
# To get all keywords names:
import keyword
print(keyword.kwlist)

# find
print('search'.find('s'))
# end
# sep
# strip lstrip rstrip


# Format text strings: %-formatting, str.format(), string.Template, f-strings (PEP 498 - Literal string interpolation)

# SimplePROGRAMS : 

# Arithmetic operations:
# operand(x,num,5,7.2,..) operator(+,-,*,/,..) operand(x,num,5,7.2,..) = result
a = int(input("First no : "))
b = int(input("Second no : "))
op = input("Which operation do u want? [+ - * /] : ")
result = 0
if op=='+' :
    result = a + b
elif op=='-' :
    result = a - b
elif op=='*' :
    result = a * b
elif op=='/' :
    result = a / b
else :
    print("invalid operator")
    break
print(a, op, b, '=', result)

# Odd / Even
n = int(input("Enter no : "))
if n%2 == 0 :
    print(n,"is Even")
else :
    print(n,"is Odd")

# Multiplication table
n = int(input("TABLE of : "))
for i in range(1,11):
    print(n,'x',i,'=',n*i)

# Age Calculator
def age(birthyear):
    your_age = 2021 - birthyear
    return your_age
yr = int(input("Enter your birth year : "))
ans = age(yr)
print("You are",ans,"years old.")

# Power
a = int(input("Enter base no : "))
b = int(input("Enter power : "))
power = a**b
print(power)

# Divisibility
a = int(input("Enter the no : "))
b = int(input("Enter second no : "))
if a%b == 0 :
    print(a,"is divisible by",b)
else :
    print(a,"is not divisible by",b)

# Division
a = int(input("First no (Divident) : "))
b = int(input("Second no (Divisor) : "))
d = a/b
q = a//b
r = a%b
print("Division :",d)
print("Quotient :",q)
print("Remainder :",r)

# Which character
ch = input("Enter any character : ")
if ch>='A' and ch<='Z' :
    print('You entered a Uppercase character')
elif ch>='a' and ch<='z' :
    print('You entered a Lowercase character')
elif ch>='0' and ch<='9' :
    print('You entered a Digit')
else :
    print('You entered a Special character')

# Swap variables
a = int(input("Enter no. a : "))
b = int(input("Enter no. b : "))
swap = a
a = b
b = swap
#or without third variable:

a += b
b = a - b
a = a - b
print("a:",a,"b:",b)


num = int(input("Enter a no. : "))
s = str(num)
l = len(s)
add = 0
for i in range(l):
    add += int(s[i])
print(add)

# Calendar - month
import calendar
mm = int(input("Enter month : "))
yy = int(input("Enter year : "))
print(calendar.month(yy,mm))

# Calendar - year
import calendar
yy = int(input("Enter year : "))
for mm in range(1,13):
    print(calendar.month(yy,mm))

# Convert ascii
choose = input("What do u have? ord or chr : ")
if choose=='ord' :
    a = int(input("Enter order : "))
    c = chr(a)
    print(c)
elif choose=='chr' :
    a = str(input("Enter chracter : "))
    o = ord(a)
    print(o)
else :
    print("Choose ord/chr ")


d = int(input("Enter decimal : "))
b = bin(d)
o = oct(d)
h = hex(d)
print('Binary :',b,'Octa :',o,'Hexa :',h)

# randomly print taken ; to be modified for input of bin;oct;hex

choose = input("binary,octa or hexa : ")
if choose=='binary' :
    print("Write 0b'number' :")
elif choose=='octa' :
    print("Write 0o'number' :")
elif choose=='hexa' :
    print("Write 0x'number' :")
else :
    print("invalid option")

# Dice
import random
dice = random.randint(1,6)
print(dice)

# Toss
import random
ans = random.randint(1,2)
if ans==1 :
    print("True")
elif ans==2 :
    print("False")
else :
    print("Doubt")
print(ans)

# Maximum
x=y=z=0
x = int(input("Enter 1st no. : "))
y = int(input("Enter 2nd no. : "))
z = int(input("Enter 3rd no. : "))
max = x
if y>max :
    max = y
if z>max :
    max = z
print("Largest no is",max)

# Quadratic Equation
import math
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
x1 = -b + math.sqrt( b**2 - 4*a*c ) / 2*a
x2 = -b - math.sqrt( b**2 - 4*a*c ) / 2*a

# Reverse of a 2 digit no.
n = int(input("Enter a 2 digit no. : ")) #32 #48
d1 = n//10   #3 #4
d2 = n%10    #2 #8
rev = d2 * 10 + d1
print("Reversed no. is",rev)

# Triangle
import math
a = int(input("Enter side 1 : "))
b = int(input("Enter side 2 : "))
c = int(input("Enter side 3 : "))
pm = a + b + c
# s = (a + b + c) / 2
s = (pm) / 2
area = math.sqrt( s*(s-a)*(s-b)*(s-c) )
print("Perimeter :",pm)
print("Area :",area)

# starPATTERN
n = int(input("Enter rows: "))
for i in range(n+1):
    print('*' * i)


# User input List

from typing import List
l = [int(l) for l in input("Enter elements seperated by commas(,) : ").split(',')]
print("The list is: ",l)

lst = []
n = int(input("Enter the total number of elements: "))
for ele in range(1, n+1):
    element = int(input(f"Enter element {ele}: "))
    lst.append(element)
print("The list is: ",lst)


# smallest
smallest = lst[0]
for i in lst:
    if i < smallest:
        smallest = i
print("Smallest is", smallest)

# smallest using min
print("Smallest is", min(lst))


# ERRORS
'''
    Syntax
    Semantics
    Logical
    _
    Standard
    Arithmetic
    Assertion
    Attribute
    Environment
    EOF
    FloatingPoint
    Import
    Index
    IO
    Key
    KeyboardInterrupt
    Lookup
    Memory
    Name
    NotImplemented
    OS
    Overflow
    Runtime
    Syntax
    System
    SystemExit
    Type
    UnboundLocal
    Unicode
    Value
    Windows
    ZeroDivision
'''
# Exception
try:
    pass
except:
    pass

# OOPS
''' '''

# dictionaries of the list class
print(dir(list))

# __name__  __main__
# __init__


# 



''' TRICKS '''

# import this
# import antigravity

```
