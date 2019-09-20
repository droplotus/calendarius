
from calen import *
from button import *

root = Tk()
canvas = Canvas(root, width=400, height=600, bg="#6485a4")

calen = Calen(canvas, 380, 300)

button_right = Button(canvas, 367, 38)
button_right.draw()
button_left = Button(canvas, 337, 38)
button_left.draw()

calen.draw_rectangles()
calen.draw_text(calen.get_tabs())

width = 380
height = 300

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


canvas.bind("<Button-1>", callback)
canvas.pack()


root.mainloop()