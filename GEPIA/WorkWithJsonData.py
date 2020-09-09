''' 

JSON: JavaScript Object Notation 

Python Tutorial: Working with JSON Data using the json Module

'''

import json

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5513",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

data = json.loads(people_string)

print(type(data['people']))
# print(data)

for person in data['people']:
    # print(person['name'])
    del person['phone']
    
new_string = json.dumps(data, indent=4, sort_keys=True)

print(new_string)