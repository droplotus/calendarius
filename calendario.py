
from calen import *
from button import *

root = Tk()
root.geometry("400x605")
frame = Frame(root, width=400, height=605, bg="#6485a4")
canvas = Canvas(frame, width=400, height=380, bg="#6485a4", highlightthickness=1, highlightbackground="#6485a4")

dreams = []
dais = []
dai = None

# setting up main page with some widgets
calen = Calen(canvas, 380, 300)

button_right = Bbutton(canvas, 367, 28, ">", 20, 15)
button_right.draw()
button_left = Bbutton(canvas, 337, 28, "<", 20, 15)
button_left.draw()

calen.draw_rectangles()
calen.draw_text(calen.get_tabs())
dais = calen.dais

scroll = Scrollbar(frame)

text_area = Text(frame, width=40, height=11, yscrollcommand=scroll.set, background="#9ab4cc", borderwidth=0, relief=SOLID, wrap=WORD)
scroll.config(command=text_area.yview)

def buttonclicked():
	content = text_area.get("1.0", CURRENT)

	if dai is None:
		return

	day = dai.day
	month = calen.month
	year = calen.year
	datee = date(year, month, day)

	datee = datee.strftime("%d/%m/%Y")
	for i in range(len(dreams)-1, -1, -1):
		if dreams[i].data == datee:
			dreams.remove(dreams[i])	

	dreams.append(Dream(datee, content))
	writeFile()

b = Button(frame, text="update", command = buttonclicked, borderwidth=0, bg="#9ab4cc")

# from calendar
width = 380
height = 300

title = ""
text = ""
clicking = [0, 0]
last_dai = None

class Dream():
	def __init__(self, data, content=""):
		self.data = data
		self.content = content

def readFile():
	f = open("dreams.txt","r+")
	while True:
		data = f.readline().splitlines()
		driam = f.readline().splitlines()
		if not data:
			break;
		dreams.append(Dream(data[0], driam[0]))

	for dream in dreams:
		for temp in dais:
			for day in temp:
				if day == 0:
					continue
				if day.data == dream.data:
					day.text = dream.content

def writeFile():
	f = open("dreams.txt","w")
	for dream in dreams:
		f.write(str(dream.data)+"\n")
		f.write(str(dream.content)+"\n")

def callback(event):
	global last_dai
	global dais
	global dai

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
b.pack(pady = 2)

readFile()

root.mainloop()