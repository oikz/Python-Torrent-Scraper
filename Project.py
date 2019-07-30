from tkinter import *
from bs4 import BeautifulSoup
import requests

def scraper():
    top5titles=[]
    top5urls=[]
    top5seeders=[]
    if thepiratebay.get():
        global searchterm
        piratebayurl="https://thepiratebay.org/search/search%20term/"
        #base url for the program to modify
        replacewith=searchbox.get()
        piratebayurl.replace('search%20term', replacewith)
        #replaces the search%20term in the url with the users chosen search term 
        response = requests.get(piratebayurl.replace('search%20term', replacewith))
        #requests the html of the page
        html = response.text
        #saves the html as a big string
        soup = BeautifulSoup(html, "lxml")
        #does some magic
        soup.prettify()
        #prettifies it?
        try:
            #try accept in an attempt to fix problems with specific websites not working
            titles=soup.find_all(class_="detLink")
            #creates an object containing all of the tags in the webpage that contain the class "detLink"
            #all these tags include a title of the torrent, a link to the download page and comments etc that can be added later
            seeders=soup.find_all('td', {'align': 'right'})
            #finds all tags that have the align right attribute which is all of the seeders and leechers information
            del seeders[1::2]
            #deletes the leechers of each file as it wont be in the program
            #may be added at a later date
        except:
            scraper()
        #placed in try accept as the website can go down and may break this part of the program
        i=0
        #sets a base i value of 0 to be used next
        while (i <=4):
            #repeats 5 times
            if titles!=[]:
                currenttitle=titles[i]
                #saves the currently being used title as currenttitle for easier modification
                currenttitle=currenttitle.text
                #uses the built in Beautiful Soup function that only saves the text portion of the tag - the title of the file
                currenturl=str(titles[i])
                #saves the currently being used tag to be modified to get the url as a string
                currenturl=currenturl.replace('<a class="detLink" href="','')
                #removes the first part of the string before the link
                currenturl=currenturl.split('" title', 1)[0]
                #removes everything after the link
                currenturl="https://thepiratebay.org"+currenturl
                #adds the base url to the extension (urls on the website are saved as /torrent/variousnumbers/title)
                currentseeders=seeders[i]
                #saves current seeder value as a different variable for easier manipulation
                currentseeders=currentseeders.text
                #uses built in Beautiful Soup function to only save the text from the tag
                #print(currenttitle)
                #print(currenturl)
                #print(currentseeders)
                top5titles.append(currenttitle)
                #adds the top 5 torrents into the list
                top5urls.append(currenturl)
                #adds the top 5 torrents urls to the list
                top5seeders.append(currentseeders)
                #adds the top 5 torrents seeders into the list
                i=i+1
                #increases i value by one each time
            else:
                print("No Results from Piratebay")
                break
        print(top5titles)
        print(top5urls)
        print(top5seeders) 
        #print for testing purposes
    else:
        print("")
    if x1337.get():
        print("Nice")
        global searchterm
        x1337url="https://1337x.to/search/search+term/1/"
        #base url for the program to modify
        replacewith=searchbox.get()
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/41.0.2227.1 Safari/537.36'}
        #sets a "headers" because 1337x "declines" the request for the html because it thinks thats not a browser
        x1337url=x1337url.replace('search+term', replacewith)
        #replaces the search+term in the url with the users chosen search term 
        response = requests.get(x1337url.replace('search+term', replacewith), headers=headers)
        #print(x1337url)
        #requests the html of the page
        html = response.text
        #saves the html as a big string
        soup = BeautifulSoup(html, "lxml")
        #does some magic
        soup.prettify()
        #prettifies it?
        print(soup)
        #rows=soup.find_all('tr')
        #creates an object containing all of the tr rows as each of these includes all the information for one torrent
        #Print for testing purposes
        titles=soup.find_all(class_="coll-1 name")
        print(titles)
        i=0
        #while (i <=4):

    else:
        print("")


def restart():
    menuframe1.pack_forget()
    menuframe2.pack_forget()
    menuframe3.pack_forget()
    searchedframe1.pack_forget()
    searchedframe2.pack_forget()
    searchedframe3.pack_forget()
    tooshort=False
    #chosensite=False
    searchbutton()

def searched():
    global chosensite
    global searchedframe1
    global searchedframe2
    global searchedframe3 
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
#    if searchbox.get()=="Must be longer than 3 characters" or tooshort==True:
#        searchbutton()
#        tooshort=False
#    else:
#        print("")
    if thepiratebay.get() == 1 or x1337.get() == 1 or rarbg.get() == 1 or limetorrents.get() == 1 or katcr.get() == 1 or torrentdownloads.get() == 1:
        print("")
        chosensite=True
    else:
        chosensite=False
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

    tryagainbutton=Button(searchedframe3, text="New Search", command=restart)
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
            searchedframe3.pack_forget()
            menuframe1.pack_forget()
            menuframe2.pack_forget()
            menuframe3.pack_forget()
            #menuframe1.destroy()
            #menuframe2.destroy()
            #menuframe3.destroy()
            tooshort=True
            searchbutton()
            #clears everything and sets the variable "tooshort" to true for future use
        else:
            tooshort=False

    except:
        print("")

    try:
        if chosensite==False:
            #Sends the user back to the search page if they have not chosen any websites to search
            searchedframe1.pack_forget()
            searchedframe2.pack_forget()
            searchedframe3.pack_forget()
            menuframe1.pack_forget()
            menuframe2.pack_forget()
            menuframe3.pack_forget()
            #menuframe1.destroy()
            #menuframe2.destroy()
            #menuframe3.destroy()
            searchbutton()
            #clears everything
        else:
            print("")

    except:
        print("")

    scraper()

def cleartext():
    searchbox.delete(0, END)
    #Clears the searchbox so the user can try again
    menuframe1.pack_forget()
    #Clears the menuframes so they can be remade 
    menuframe2.pack_forget()
    menuframe3.pack_forget()
    searchbutton()
    tooshort=False
    chosensite=False

def searchbutton():
    global chosensite
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
    title = Label(menuframe1, text="Welcome to my Legal Only Torrent searcher", font=("Arial Bold", 25))
    title.pack(pady=(25,30), side=TOP)
    # A basic label with a title "Welcome to this program" using Arial Bold Font size 25
    # Packs the Label into the menuframe and aligns it TOP with padding above of 25px and padding below of 30
    if tooshort==True:
        title2=Label(menuframe1, text="Your search must be longer than 3 characters", font=("Arial Bold", 20))
        title2.pack(side=TOP)
        tooshort=False
    else: 
        print("")
    if chosensite==False:
        title3=Label(menuframe1, text="You have not chosen any websites to search", font=("Arial Bold", 20))
        title3.pack(side=TOP)
        chosensite=True

    else:
        print("")
    searchbox = Entry(menuframe1, text="Enter Search Term", width="35")
    searchbox.pack(side=TOP, pady=10)
    # A basic searchbox for the user to enter their search term to be used by the program to search sites
    # Packs the searchbox into the menuframe, aligned TOP and with a padding of 10px above and below
    #Adds a background text to the box to tell the user that the search must be longer than 3 characters
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
global chosensite

chosensite=True
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
