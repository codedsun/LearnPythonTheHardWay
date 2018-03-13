from sys import argv

sys, filename = argv
print("We are going to erase %r",filename)
print("If you don\'t want it hit ctrl+c ")
print("If you want it hit enter")
input("?")

print("Opening the file")

file = open(filename,'w')

print("Truncating the file")
file.truncate()

print("Now enter 3 lines")
line1 = input("Enter the first line \n")
line2 = input("Enter the second line \n")
line3 = input("Enter the third line \n")

print("I am going to write them into the file \n")

file.write(line1+"\n"+line2+"\n"+line3)

print("Finally closing it")
file.close()
