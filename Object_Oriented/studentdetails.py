class studentdetails:
    
    def __init__(self,sname,marks):
        self.sname=sname
        self.marks=marks

    def studentMarks(self):
        return ("student {} got marks as {}".format(self.sname,sum(self.marks)/len(self.marks)))
    
    def __len__(self):
        return len(self.marks)


s1=studentdetails("lokesh",[90,80,60])

print(s1.studentMarks())
print(len(s1))
print("last :",s1.__len__())
















# # creating an object of studentdetails class 
# s1= studentdetails()
# s2=studentdetails()

# print(s1.studentInfo())

# print("s1 :",s1.s_id)

# s1.s_id=101
# print("s1 after change:",s1.s_id)

# print("class  :",studentdetails.s_id)

# studentdetails.s_id=1021
# print("class after change :",studentdetails.s_id)
# s3=studentdetails()

# print("s3 :",s3.s_id)


# '''if we a class variable and we make the changes to object , changes will done in memory object , original data will remain same'''