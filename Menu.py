from tkinter import *
import os

def openAnotherWindow():
    os.system("python Game.py")

root = Tk()

bg=PhotoImage(file="castle.png")
# Create Canvas 
canvas1 = Canvas( root, width = 512, 
                 height = 512) 
  
canvas1.pack(fill = "both", expand = True) 
  
# Display image 
canvas1.create_image( 0, 0, image = bg,  
                     anchor = "nw") 
  
# Add Text
text=canvas1.create_text( 250, 150, text = "Generic Text Based RPG",fill="dark red", font=("Times", 30))

bbox=canvas1.bbox(text)
canvas1.create_rectangle(bbox, outline="black")

button1 = Button( root, text = "Start", command=openAnotherWindow) 
button1_canvas = canvas1.create_window( 238,250,  
                                       anchor = "nw", 
                                       window = button1) 

root.mainloop()