#making dict and print it by calling the keys
d = {'name':'ram', 'age':23, 'surname':'obroei'}

print(d['name'])
print(d['age'])
print(d['surname'])

#changing name in the dictionary
d['name'] = 'kaalu'
print(d['name'])

#delete element or dictionary
#after deleting elements, it won't print the keys & values that you deleted
del d['surname']
print(d)
#del d
# writing "print(d)" and running it will give error as the dict gets deleted when you write and run it once

#get all keys and values
keys = d.keys()
print(keys)
values = d.values()
print(values)