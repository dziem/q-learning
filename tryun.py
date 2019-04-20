import random
#read file
f = open('DataTugas3ML2019.txt', 'r')
x = f.read().split('\n')
f.close()
z = []
for i in x:
	a = i.split('\t')
	z.append(a)   
#const
learning_rate = 0.0025
discount_rate = 0.075
min_step = 28
max_step = min_step * 50
learn = 7 #times
#function
def movemate(x_pos, y_pos):
	while True: #generate move and check if hit a wall, if hit a wall, generate new move
		move = random.randint(0, 3) #0 north, 1 east, 2 south, 3 west
		if(move == 0 and x_pos != 0):
			break
		elif(move == 1 and y_pos != 14):
			break
		elif(move == 2 and x_pos != 14):
			break
		elif(move == 3 and y_pos != 0):
			break
		else:
			map[x_pos][y_pos][move] = -99999 
			#change the bit in the table if move into the wall so that the move will just be ignored
	return move
def testmove(x, y):
	max_index = random.randint(0,3)
	max = map[x][y][max_index]
	for i in range (0, 4):
		if(map[x][y][i] > max):
			max = map[x][y][i]
			max_index = i
	return max_index
def maxi(x, y):
	max = map[x][y][0]
	for i in range (0, 4):
		if(map[x][y][i] > max):
			max = map[x][y][i]
	return max
#the learn table thing 
map = [] 
for i in range (0, 15):
	new = []
	for j in range (0, 15):
		new2 = []
		for k in range (0, 4):
			foo = 0
			new2.append(foo)
		new.append(new2)
	map.append(new)
#algorithm
i = 0
target = 0
while i < learn:
	step = random.randint(min_step,max_step)
	x_pos = 14
	y_pos = 0
	j = 0
	while j < step:
		move = movemate(x_pos, y_pos)
		if(move == 0):
			next_x = x_pos - 1
			next_y = y_pos
		elif(move == 1):
			next_x = x_pos
			next_y = y_pos + 1
		elif(move == 2):
			next_x = x_pos + 1
			next_y = y_pos
		elif(move == 3):
			next_x = x_pos
			next_y = y_pos - 1
		map[x_pos][y_pos][move] = map[x_pos][y_pos][move] + learning_rate * (int(z[x_pos][y_pos]) + (discount_rate * maxi(next_x, next_y)) - map[x_pos][y_pos][move])
		x_pos = next_x
		y_pos = next_y
		if(x_pos == 0 and y_pos == 14): #target reached
			target += 1
			break
		j += 1
	i += 1
#testy bits
print(target)
x_pos = 14
y_pos = 0
score = 0
j = 0
while True:
	score += int(z[x_pos][y_pos])
	move = testmove(x_pos, y_pos)
	#print(move)
	if(move == 0):
		x_pos  -= 1
	elif(move == 1):
		y_pos += 1
	elif(move == 2):
		x_pos += 1
	elif(move == 3):
		y_pos -= 1
	if(x_pos == 0 and y_pos == 14):
		print('target reached')
		break
	j += 1
	if(j > 1000):
		print('timeout')
		break
print(score)