class Solver:
	def __init__(self, length):
		self.length = length
		self.answer = [] 
		self.productionCheck()

	def check(self):
		string = str(self.product)
		if string[::1] == string[::-1]:
			return True

	def productionCheck(self):
		for num1 in range(10**self.length-1, 10**(self.length-1)-1, -1):
			for num2 in range(10**self.length-1, 10**(self.length-1)-1, -1):
				self.product = num1 * num2
				if self.check():
					self.answer.append(self.product)
		self.product = max(self.answer)
		return self.product

a = Solver(3)
result = a.productionCheck()
print (result)
