'''
file handling :
            logging => module ( for logs maintaining)
            read and write operation
            stored in hard disk
            output with the (flash/ RAM )
            
            file operation:
                    open file
                    do operation 
                    close the file

'''

# filehandler=open("text.txt","r")
# datafile=filehandler.read()
# filehandler.close()
# print(datafile)

# writing to a file
# filehandler=open("text.txt","w")
# datafile=filehandler.write("hello guys")
# filehandler.close()
# print(datafile)

# reading and writing a file
# filehandler=open("text.txt","r+")
# datafile=filehandler.read()
# filehandler.write("wonderful")
# filehandler.close()
# print(datafile)


#appending and writing to a file
# filehandler=open("text.txt","r+")
# datafile=filehandler.read(3)
# print("current position :",filehandler.tell())
# filehandler.write("lokesh")
# filehandler.seek(15)
# filehandler.write("kumar")
# filehandler.close()
# print(datafile)

#appending and writing to a file
# filehandler=open("text.txt","a+")
# filehandler.seek(0)
# datafile=filehandler.read(3)
# print("current position :",filehandler.tell())
# filehandler.write("handling")
# filehandler.seek(15)
# filehandler.write("file")
# filehandler.close()
# print(datafile)

'''
Q.: to convert a number into binary , hexadecimal and octal 

'''
def binary_conversion(num):
    return bin(num)
def octal_conversion(num):
    return oct(num)

def hexadecimal_conversion(num):
    return hex(num)
    
def conversion():
    n=int(input("enter a number :"))
    b=binary_conversion(n)
    o=octal_conversion(n)
    h=hexadecimal_conversion(n)
    print("Binary Equivalent :",b)
    print("Octal Equivalent :",o)
    print("Hexadecimal equivalent :",h)
    st="{} can be written in binary as {} and in octal as {} and in hexadecimal as {}\n".format(n,b,o,h)
    fh1=open("conversion.txt","a+")
    fh1.write(st)
    fh1.close()


'''
take a input from a user separated by commas, we need to check whether :
that particular word is available in the line of another file, if it is available , we will save it to datamatch.txt ,
in case file not match create a file 
'''

def content_checker():
    fh1=open("text.txt","r+")
    datafh1=fh1.read()
    fh1.close()
    inp=input("enter words separated by commas :")
    inpList=inp.split(",")
    fh2=open("textmatch.txt","w+")
    fh3=open("textnotmatch.txt","w+")
    
    for val in inpList:
        if val in datafh1:
            fh2.write(val)
        else:
            fh3.write(val)
        fh2.write("\n")
        fh3.write("\n")
    fh2.close()
    fh3.close()


def content_checker_deeply():
    fh1=open("text.txt","r+")
    datafh1=fh1.read().lower()
    fh1.close()

    inp=input("enter words separated by commas :")
    inpList=inp.split(",")
    inpList=list(set(inpList))
    fh2=open("textmatch.txt","w+")
    fh3=open("textnotmatch.txt","w+")
    print(datafh1,type(datafh1))
    for val in inpList:
        if val.lower() in datafh1:
            fh2.write(val)
            fh2.write("\n")
        else:
            fh3.write(val)
            fh3.write("\n")

        
    fh2.close()
    fh3.close()


# content_checker_deeply()

# ====================================================================================================================================

# working with CSV files
'''
how to read a csv file in python (csvData.txt)
    example
    name, age , email 
    lokesh, 23, lokesh@gmail.com
    happy, 20, happy @gmail.com

'''
def csv_handler():
    filehandler=open("csvData.txt","a+")
    filehandler.seek(0)
    datafile=filehandler.readlines()
    filehandler.close()
    print("data fetched successfully")
    fh2=open("gmailaccount.txt","w+")
    for data in datafile:
        mylist=data.split(",")
        if "gmail" in mylist[2]:
            s="{} is of {} age and having id as {}".format(mylist[0],mylist[1],mylist[2])
            fh2.write(s)
            fh2.write("\n")
    print("operation successful")
    fh2.close()





csv_handler()
