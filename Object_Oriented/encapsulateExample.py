from abc import ABC, abstractmethod
class company:
    companyName="Futurense"

    @abstractmethod
    def department(self):
        pass

class marketingDept(company):
    def department(self):
        print("This is Marketing department ")
    
class hrDept(company):
    def department(self):
        print("This is HR Department")


h1=hrDept()
# print(h1.department())
# print(h1.companyName)
company.department(h1)