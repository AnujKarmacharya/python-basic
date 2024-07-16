# string -->> str
name="Ram 12"
print(type(name))


# numeric data type
# 1. Integer
a=10
print(type(a))

# 2. Float
a=10.1
print(type(a))

# sequence data type
fruits=["apple",2,"banana"]
print(fruits[1])    


# tuple

fruit=("apple",2,"banana")


# set

a={
    1,"hello",5,2,9
}

print(a)


# dictionary

person = {
    "name": "Ram",
    "age": 2,
    "gender": "male",
    "address": "hyd",
    "phone": 9876543210,
    "hobbies": [
        "singing",
        "dancing",
    ],
    "fav_movies": [
        "3 idiots",
        "3 idiots 2",
        "3 idiots 3",
    ],
    "friends": [
        {
            "name": "Shyam",
            "age": 3,
            "gender": "male",
            "address": "hyd",
            "phone": 9876543210,
            "hobbies": [
                "singing",
                "dancing",
            ],
            "fav_movies": [
                "3 idiots",
                "3 idiots 2",
                "3 idiots 3",
            ],
        },
        {
            "name": "Hari",
            "age": 3,
            "gender": "male",
            "address": "hyd",
            "phone": 9876543210,
            "hobbies": [
                "singing",
                "dancing",
            ],
            "fav_movies": [
                "3 idiots",
                "3 idiots 2",
                "3 idiots 3",
            ],
        },
    ]
}

# # print(person["name"])
# print(person["hobbies"][1])
# print(person['name'])
print(person["friends"][1]["fav_movies"][0])


# type casting

p=3.14
print(p)
p=int(p)
print(p)
p=str(p)


islogin=False
print(islogin)


