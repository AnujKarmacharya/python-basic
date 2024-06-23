values={}

def star(func):
    def wrapper():
        print("*" * 20)
        print("%" * 20)
        func()
        print("*" * 20)
        print("%" * 20)
    return wrapper

@star
def start():
    print(
        """1.Login
2.Sign up""")
start()

def login():
    a=input("Enter you Email:-")
    b=input("Enter you Password:-")
    
    temp1=values.keys()
    temp2=values.values()
    for j,i in temp1,temp2:
        if j == a and i==b:
            f=open("record.txt","r")
            print(f.read())
        else:
            print("Wrong Email or password")


def signup():
    f=open("record.txt", "a")
    email=input("Enter Email")
    password=input("Enter password")
    values.update({email:password})
    f.write(f"{values}")
    f.close()

    


ch=input("Chose what do you want to do:-")

if int(ch) == 1 or ch.lower() == "login":
    login()

elif int(ch) == 2 or ch.lower() == "signup" or ch.lower()=="sign up":
    signup()

    


