#Exercise 19: Functions and Variables

def cheese_and_crackers(cheese_count,box_of_crackers):
    print("You have %d cheeses!"%cheese_count)
    print("You have %d boxes of crackers"%box_of_crackers)
    print("That\'s enough for the party man! Get the blanket \n")

print("We can just give the functions number directly")
cheese_and_crackers(10,20)

# using variables from out string
print("Using variables")
cheese_count = 10
box_of_cracker = 20
cheese_and_crackers(cheese_count, box_of_cracker)

print("Doing maths inside this is also fun, Let's try")
cheese_and_crackers(10+4,20+4)

