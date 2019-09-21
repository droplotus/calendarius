
from calen import *
from button import *

root = Tk()
root.geometry("400x600")
frame = Frame(root, width=400, height=600, bg="#6485a4")
canvas = Canvas(frame, width=400, height=400, bg="#6485a4", highlightthickness=1, highlightbackground="#6485a4")

dreams = []
dais = []

# setting up main page with some widgets
calen = Calen(canvas, 380, 300)

button_right = Button(canvas, 367, 28, ">", 20, 15)
button_right.draw()
button_left = Button(canvas, 337, 28, "<", 20, 15)
button_left.draw()

calen.draw_rectangles()
calen.draw_text(calen.get_tabs())
dais = calen.dais

scroll = Scrollbar(frame)

text_area = Text(frame, width=40, height=11, yscrollcommand=scroll.set, background="#9ab4cc", borderwidth=0, relief=SOLID, wrap=WORD)
scroll.config(command=text_area.yview)

# from calendar
width = 380
height = 300

title = ""
text = ""
clicking = [0, 0]
last_dai = None

class Dream():
	def __init__(self, data, title, content):
		self.data = data
		self.title = title
		self.content = content

def readFile():
	f = open("dreams.txt","r+")
	while True:
		data = f.readline().splitlines()
		title = f.readline().splitlines()
		driam = f.readline().splitlines()
		if not data:
			break;
		dreams.append(Dream(data[0], title[0], driam[0]))
	for dream in dreams:
		for temp in dais:
			for day in temp:
				if day == 0:
					continue
				if day.data == dream.data:
					day.title = dream.title
					day.text = dream.content

def callback(event):
	global last_dai
	global dais
	clicking[0] = int((event.x-12)/calen.width)
	clicking[1] = int((event.y-52)/calen.height)
	if button_left.clickin((event.x, event.y)):
		calen.previous_month()
		calen.draw_text(calen.get_tabs())
		calen.draw_rectangles()
		dais = calen.dais
		readFile()
	if button_right.clickin((event.x, event.y)):
		calen.next_month()
		calen.draw_text(calen.get_tabs())
		calen.draw_rectangles()
		dais = calen.dais
		readFile()
	if calen.clickin((event.x, event.y)):
		dai = calen.getDaiByClick((clicking[1], clicking[0]))
		if dai:
			calen.resetDais()
			dai.touched = True
			canvas.itemconfig(dai.rectangle, fill="#43586d")
			if last_dai:
				last_dai.text = text_area.get("1.0",END)
			text_area.delete("1.0", END)
			text_area.insert("1.0", dai.text[:len(dai.text)])
			text_area.delete(CURRENT, END)
			last_dai = dai

	

canvas.bind("<Button-1>", callback)
frame.pack()
frame.pack_propagate(0)
canvas.pack()
scroll.pack(side=RIGHT, fill=Y)
text_area.pack()

readFile()

root.mainloop()