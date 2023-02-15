
def topper(val1,func):
    
    def decorator_function(func,val1):
        print(val1)
        def wrapper_function(*args,**kwargs):
            print(kwargs.values())
            if "Tushar" in kwargs.values():
                print("True")
                func(*args,**kwargs)
            else:
                print("access denied")
        return wrapper_function
    return decorator_function(func,val1)

def test(**kwargs):
    print("original")
    for key,val in kwargs.items():
        print(f"{key }: {val}")

mydictionary={"name":"lk","pass":"123456"}


x=topper(10,test(**mydictionary))

'''
create a list of dictionary containing two keys 
'''