class Sequence:
	def __init__(self, number):
		self.number = number
		self.cnt = 3
		self.order = 1

	def primeCheck(self, n):
		for num in range(2, n):
			if n%num == 0:
				return False
		return True

	def finder(self):
		while self.order < self.number:
			if self.primeCheck(self.cnt):
				self.order += 1
			self.cnt+=1
		return self.cnt-1


a = Sequence(10001)
result = a.finder()
print (result)