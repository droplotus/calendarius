from tkinter import *
from calendar import monthrange
from datetime import date, datetime, timedelta
from day import *
import time

class Calen():
	def __init__(self, canvas, x, y):
		self.x = x
		self.y = y
		self.rectangles = []
		self.dais = []
		self.canvas = canvas
		self.year = date.today().year
		self.month = date.today().month
		self.days = monthrange(self.year, self.month)[1]
		self.weekday = date(self.year, self.month, 1).weekday()
		self.month_name = datetime.now().strftime('%B')
		self.text_month = ""
		self.text_year = ""
		self.cols = 7
		self.rows = 1 
		# Counting month rows (weeks)
		for i in range(1, self.days+1):
			if date(self.year, self.month, i).weekday() == 6:
				self.rows += 1

		self.width = int(x/self.cols)
		self.height = int(y/self.rows)

	def delete_widgets(self):
		for rect in self.rectangles:
			self.canvas.delete(rect)
		for temp in self.dais:
			for dai in temp:
				if dai == 0:
					continue
				self.canvas.delete(dai.string)
				self.canvas.delete(dai.rectangle)
		self.canvas.delete(self.text_month)
		self.canvas.delete(self.text_year)

	def previous_month(self):
		self.delete_widgets()
		today = date(self.year, self.month, self.days)
		first = today.replace(day=1)
		lastMonth = first - timedelta(days=1)
		self.year = int(lastMonth.strftime("%Y"))
		self.month = int(lastMonth.strftime("%m"))
		self.days = int(lastMonth.strftime("%d"))
		self.weekday = date(self.year, self.month, 1).weekday()
		self.month_name = date(self.year, self.month, 1).strftime('%B')
		self.rows = 1 
		# Counting month rows (weeks)
		for i in range(1, self.days+1):
			if date(self.year, self.month, i).weekday() == 6:
				self.rows += 1

	def next_month(self):
		self.delete_widgets()
		today = date(self.year, self.month, self.days)
		lastMonth = today + timedelta(days=1)
		self.year = int(lastMonth.strftime("%Y"))
		self.month = int(lastMonth.strftime("%m"))
		self.days = monthrange(self.year, self.month)[1]
		self.weekday = date(self.year, self.month, 1).weekday()
		self.month_name = date(self.year, self.month, 1).strftime('%B')
		self.rows = 1 
		# Counting month rows (weeks)
		for i in range(1, self.days+1):
			if date(self.year, self.month, i).weekday() == 6:
				self.rows += 1

	def get_tabs(self):
		tabs = 0
		for i in range(self.weekday):
			tabs += 1
		return tabs

	def draw_text(self, tabs):
		gap = 1
		self.dais = []
		temp = []
		self.text_month = self.canvas.create_text(10, 30, fill="#161d24", font="Arial 25 bold", anchor="w", text=self.month_name)
		self.text_year = self.canvas.create_text(250, 35, fill="#161d24", font="Arial 15 bold", anchor="w", text=self.year)
		for i in range(self.rows):
			temp = []
			for j in range(self.cols):
				if tabs>0:
					tabs -= 1
					temp.append(0)
					continue
				if gap == self.days+1:
					break
				temp.append(Dai(self.canvas, gap, i, j, self.width, self.height, date(self.year, self.month, gap).strftime("%d/%m/%Y")))
				gap += 1
			self.dais.append(temp)

	def draw_rectangles(self):
		day = 1
		for i in range(self.cols):
			temp = []
			for j in range(self.rows):
				rectangle = self.canvas.create_rectangle(11 + i*self.width, 51 + j*self.height, 11 + i*self.width + self.width, 51 + j*self.height + self.height, outline="#212c36")
				temp.append(rectangle)
				day += 1
			self.rectangles.append(temp)

	def clickin(self, p):
		if p[0] > 11 and p[0] < 10 + self.x:
			if p[1] > 51 and p[1] < 51 + self.y:
				return True
		return False
	
	def getDaiByClick(self, p):
		try:
			if isinstance(self.dais[p[0]][p[1]], Dai):
				return self.dais[p[0]][p[1]]
		except IndexError:
			return None

	def resetDais(self):
		for temp in self.dais:
			for dai in temp:
				if dai == 0:
					continue
				if dai.touched == True:
					dai.touched = False
					self.canvas.itemconfig(dai.rectangle, fill="#597692")
