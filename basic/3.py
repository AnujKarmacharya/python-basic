import os.path

isvalid = True
while isvalid:
    print(
        """1. Create file:-
2. Add data in file:-
3. Delete File"""
    )
    ch = int(input("Enter Your Choice:-"))

    if ch == 1:
        f_name = input("Enter file name with extension:-")
        if os.path.isfile(f_name):
            print("File already exists")
        else:
            f = open(f_name, "w")
            w = input("Do you want to add data?Y/N:-")

            if w.lower() == "y":
                data = input("Enter the data:-")
                f.write(data)
                f.close()
            else:
                f.close()

    elif ch == 2:
        file = input("Enter the file name you want to add data to:-")
        if os.path.isfile(file):
            f = open(file, "a")
            data = input("Add data :-")
            f.write(data)
            f.close()
        else:
            print("File not found")

    elif ch == 3:
        f_name = input("Enter file name:-")
        if os.path.isfile(f_name):
            os.remove(f_name)
        else:
            print("File doesn't exist")

    else:
        print("Enter Valid input:")

    check = input("Do you want to continue?Y/N:-")
    if check.lower() == "y":
        isvalid = True
    else:
        isvalid = False
