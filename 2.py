def Fibonacci(n):
	if n > 2:
		return Fibonacci(n-1)+Fibonacci(n-2)

	if n == 1:
		return 1

	if n == 2:
		return 2	

class Solver:
	def __init__(self, upperlimit):
		self.upperlimit = upperlimit
		self.FibonacciList = []
		self.ListCreation()
	
	def ListCreation(self):
		number = 1
		while Fibonacci(number) < self.upperlimit:
			num = Fibonacci(number)
			if num%2 == 0: 
				self.FibonacciList.append(num)
			number += 1

	def EvenSum(self):
		cnt = 0
		for num in self.FibonacciList:
			cnt += num
		return cnt


a = Solver(4000000)
result = a.EvenSum()
print (result)
