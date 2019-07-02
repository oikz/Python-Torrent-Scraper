from tkinter import *
def searched():
    menuframe1.pack_forget()
    menuframe2.pack_forget()
    menuframe3.pack_forget()
    searchedframe1=Frame(window)
    searchedframe1.pack()
    title=Label(searchedframe1, text="Results:", font=("Arial Bold", 25))
    title.pack()
    print("thepiratebay")
    print(thepiratebay.get())
    print("1337x")
    print(x1337.get())
    print("rarbg")
    print(rarbg.get())
    print("limetorrents")
    print(limetorrents.get())
    print("katcr")
    print(katcr.get())
    print("torrentdownloads")
    print(torrentdownloads.get())

    try:
        if len(searchbox.get()) <= 3:
            print("Too short")
        else:
            print("Nice")

    except:
        print("Please enter a search term")

def cleartext():
    searchbox.delete(0, END)
    searchbutton()

def searchbutton():
    global window
    global searchbox
    global menuframe1
    global menuframe2
    global menuframe3
    menuframe1=Frame(window)
    menuframe1.pack_forget()
    menuframe1.pack()
    menuframe2=Frame(window)
    menuframe2.pack_forget()
    menuframe2.pack()
    menuframe3=Frame(window)
    menuframe3.pack_forget()
    menuframe3.pack()
    window.title("Torrent Scraper")
    title = Label(menuframe1, text="Welcome to this Program", font=("Arial Bold", 25))
    title.pack(pady=(25,30), side=TOP)
    # A basic label with a title "Welcome to this program" using Arial Bold Font size 25
    # Packs the Label into the menuframe and aligns it TOP with padding above of 25px and padding below of 30
    searchbox = Entry(menuframe1, text="Enter Search Term", width="35")
    searchbox.pack(side=TOP, pady=10)
    # A basic searchbox for the user to enter their search term to be used by the program to search sites
    # Packs the searchbox into the menuframe, aligned TOP and with a padding of 10px above and below
    search = Button(menuframe1, text="Search", command=searched)
    search.pack(side=RIGHT)
    # Adds a search button for the user to execute the search with their chosen options and executes the searched() function
    # Packs button to the right
    clear = Button(menuframe1, text="Clear", command=cleartext)
    clear.pack(side=RIGHT)
    # Adds a Clear button for the user to clear their search preferences   
    checkbox1=Checkbutton(menuframe2, text="ThePirateBay", variable=thepiratebay)
    checkbox1.pack(side=LEFT)
    # Adds a checkbox for the user to select which websites they would like the program to search and saves it as a var
    # Packs it below the title and searchbox aligned left
    checkbox2=Checkbutton(menuframe2, text="1337x", variable=x1337)
    checkbox2.pack(side=LEFT)
    #
    checkbox3=Checkbutton(menuframe2, text="Rarbg", variable=rarbg)
    checkbox3.pack(side=LEFT)
    #
    checkbox4=Checkbutton(menuframe3, text="Lime Torrents", variable=limetorrents)
    checkbox4.pack(side=LEFT)
    #
    checkbox5=Checkbutton(menuframe3, text="Kickass Torrents", variable=katcr)
    checkbox5.pack(side=LEFT)
    #
    checkbox6=Checkbutton(menuframe3, text="Torrent Downloads", variable=torrentdownloads)
    checkbox6.pack(side=LEFT)
    #





global search
global searchbox
global window
global thepiratebay
global x1337
global rarbg
global limetorrents
global katcr
global torrentdownloads
global menuframe1
global menuframe2
global menuframe3



window=""
window=Tk()
window.geometry('650x250')
thepiratebay=IntVar(window)
x1337=IntVar(window)
rarbg=IntVar(window)
limetorrents=IntVar(window)
katcr=IntVar(window)
torrentdownloads=IntVar(window)
searchbutton()
window.mainloop()
