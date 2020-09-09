import json

with open('./states.json') as f:
    data = json.load(f)
    # print(data)
    
for person in data['people']:
    # print(person['name'], person['phone'])
    del person['has_license']

with open('./new_states.json', 'w') as f:
    json.dump(data, f, indent=2)
    