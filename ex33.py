#Ex 33 : While loops

list= []
i=0
while(i<6):
    list.append(i)
    print("At the top i is %d"%i)
    i=i+1
    print("Numbers now %r"%list)
    print("At the bottom i is %d"%i)

print("The numbers:")
for n in list:
    print(n)
