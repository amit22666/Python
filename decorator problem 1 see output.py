https://www.youtube.com/watch?v=dUffZZxSoXc&list=PLwgFb6VsUj_lQTpQKDtLXKXElQychT_2j&index=175&t=92s
Decorators Practice : Python tutorial 172

from functools import wraps

def print_function_data(func):
    @wraps(func)
    def wrapper_func(*args,**kwargs):
        print(f"you are calling add function {func.__name__}")
        print(f"{func.__doc__}")
        return func(*args,**kwargs) #caller ka return
    return wrapper_func  #decorator ka return

@print_function_data
def add(a,b):
   '''This function takes two numbers as arguments and return their sum'''
   return a+b
print(add(4,5))

implementation of wrapper
# wrapper_func = print_function_data(add)
# wrapper_func()

#output
#you are calling add function
#This function takes two numbers as parameters and return their sum
#9
