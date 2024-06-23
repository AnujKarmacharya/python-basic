person = {
    "name": "Ram",
    "age": 2,
    "gender": "male",
    "address": "hyd",
    "phone": 9876543210,
    "hobbies": [
        "singing",
        "dancing",
    ]
}
print(len(person))
print(person.keys())
print(person.values())
print(person.items())

print(person.get('names', "kei xaina"))
person.update(
    {
        'name':"shyam"
    }
    )
print(person.get('name', "kei xaina"))
print(person.values())

# tuple
numbers=(1,3,4,2,1)
print(numbers.count(1))


# set

a={1,5,4,9,3}
b={4,2,7,8}
print(a.intersection(b))
print(a.union(b))
print(a.difference(b))
     
