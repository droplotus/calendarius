from tkinter import *
from calendar import monthrange
from datetime import date, datetime, timedelta
from day import *
import time

class Calen():
	def __init__(self, canvas, x, y):
		self.rectangles = []
		self.dais = []
		self.canvas = canvas
		self.year = date.today().year
		self.month = date.today().month
		self.days = monthrange(self.year, self.month)[1]
		self.weekday = date(self.year, self.month, 1).weekday()
		self.month_name = datetime.now().strftime('%B')
		self.text_month = ""
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
				self.canvas.delete(dai.string)
				self.canvas.delete(dai.rectangle)
		self.canvas.delete(self.text_month)

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
		self.text_month = self.canvas.create_text(10, 50, fill="#161d24", font="Arial 25 bold", anchor="w", text=self.month_name)
		
		for i in range(self.rows):
			temp = []
			for j in range(self.cols):
				if tabs>0:
					tabs -= 1
					continue
				if gap == self.days+1:
					break
				temp.append(Dai(self.canvas, gap, i, j, self.width, self.height))
				gap += 1
			self.dais.append(temp)

		print(len(self.dais))

	def draw_rectangles(self):
		day = 1
		for i in range(self.cols):
			temp = []
			for j in range(self.rows):
				rectangle = self.canvas.create_rectangle(11 + i*self.width, 71 + j*self.height, 11 + i*self.width + self.width, 71 + j*self.height + self.height, outline="#212c36")
				temp.append(rectangle)
				day += 1
			self.rectangles.append(temp)