import Tkinter as Tk # for python 2
# import tkinter as Tk # for python 3
root = Tk.Tk()
w = Tk.Canvas(root,
              height = 500,
              width = 500)
w.pack()
w.create_rectangle(100,
                    100,
                    120,
                    150,
            fill = 'red')
            
def callback(event):
    print "hello world!"
    
def callback2(event):
    w.create_rectangle(event.x,
                    event.y,
                    event.x+20,
                    event.y+20,
            fill = 'red')
            
w.bind("<Button-1>",callback2)    
# w.bind("<Button-1>",callback)

root.mainloop()