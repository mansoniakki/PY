print("Learning about dictionaries")

#mydict = {'name' : 'Mangal', 'age' : 35, 'height' : '170cm'}

#print(mydict)
#print(mydict['name'])

#print(mydict['age'])

#print(mydict['height'])

#mydict['city'] = 'London'

#print(mydict)

#mydict[1] = 'One'
#mydict[2] = 'Two'
#print(mydict)

#del mydict[2]

#print(mydict)

states = {'Oregon': 'OR','Florida': 'FL', 'California': 'CA', 'New York': 'NY', 'Michigan': 'MI'}
cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'
print("cities: ", cities)
print ('-' * 100)

print('NY state has: ', cities['NY'])
print('CA state has: ', cities['CA'])
