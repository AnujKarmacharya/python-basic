# def myfun(n):
#     return lambda a:a*n
# # lambda always return type

# dodubler=myfun(2)
# print(dodubler(3))


def star(func):
    def wrapper():
        print("*" * 10)
        func()
        print("*" * 10)

    return wrapper


@star
def hello():
    print("hello")


hello()
