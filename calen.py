from tkinter import *
from calendar import monthrange
from datetime import date, datetime

class Calen():
	def __init__(self, canvas, x, y):
		self.rectangles = []
		self.canvas = canvas
		self.year = date.today().year
		self.month = date.today().month
		self.days = monthrange(self.year, self.month)[1]
		self.weekday = date(self.year, self.month, 1).weekday()
		self.month_name = datetime.now().strftime('%B')
		self.cols = 7
		self.rows = 1 
		# Counting month rows (weeks)
		for i in range(1, self.days+1):
			if date(self.year, self.month, i).weekday() == 6:
				self.rows += 1

		self.width = int(x/self.cols)
		self.height = int(y/self.rows)

	def get_tabs(self):
		tabs = 0
		for i in range(self.weekday):
			tabs += 1
		return tabs

	def draw_text(self, tabs):
		gap = 1
		self.canvas.create_text(98, 50, fill="black", font="Arial 25 bold", text=self.month_name)
		for i in range(self.rows):
			for j in range(self.cols):
				if tabs>0:
					tabs -= 1
					continue
				if gap == self.days+1:
					break
				self.canvas.create_text(38+j*self.width, 95+i*self.height, fill="black", font="Arial 15", text=gap)
				gap += 1

	def draw_rectangles(self):
		day = 1
		for i in range(self.cols):
			temp = []
			for j in range(self.rows):
				rectangle = self.canvas.create_rectangle(11 + i*self.width, 71 + j*self.height, 11 + i*self.width + self.width, 71 + j*self.height + self.height)
				temp.append(rectangle)
				day += 1
			self.rectangles.append(temp)