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
canvas.create_rectangle(5,5,100,25, fill="red")

#######
# Event Loop
#######
root.mainloop()