from math import *
while(1>0):
	print("THE CALCULATOR")
	print("1.addition")
	print("2.subraction")
	print("3.multiplication")
	print("4.division")
	print("5.all")
	print("6.exponential and factorial")
	print("7.square root and cube root")
 	print("8.sin cos tan")
	print("9.log and ln")
	print("10.angular conversion")
	print("11.sinh cosh tanh")
	print("12.constants")
	print("13.exit")
	a=float(input("enter your choice:"))
	if(a==1):
		b=float(input("enter the num1 "))
        	c=float(input("enter the num2 "))
		print("the addition of %f and %f is %f" % (b,c,b+c))
	if(a==2):
		b=float(input("enter the num1 "))
        	c=float(input("enter the num2 "))
		print("the subraction of %f and %f is %f" % (b,c,b-c))
	if(a==3):
		b=float(input("enter the num1 "))
        	c=float(input("enter the num2 "))
		print("the multiplication of %f and %f is %f" % (b,c,b*c))
	if(a==4):
		b=float(input("enter the num1 "))
        	c=float(input("enter the num2 "))
		print("the division of %f and %f is %f" % (b,c,b/c))
	if(a==5):
		b=float(input("enter the num1 "))
        	c=float(input("enter the num2 "))
		print("the addition of %f and %f is %f" % (b,c,b+c))
		print("the subraction of %f and %f is %f" % (b,c,b-c))
		print("the multiplication of %f and %f is %f" % (b,c,b*c))
		print("the division of %f and %f is %f" % (b,c,b/c))
	if(a==6): 
		import math
		b=float(input("enter the num1 "))
		c=float(input("enter the power "))
		d=b**c
		e=math.factorial(b)
		print("%f to the power %f is %f" % (b,c,d))
		print("factorial of %f is %f" % (b,e))
	if(a==7):
		b=float(input("enter the num1 "))
		c=math.sqrt(b)
		d=pow(b,0.33333333)
		print("square root=%f  cube root=%d" % (c,d))
	if(a==8):
		b=float(input("enter the num "))
                c=sin(b)
		d=cos(b)
		e=tan(b)
 		print("sin value=%f  cos value=%f  tan value=%f" % (c,d,e))
	if(a==9):
		import math
		b=float(input("enter the num "))
		c=math.log10(b)
		d=math.log1p(b)
		print("log value=%f  ln value=%f" % (c,d))
	if(a==10):
		import math
		b=float(input("enter the angle in deg "))
		print(math.radians(b))
		c=float(input("enetr the angle in rad "))
		print(math.degrees(b))
	if(a==11):
		import math
		b=float(input("enter the num "))
                c=math.sinh(b)
		d=math.cosh(b)
		e=math.tanh(b)
 		print("sinh value=%f  cosh value=%f  tanh value=%f" % (c,d,e))
	if(a==12):
		import math
		print("pi=%f" % math.pi)
		print("e=%f" % math.e)	
	if(a==13):
		break
	
		



		
	

	
