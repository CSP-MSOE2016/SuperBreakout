####
# MSOE PLTW CSP Core Training
# 1.5.4 Canvas Template
####

import Tkinter #often people import Tkinter as *
import random
import math
''' Test comment for syncing
'''




#####
# Create root window 
####
root = Tkinter.Tk()

text = Tkinter.Label(root, text='Place off screen buttons here')
text.grid(row=0, column=4)

ref_list = [] # create empty list to reference blocks for collision
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
                 list_of_blocks.remove(block)
                 # for now, make block black
                 canvas.itemconfig(block, fill="black")
                 return True  # there was a collision
    return False

 
def draw_rows(rows):  
    ''' This code draws the blocks across the board
        and then down on the next rows
    '''
    colors = ["red", "blue", "green", "cyan", "magenta", "yellow",
                    "white", "orange"]
    y0 = 5
    y1 = 25
    
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

'''
    
def callback():
    xba1, yba1, xba2, yba2 = canvas.coords(ball)
    canvas.coords(ball,xba1, yba1-10, xba2, yba2-10)
    process_blocks(ref_list,canvas,ball)

b = Tkinter.Button(root, text="OK", command=callback)
b.grid(row=0, column=1)
      
ball = canvas.create_oval(400, 300, 420, 320, outline='#000000', fill='#00FFFF')      
'''

# Create a circle on the canvas to match the initial model
speed_intvar = Tkinter.IntVar()
speed_intvar.set(10) # Initialize y coordinate
# radius and x-coordinate of circle
r = 10
x = 300
y = 400
direction = 1 # radians of angle in standard position, ccw from positive x axis
 
circle_item = canvas.create_oval(x-r, y-r, x+r, y+r, 
                                 outline='#000000', fill='#00FFFF')

def animate():
    # Get the slider data and create x- and y-components of velocity
    velocity_x = speed_intvar.get() * math.cos(direction) # adj = hyp*cos()
    velocity_y = speed_intvar.get() * math.sin(direction) # opp = hyp*sin()
    # Change the canvas item's coordinates
    canvas.move(circle_item, velocity_x, velocity_y)
    global direction
    
    # check for collision with bricks
    if process_blocks(ref_list,canvas,circle_item):
        # there was was a collision
        # If crossing top or bottom of canvas
        direction = -1 * direction # Reverse the y-component of velocity
        

    
    
    
    
    # Get the new coordinates and act accordingly if ball is at an edge
    x1, y1, x2, y2 = canvas.coords(circle_item)
    # If crossing left or right of canvas
    if x2>canvas.winfo_width() or x1<0: 
        direction = math.pi - direction # Reverse the x-component of velocity
    # If crossing top or bottom
    if y2>canvas.winfo_height(): 
        direction = -1 * direction # Reverse the y-component of velocity
    
    # Create an event in 1 msec that will be handled by animate(),
    # causing recursion        
    canvas.after(1, animate)
# Call function directly to start the recursion
animate()

#test
#######
# Event Loop
#######
root.mainloop()
























#######
# Event Loop
#######
root.mainloop()