def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)



thing = int(input("write a number"))
print (fib(thing))
