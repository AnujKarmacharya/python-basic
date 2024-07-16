# class House:
#     door=1
#     window=2
#     color="red"

#     def set_color(self, color):
#         self.color=color
    
#     def get_color(self):
#         return self.color
# ram_house=House()
# shyam_house=House()

# print(ram_house.color)
# ram_house.set_color("green")
# print(ram_house.get_color())


class Pizza:
    
    def roti(self):
        print("roti")
        return self
    
    def tomatoes(self):
        print("tomtoes")
        return self
    
    def cheese(self):
        print("cheese")
        return self

cheese_pizza=Pizza()

cheese_pizza.roti().tomatoes().cheese()


class Momo:
    
    def stuffing(self):
        print("kimma")
        return self
    def pitho(self):
        print("pitho")
        return self
    def design(self):
        print("classic")
        return self
    
momo=Momo()

momo.stuffing().pitho().design()

