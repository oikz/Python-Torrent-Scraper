from tkinter import *

def restart():

    menuframe1.pack_forget()
    menuframe2.pack_forget()
    menuframe3.pack_forget()
    searchedframe1.pack_forget()
    searchedframe2.pack_forget()
    searchedframe3.pack_forget()
    searchedframe4.pack_forget()
    searchbutton()
def searched():
    global searchedframe1
    global searchedframe2
    global searchedframe3
    global searchedframe4   
    global tooshort 
    global title
    menuframe1.pack_forget()
    menuframe2.pack_forget()
    menuframe3.pack_forget()
    searchedframe1=Frame(window)
    searchedframe1.pack()
    searchedframe2=Frame(window)
    searchedframe2.pack()
    searchedframe3=Frame(window)
    searchedframe3.pack()
    searchedframe4=Frame(window)
    searchedframe4.pack()
    if searchbox.get()=="Must be longer than 3 characters" or tooshort==True:
        searchbutton()
    else:
        print("")
    if thepiratebay.get() == 1 or x1337.get() == 1 or rarbg.get() == 1 or limetorrents.get() == 1 or katcr.get() == 1 or torrentdownloads.get() == 1:
        print("continuing")
    else:
        title=Label(searchedframe1, text="Please select at least one website")
    title=Label(searchedframe1, text="Results for: " + searchbox.get(), font=("Arial Bold", 25))
    if thepiratebay.get():
        piratebaylabel=Label(searchedframe2, text="ThePirateBay.org")
        piratebaylabel.pack(side=LEFT)
    else:
        print("")
    if x1337.get():
        x1337label=Label(searchedframe2, text="1337x.to")
        x1337label.pack(side=LEFT)
    else:
        print("")
    if rarbg.get():
        rarbglabel=Label(searchedframe2, text="rarbg.to")
        rarbglabel.pack(side=LEFT)
    else:
        print("")
    if limetorrents.get():
        limetorrentslabel=Label(searchedframe2, text="LimeTorrents")
        limetorrentslabel.pack(side=LEFT)
    else:
        print("")
    if katcr.get():
        katcrlabel=Label(searchedframe2, text="Kickass Torrents")
        katcrlabel.pack(side=LEFT)
    else:
        print("")
    if torrentdownloads.get():
        torrentdownloadslabel=Label(searchedframe2, text="Torrent Downloads")
        torrentdownloadslabel.pack(side=LEFT)
    title.pack()

    tryagainbutton=Button(searchedframe4, text="New Search", command=restart)
    tryagainbutton.pack(side=RIGHT)

    #original output testing for checkboxes    
    #print("thepiratebay")
    #print(thepiratebay.get())
    #print("1337x")
    #print(x1337.get())
    #print("rarbg")
    #print(rarbg.get())
    #print("limetorrents")
    #print(limetorrents.get())
    #print("katcr")
    #print(katcr.get())
    #print("torrentdownloads")
    #print(torrentdownloads.get())

    try:
        if len(searchbox.get()) <= 3 or searchbox.get()=="Must be longer than 3 characters":
            #Sends the user back to the search page if their search term is smaller than 3 characters
            searchedframe1.pack_forget()
            searchedframe2.pack_forget()
            menuframe1.destroy()
            menuframe2.destroy()
            menuframe3.destroy()
            tooshort=True
            searchbutton()
            #clears everything and sets the variable "tooshort" to true for future use
        else:
            print("Nice")
            tootshort=False

    except:
        print("Please enter a search term")

def cleartext():
    searchbox.delete(0, END)
    #Clears the searchbox so the user can try again
    menuframe1.pack_forget()
    #Clears the menuframes so they can be remade 
    menuframe2.pack_forget()
    menuframe3.pack_forget()
    searchbutton()

def searchboxfocused(event):
#Function is called when the searchbox is clicked on
    if searchbox.get() == 'Must be longer than 3 characters':
       searchbox.delete(0, "end") # delete all the text in the entry
       searchbox.insert(0, '') #Insert blank for user input
       searchbox.config(fg = 'black')

def searchbutton():
    global tooshort
    global window
    global title
    global searchbox
    global menuframe1
    global menuframe2
    global menuframe3
    menuframe1=Frame(window)
    #Creates menuframe1 in the wndow element
    menuframe1.pack()
    #Packs the menuframe1 into the window created
    menuframe2=Frame(window)
    menuframe2.pack()
    menuframe3=Frame(window)
    menuframe3.pack()
    window.title("Torrent Scraper")
    #Gives the window a title
    title = Label(menuframe1, text="Welcome to this Program", font=("Arial Bold", 25))
    title.pack(pady=(25,30), side=TOP)
    # A basic label with a title "Welcome to this program" using Arial Bold Font size 25
    # Packs the Label into the menuframe and aligns it TOP with padding above of 25px and padding below of 30
    if tooshort:
        #title.destroy()
        title2=Label(menuframe1, text="Your search must be longer than 3 characters", font=("Arial Bold", 20))
        title2.pack(side=TOP)
        tooshort=False
    else:
        print("")
    searchbox = Entry(menuframe1, text="Enter Search Term", width="35")
    searchbox.pack(side=TOP, pady=10)
    # A basic searchbox for the user to enter their search term to be used by the program to search sites
    # Packs the searchbox into the menuframe, aligned TOP and with a padding of 10px above and below
    searchbox.delete(0, END)
    searchbox.insert(0, 'Must be longer than 3 characters')
    searchbox.config(fg = 'grey')
    #Adds a background text to the box to tell the user that the search must be longer than 3 characters
    searchbox.bind('<FocusIn>', searchboxfocused)
    #Enables the searchbox to show "must be longer than 3 characters" until the user clicks it, then it disappears
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




#Declare Global Variables
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
global tooshort


tooshort=False
window=""
window=Tk()
window.geometry('650x250')
#Set window size to 650x250 pixels
thepiratebay=IntVar(window)
x1337=IntVar(window)
rarbg=IntVar(window)
limetorrents=IntVar(window)
katcr=IntVar(window)
torrentdownloads=IntVar(window)
#Declare future variables used in widgets
searchbutton()
#Calls first function
window.mainloop()
#Starts the window loop to keep it open
