class Solver:
	def __init__(self, number):
		self.number = number
		self.primelist = []
		self.listcreation()
	
	def primeFinder(self,n):
		for num in range(2, n):
			if n%num == 0:
				return False
		return True	

	def listcreation(self):
		for num in range (2, self.number+1):
			if self.primeFinder(num):
				self.primelist.append(num)
		print (self.primelist)

	def smallestEven(self):
		multiple = 4
		for num in self.primelist:
			multiple = multiple*num
		
		for n in range(1, self.number+1):
			div = multiple*n
			if EvenDiv(div, self.number) == True:
				return div


def EvenDiv(n, upperlimit):
	for num in range(2, upperlimit+1):
		if n%num != 0:
			return False
	return True


a = Solver(20)
result = a.smallestEven()
print (result)