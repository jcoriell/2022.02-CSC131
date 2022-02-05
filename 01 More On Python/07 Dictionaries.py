# A dictionary is a set of key-value pairs

person_1 = {
    "first_name": "Josh",
    "last_name": "Coriell",
    "age": 954
}

person_2 = {
    "first_name": "Heath",
    "last_name": "Tims",
    "age": 7867, 
    "stats": {
        "vertical": 657,
        "max_speed": 675
    }
}

print(person_2["first_name"])
print(person_2["last_name"])

people = [person_1, person_2]

for person in people:
    print(person["first_name"])
    print(person.get("stats", ""))

print(person_2["stats"]["vertical"])


# accessing keys
for k in person_2.keys():
    print(k)

# accessing keys and values
for key, value in person_2.items():
    print(key, value)

# accessing the values
for value in person_2.values():
    print(value)

