#Exercise 32: Loops and List
the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quaters']

#for loop in the list

for number in the_count:
    print("This is %d count"%number)

for fruit in fruits:
    print("A fruit of type %s"%fruit)

for i in change:
    print("I got %r"%i)

#Building empty list and then appending it

element=[]
for i in range(0,6):
    print("Adding the %d in the list"%i)
    element.append(i)

for i in element:
    print("Element %d"%i)
    
