
class Button():
	def __init__(self, canvas, x, y, text, width, height):
		self.x = x
		self.y = y
		self.canvas = canvas
		self.rectangle = None
		self.text = text
		self.width = width
		self.height = height

	def draw(self):
		self.rectangle = self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill="#4e6780", outline="#43586d")
		self.text = self.canvas.create_text(self.x + 10, self.y + 7, text=self.text, fill="#212c36")

	def clickin(self, p):
		if p[0] > self.x and p[0] < self.x + self.width:
			if p[1] > self.y and p[1] < self.y + self.height:
				return True
		return False