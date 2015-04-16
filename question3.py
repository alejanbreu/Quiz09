def superpower(x,y):
    a = 1
    b = x
    while (a < y):
        b = b*x
        a = a+1
    return b
x= int(input("Write the number"))
y= int(input("Write the exponential"))

answer=superpower(x,y)
print(answer)
