

class MultipleSolver:
	def __init__(self, num1, num2, upperlimit):
		self.num1 = num1
		self.num2 = num2
		self.upperlimit = upperlimit
		self.mutiplelist = []

	def findmultiple(self):
		for number in range(self.upperlimit):
			if number not in self.mutiplelist:
				if number%self.num1 == 0:
					self.mutiplelist.append(number)

		for number in range(self.upperlimit):
			if number not in self.mutiplelist:
				if number%self.num2 == 0:
					self.mutiplelist.append(number)

	def Sum(self):
		cnt = 0
		for number in self.mutiplelist:
			cnt += number
		return cnt

result = MultipleSolver(3, 5, 1000)
result.findmultiple()
myresult = result.Sum()
print (myresult)

