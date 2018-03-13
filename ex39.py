#ex39: Doing things to a list

ten_things = "Apples Oranges Crows Telephones Light Sugar"

print("There are not 10 things in the list, let me fix that")

stuff = ten_things.split(' ')
more_stuff = ['Day','Night','Song','Frisbee','Corn','Banana','Girl','Boy']

while(len(stuff)!=10):
    next_one = more_stuff.pop()
    print("Adding",next_one)
    stuff.append(next_one)
    print("There are %d items in a row"%len(stuff))

print("There we go ",stuff)

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff))
