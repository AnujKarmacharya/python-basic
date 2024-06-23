# def greet(name):
#     print(f"hello!!{name}")
#     print("How are you?")
# greet("ram")

# def per(name,age):
#     print(f"""
#         Hello !!{name}
#         Age:{age}
#     """)
# per(age=10,name="ram")


# def sum(*args):
#     total=0
#     for n in args:
#         total+=n
#     print(total)

# sum(1,2,3,4)

# # kwargs
# def person(**kwargs):
#     print(kwargs["name"],kwargs["age"])
# person(name="ram",age=5,gender="male",birth=2012)

# def sum(a,b):
#     return a+b

# fun=sum(1,2)
# print(fun)

# recurssion

def num(n):
    print(n)
    if n == 10:
        return
    num(n+1)
num(1)




