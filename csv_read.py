file = open('csv_data.txt', 'r')
data = file.readlines()
file.close()

data = [line.strip() for line in data[1:]]

for line in data:
    person_data = line.split(',')
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].title()
    degree = person_data[3].capitalize()

    print(f'{name} is {age}, studying {degree} at {university}.')