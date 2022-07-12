import sys
import pygame as pg
import math

# some constants

SIZE= 720, 720
COLOR_BLACK = 0, 0, 0
COLOR_WHITE = 255, 255, 255
COLOR_GREEN = 0, 255, 0
COLOR_RED = 255, 0, 0
COLOR_BLUE = 0, 0, 255
RADIANS = list()

# converting to a more intuitive coordinate system
def camera(x, y):
	ret = (x + SIZE[0] / 2, y + SIZE[1] / 2)
	#print(ret)
	return ret

# get x
def getX(radius, radians):
	return radius * math.cos(radians)

# get y
def getY(radius, radians):
	return radius * math.sin(radians)

# get circle increments
def inc():
	conv = (math.tau / 2) / 180
	m = 20
	for i in range (18):
		#print(f'{conv} {m}')
		k = m * conv
		#print(k)
		RADIANS.append(k)
		m += 20
inc()
#print(RADIANS)

# graph circle increments at given coords
def drawCircle(surface):
	for i in range(500):
		if (i % 10 == 0):
			for r in RADIANS:
				x = getX(i, r)
				y = getY(i, r)
				c = camera(x, y)
				pg.draw.circle(surface, COLOR_BLUE, c, i % 9)
				print(c)

# multiples of 3
def mofThree(surface):
	for i in range(1, 500001):
		if (i % 3 == 0):
			x = getX(i / 25, i / 25)
			y = getY(i / 25, i / 25)
			c = camera(x, y)
			pg.draw.circle(surface, COLOR_GREEN, c, 1)

# multiples of 7
def mofSeven(surface):
	for i in range(1, 500001):
		if (i % 7 == 0):
			x = getX(i / 25, i / 25)
			y = getY(i / 25, i / 25)
			c = camera(x, y)
			pg.draw.circle(surface, COLOR_RED, c, 1)

# check for prime
def isPrime(n):
	if (n <= 1):
		return False
	for i in range(2, int(math.sqrt(n)) + 1):
		if (n % i == 0):
			return False
	return True

# draw prime pairs
def drawPrimes(surface):
	for i in range(1,500001):
		if (isPrime(i)):
			x = getX(i / 25, i / 25)
			y = getY(i / 25, i / 25)
			c = camera(x, y)
			pg.draw.circle(surface, COLOR_WHITE, c, 1)
			#print(f'{c}    {i}')
	


# x = r cos(a)
# y = r sin(a)
# where r is radius and a is angle in radians

pg.init()
SCREEN = pg.display.set_mode(SIZE)
#pg.draw.circle(SCREEN, COLOR_WHITE, camera(0, 0), 20)

#drawCircle(SCREEN)
drawPrimes(SCREEN)
#mofThree(SCREEN)
#mofSeven(SCREEN)

while 1:	

	for event in pg.event.get():
		if event.type == pg.QUIT: sys.exit()

	pg.display.flip()
