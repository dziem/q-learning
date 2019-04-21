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
min_step = 28 #minimum possible step to reach 15,15 (500)
max_step = min_step * 20
learn = 200 #times
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
#the learn table thing or q-table to be exact
map = [] #map = q-table
for i in range (0, 15):
	new = []
	for j in range (0, 15):
		new2 = []
		for k in range (0, 4):
			if(i == 0 and k == 0): #if top and move north
				foo = -99999 #make the map out of map move disabled and prevent error
			elif(i == 14 and k == 2): #if bottom and move south
				foo = -99999 #make the map out of map move disabled and prevent error
			elif(j == 0 and k == 3): #if left and move west
				foo = -99999 #make the map out of map move disabled and prevent error
			elif(j == 14 and k == 1): #if right and move east
				foo = -99999 #make the map out of map move disabled and prevent error
			else:
				foo = 0 #init zero
			new2.append(foo)
		new.append(new2)
	map.append(new)
#algorithm
i = 0
#target = 0 #try bits ; how many times the episode reach 15,15
while i < learn:
	step = random.randint(min_step,max_step) #how long an episode is
	x_pos = 14 #start x
	y_pos = 0 #start y
	j = 0
	while j < step:
		randomate = random.random()
		if(randomate < learnmate(i)):
			move = movemate(x_pos, y_pos) #explore
			#print('move/random')
		else:
			move = np.argmax(map[x_pos][y_pos]) #exploit
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
		if(x_pos == 0 and y_pos == 14): #target reached ; finish episode
			#target += 1
			break
		j += 1
	i += 1
#testy bits
#print(target)
x_pos = 14 #start x
y_pos = 0 #start y
score = 0
j = 0
#print(map)
#the actual try to get the 15,15
while True:
	score += int(z[x_pos][y_pos])
	move = np.argmax(map[x_pos][y_pos])
	#print(x_pos, y_pos) #trace bits
	if(move == 0):
		x_pos  -= 1
	elif(move == 1):
		y_pos += 1
	elif(move == 2):
		x_pos += 1
	elif(move == 3):
		y_pos -= 1
	if(x_pos == 0 and y_pos == 14): #target reached
		score += int(z[x_pos][y_pos])
		print('target reached')
		break
	j += 1
	#print(move) #trace bits
	#print(score) #trace bits
	if(j > 1000): #to stop the infinite loop thing
		print('timeout')
		break
print('final score : ',score)