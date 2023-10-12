import datasource
import tkinter as tk
from tkinter import ttk


class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("台灣郷鎮人口統計")
        self.config(background="#E16B8C")

        topframe = tk.Frame(self, background="#B54434")
        label = ttk.Label(topframe, text="台灣郷鎮人口統計", font=('helvetrica', '30'))
        label.pack(padx=100, pady=100)
        topframe.pack()

        bottomFrame = tk.Frame(self, background="#B9887D")
        choices = datasource.cityNames()
        choicevar = tk.StringVar(value=choices)
        listbox = tk.Listbox(bottomFrame, listvariable=choicevar)
        listbox.pack()
        bottomFrame.pack(expand=True, fill='x')


def main():
    window = Window()
    # window.title("米樂金第一個TKINTER window App")
    window.mainloop()


if __name__ == "__main__":
    main()
