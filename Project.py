from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup
import requests
import time
import webbrowser


class scraper:
    #top5titles = []
    #top5urls = []
    #top5seeders = []

    def __init__(self, top5titles, top5urls, top5seeders):
        self.top5titles = top5titles
        self.top5urls = top5urls
        self.top5seeders = top5seeders

    def piratebayscraper(self):
        global searchterm
        titles = []
        piratebayurl = "https://thepiratebay.org/search/search%20term/"
        # base url for the program to modify
        replacewith = searchbox.get()
        piratebayurl.replace('search%20term', replacewith)
        # replaces the search%20term in the url with the users chosen search term
        # try accept in an attempt to fix problems with specific websites not working
        response = requests.get(
            piratebayurl.replace('search%20term', replacewith))
        # requests the html of the page
        html = response.text
        # saves the html as a big string
        soup = BeautifulSoup(html, "lxml")
        # does some magic
        soup.prettify()
        # prettifies it?

        titles = soup.find_all(class_="detLink")
        # creates an object containing all of the tags in the webpage that contain the class "detLink"
        # all these tags include a title of the torrent, a link to the download page and comments etc that can be added later
        seeders = soup.find_all('td', {'align': 'right'})
        # finds all tags that have the align right attribute which is all of the seeders and leechers information
        del seeders[1::2]
        # deletes the leechers of each file as it wont be in the program
        # may be added at a later date
        if html.find("The initial connection between Cloudflare's network and the origin web server timed out. As a result, the web page can not be displayed.") == -1:
            # if it can find the phrase
            print("Website seems to work")
        else:
            print("Retrying")
            piratebayobj.piratebayscraper()
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
                self.top5seeders.append(int(currentseeders))
                # adds the top 5 torrents seeders into the list
                i = i+1
                # increases i value by one each time
                # print(currenttitle)
                # print(currenturl)
                # print(currentseeders)
            else:
                print("No Results from Piratebay")
                break
        # print(self.top5titles)
        # print(self.top5urls)
        # print(self.top5seeders)
        # print for testing purposes

    def x1337scraper(self):
        global searchterm
        titles = []
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
                self.top5seeders.append(int(currentseeders))
                i = i+1
                # print(currenttitle)
                # print(currenturl)
                # print(currentseeders)
            else:
                print("No Results from 1337x")
                break
        # print(self.top5titles)
        # print(self.top5urls)
        # print(self.top5seeders)

    def rarbgscraper(self):
        global searchterm
        titles = []
        rarbgurl = "https://rarbg.to/torrents.php?search=search+term"
        # base url for the program to modify
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/41.0.2227.1 Safari/537.36'}

        replacewith = searchbox.get()
        rarbgurl = rarbgurl.replace('search+term', replacewith)
        # replaces search+term with the users chosen term
        rarbgurl = rarbgurl+"&order=seeders&by=DESC"
        response = requests.get(rarbgurl, headers)
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
            if titles != []:
                currenttitle = titles[i+13]
                currenttitle = currenttitle.text
                currenttitle = currenttitle.split('title="')
                currenturl = titles[i+13]
                currenturl = str(currenturl)
                currenturl = currenturl.replace(
                    '<td align="left" class="lista"><a href="', '')
                currenturl = currenturl.split('" onmouseout')[0]
                currenturl = rarbgurl.replace("search+term", currenturl)
                currentseeders = titles[i+16]
                currentseeders = currentseeders.text
                self.top5titles.append(currenttitle)
                self.top5urls.append(currenturl)
                self.top5seeders.append(int(currentseeders))
                i = i+8
                # print(currenttitle)
                # print(currenturl)
                # print(currentseeders)
            else:
                print("No Results from rarbg")
                break
        # print(self.top5titles)
        # print(self.top5seeders)
        # print(self.top5urls)

    def zooqlescraper(self):
        global searchterm
        zooqleurl = "https://zooqle.com/search?q=Search+Term"
        replacewith = searchbox.get()
        zooqleurl = zooqleurl.replace('Search+Term', replacewith)
        zooqleurl = zooqleurl+'&s=ns&v=t&sd=d'
        response = requests.get(zooqleurl)
        # requests the html of the page
        html = response.text
        # saves the html as a big string
        soup = BeautifulSoup(html, "lxml")
        # parses the html and saves it
        soup.prettify()
        # converts the "soup" parse tree into a long string object thing
        titles = soup.find_all(class_="text-trunc text-nowrap")
        seeders = soup.find_all(
            class_="progress-bar smaller prog-green prog-l")
        i = 0
        while (i <= 4):
            if titles != []:
                currenttitle = titles[i]
                currenttitle = str(currenttitle)
                currenttitle2 = currenttitle.split('">')[3]
                currenttitle2 = currenttitle2.split('</a>', 1)[0]
                currenttitle2 = currenttitle2.replace('<hl>', '')
                currenttitle2 = currenttitle2.replace('</hl>', '')
                currenturl = titles[i]
                ##
                currenturl = str(currenturl)
                if currenturl.find('<a class="small"')!=-1:
                    currenturl = currenturl.split('<a class="small"', 1)[1]
                else:
                    currenturl = currenturl.split('<a class="text-muted2 small"', 1)[1]
                currenturl = currenturl.replace(' href="', '')
                currenturl = currenturl.split('">')[0]
                currenturl = currenturl.replace(' /', '')
                currenturl = "https://zooqle.com"+currenturl
                ##
                currentseeders = seeders[i]
                currentseeders = currentseeders.text
                currentseeders = currentseeders.replace(' K', 'K')
                # removes the gap before the K because i didnt like it
                self.top5titles.append(currenttitle2)
                self.top5urls.append(currenturl)
                self.top5seeders.append(int(currentseeders))
                # print(currenttitle2)
                # print(currenturl)
                # print(currentseeders)
                i = i+1
            else:
                print("No Results from Zooqle")
                break


class gui:
    def __init__(self, alltitles, allurls, allseeders):
        self.alltitles = alltitles
        self.allurls = allurls
        self.allseeders = allseeders

    def callback(url):
        webbrowser.open_new(url)

    def restart(self):
        menuframe1.pack_forget()
        menuframe2.pack_forget()
        menuframe3.pack_forget()
        searchedframe1.pack_forget()
        searchedframe2.pack_forget()
        searchedframe3.pack_forget()
        searchedframe4.pack_forget()
        tooshort = False
        # chosensite=False
        guiobject.mainmenu()

    def searched(self):
        global chosensite
        global searchedframe1
        global searchedframe2
        global searchedframe3
        global searchedframe4
        global tooshort
        global title
        global piratebayobj
        alltitles = []
        allurls = []
        allseeders = []
        menuframe1.pack_forget()
        menuframe2.pack_forget()
        menuframe3.pack_forget()
        searchedframe1 = Frame(window)
        searchedframe1.pack()
        searchedframe2 = Frame(window)
        searchedframe2.pack()
        searchedframe3 = Frame(window)
        searchedframe3.pack()
        searchedframe4 = Frame(window)
        searchedframe4.pack()
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
            alltitles = alltitles+piratebayobj.top5titles
            allurls = allurls+piratebayobj.top5urls
            allseeders = allseeders+piratebayobj.top5seeders

        else:
            print("")
        if x1337.get():
            x1337label = Label(searchedframe2, text="1337x.to")
            x1337label.pack(side=LEFT)
            x1337obj = scraper([], [], [])
            x1337obj.x1337scraper()
            alltitles = alltitles+x1337obj.top5titles
            allurls = allurls+x1337obj.top5urls
            allseeders = allseeders+x1337obj.top5seeders

        else:
            print("")
        if rarbg.get():
            rarbglabel = Label(searchedframe2, text="rarbg.to")
            rarbglabel.pack(side=LEFT)
            rarbgobj = scraper([], [], [])
            rarbgobj.rarbgscraper()
            alltitles = alltitles+rarbgobj.top5titles
            allurls = allurls+rarbgobj.top5urls
            allseeders = allseeders+rarbgobj.top5seeders

        else:
            print("")
        if zooqle.get():
            zooqlelabel = Label(searchedframe2, text="zooqle")
            zooqlelabel.pack(side=LEFT)
            zooqleobj = scraper([], [], [])
            zooqleobj.zooqlescraper()
            alltitles = alltitles+zooqleobj.top5titles
            allurls = allurls+zooqleobj.top5urls
            allseeders = allseeders+zooqleobj.top5seeders
        else:
            print("")
        title.pack()
        titlelist = Text(searchedframe4)
        if allseeders != []:
            allseeders, allurls, alltitles = zip(*sorted(zip(allseeders, allurls, alltitles), reverse=True))
            #sorts all 3 lists relative to each other based on the number of seeders
        else:
            print("Hoge")
        print(alltitles)
        #print(allurls)
        print(allseeders)
        j=0
        tree = ttk.Treeview(searchedframe4, columns=3)
        tree.heading("#0", text="Titles")
        tree.column("#0",minwidth=0,width=100)
        #tree.heading("A", text="")   
        #tree.column("A",minwidth=0,width=200, stretch=NO) 
        tree.heading("#1", text="Seeders")   
        tree.column("#1",minwidth=0,width=20)

        for i in alltitles:
            tree.insert("", "end", text="%s" % i)
        tree.pack(expand=True)    
        #for i in alltitles:
        #    currenturl=allurls[j]
        #    titlelist.insert(END, i + '\n')
        #    #titlelist.bind("<Button-1>", lambda e: gui.callback(currenturl))
        #    j=j+1
        #titlelist.pack(side=LEFT)
        #    i=0
        #    titlelist=Label(searchedframe2, text=scraper.top5titles[i])

        tryagainbutton = Button(
            searchedframe3, text="New Search", command=guiobject.restart)
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
                searchedframe4.pack_forget()
                menuframe1.pack_forget()
                menuframe2.pack_forget()
                menuframe3.pack_forget()
                # menuframe1.destroy()
                # menuframe2.destroy()
                # menuframe3.destroy()
                tooshort = True
                guiobject.mainmenu()
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
                searchedframe4.pack_forget()
                menuframe1.pack_forget()
                menuframe2.pack_forget()
                menuframe3.pack_forget()
                # menuframe1.destroy()
                # menuframe2.destroy()
                # menuframe3.destroy()
                guiobject.mainmenu()
                # clears everything
            else:
                print("")

        except:
            print("")

    def cleartext(self):
        searchbox.delete(0, END)
        # Clears the searchbox so the user can try again
        menuframe1.pack_forget()
        # Clears the menuframes so they can be remade
        menuframe2.pack_forget()
        menuframe3.pack_forget()
        guiobject.mainmenu()
        tooshort = False
        chosensite = False

    def mainmenu(self):
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
        search = Button(menuframe1, text="Search", command=guiobject.searched)
        search.pack(side=RIGHT)
        # Adds a search button for the user to execute the search with their chosen options and executes the searched() function
        # Packs button to the right
        clear = Button(menuframe1, text="Clear", command=guiobject.cleartext)
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
        # checkbox5 = Checkbutton(
        #    menuframe3, text="Kickass Torrents", variable=katcr)
        # checkbox5.pack(side=LEFT)
        #
        # checkbox6 = Checkbutton(
        #    menuframe3, text="Torrent Downloads", variable=torrentdownloads)
        # checkbox6.pack(side=LEFT)
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
guiobject = gui([], [], [])
guiobject.mainmenu()
# Calls first function
window.mainloop()
# Starts the window loop to keep it open
