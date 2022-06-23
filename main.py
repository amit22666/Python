Chapter 14 Intro

def square(x):
    return x**2

# variable mein ek function daal dia. s bhi square ko point karega
s = square

print(s.__name__)
print(square.__name__)

print(s)
print(square)

#### OUTPUT
square
square
<function square at 0x7fc52af92d30>
<function square at 0x7fc52af92d30>
####

---
# Pass function as argument : Python tutorial 166

l = [1,2,3,4]  #iterable

def func(x):
    return x**2

# 3 approach to do square

#1st #list comprehension
print([func(i) for i in l])

# 2nd
# print(list(map(func,l)))

# 3rd
# def my_app(func,l):
#     new_list = []
#     for i in l:
#         new_list.append(func(i))
#     return new_list
    
# print(my_app(func , l))

---

# Function returning function : Python tutorial 167
# bakchodi

def outer_func():
    def inner_func():
        print("inner func print")
    return inner_func
    
var = outer_func()
var()

###OUTPUT
inner func print

---
# Decorators Part 2 : Python tutorial 170

# Decorators - enhance the functionality of other function
# @ use for decorator

# this decorator have errors
def decorator_function(any_function):
    def wrapper_function():
        print('this is awesome function')
        any_function()
    return wrapper_function


#ye fucntion execute hone se pehle kuch functionality execute ho - for that i will use decorator
@decorator_function  #expect a function
def func1():
    #because of decorator -> wapper_function will execute here
    print("this is function 1")
    
func1()

# # implementation of decorator function
# wrapper_function=decorator_function(apna_function)
# wrapper_function()

# in video
# func=decorator_function(func)
# func()

##3 problems in decorator - argument,return handling, doc string -> solution use args and kwargs , use return in wrapper , use @wraps

def decorator_function(any_function):
   def wrapper_function(*args,** kwargs):  #problem solved
        print('this is awesome function')
        return any function(*args,** kwargs)  #problem solved
    return wrapper_function
    
@decorator_function
def func(a):
    print(f'this is function with argument{a}')
func(5)
              I
@decorator_function
def add(a,b):
    returna+b
print(add(2,3))

---
Decorators part 3 : Python tutorial 171

from functools import wraps
def decoratpr_function(any_function):
   @wraps(any_function)
    def wrapper_function(*args,** kwargs):
        """this is wrapper function
        print('this is awesome function')
        return any_function(*args,** kwargs)
    return wrapper_function
    
@decorator_function
def add(a,b):
    "this is add function
    returna+b
print(add.__doc__)
print(add .__ name__)
                             

# function.__doc__ -> to get the doc string
# function.__name__ -> to get the function name

-----
