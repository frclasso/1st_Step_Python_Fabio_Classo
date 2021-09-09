
# importing 
import json

# a partir de uma string
# string to json
person = '{"name":"Bob","languages": ["English", "French"]}'

print(type(person))
print(person)
print()

person_dict = json.loads(person) # READ A STRING
print(type(person_dict))
print(person_dict)
print(person_dict['languages'])
print()

# prettify
#print(json.dumps(person_dict, indent=4))
print(json.dumps(person_dict, indent=4, sort_keys=True))