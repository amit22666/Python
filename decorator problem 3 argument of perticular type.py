def only_int_argument(func):
    
    def wrapper_function(*args):
        #checking 
        # for arg in args:
        #     if type(arg)!=int:
        #         print("logger -> invalid arg")
        #         return
        # return func(*args)
        
        #improvement in thinking
        if all([type(arg)==int for arg in args]):
            return func(*args)
        print("logger -> invalid arg")
    return wrapper_function


@only_int_argument
def add_all(*args):
    total=0
    # print(type(add_all)
    for i in args:
        total+=i
    return total
    
print(add_all(1,2,3,4,5))
