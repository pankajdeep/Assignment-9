#Q.1- Name and handle the exception occured in the following program:
#a=3
#if a<4:
#   a=a/(a-3)
#   print(a)
a=3
try:
    if(a<4):
        a=a/(a-3)
        print(a)
except ZeroDivisionError as msg:
    print("The name of the exception is ZeroDivisionError and the message is:",msg)


#Q.2- Name and handle the exception occurred in the following program: 
#l=[1,2,3] 
#print(l[3])
l=[1,2,3]
try:
    print(l[3])
except:
    print("The name of the Exception is IndexError and the message is list index out of range")


#Q.3- What will be the output of the following code:
# Program to depict Raising Exception
#try:
#   raise NameError("Hi there")  # Raise Error
#except NameError:
#   print("An exception")
#   raise  # To determine whether the exception was raised or not
Output is:
An exception
NameError:Hi there


#Q.4- What will be the output of the following code: 
# Function which returns a/b
#def AbyB(a , b):
#    try:
#        c = ((a+b) / (a-b))
#    except ZeroDivisionError:
#        print("a/b result in 0")
#    else:
#        print(c)
#Driver program to test above function
#    AbyB(2.0, 3.0)
#    AbyB(3.0, 3.0)
Output is:
case 1 output: -5
case 2 output: a/b result in 0


#Q.5- Write a program to show and handle following exceptions: 
#1. Import Error 
#2. Value Error 
#3. Index Error
1.Import Error
try:
    import maths
except ImportError:
    print("Import error Occured")

2.Value Error
try:
    inp=int(input("Enter a string to throw value error exception"))
except ValueError:
    print("Cant enter string to an integer variable")

3.Index Error
try:
    arr=['a','b',3,4]
    print(arr[4])
except IndexError:
    print("Index out of bound")
