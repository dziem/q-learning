import random
import math
import numpy as np
#read file
f = open('DataTugas3ML2019.txt', 'r')
x = f.read().split('\n')
f.close()
z = []
for i in x:
	a = i.split('\t')
	z.append(a)   
#const
learning_rate = 1
discount_rate = 0.9
min_step = 28
max_step = min_step * 20
learn = 100 #times
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
			#change the bit in the table if move into the wall so that the move will just be ignored
	return move
def learnmate(t): #learning rate decreases over time
	return learning_rate * math.exp( -1 * (t / learn) )
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
#make the map out of map move disabled
for i in range (0, 15):
	new = []
	for j in range (0, 15):
		new2 = []
		for k in range (0, 4):
			if(i == 0 and k == 0):
				map[i][j][k] = -99999
			elif(i == 14 and k == 2):
				map[i][j][k] = -99999 
			elif(j == 0 and k == 3):
				map[i][j][k] = -99999 
			elif(j == 14 and k == 1):
				map[i][j][k] = -99999 
#algorithm
i = 0
target = 0
while i < learn:
	step = random.randint(min_step,max_step)
	x_pos = 14
	y_pos = 0
	j = 0
	while j < step:
		randomate = random.random()
		if(randomate < learnmate(i)):
			move = movemate(x_pos, y_pos)
			#print('move/random')
		else:
			move = np.argmax(map[x_pos][y_pos])
			#print('test')
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
		map[x_pos][y_pos][move] = map[x_pos][y_pos][move] + learnmate(i) * (int(z[next_x][next_y]) + (discount_rate * np.max(map[next_x][next_y])) - map[x_pos][y_pos][move])
		x_pos = next_x
		y_pos = next_y
		if(x_pos == 0 and y_pos == 14): #target reached
			target += 1
			break
		j += 1
	i += 1
#testy bits
#print(target)
x_pos = 14
y_pos = 0
score = 0
j = 0
#print(map)

while True:
	score += int(z[x_pos][y_pos])
	move = np.argmax(map[x_pos][y_pos])
	#print(x_pos, y_pos)
	if(move == 0):
		x_pos  -= 1
	elif(move == 1):
		y_pos += 1
	elif(move == 2):
		x_pos += 1
	elif(move == 3):
		y_pos -= 1
	if(x_pos == 0 and y_pos == 14):
		score += int(z[x_pos][y_pos])
		print('target reached')
		break
	j += 1
	#print(move)
	#print(score)
	if(j > 1000):
		print('timeout')
		break
print('final score : ',score)