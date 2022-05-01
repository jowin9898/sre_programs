n=int(input(" Please Enter the Maximum Value : "))
t=0
s=0
for number in range(1, n+1):
    if(number % 2 == 0):
        t=t+number
    elif(not(number % 2 == 0)):
        s=s+number
print("The Sum of Even Numbers = "  ,t)
print("The sum of Odd Number = : " ,s)
