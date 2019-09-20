
class Dai():
	def __init__(self, canvas, day, i, j, width, height):
		self.touched = False
		self.canvas = canvas
		self.day = day
		self.width = width
		self.height = height
		self.i = i
		self.j = j
		self.title = ""
		self.text = ""
		self.rectangle = self.canvas.create_rectangle(11 + j*self.width, 71 + i*self.height, 11 + j*self.width + self.width, 71 + i*self.height + self.height, fill="#597692")
		self.string = self.canvas.create_text(38+j*width, 95+i*height, fill="#212c36", font="Arial 15", text=day)
		print(day)

	def __repr__(self):
		return str(self.day)