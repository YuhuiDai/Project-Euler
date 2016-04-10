class Solver:
	def __init__(self, upperN):
		self.upperN = upperN
		self.Sum1 = 0
		self.Sum2 = 0
		self.SumOfSquare()
		self.SquareOfSum()

	def SumOfSquare(self):
		for num in range (1, self.upperN+1):
			self.Sum1 += num**2

	def SquareOfSum(self):
		cnt = 0
		for num in range (1, self.upperN+1):
			cnt += num
		self.Sum2 = cnt**2

	def Difference(self):
		return abs(self.Sum1-self.Sum2)

a = Solver(100)
dif = a.Difference()
print (dif)