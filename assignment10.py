import tkinter as tk
import webbrowser

def navigate():
    site = entry.get()
    
    webbrowser.open("https://www.google.com/search?q="+site)
    print(f"Navigating to {site}...")
    


window = tk.Tk(className=" Search")



input = tk.Label(window, text="Enter a website URL:")

input.pack()

entry = tk.Entry(window)
entry.pack()


button = tk.Button(window, text="Seacrh", command=navigate)
button.pack()


window.mainloop()