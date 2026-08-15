x=0
for x in range (1, 21):
    if x%2==0:
        print("Even: ", x)
    elif x==13:
        continue
    else: 
        print("Odd: ", x)
print("The final value of x is: ", x)