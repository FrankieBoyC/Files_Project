import json

file = open('friends_json.txt', 'r')
file_contents = json.load(file) #reads file and turns it into a dictionary

file.close()

print(file_contents['friends'][0])

cars = [
    {'make': 'Toyota', 'year': 2014},
    {'make': 'Ford', 'year': 2013},
    {'make': 'Honda', 'year': 2012}
]

#Use json.dump function to load dictionary into a file
file = open('cars_json.txt', 'w')
json.dump(cars, file)
file.close()

