
def primeNcheck(n):
	for num in range(2, n):
		if n%num == 0:
			return False
	return True


class Solver:
	def __init__(self, number):
		self.number = number
		self.cnt = 2

	def summation(self):
		for n in range(3, self.number+1, 2):
			if primeNcheck(n):
				self.cnt+=n
		return self.cnt

a = Solver(2000000)
result = a.summation()
print (result)
	