# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:
import json

json_list = []

try:
    with open('csv_exerciseTwo.txt', 'r') as file_reader:
        for lines in file_reader.readlines():
            team, city, state = lines.strip().split(',')
            data = {'team': team,
                    'city': city,
                    'state': state}
            json_list.append(data)
except IOError:
    print('File not found!')

try:
    with open('json_file.txt', 'w') as json_file:
        json.dump(json_list, json_file)
except IOError:
    print('File not found!')