from graphics import *
from time import sleep
import random

STOCK_price = 130
STOCK_amount = 0
MONEY = 400
stateDown = False # to switch between screens
stateUp = True # same
stateUpper = False # same
start = 50 # starting point for graphs
Up = False # to make graphs only go up
Down = False # same but down
Buy_Amount = 1
step = 5 # how much to add or substract of Buy_Amount
stepDelta = 1 # manage 'step'
buy_point = Point(0, 0) # point where circles appear when purchasing or selling


def main(): # func to create every object
	win = GraphWin('My window', 1200, 700)
	key = win.checkKey()

	rec1 = Rectangle(Point(50, 50), Point(1150, 450))
	rec1.setFill(color_rgb(38, 50, 56))
	circ1 = Circle(Point(50, 450 - STOCK_price*4), 5)

	txt1 = Text(Point(600, 26), 'Press S to start')
	txt2 = Text(Point(300, 26), 'B to buy')
	txt3 = Text(Point(900, 26), 'S to sell')
	txt4 = Text(Point(845, 530), 'Use arrow keys to navigate')
	txt4 = Text(Point(845, 530), f'{step}p.p, +{stepDelta}') #p.p - per press
	txtStockPrice = Text(Point(360, 485), f'Stocks price: {STOCK_price}')
	txtStockPrice.setSize(15)
	txtYourStocks = Text(Point(360, 510), f'Your stocks: {STOCK_amount}')
	txtYourStocks.setSize(15)
	val = STOCK_amount * STOCK_price
	txtYourStocksValue = Text(Point(360, 535), f'Your stocks value: ${STOCK_amount}')
	txtYourStocksValue.setSize(15)
	txtYourMoney = Text(Point(840, 485), f'Money: ${MONEY}')
	txtYourMoney.setSize(15)
	txtBuyAmount = Text(Point(845, 510), f'You wull buy {Buy_Amount} stocks')
	txtBuyAmount.setSize(15)

	for i in range(0, 101, 10): #making price wall on the left side
			y_axis = Text(Point(35, 450-i*4), str(100+i))
			y_axis.setFace('Segoe UI')
			y_axis.draw(win)

	def UI(): #to draw everything needed for the first time
		circ1.draw(win)
		rec1.draw(win)
		txt1.draw(win)
		txt2.draw(win)
		txt3.draw(win)
		txt4.draw(win)
		txtStockPrice.draw(win)
		txtYourStocks.draw(win)
		txtYourMoney.draw(win)
		txtYourStocksValue.draw(win)
		txtBuyAmount.draw(win)

	def redraw(state): # to update rectangle with graphs
		whitebox = Rectangle(Point(0, 458), Point(49, 43))
		whitebox.setFill(color_rgb(240, 240, 240))
		whitebox.setOutline(color_rgb(240, 240, 240))
		if state == 'down': # the lower screen (0=100)
			whitebox.draw(win)
			for i in range(0, 101, 10):
				y_axis = Text(Point(35, 450-i*4), str(i))
				y_axis.setFace('Segoe UI')
				y_axis.draw(win)
		if state == 'upper': # upper screen (200=300)
			whitebox.draw(win)
			for i in range(0, 101, 10):
				y_axis = Text(Point(35, 450-i*4), str(200+i))
				y_axis.setFace('Segoe UI')
				y_axis.draw(win)
		if state == 'up': # starting screen (100-200)
			whitebox.draw(win)
			for i in range(0, 101, 10):
				y_axis = Text(Point(35, 450-i*4), str(100+i))
				y_axis.setFace('Segoe UI')
				y_axis.draw(win)
		if state == 'y': # to reset graphs' position
			rec2 = Rectangle(Point(50, 50), Point(1150, 450))
			rec2.setFill(color_rgb(38, 50, 56))
			rec2.draw(win)


	def screenUpdate(): #updates every value and the graphs
		global STOCK_price
		global stateUp
		global stateDown
		global start
		global Up
		global Down
		global STOCK_amount
		global buy_point
		global stateUpper

		delta = round(random.uniform(-5, 5), 2) # the difference in cost between old and new price of a stock
		if Up == True: # for tests. Price will only go up
			delta = round(random.uniform(0, 5), 2)
		elif Down == True: # for tests. Price will only go down
			delta = round(random.uniform(-5, 0), 2)
		old_price = STOCK_price # for the first point in graph line
		STOCK_price += delta

		if STOCK_price >= old_price: # to calculate margin
			margin = (STOCK_price/old_price) * 100 - 100
		if STOCK_price <= old_price:
			margin = (100 - ((STOCK_price/old_price) * 100)) * -1


		##### UPDATE TXTS #####
		txtStockPrice.setText(f'Stocks price: {round(STOCK_price, 2)}, ({round(margin, 2)}%)')
		txtYourStocks.setText(f'Your stocks: {STOCK_amount}')
		txtYourMoney.setText(f'Money: ${round(MONEY, 2)}')
		val = round(STOCK_price, 2) * STOCK_amount
		txtYourStocksValue.setText(f'Your stocks value: {round(val, 2)}')

		##### UPDATE GRAPHS #####
		gap = 4
		const = 4
		rold_price = old_price
		rSTOCK_price = STOCK_price
		rold_price -= 100 # it is to make graphs work. They operate between -100 and 100 values
		rSTOCK_price -= 100 # same 

		if STOCK_price >= 100 and STOCK_price <= 200:
			if stateUp == False:
				start = 50
				redraw('y')
			point1 = Point(start, 450 - rold_price*const)
			point2 = Point(start+gap, 450 - rSTOCK_price*const)

		if STOCK_price >= 200:
			if stateUpper == False:
				start = 50
				redraw('y')
			rold_price -= 100
			rSTOCK_price -= 100
			point1 = Point(start, 450 - rold_price*const)
			point2 = Point(start+gap, 450 - rSTOCK_price*const)

		if STOCK_price < 100:
			if stateDown == False:
				start = 50
				redraw('y')
			point2 = Point(start, 50 - rold_price*const)
			point1 = Point(start+gap, 50 - rSTOCK_price*const)
		graph = Line(point1, point2)
		graph.setFill('white')
		graph.draw(win)
		buy_point = point2
		start += gap

		if start >= 1150:
			start = 50
			redraw('y')

		########################

		##### UPDATE y_axis #####
		if STOCK_price < 100 and stateDown == False: # switch between screens (0-100)
			stateDown = True
			stateUp = False
			stateUpper = False
			redraw('down')

		if STOCK_price > 100 and STOCK_price < 200 and stateUp == False: # switch between screens (100-200)
			stateDown = False
			stateUp = True
			stateUpper = False
			redraw('up')

		if STOCK_price >= 200 and stateUpper == False: # switch between screens (200-300)
			stateDown = False
			stateUp = False
			stateUpper = True
			redraw('upper')

		#########################

	def buySell(par): # to sell or buy stonks
		global Buy_Amount
		global STOCK_price
		global MONEY
		global STOCK_amount

		if par == 'b':
			if MONEY - Buy_Amount * STOCK_price >= 0:
				STOCK_amount += Buy_Amount
				MONEY -= Buy_Amount * STOCK_price
				circbuy = Circle(buy_point, 3)
				circbuy.setFill('yellow')
				circbuy.draw(win)
		if par == 's':
			if STOCK_amount - Buy_Amount >= 0:
				STOCK_amount -= Buy_Amount
				MONEY += Buy_Amount * STOCK_price
				print(buy_point)
				circbuy = Circle(buy_point, 3)
				circbuy.setFill(color_rgb(0, 255, 0))
				circbuy.draw(win)
	def collapse():
		rect2 = Rectangle(Point(0, 0), Point(1200, 700))
		rect2.setFill(color_rgb(240, 240, 240))
		rect2.draw(win)

		rect = Rectangle(Point(50, 50), Point(1150, 450))
		rect.setFill(color_rgb(38, 50, 56))
		rect.draw(win)

		for i in range(0, 101, 10):
			y_axis = Text(Point(35, 450-i*4), str(100+i))
			y_axis.setFace('Segoe UI')
			y_axis.draw(win)

		txt = Text(Point(625, 275), 'Stonks Exchange collapsed. Restart the application to continue')
		txt.setFace('roboto')
		txt.setSize(20)
		txt.setFill('red')
		txt.draw(win)

		start()
		
	def update(): #to cath if any key is pressed
		while True:
			global Up
			global Down
			global step
			global stepDelta
			global Buy_Amount
			global STOCK_price
			key = win.checkKey()

			###### DEV KEYS ######
			if key == 'm':
				check = win.getMouse()
				print(f'Clickpoint added on {check}')
			if key == 'k':
				check = win.getKey()
				print(f'Last key is {check}')
			if key == 'space': # to debug and make graphs act naturally
				Down = False
				Up = False
				print('space')
			if key == '6': # works with numpad
				Down = False
				Up = True
			if key == '3': # works with numpad
				Up = False
				Down = True
			###### DEV KEYS ######

			if key == 'b':
				buySell('b')
			if key == 's':
				buySell('s')
			if key == '1':
				buySell('b')
			if key == '2':
				buySell('s')
			if key == 'Up':
				Buy_Amount += step
				txtBuyAmount.setText(f'You wull buy {Buy_Amount} stocks')
			if key == 'Down':
				if Buy_Amount - step >= 0:
					Buy_Amount -= step
					txtBuyAmount.setText(f'You wull buy {Buy_Amount} stocks')
			if key == 'Left':
				if step - stepDelta >= 0:
					step -= stepDelta
					txt4.setText(f'{step}p.p')
			if key == 'Right':
				step += stepDelta
				txt4.setText(f'{step}p.p')


			if STOCK_price < -10:
				collapse()
				break
			elif STOCK_price > 310:
				collapse()
				break

			screenUpdate()
			sleep(0.1)
			if key == 'Escape':
				break

	def start():
		while True:
			key = win.checkKey()
			if key == 's':
				txt1.setText('Press ESC to exit')
				update()
				break
			if key == 'Escape':
				break
	UI()
	start()
	#update()
	win.close()

main()