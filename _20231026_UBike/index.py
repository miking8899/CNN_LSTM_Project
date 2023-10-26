import tkinter as tk 
from tkinter import ttk 


class Window(tk.Tk):
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    pass


def main():
    window=Window()
    window.title("台北市 YOUBIKE")
    
    pass


if __name__=='main':
    main()
    