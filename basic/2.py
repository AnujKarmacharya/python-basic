# print string in line

word=input("Enter any word or string")
for i in word:
    print(i)

# print multiplication table

n=int(input("Enter the  number for multiplication table:"))
t=int(input("Enter upto which term:"))

i=1
while i<=t :
    print(f"{n} * {i} = {n*i}")
    i+=1
