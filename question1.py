def distance(x1,x2,y1,y2):
	if(x1>x2):
		a=x1-x2
	else:
		a=x2-x1
	if(y1>y2):
		b=y1-y2
	else:
		b=y2-y1
	import math
	c=math.sqrt(a**2+b**2)
	return c

x1=int(input("Write the x1"))
y1=int(input("Write the y1"))
x2=int(input("Write the x2"))
y2=int(input("Write the y2"))

answer=distance(x1,x2,y1,y2)
print(answer)
