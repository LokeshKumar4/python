s="user"
# for i in s:
#     print(i)

# print(next(s))

stringIterator =iter(s)

print(next(stringIterator))

'''
Iterable :
        we can run a for loop
        any iterable => iter() => iterator 
        iterable are going to be finite
    
Iterator :are those object where we get one  element at a time using next() 
        on  next() => gives next value
        if no element => returns message - stop execution 
        if you call iter method on iterator then it will gives same iterator 
        iterable are going to be finite ,but iterator can be finite or infinite

    
'''

'''
craete a user defined exception :
                in case first value < second value => raise bigNumber
                else => raise smallNumber



'''