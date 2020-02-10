import math  

class Arguments:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c


def diskremenant(a, b, c):
	
	if a == 0:
		if b != 0:
			print(c/b)
			return
		else:
			print("lucum goytuyun chuni")
			return
		
	deskriminant = (b ** 2) - (4 * a * c)
	
	if deskriminant > 0:
		print("uni erku lucum")
		x1 = (b + math.sqrt((deskriminant))) / (2 * a)
		x2 = (b - math.sqrt((deskriminant))) / (2 * a)
		print(x1)
		print(x2)
	elif deskriminant == 0:
		print("uni mek lucum")
		x = -b / 2 * a
		print("x="+x)
	else:
		print("lucum goytuyun chuni")

argumentsList = [] 

argumentsList.append( Arguments(0, 0, 0)) 
argumentsList.append( Arguments(1, 4, 2)) 

for argumnets in argumentsList: 
	diskremenant(argumnets.a, argumnets.b, argumnets.c)
