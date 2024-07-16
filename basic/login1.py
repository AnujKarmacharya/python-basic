val={}
islogin = True
while islogin:

    print("""What would you like to do:-
1>Login
2>Sign up""")

    ch=input("Enter your choice:-")

    if(ch.lower()=="signup" or ch.lower()=="sign up" or int(ch)==2):
        mail=input("Enter Email:-")
        password=input("Enter Password:-")
        val.update({mail:password})

    elif(ch.lower()=="login" or int(ch)==1):

        mail=input("Enter Email:-")
        password=input("Enter Password:-")

        temp1=list(val.keys())
        temp2=list(val.values())

        count=len(temp1)

        for i in range(count):

            if (temp1[i]==mail and temp2[i]==password):
                print(val)

            else:
                print("Incorrect Email or Password")


    else:
        print("Please Enter login or signup!!!")

        
    check=input("Do you want to continue? Y/N:-")
    if check.lower() == "y":
        islogin=True
    elif check.lower()=="n":
        islogin = False