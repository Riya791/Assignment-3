# Python program to read
# json file


import json

# Opening JSON file
f = open('input.json', "r")

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
my_list = []
for i in data['parametersList']:
    my_dict = {
        "parameterName": i['parameterName'],
        "min": i['min'],
        "max": i['max'],
        "avg": i['avg']

    }

    my_list.append(my_dict)
R_list = json.dumps(my_list)


with open("input.json", "w") as file1:
    file1.write(R_list)
print(my_list)

# Closing filez
f.close()
