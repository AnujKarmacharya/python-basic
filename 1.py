

a=input("Enter any operator +, -, *, /, %, **, //:-")
b=int(input("Enter 1st Number:")) 
c=int(input("Enter 2nd Number:"))



if a=="+" :
    print("Answer =",b+c)
elif a=="-" :
    print("Answer =",b-c)
elif a=="*" :
    print("Answer =",b*c)
elif a=="/" :
    if(c==0):
        print("Cannot divide the numbers i.e infinity")
    else:
        print("Answer =",b/c)
elif a=="%" :
    print("Answer =",b%c)
elif a=="**" :
    print("Answer =",b**c)
elif a=="//" :
    print("Answer =",b//c)
else :
    print("No such Operator")
    


