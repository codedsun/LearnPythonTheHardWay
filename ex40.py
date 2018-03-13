#Ex40: Dictionaries

cities = {'CA': 'San Francisco', 'MI':'Detroit', 'FL':'Jacksonville'}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(the_map, state):
    if state in the_map:
        return the_map[state]
    else:
        return "Not Found"

cities['_find'] = find_city
while(True):
    print("State? Enter to quit")
    state = input(">")

    if not state:break
    city_found= cities['_find'](cities,state)
    print(city_found)
