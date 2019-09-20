
class Button():
	def __init__(self, canvas, x, y):
		self.x = x
		self.y = y
		self.canvas = canvas
		self.rectangle = None
		self.width = 20
		self.height = 25

	def draw(self):
		self.rectangle = self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill="#4e6780", outline="#43586d")

	def clickin(self, p):
		if p[0] > self.x and p[0] < self.x + self.width:
			if p[1] > self.y and p[1] < self.y + self.height:
				return True
		return False