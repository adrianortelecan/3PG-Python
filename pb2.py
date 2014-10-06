# 2. Second problem
# Define a class with two methods
# Use getString to read from console
# Print the input in upper case using printString
# Using __init__ method to construct the params.

class Test(object):
	def __init__(self,x):
		self.string = x 
	def printString(self):
		print(self.string.upper())
	def getString(self):	
		self.string = (raw_input("Please input a string: "))
	
testing = Test('String for test')
testing.printString()
testing.getString()
testing.printString()
