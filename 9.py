def solver():
	for a in range(1, 334):
		for b in range (2, 335):
			c = 1000 - a - b
			if a != b and b != c and a != c and a<b<c:
				if a**2+b**2 == c**2:
					print (a,b,c)
					return a*b*c

result = solver()
print (result)