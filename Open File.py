import os
import requests
import json         # The json module makes it easy to parse JSON strings and files containing JSON object.
#import jsonpath
import os           ## import os operating sytem library
os.chdir ("L:/SOFTWARE/PYTHON/TEMP")
os.getcwd()
############################################################################
f = open("person.json","")    # "w" for write "r" for read
f.close()
print ("Found file=person.json")

person = '{"name": "Bob", "languages": ["English", "Fench"]}'
person_dict = json.loads(person)
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print( person_dict)
# Output: ['English', 'French']
print(person_dict['languages'])     # parse the json using json.loads to create a dictionary
#-------------------------------------------------------------------------------
#{"name": "Bob", 
#"languages": ["English", "Fench"]   }
#-------------------------------------------------------------------------------
f = open('c:\temp\person.json') as f:
  data = json.load(f)
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(data)
