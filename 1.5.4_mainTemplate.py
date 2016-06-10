####
# MSOE PLTW CSP Core Training
# 1.5.4 Canvas Template
####

import Tkinter #often people import Tkinter as *
import random
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
<<<<<<< HEAD
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
=======

 
def draw_rows(rows):  
    ''' This code draws the blocks across the board
        and then down on the next rows
    '''
    colors = ["red", "blue", "green", "cyan", "magenta", "yellow",
                    "white", "orange"]
    y0 = 5
    y1 = 25
    ref_list = [] # create empty list to reference blocks for collision
    for row in range(rows):
        color = random.choice(colors)
        counter = 0
        x0 = 3
        x1 = 80
        while counter < 10:
            color = random.choice(colors)
            ref_list.append(canvas.create_rectangle(x0,y0,x1,y1, fill=color))
            x0 += 80
            x1 += 80
            counter += 1 
        y0 += 25
        y1 += 25
    print ref_list
            
draw_rows(6)    
    
'''def draw_all():
     This code will call to the draw_code() 
        function and draw a few rows of blocks
        allowing for the program to draw a full board
    
    count = 0
    y0 = 3
    y1 = 25
    while count < 4:
        draw_row()
        y0 += 25
        y1 += 25
'''
       
        

>>>>>>> origin/blocks

#######
# Event Loop
#######
root.mainloop()