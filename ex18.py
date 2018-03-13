#now using functions
from sys import argv

def print_two(*args):
    for arg in args:
        print(arg)
        

#bullshit 
def print_two_again(arg1, arg2):
    print("arg1 %s, arg2 %s"%(arg1,arg2))

def print_one(arg1):
    print("arg1 %s",arg1)

def print_two(arg1, arg2):
    print("arg1 %s, arg2 %s"%(arg1,arg2))
    
def print_none():
    print("I got nothing")


#Now calling functions

print_two("Suneet","Sasas")
print_two_again("Suneet","Srivastava")
print_one("Suneet")
print_two("Suneet","Srivastava")
print_none()
