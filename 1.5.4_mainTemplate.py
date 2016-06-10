####
# MSOE PLTW CSP Core Training
# 1.5.4 Canvas Template
####

import Tkinter #often people import Tkinter as *
''' Test comment for syncing
'''




#####
# Create root window 
####
root = Tkinter.Tk()

text = Tkinter.Label(root, text='Place off screen buttons here')
text.grid(row=0, column=4)

# comkment

######
# Create View
#######
# Create and place a canvas
canvas = Tkinter.Canvas(root, width=800, height=600, background='#AAAAAA')
canvas.grid(row=2, rowspan=2, column=4)


#####

text = Tkinter.Label(root, text='Place off screen buttons here')
text.grid(row=0, column=4)

######
# Create brick(s)
######
'''counter = 0
while counter < 5:
'''
blocks = [] #empty list    
blocks.append(canvas.create_rectangle(5,5,100,25, fill="red"))

def process_blocks(list_of_blocks,canvas,ball):
    
    for block in list_of_blocks:
        xbl1, ybl1, xbl2, ybl2 = canvas.coords(block)
        xba1, yba1, xba2, yba2 = canvas.coords(ball)
        # check for collision - that is, if ball's min y <= blocks's
        # max y (since we are upsidedown), and ball's mid x is with block's
        # x range
        if min(yba1, yba2) <= max(ybl1,ybl2):
            if (xba1 + xba2)/2 >= min(xbl1,xbl2) and (xba1 + xba2)/2 <= max(xbl1,xbl2):
                 # collision!!!
                 
                 # for now, make block black
                 canvas.itemconfig(block, fill="black")
                 return True  # there was a collision
    return False

#######
# Event Loop
#######
root.mainloop()