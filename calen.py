from tkinter import *
from calendar import monthrange
from datetime import date, datetime, timedelta
import time

class Calen():
	def __init__(self, canvas, x, y):
		self.rectangles = []
		self.text = []
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

	def delete_widgets(self):
		for rect in self.rectangles:
			self.canvas.delete(rect)
		for txt in self.text:
			self.canvas.delete(txt)

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

		print (first, lastMonth)

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
		text_month = self.canvas.create_text(98, 50, fill="#161d24", font="Arial 25 bold", text=self.month_name)
		self.text.append(text_month)
		for i in range(self.rows):
			for j in range(self.cols):
				if tabs>0:
					tabs -= 1
					continue
				if gap == self.days+1:
					break
				new_text = self.canvas.create_text(38+j*self.width, 95+i*self.height, fill="#212c36", font="Arial 15", text=gap)
				self.text.append(new_text)
				gap += 1

	def draw_rectangles(self):
		day = 1
		for i in range(self.cols):
			temp = []
			for j in range(self.rows):
				rectangle = self.canvas.create_rectangle(11 + i*self.width, 71 + j*self.height, 11 + i*self.width + self.width, 71 + j*self.height + self.height, outline="#212c36")
				temp.append(rectangle)
				day += 1
			self.rectangles.append(temp)