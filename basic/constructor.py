class House:
    door = 1
    window = 2
    color = "red"

    def __init__(self, door, window, color):
        self.door = door
        self.window = window
        self.color = color

    def __str__(self):
        return self.color


ram_house = House(door=2, window=4, color="blue")
print(ram_house)
# print(ram_house.color)
# print(ram_house.window)
# print(ram_house.door)

# hari = House(door=1,window=4,color="red")
# print(hari.color)
# print(hari.window)
# print(hari.door)

# class Employee:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary

#     def __eq__(self, object) -> bool:
#         return self.salary == object.salary

#     def __le__(self,object):
#         return self.age <= object.age

# ram=Employee("ram",20,19000)
# shyam=Employee("shyam",21,18000)

# print(ram<=shyam)
