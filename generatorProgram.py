
'''
def func():
    count=0
    while(count<100):
        count+=1

        yield count

g=func()
print(next(g))
print(next(g))
print(g)

for val in g:
    print(val,end=" ")

'''
# =====================================================================================================================
''' create a class will be using next dunder value to generate the value upto the value 10 '''

class value:
    def __init__(self,num):
        self.num=num
        self.index=0

    def __next__(self):
        if self.index < self.num :
            self.index=self.index+1
            return self.index
        else:
            return "stop iteration"

class iterablegenerator:
    def __init__():
        return value(num)


val1=iterablegenerator(10)
print(next(val1))
print(next(val1))
print(next(val1))
print(next(val1))
print(next(val1))
print(next(val1))
print(next(val1))
print(next(val1))
print(next(val1))
print(next(val1))
print(next(val1))




    
