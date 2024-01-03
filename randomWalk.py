import random
def random_walk(n):
	""" Return coordinates after 'n' block random walk."""
	x = 0; y = 0
	for i in range(n):
		step = random.choice(['N', 'S', 'E', 'W'])
		if step == 'N':
			y += 1
		elif step == 'S':
			y -= 1
		elif step == 'E':
			x += 1
		else:
			x -= 1
	return (x,y)

def walk(n,s=10):
	dist = []
	for i in range(n):
		walk = random_walk(s)
		dist.append(abs(walk[0]) + abs(walk[1]))
	return sum(dist)/n
	#print("Average Distance = ", sum(dist)/n)


def walkTest(n,s):
	res = []
	for i in range(n):
		res.append(walk(1000,s))
	return (sum(res)/n)




def test():
	res = []
	for i in range(4,31):
		w = walkTest(100,i)
		#print(w)
		if w <= 4:
			res.append((w,i))
	#return res
	maxList = []
	for i in range(len(res)):
		maxList.append(res[i][1])
	return max(maxList)

#print(test())
print(walkTest(100,12))





