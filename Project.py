from tkinter import *
def searched():
    frame.pack_forget() 
    clear = Button(window, text=searchbox.get())
    clear.pack()
    #
def searchbutton():
    global window
    global searchbox
    global frame
    frame=Frame(window)
    frame.pack()
    window.title("Torrent Scraper")
    title = Label(frame, text="Welcome to this Program", font=("Arial Bold", 25))
    title.pack(pady=(25,30), side=TOP)
    #
    searchbox = Entry(frame, text="Enter Search Term", width="35")
    searchbox.pack(side=TOP, pady=10)
    #
    search = Button(frame, text="Search", command=searched)
    search.pack(side=RIGHT, padx=0, pady=0)
    #
    clear = Button(frame, text="Clear")
    clear.pack(side=RIGHT, padx=0, pady=0)
    #





global searchbox
global window
window=""
window=Tk()
window.geometry('500x250')
searchbutton()
window.mainloop()