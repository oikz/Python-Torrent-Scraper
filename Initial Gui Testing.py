from tkinter import *
def searched():
    clear = Button(window, text=searchbox.get())
    clear.grid(column=0, row=1)
    clear.place(relx=0.5, rely=0.8, anchor=CENTER)
def searchbutton():
    global window
    global searchbox
    window = Tk()
    window.title("Torrent Scraper")
    title = Label(window, text="Welcome to this Program", font=("Arial Bold", 25))
    title.grid(column=0, row=0)
    title.place(relx=0.5, rely=0.1, anchor=CENTER)
    search = Button(window, text="Search", command=searched)
    search.grid(column=0, row=1)
    search.place(relx=0.4, rely=0.8, anchor=CENTER)
    clear = Button(window, text="Clear")
    clear.grid(column=0, row=1)
    clear.place(relx=0.6, rely=0.8, anchor=CENTER)
    searchbox = Entry(window, text="Enter Search Term", width="10")
    searchbox.grid(column=0, row=0)
    searchbox.place(relx=0.5, rely=0.5, anchor=CENTER)
    window.geometry('500x250')


global searchbox
global window
window=""
searchbutton()
window.mainloop()
