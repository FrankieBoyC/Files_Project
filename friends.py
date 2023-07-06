"""
1) Ask the user for a list of three friends.
2) For each friend, tell the user whether they are in the same city or not.
3) For each nearby friend, we'll save their name to 'nearby_friends.txt.'
"""

friends = input("Enter a list of three friends separated by commas no spaces: ").split(',')

people = open("people.txt", "r")
people_nearby = [line.strip() for line in people.readlines()]

people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open("nearby_friends.txt", "w")

for friend in friends_nearby_set:
    print(f'{friend} is nearby! Meet up with them.')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()