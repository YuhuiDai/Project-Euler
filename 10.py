class Solver:
	def __init__(self, power):
		self.power= power

	def sumDigit(self):
		num = 2**self.power
		string = str(num)
		mylist = list(string)
		cnt = 0
		for n in mylist:
			cnt += int(n)
		return cnt

a = Solver(1000)
result = a.sumDigit()
print (result)