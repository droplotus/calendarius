
from calen import *

root = Tk()
canvas = Canvas(root, width=400, height=600, bg="#126077")

calen = Calen(canvas, 380, 300)

calen.draw_rectangles()
calen.draw_text(calen.get_tabs())

width = 380
height = 300

clicking = [0, 0]
def callback(event):
	clicking[0] = int((event.x-10)/calen.width)
	clicking[1] = int((event.y-70)/calen.height)
	print(clicking)

canvas.bind("<Button-1>", callback)
canvas.pack()


root.mainloop()