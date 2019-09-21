
from calen import *
from button import *

root = Tk()
root.geometry("400x600")
frame = Frame(root, width=400, height=600, bg="#6485a4")
canvas = Canvas(frame, width=400, height=400, bg="#6485a4", highlightthickness=1, highlightbackground="#6485a4")

# setting up main page with some widgets
calen = Calen(canvas, 380, 300)

button_right = Button(canvas, 367, 28, ">", 20, 15)
button_right.draw()
button_left = Button(canvas, 337, 28, "<", 20, 15)
button_left.draw()

calen.draw_rectangles()
calen.draw_text(calen.get_tabs())

scroll = Scrollbar(frame)

text_area = Text(frame, width=40, height=11, yscrollcommand=scroll.set)
scroll.config(command=text_area.yview)
text_area.insert(END, "Child widget of the LabelFrame")

# from calendar
width = 380
height = 300

title = ""
text = ""
clicking = [0, 0]
def callback(event):
	clicking[0] = int((event.x-10)/calen.width)
	clicking[1] = int((event.y-70)/calen.height)
	if button_left.clickin((event.x, event.y)):
		calen.previous_month()
		calen.draw_text(calen.get_tabs())
		calen.draw_rectangles()
	if button_right.clickin((event.x, event.y)):
		calen.next_month()
		calen.draw_text(calen.get_tabs())
		calen.draw_rectangles()
	if calen.clickin((event.x, event.y)):
		dai = calen.getDaiByClick((clicking[1], clicking[0]))
		if dai:
			calen.resetDais()
			dai.touched = True
			canvas.itemconfig(dai.rectangle, fill="#43586d")

canvas.bind("<Button-1>", callback)
frame.pack()
frame.pack_propagate(0)
canvas.pack()
scroll.pack(side=RIGHT, fill=Y)
text_area.pack()

root.mainloop()