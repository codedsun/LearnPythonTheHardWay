#Exercise 20
from sys import argv
script, filename = argv

def print_all(f):
    print(f.read())

def rewind(f):
    print(f.seek(0))

def print_a_line(linecount, f):
    print (linecount, f.readline())

currentFile = open(filename)

print("First let's print everything present in the file")

print_all(currentFile)

print("Reversing the file like a tape")
rewind(currentFile)

currentLine = 1
print_a_line(currentLine, currentFile)

currentLine = currentLine+1

print_a_line(currentLine, currentFile)
    
