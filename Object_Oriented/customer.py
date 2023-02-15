class driver:
    def __init__(self,name,email,wallet):
        self.name=name
        self.email=email
        self.wallet=wallet
        print("driver")
    def printDetails(self):
        return ("{} having email-{} and wallet amount- {}".format(self.name, self.email, self.wallet))




class customer(driver):
    def __init__(self,name,email, wallet,trip_status):
        print("customer")

        driver.__init__(self,name,email,wallet)
        self.trip_status=trip_status



# c1= customer("lokesh","lokesh@gmail.com",10101011,"Active")
# print(c1.name,c1.email, c1.trip_status)
# print(c1.printDetails())






''' 
create a class having 3 instance variable 
- compare the addition of square of each individual is greater than the addition of square of second object 
return false otherwise return true

Example: (2,1,4)  (3,4,1)
        2**2+ 1**2 + 4**2 => 21
        3**2 + 4**2 +1**2 => 25
        21<25 (return true ) otherwise false
'''

class squareSum:
    def __init__(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        

    def __gt__(self,d):
        return not((self.num1**2 + self.num2**2 + self.num3**2)>(d.num1**2 + d.num2**2 + d.num3**2))



# a1=squareSum(2,1,4)
# a2=squareSum(3,4,1)
# print(a1.__gt__(a2))