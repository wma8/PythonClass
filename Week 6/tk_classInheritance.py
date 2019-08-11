#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 03:32:49 2018

"""

import Tkinter as tk

class MainScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.pack()
        self.parent = parent

        self.push_count = 0

        self.button = tk.Button(
            self, 
            text = 'Character Window', 
            command = self.new_window,
            height = 10,
            width = 50)
        self.button.pack()

        self.push_counter = tk.Button(
            self, 
            text = 'You need to click me', 
            command = self.push_me,
            height = 10,
            width = 50)
        self.push_counter.pack()

    def new_window(self):
        self.button['state'] = tk.DISABLED
        self.newWindow = tk.Toplevel(self)
        CharWindow(self) #pass the entire self class

    def push_me(self):
        self.push_count += 1
        self.push_counter['text'] = "you pushed me %d times"%self.push_count

class CharWindow(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent.newWindow) 
        self.pack()
        self.parent = parent

        self.push_count = 0

        self.quitButton = tk.Button(
            self, 
            text = 'Quit',
            command = self.close_windows,
            height = 10,
            width = 50)
        self.quitButton.pack()

        self.push_counter = tk.Button(
            self, 
            text = 'You need to click me', 
            command = self.push_me,
            height = 10,
            width = 50)
        self.push_counter.pack()

    def close_windows(self):
        self.parent.button['state'] = tk.NORMAL #so now you have the MainScreen instance available as self.parent
        self.parent.newWindow.destroy()

    def push_me(self):
        self.push_count += 1
        self.push_counter['text'] = "you pushed me %d times"%self.push_count

def main(): 
    root = tk.Tk()
    app = MainScreen(root)
    root.mainloop()

if __name__ == '__main__':
    main()