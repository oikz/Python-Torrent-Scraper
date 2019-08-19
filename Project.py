from tkinter import *
from bs4 import BeautifulSoup
import requests
import time


class scraper:
    top5titles = []
    top5urls = []
    top5seeders = []

    def __init__(self, top5titles, top5urls, top5seeders):
        self.top5titles = top5titles
        self.top5urls = top5urls
        self.top5seeders = top5seeders

    def piratebayscraper(self):
        global searchterm
        piratebayurl = "https://thepiratebay.org/search/search%20term/"
        # base url for the program to modify
        replacewith = searchbox.get()
        piratebayurl.replace('search%20term', replacewith)
        # replaces the search%20term in the url with the users chosen search term
        response = requests.get(
            piratebayurl.replace('search%20term', replacewith))
        # requests the html of the page
        html = response.text
        # saves the html as a big string
        soup = BeautifulSoup(html, "lxml")
        # does some magic
        soup.prettify()
        # prettifies it?
        try:
            # try accept in an attempt to fix problems with specific websites not working
            titles = soup.find_all(class_="detLink")
            # creates an object containing all of the tags in the webpage that contain the class "detLink"
            # all these tags include a title of the torrent, a link to the download page and comments etc that can be added later
            seeders = soup.find_all('td', {'align': 'right'})
            # finds all tags that have the align right attribute which is all of the seeders and leechers information
            del seeders[1::2]
            # deletes the leechers of each file as it wont be in the program
            # may be added at a later date
        except:
            print("Piratebay Ded")
        # placed in try accept as the website can go down and may break this part of the program
        i = 0
        # sets a base i value of 0 to be used next
        while (i <= 4):
            # repeats 5 times
            if titles != []:
                currenttitle = titles[i]
                # saves the currently being used title as currenttitle for easier modification
                currenttitle = currenttitle.text
                # uses the built in Beautiful Soup function that only saves the text portion of the tag - the title of the file
                currenturl = str(titles[i])
                # saves the currently being used tag to be modified to get the url as a string
                currenturl = currenturl.replace(
                    '<a class="detLink" href="', '')
                # removes the first part of the string before the link
                currenturl = currenturl.split('" title', 1)[0]
                # removes everything after the link
                currenturl = "https://thepiratebay.org"+currenturl
                # adds the base url to the extension (urls on the website are saved as /torrent/variousnumbers/title)
                currentseeders = seeders[i]
                # saves current seeder value as a different variable for easier manipulation
                currentseeders = currentseeders.text
                # uses built in Beautiful Soup function to only save the text from the tag
                # print(currenttitle)
                # print(currenturl)
                # print(currentseeders)
                self.top5titles.append(currenttitle)
                # adds the top 5 torrents into the list
                self.top5urls.append(currenturl)
                # adds the top 5 torrents urls to the list
                self.top5seeders.append(currentseeders)
                # adds the top 5 torrents seeders into the list
                i = i+1
                # increases i value by one each time
            else:
                print("No Results from Piratebay")
                break
        print(self.top5titles)
        print(self.top5urls)
        print(self.top5seeders)
        # print for testing purposes

    def x1337scraper(self):
        global searchterm
        x1337url = "https://1337x.to/search/search+term/1/"
        # base url for the program to modify
        replacewith = searchbox.get()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/41.0.2227.1 Safari/537.36'}
        # sets a "headers" because 1337x "declines" the request for the html because it thinks thats not a browser
        # literlly stole this from stack overflow
        x1337url = x1337url.replace('search+term', replacewith)
        # replaces the search+term in the url with the users chosen search term
        response = requests.get(x1337url, headers=headers)
        # .replace(
        #    'search+term', replacewith), headers=headers)
        # print(x1337url)
        # requests the html of the page
        html = response.text
        # saves the html as a big string
        soup = BeautifulSoup(html, "lxml")
        # does some magic
        soup.prettify()
        # prettifies it?
        # rows=soup.find_all('tr')
        # creates an object containing all of the tr rows as each of these includes all the information for one torrent
        # Print for testing purposes
        titles = soup.find_all(class_="coll-1 name")
        comments = soup.find_all(class_="comments")
        seeders = soup.find_all(class_="coll-2 seeds")
        # grabs all of the elements with the clas of coll-1 name
        # print(titles)
        i = 1
        # set at 1 instead of 0 as the first element with coll-1 name is not relevant for this program
        while (i <= 5):
            if titles != []:
                currenttitle = titles[i]
                # gets a title based on the value of i
                currenttitle = currenttitle.text
                currentcomment = comments[i-1]
                # grabs comments at i-1 as i is based on the coll-1 name classes which ignore the first one
                currentcomment = str(currentcomment)
                # converts to string
                currentcomment = currentcomment.replace(
                    '<span class="comments"><i class="flaticon-message"></i>', '')
                # removes everything before the number of comments
                currentcomment = currentcomment.split('</span>', 1)[0]
                currenttitle = currenttitle.replace(currentcomment, '')
                # replaces the number at the end of the title (the number of comments) with a blank space
                currenturl = titles[i]
                # print(currenturl)
                currenturl = str(currenturl)
                # converts currenturl to a string
                currenturl = currenturl.replace(
                    '<td class="coll-1 name"><a class="icon" href="/sub/10/0/"><i class="flaticon-apps"></i></a><a href="', '')
                # removes all of the irrelevant html info from before the url
                currenturl = currenturl.split('">', 1)[0]
                # removes irrelevant information from after the url
                currenturl = "http://www.1337x.to"+currenturl
                currentseeders = seeders[i-1]
                currentseeders = str(currentseeders)
                currentseeders = currentseeders.replace(
                    '<td class="coll-2 seeds">', '')
                currentseeders = currentseeders.split('</td>', 1)[0]
                self.top5titles.append(currenttitle)
                self.top5urls.append(currenturl)
                self.top5seeders.append(currentseeders)
                i = i+1
            else:
                print("No Results from 1337x")
                break
        print(self.top5titles)
        print(self.top5urls)
        print(self.top5seeders)

    def rarbgscraper(self):
        global searchterm
        rarbgurl = "https://rarbg.to/torrents.php?search=search+term"
        # base url for the program to modify
        replacewith = searchbox.get()
        rarbgurl = rarbgurl.replace('search+term', replacewith)
        # replaces search+term with the users chosen term
        rarbgurl = rarbgurl+"&order=seeders&by=DESC"
        response = requests.get(rarbgurl)
        # requests the html of the page
        html = response.text
        # saves the html as a big string
        soup = BeautifulSoup(html, "lxml")
        # parses the html and saves it
        soup.prettify()
        # converts the "soup" parse tree into a long string
        titles = soup.find_all(class_="lista")
        i = 1
        while (i <= 40):
            currenttitle = titles[i+13]
            currenttitle = currenttitle.text
            currenturl = titles[i+13]
            currenturl = str(currenturl)
            currenturl = currenturl.replace('<td align="left" class="lista"><a href="', '')
            print(currenturl)
            currentseeders = titles[i+16]
            currentseeders = currentseeders.text
            self.top5titles.append(currenttitle)
            self.top5urls.append(currenturl)
            self.top5seeders.append(currentseeders)
            i = i+8
        print(self.top5titles)
        print(self.top5seeders)
        print(self.top5urls)

    def zooqlescraper(self):
        global searchterm
        zooqleurl="https://zooqle.com/search?q=Search+Term"
        replacewith= searchbox.get()
        zooqleurl=zooqleurl.replace('Search+Term', replacewith)
        zooqleurl=zooqleurl+'&s=ns&v=t&sd=d'
        response = requests.get(zooqleurl)
        # requests the html of the page
        html = response.text
        # saves the html as a big string
        soup = BeautifulSoup(html, "lxml")
        # parses the html and saves it
        soup.prettify()
        # converts the "soup" parse tree into a long string object thing
        titles = soup.find_all(class_="text-trunc text-nowrap")
        i = 0
        while (i <= 5):
            currenttitle=titles[i]
            #currenttitle=currenttitle.text
            currenttitle=str(currenttitle)
            currenttitle2=currenttitle.split('<hl>', 1)[1]
            currenttitle2=currenttitle2+currenttitle[2]
            currenttitle2=currenttitle2.split('</a>', 1)[0]
            currenttitle2=currenttitle2.replace('</hl>','')
            print(currenttitle2)
            i=i+1




class gui:
    def restart():
        menuframe1.pack_forget()
        menuframe2.pack_forget()
        menuframe3.pack_forget()
        searchedframe1.pack_forget()
        searchedframe2.pack_forget()
        searchedframe3.pack_forget()
        tooshort = False
        # chosensite=False
        gui.mainmenu()

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
        searchedframe1 = Frame(window)
        searchedframe1.pack()
        searchedframe2 = Frame(window)
        searchedframe2.pack()
        searchedframe3 = Frame(window)
        searchedframe3.pack()
        # if searchbox.get()=="Must be longer than 3 characters" or tooshort==True:
        # mainmenu()
        # tooshort=False
        # else:
        # print("")
        if thepiratebay.get() == 1 or x1337.get() == 1 or rarbg.get() == 1 or zooqle.get() == 1 or katcr.get() == 1 or torrentdownloads.get() == 1:
            print("")
            chosensite = True
        else:
            chosensite = False
        title = Label(searchedframe1, text="Results for: " +
                      searchbox.get(), font=("Arial Bold", 25))
        if thepiratebay.get():
            piratebaylabel = Label(searchedframe2, text="ThePirateBay.org")
            piratebaylabel.pack(side=LEFT)
            piratebayobj = scraper([], [], [])
            piratebayobj.piratebayscraper()
        else:
            print("")
        if x1337.get():
            x1337label = Label(searchedframe2, text="1337x.to")
            x1337label.pack(side=LEFT)
            x1337obj = scraper([], [], [])
            x1337obj.x1337scraper()
        else:
            print("")
        if rarbg.get():
            rarbglabel = Label(searchedframe2, text="rarbg.to")
            rarbglabel.pack(side=LEFT)
            rarbgobj = scraper([], [], [])
            rarbgobj.rarbgscraper()
        else:
            print("")
        if zooqle.get():
            zooqlelabel = Label(searchedframe2, text="zooqle")
            zooqlelabel.pack(side=LEFT)
            zooqleobj=scraper([], [], [])
            zooqleobj.zooqlescraper()
        else:
            print("")
        if katcr.get():
            katcrlabel = Label(searchedframe2, text="Kickass Torrents")
            katcrlabel.pack(side=LEFT)
            katcrobj = scraper([], [], [])
            katcrobj.katcrscraper()
        else:
            print("")
        if torrentdownloads.get():
            torrentdownloadslabel = Label(
                searchedframe2, text="Torrent Downloads")
            torrentdownloadslabel.pack(side=LEFT)
            scraper.torrentdownloadsscraper()
        title.pack()

        tryagainbutton = Button(
            searchedframe3, text="New Search", command=gui.restart)
        tryagainbutton.pack(side=RIGHT)

        # original output testing for checkboxes
        # print("thepiratebay")
        # print(thepiratebay.get())
        # print("1337x")
        # print(x1337.get())
        # print("rarbg")
        # print(rarbg.get())
        # print("zooqle")
        # print(zooqle.get())
        # print("katcr")
        # print(katcr.get())
        # print("torrentdownloads")
        # print(torrentdownloads.get())

        try:
            if len(searchbox.get()) <= 3 or searchbox.get() == "Must be longer than 3 characters":
                # Sends the user back to the search page if their search term is smaller than 3 characters
                searchedframe1.pack_forget()
                searchedframe2.pack_forget()
                searchedframe3.pack_forget()
                menuframe1.pack_forget()
                menuframe2.pack_forget()
                menuframe3.pack_forget()
                # menuframe1.destroy()
                # menuframe2.destroy()
                # menuframe3.destroy()
                tooshort = True
                gui.mainmenu()
                # clears everything and sets the variable "tooshort" to true for future use
            else:
                tooshort = False

        except:
            print("")

        try:
            if chosensite == False:
                # Sends the user back to the search page if they have not chosen any websites to search
                searchedframe1.pack_forget()
                searchedframe2.pack_forget()
                searchedframe3.pack_forget()
                menuframe1.pack_forget()
                menuframe2.pack_forget()
                menuframe3.pack_forget()
                # menuframe1.destroy()
                # menuframe2.destroy()
                # menuframe3.destroy()
                gui.mainmenu()
                # clears everything
            else:
                print("")

        except:
            print("")

    def cleartext():
        searchbox.delete(0, END)
        # Clears the searchbox so the user can try again
        menuframe1.pack_forget()
        # Clears the menuframes so they can be remade
        menuframe2.pack_forget()
        menuframe3.pack_forget()
        gui.mainmenu()
        tooshort = False
        chosensite = False

    def mainmenu():
        global chosensite
        global tooshort
        global window
        global title
        global searchbox
        global menuframe1
        global menuframe2
        global menuframe3
        menuframe1 = Frame(window)
        # Creates menuframe1 in the wndow element
        menuframe1.pack()
        # Packs the menuframe1 into the window created
        menuframe2 = Frame(window)
        menuframe2.pack()
        menuframe3 = Frame(window)
        menuframe3.pack()
        window.title("Torrent Scraper")
        # Gives the window a title
        title = Label(menuframe1, text="Welcome to my Legal Only Torrent searcher", font=(
            "Arial Bold", 25))
        title.pack(pady=(25, 30), side=TOP)
        # A basic label with a title "Welcome to this program" using Arial Bold Font size 25
        # Packs the Label into the menuframe and aligns it TOP with padding above of 25px and padding below of 30
        if tooshort == True:
            title2 = Label(menuframe1, text="Your search must be longer than 3 characters", font=(
                "Arial Bold", 20))
            title2.pack(side=TOP)
            tooshort = False
        else:
            print("")
        if chosensite == False:
            title3 = Label(menuframe1, text="You have not chosen any websites to search", font=(
                "Arial Bold", 20))
            title3.pack(side=TOP)
            chosensite = True

        else:
            print("")
        searchbox = Entry(menuframe1, text="Enter Search Term", width="35")
        searchbox.pack(side=TOP, pady=10)
        # A basic searchbox for the user to enter their search term to be used by the program to search sites
        # Packs the searchbox into the menuframe, aligned TOP and with a padding of 10px above and below
        # Adds a background text to the box to tell the user that the search must be longer than 3 characters
        search = Button(menuframe1, text="Search", command=gui.searched)
        search.pack(side=RIGHT)
        # Adds a search button for the user to execute the search with their chosen options and executes the searched() function
        # Packs button to the right
        clear = Button(menuframe1, text="Clear", command=gui.cleartext)
        clear.pack(side=RIGHT)
        # Adds a Clear button for the user to clear their search preferences
        checkbox1 = Checkbutton(
            menuframe2, text="ThePirateBay", variable=thepiratebay)
        checkbox1.pack(side=LEFT)
        # Adds a checkbox for the user to select which websites they would like the program to search and saves it as a var
        # Packs it below the title and searchbox aligned left
        checkbox2 = Checkbutton(menuframe2, text="1337x", variable=x1337)
        checkbox2.pack(side=LEFT)
        #
        checkbox3 = Checkbutton(menuframe2, text="Rarbg", variable=rarbg)
        checkbox3.pack(side=LEFT)
        #
        checkbox4 = Checkbutton(menuframe3, text="Zooqle", variable=zooqle)
        checkbox4.pack(side=LEFT)
        #
        #checkbox5 = Checkbutton(
        #    menuframe3, text="Kickass Torrents", variable=katcr)
        #checkbox5.pack(side=LEFT)
        #
        #checkbox6 = Checkbutton(
        #    menuframe3, text="Torrent Downloads", variable=torrentdownloads)
        #checkbox6.pack(side=LEFT)
        #


# Declare Global Variables
chosensite = True
tooshort = False
window = ""
window = Tk()
window.geometry('650x250')
# Set window size to 650x250 pixels which works well for the things in my project
thepiratebay = IntVar(window)
x1337 = IntVar(window)
rarbg = IntVar(window)
zooqle = IntVar(window)
katcr = IntVar(window)
torrentdownloads = IntVar(window)
# Declare future variables used in widgets
gui.mainmenu()
# Calls first function
window.mainloop()
# Starts the window loop to keep it open
