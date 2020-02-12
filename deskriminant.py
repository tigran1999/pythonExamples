import math  

class Arguments:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c


def discriminant(a, b, c):
	
	if a == 0:
		if b != 0:
			print(c/b)
			return
		else:
			print("there is't any solution")
			return
		
	discriminant = (b ** 2) - (4 * a * c)
	
	if discriminant > 0:
		print("there is two solutions")
		x1 = (b + math.sqrt((deskriminant))) / (2 * a)
		x2 = (b - math.sqrt((deskriminant))) / (2 * a)
		print(x1)
		print(x2)
	elif discriminant == 0:
		print("there is one solution")
		x = -b / 2 * a
		print("x="+x)
	else:
		print("there is't any solution")

argumentsList = [] 

argumentsList.append( Arguments(0, 0, 0)) 
argumentsList.append( Arguments(1, 4, 2)) 

for argumnets in argumentsList: 
	discriminant(argumnets.a, argumnets.b, argumnets.c)
