import datasource
import tkinter as tk


def main():
    names = datasource.cityNames()
    city = datasource.cities_info("屏東縣新埤")
    print(city)

    window = tk.Tk()
    window.title("米樂金第一個TKINTER window App")
    window.mainloop()


if __name__ == "__main__":
    main()
