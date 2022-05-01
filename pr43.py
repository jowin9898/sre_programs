n1=int(input("enter the 1st number "))
n2=int(input("enter the 2nd number "))
n3=int(input("enter the 3rd number "))
if(n1>=n2) and (n1>= n3):
    a=n1
elif(n2>=n1) and (n2>=n3):
    a=n2
else:
    a=n3
print("the largest number is " ,a)
