def triangle(n):

    for ts in range(1,n+1):
        print("T"*ts)
    for ts in range(n,0,-1):
        print("T"*ts)

ts= int(input("Write the number of T"))

triangle(ts)
