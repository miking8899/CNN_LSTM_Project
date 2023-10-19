##
##      Tkinter Canvas 20231016 上午信義 大安區 3樓
##

import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("Image")
        self.geometry("400x300")
        self.configure(background='#F75C2F')
        self.pets=ImageTk.PhotoImage(self.img)
        canvas=tk.Canvas(self,
                         width=50,
                         height=50
                         )
        canvas.crate_image(24,24,image=self.pets,anchor=tk.CENTER)
        canvas.pack()
        self.pack(expand=1,fill='both')




def main():
    window=Window()
    myFrame=MyFrame(window)
    window.mainloop()
    
if __name__=='__main__':
    main()
    