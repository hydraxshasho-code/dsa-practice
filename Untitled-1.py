x = 0
for x in range(1, 11):
    if x == 10:
        continue          # skip printing when x is 10
    print("The value of x is: ", x)

print("The final value of x is: ", x)

if x == 10:
    print("x is 10")
else:
    print("x is not 10")