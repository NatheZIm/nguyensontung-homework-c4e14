#1
#How to check a variable’s type?
#- by using function type() which can tell you the value's type and variable's type
#eg:		
	#>>type(21)
	#<class ’int’>
#or 
	#>>n="Hello world"
	#<class ’str’>

	
	
#In what cases, you will get SyntaxError from the compiler telling you that some of your variables have invalid names? Can you give 3 different examples of invalid names?
#when you give illigal variable name or a name already exist in python keyword or libary , you will get SyntaxError
#EG:
#420blaeit="smoke weed" <---- this is illegal because variable started with number
#steven#$% = 45 <--- this variable contain illegal letter 
#class = "Computer Science 101" <---- class is a keyword in python 



#2
# r=int(input("Radius ? "))
# S=r*r*3.14
# print("Radius = ",S)

#3
# c=int(input("Enter the temperature ine Celsius "))
# f=c*1.8+32
# print(c,"(C) = ",f,"(F)")

#turtle

#1.Square
# from turtle import *
# color("green",'#FFEE58')
# shape("turtle")
# speed(2)
# begin_fill()
# for i in range (4):
#     forward(300)
#     left(90)
# end_fill()
# mainloop()

#2.Triangle
# from turtle import *
# color("green",'#FFEE58')
# shape("turtle")
# speed(2)
# begin_fill()
#
# for i in range (2):
#     forward(300)
#     left(120)
# forward(300)
# end_fill()
# mainloop()

#3. Circle
# from turtle import *
# color("green",'#FFEE58')
# shape("turtle")
# speed (-1)
# begin_fill()
# circle(150)
# end_fill()
# mainloop()
