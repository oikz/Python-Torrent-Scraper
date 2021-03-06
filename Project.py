from tkinter import *
#tkinter library used for basic GUI function
from tkinter import ttk
#ttk extension used for Treeview and more advanced GUI functions
from bs4 import BeautifulSoup
#BeautifulSoup used for the html scraping
import requests
#Requests used for grabbing the html from the website and saving it locally
import webbrowser
#import libraries that i need to use for my program


class scraper:
    #creates Scraper Class

    def __init__(self, top5titles, top5urls, top5seeders, top5sites):
        self.top5titles = top5titles
        self.top5urls = top5urls
        self.top5seeders = top5seeders
        self.top5sites = top5sites
        #initialises variables for each scraper object
        #used to collate all of the different scraper requests into one set of variables

    def piratebayscraper(self):
        global searchterm
        global retry
        #grabs searchterm from the outside code
        titles = []
        #creates an initial list for titles to be appended to
        piratebayurl = "https://thepiratebay.org/search/search%20term/"
        # base url for the program to modify
        replacewith = searchbox.get()
        #gets variable replacewith by calling searchbox.get() to get what the user searched for
        piratebayurl = piratebayurl.replace('search%20term', replacewith)
        # replaces the search%20term in the url with the users chosen search term
        headers = requests.utils.default_headers()
        headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        try:
            response = requests.get(piratebayurl, headers=headers)
        except requests.exceptions.RequestException:
            print("Piratebay Not working")
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
        if html.find("The initial connection between Cloudflare's network and the origin web server timed out. As a result, the web page can not be displayed.") == -1 or html.find("Database maintenance,")==-1:
            #If the program can find this string inside the html, it means the website is down 
            print("")
            #Simply continues down the program to the next part
        else:
            if retry==0:
                retry=1
                piratebayobj.piratebayscraper()

                
            #if the program can find the string, it retries once 
            #may continue going, need to test
            
        i = 0
        # sets a base i value of 0 to be used next
        while (i <= 4):
            # repeats 5 times
            print(len(titles))
            if titles != [] and len(titles)>i:
                #if the titles list contains something
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
                self.top5titles.append(currenttitle)
                # adds the top 5 torrents into the list
                self.top5urls.append(currenturl)
                # adds the top 5 torrents urls to the list
                self.top5seeders.append(int(currentseeders))
                # adds the top 5 torrents seeders into the list
                self.top5sites.append("Thepiratebay.org")
                #adds instances of "thepiratebay.org" to the list based on number of files to be displayed on reuslts page
                i = i+1
                # increases i value by one each time
                # print(currenttitle)
                # print(currenturl)
                # print(currentseeders)
            else:
                #if the title list contains no values the lopp breaks and the program continues
                print("No Results from Piratebay")
                break
        # print(self.top5titles)
        # print(self.top5urls)
        # print(self.top5seeders)
        # print for testing purposes

    def x1337scraper(self):
        global searchterm
        titles = []
        #creates initial titles list
        x1337url = "https://1337x.to/search/search+term/1/"
        # base url for the program to modify
        replacewith = searchbox.get()
        #gets variable replacewith from the users search term
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/41.0.2227.1 Safari/537.36'}
        # sets a "headers" because 1337x "declines" the request for the html because it thinks thats not a browser
        #just a random headers thing i found
        # literlly stole this from stack overflow
        x1337url = x1337url.replace('search+term', replacewith)
        # replaces the search+term in the url with the users chosen search term
        response = requests.get(x1337url, headers=headers)
        # requests the html of the page
        html = response.text
        # saves the html as a big string
        soup = BeautifulSoup(html, "lxml")
        # does some magic
        soup.prettify()
        # prettifies it?
        # Print for testing purposes
        titles = soup.find_all(class_="coll-1 name")
        #grabs all of the elements with the clas of coll-1 name and saves as "titles" to be used for both titles and url
        seeders = soup.find_all(class_="coll-2 seeds")
        i = 1
        # set at 1 instead of 0 as the first element with coll-1 name is not relevant for this program
        while (i <= 5):
            if titles != [] and len(titles) >i:
                #second part is to stop the program from running this code and getting an error if there is less than the expected 5 responses
                print(i)
                print(len(titles))
                #if the titles list contains values
                currenttitle = titles[i]
                # gets a title based on the value of i
                currentcomment = str(currenttitle)
                #saves currentcomment variable a string conversion of "currentitle"
                if currenttitle.find("comments")==-1:
                    currentcomment = currentcomment.split('</i>')[2]
                    #splits currentcomment into parts split by </i> and then chooses the 3rd value as the requested one
                    currentcomment = str(currentcomment)
                    # converts to string
                    currentcomment = currentcomment.split('</span>', 1)[0]
                    # removes everything before the number of comments
                currenttitle = currenttitle.text
                #grabs only the text portion of currentitle using BeautifulSoup4

                currenttitle = currenttitle.replace(currentcomment, '')
                # replaces the number at the end of the title (the number of comments) with a blank space
                currenturl = titles[i]
                # print(currenturl)
                currenturl = str(currenturl)
                # converts currenturl to a string
                #currenturl = currenturl.replace(
                #    '<td class="coll-1 name"><a class="icon" href="/sub/10/0/"><i class="flaticon-apps"></i></a><a href="', '')
                currenturl = currenturl.split('href="', 2)[2]
                # removes all of the irrelevant html info from before the url
                currenturl = currenturl.split('">', 1)[0]
                # removes irrelevant information from after the url
                currenturl = "https://www.1337x.to"+currenturl
                #adds the base url for 1337x.to to the front of the url given by the program
                currentseeders = seeders[i-1]
                #gets currentseeders based on i-1 as the value of i is not the correct value for each file
                currentseeders = str(currentseeders)
                #converts currentseeders to string
                currentseeders = currentseeders.replace(
                    '<td class="coll-2 seeds">', '')
                #Replaces certain parts of the string with '' as they are not required for the program and are constant for eac
                currentseeders = currentseeders.split('</td>', 1)[0]
                #splits the variable at </td> and saves the 0th value
                self.top5titles.append(currenttitle)
                #appends the current title to the local list of titles
                self.top5urls.append(currenturl)
                #appends the current url to the local list of urls
                self.top5seeders.append(int(currentseeders))
                #appends the current seeder value to the local list of seeders
                self.top5sites.append("1337x.to")
                #appends 1337x.to for each file that is added for display in the GUI so the user knows where the file came from
                i = i+1
                #increased i by 1 to get the next set of files
            else:
                print("No Results from 1337x")
                break


    #This scraper/website sometimes only works a couple of times before requests start getting redirected to a captcha
    #style page that i have found no workaround to - browser verification page
    def rarbgscraper(self):
        global searchterm
        titles = []
        rarbgurl = "https://rarbg.to/torrents.php?search=search+term"
        # base url for the program to modify
        replacewith = searchbox.get()
        #saves local variable replacewith as the users search term
        rarbgurl = rarbgurl.replace('search+term', replacewith)
        # replaces search+term with the users chosen term
        rarbgurl = rarbgurl+"&order=seeders&by=DESC"
        #adds part of the url to the end as this sorts the files by highest seeders first which is easier for the program
        try:
            response = requests.get(rarbgurl)
        # requests the html of the page
        except requests.exceptions.RequestException:
            print("Rarbg Not Working")
        html = response.text
        # saves the html as a big string
        soup = BeautifulSoup(html, "lxml")
        # parses the html and saves it
        soup.prettify()
        # converts the "soup" parse tree into a long string
        titles = soup.find_all(class_="lista")
        numberoffiles = soup.find_all(class_="lista2")
        #looks for the number of files based on how many instances there are of lista2 (the class for each table row for each file)
        i = 1
        #sets i to 1 for the first value
        j = 0
        while (i <= 40):
            #repeat while i is equal to or less than 40
            if titles != [] and j < len(numberoffiles):
                #if the titles list contains values
                currenttitle = titles[i+13]
                #gets the currenttitle at i+13 as the structure of the website is strange 
                currenttitle = currenttitle.text
                #gets only the text porion of the variable
                currenttitle = str(currenttitle)
                currenttitle = currenttitle.split('title="')[0]
                #splits the variable between instances of "title="
                print(type(currenttitle))
                currenturl = titles[i+13]
                #grabs current url at i+13 (the same as the title)
                currenturl = str(currenturl)
                #converts variable to a string to it can be modified
                currenturl = currenturl.replace(
                    '<td align="left" class="lista"><a href="', '')
                #replaces parts of the string that arent needed
                currenturl = currenturl.split('" onmouseout')[0]
                #splits the variable between instances of '" onmouseout"' and grabs the first one
                currenturl = rarbgurl.replace("search+term", currenturl)
                #replaces search+term with currenturl?
                currentseeders = titles[i+16]
                #takes currentseeders from i+16
                currentseeders = currentseeders.text
                #takes only the text from the variable
                self.top5titles.append(currenttitle)
                #appends the current title to the top 5 titles for the website
                self.top5urls.append(currenturl)
                #appends the current url to the top 5 urls for the website
                self.top5seeders.append(int(currentseeders))
                #appends the currentseeders as an integer to thet top 5 seeders for that website
                self.top5sites.append("Rarbg.to")
                #appends "rarbg.to" to top5sites so the program can display where this file came from
                i = i+8
                #increases i by 8 for the next file
                j=j+1
            else:
                print("No Results from rarbg")
                break
            #breaks the loop if there are no results from this website

    def zooqlescraper(self):
        global searchterm
        top5titles=[]
        top5urls=[]
        top5seeders=[]
        top5sites=[]
        mutedlist=[]
        zooqleurl = "https://zooqle.com/search?q=Search+Term"
        replacewith = searchbox.get()
        zooqleurl = zooqleurl.replace('Search+Term', replacewith)
        zooqleurl = zooqleurl+'&s=ns&v=t&sd=d'
        try:
            response = requests.get(zooqleurl)
        except requests.exceptions.RequestException:
            print("Zooqle not working")
        # requests the html of the page
        html = response.text
        # saves the html as a big string
        soup = BeautifulSoup(html, "lxml")
        # parses the html and saves it
        soup.prettify()
        # converts the "soup" parse tree into a long string object thing
        titles = soup.find_all(class_="text-trunc text-nowrap")
        seeders = soup.find_all(class_="progress prog trans70")+soup.find_all(class_="progress prog trans90")
        i = 0
        j = 0
        while (i <= 9):
            #runs 10 times to account for any files/torrents that may be listed incorrectly on the website and need to be replaced
            if titles != [] and len(titles)>i:    
                currenttitle = titles[i]             
                currenttitle = str(currenttitle)
                if currenttitle.find('<a class="text-muted2 small"')==-1:
                    #this section only adds non-muted files to the list
                    #on zooqle.com some files are listed with a class of "text-muted2" - unsure why this is but they seem to all
                    #be files that have 1 seeder and 1 torrent so may either be fake or errors on the website database or something                
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
                    currentseeders=str(currentseeders)
                    currentseeders=currentseeders.split('title="', 1)[1]
                    currentseeders = currentseeders.split(' |', 1)[0]
                    currentseeders=currentseeders.replace('Seeders: ', '')
                    print(currentseeders)
                    currentseeders = currentseeders.replace(' K', 'K')
                    # removes the gap before the K because i didnt like it
                    # print(currenttitle2)
                    # print(currenturl)
                    # print(currentseeders)
                    top5titles.append(currenttitle2)
                    top5urls.append(currenturl)
                    top5seeders.append(int(currentseeders))
                    top5sites.append("Zooqle.com")
                else:
                    #if the program finds '<a class="text-muted2 small"' in the program
                    mutedlist.append(titles[i])
                i = i+1
            else:
                print("No Results from Zooqle")
                break
        print(top5titles)
        print(mutedlist)
        #remove muted titles
        if top5seeders != []:
            top5seeders, top5urls, top5titles, top5sites = zip(*sorted(zip(top5seeders, top5urls, top5titles, top5sites), reverse=True))
            #sorts all 4 lists relative to each other based on the number of seeders 
        while (j<=4):
            if titles != [] and len(titles)>j:
                #appends 5 results from the zooqle list of files to the overall list
                self.top5titles.append(top5titles[j])
                self.top5urls.append(top5urls[j])
                self.top5seeders.append(top5seeders[j])
                self.top5sites.append(top5sites[j])
                j=j+1
            else:
                break
class gui:
    def __init__(self, alltitles, allurls, allseeders, allsites):
        #defines class variables
        self.alltitles = alltitles
        self.allurls = allurls
        self.allseeders = allseeders
        self.allsites = allsites

    def restart(self):
        menuframe1.pack_forget()
        menuframe2.pack_forget()
        menuframe3.pack_forget()
        searchedframe1.pack_forget()
        searchedframe2.pack_forget()
        searchedframe3.pack_forget()
        searchedframe4.pack_forget()
        searchedframe5.pack_forget()
        self.allseeders=[]
        self.alltitles=[]
        self.allsites=[]
        self.allurls=[]
        tooshort = False
        # chosensite=False
        guiobject.mainmenu()
        #calls the mainmenu function of the variable guiobject
        window.geometry('650x250')

    def searched(self):
        global chosensite
        global searchedframe1
        global searchedframe2
        global searchedframe3
        global searchedframe4
        global searchedframe5
        global tooshort
        global title
        global piratebayobj
        global retry
        #global Variables
        alltitles = []
        allurls = []
        allseeders = []
        allsites=[]
        #creates variables for results page
        menuframe1.pack_forget()
        menuframe2.pack_forget()
        menuframe3.pack_forget()
        #Clears the packing for the menu frames to reuse the window for the results page
        searchedframe1 = Frame(window)
        searchedframe1.pack()
        searchedframe2 = Frame(window)
        searchedframe2.pack()
        searchedframe3 = Frame(window)
        searchedframe3.pack()
        searchedframe4 = Frame(window)
        searchedframe4.pack()
        searchedframe5 = Frame(window)
        searchedframe5.pack()
        #creates 5 frames to be used by the program for sorting/displaying the results page

        window.geometry('650x420')

        if thepiratebay.get() == 1 or x1337.get() == 1 or rarbg.get() == 1 or zooqle.get() == 1:
            print("")
            chosensite = True
            #if any of the chechboxes are ticked, the program sets "chosensite" to True For use later
        else:
            chosensite = False
            #if none of the checkboxes are ticked, the program sets "chosensite" to false for the program to display a warning later
        title = Label(searchedframe1, text="Results for: " +
                      searchbox.get(), font=("Arial Bold", 25))
        #basic title for the page
        if thepiratebay.get():
            #if thepiratebay box is checked
            piratebaylabel = Label(searchedframe2, text="ThePirateBay.org")
            #creates a label to tell the user they chose this website
            piratebaylabel.pack(side=LEFT)
            piratebayobj = scraper([], [], [], [])
            #creates an object called piratebayobj using scraper and supplying 4 empty lists
            retry=0
            piratebayobj.piratebayscraper()
            #calls piratebayscraper() from inside the new object "piratebayobj"
            self.alltitles = self.alltitles+piratebayobj.top5titles
            #adds all titles from thepiratebay to the alltitles variable list thing
            self.allurls = self.allurls+piratebayobj.top5urls
            #adds all urls from thepiratebay to the allurls variable list thing
            self.allseeders = self.allseeders+piratebayobj.top5seeders
            #adds all seeder values from thepiratebay to the allseeders variable list thing
            self.allsites = self.allsites+piratebayobj.top5sites
            #adds all sites (where the torrent comes from) to the allsites variable list thing
        else:
            print("")
        if x1337.get():
            x1337label = Label(searchedframe2, text="1337x.to")
            x1337label.pack(side=LEFT)
            x1337obj = scraper([], [], [], [])
            x1337obj.x1337scraper()
            self.alltitles = self.alltitles+x1337obj.top5titles
            self.allurls = self.allurls+x1337obj.top5urls
            self.allseeders = self.allseeders+x1337obj.top5seeders
            self.allsites = self.allsites+x1337obj.top5sites

        else:
            print("")
        if rarbg.get():
            rarbglabel = Label(searchedframe2, text="rarbg.to")
            rarbglabel.pack(side=LEFT)
            rarbgobj = scraper([], [], [], [])
            rarbgobj.rarbgscraper()
            self.alltitles = self.alltitles+rarbgobj.top5titles
            self.allurls = self.allurls+rarbgobj.top5urls
            self.allseeders = self.allseeders+rarbgobj.top5seeders
            self.allsites = self.allsites+rarbgobj.top5sites
        else:
            print("")
        if zooqle.get():
            zooqlelabel = Label(searchedframe2, text="zooqle")
            zooqlelabel.pack(side=LEFT)
            zooqleobj = scraper([], [], [], [])
            zooqleobj.zooqlescraper()
            self.alltitles = self.alltitles+zooqleobj.top5titles
            self.allurls = self.allurls+zooqleobj.top5urls
            self.allseeders = self.allseeders+zooqleobj.top5seeders
            self.allsites = self.allsites+zooqleobj.top5sites
        else:
            print("")
        title.pack()

        tryagainbutton = Button(
            searchedframe3, text="New Search", command=guiobject.restart)
            #creates a button for the user to make a new search from the search page that is presented above the results
        tryagainbutton.pack(side=RIGHT)

        if self.allseeders != []:
            self.allseeders, self.allurls, self.alltitles, self.allsites = zip(*sorted(zip(self.allseeders, self.allurls, self.alltitles, self.allsites), reverse=True))
            #sorts all 4 lists relative to each other based on the number of seeders
        else:
            print("")
        

        def weblink(self):
            if titlelistbox.curselection() != ():
                #titlelistbox.curselection() returns the integer value of which part of the list is selected (0 = first line)
                #if this element is not empty
                i = titlelistbox.curselection()[0] 
                #curselection() saves result as a list with the first value being the important one
                #creates variable i with the first value of the titlelistbox.curselection() list        
                item = urlslistbox.get(i)
                #uses the integer supplied by the element clicked by the user to find the correct url from another listbox off screen
                webbrowser.open_new(item)
                #opens a new page with the supplied url
        
        title1=Label(searchedframe4,text="Filename", width=45)
        title1.pack(side=LEFT)
        title2=Label(searchedframe4,text="Seeders", width=10)
        title2.pack(side=LEFT)
        title3=Label(searchedframe4,text="Source Website")
        title3.pack(side=LEFT)
        titlelistbox = Listbox(searchedframe5, selectmode="SELECT", width=50, height=20)
        #creates a number of titles to display above the table of results to notify the user what each column means

        #creates a listbox using searchedframe4 as the frame, the mode of allowing the user to only select one item and the width at 50
        for i in self.alltitles:
            titlelistbox.insert(END, i)
            #this loop inserts each title into the listbox list at the end of the list
        titlelistbox.pack(side=LEFT)
        #packs the listbox to the left to allow the program to display 3 listboxes side-by-side 

        seederlistbox = Listbox(searchedframe5, selectmode="SELECT", width=5, height=20)
        seederlistbox.pack(side=LEFT)
        for i in self.allseeders:
            seederlistbox.insert(END, i)

        siteslistbox = Listbox(searchedframe5, selectmode="SELECT", width=20, height=20)
        siteslistbox.pack()
        for i in self.allsites:
            siteslistbox.insert(END, i)

        urlslistbox = Listbox(searchedframe5, selectmode="SELECT", width=1, height=20)
        urlslistbox.pack(side=LEFT)
        for i in self.allurls:
            urlslistbox.insert(END, i)
        
        titlelistbox.bind('<<ListboxSelect>>', weblink)
        #causes changing the value of the current list number to call weblink()
        #when the user clicks anything in the first listbox, weblink is called 


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
                searchedframe5.pack_forget()
                menuframe1.pack_forget()
                menuframe2.pack_forget()
                menuframe3.pack_forget()
                # menuframe1.destroy()
                # menuframe2.destroy()
                # menuframe3.destroy()
                tooshort = True
                # clears everything and sets the variable "tooshort" to true for future use
                guiobject.mainmenu()
                #calls he mainmenu function of the guiobject to send the user back if their search doesnt meet the parameters
                
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
                searchedframe5.pack_forget()
                menuframe1.pack_forget()
                menuframe2.pack_forget()
                menuframe3.pack_forget()
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
        #Titles based on the user search term telling the user what the problem is.
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

        # Old code used for sites that ended up not working out for my project
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
#creates "window" as root window
window.geometry('650x250')
# Set window size to 650x250 pixels which works well for the things in my project
thepiratebay = IntVar(window)
x1337 = IntVar(window)
rarbg = IntVar(window)
zooqle = IntVar(window)
#katcr = IntVar(window)
#torrentdownloads = IntVar(window)
#declare IntVar variables to be used for tick boxes for the user to select websites to search 
# Declare future variables used in widgets
guiobject = gui([], [], [], [])
guiobject.mainmenu()
# Calls first function
window.mainloop()
# Starts the window loop to keep it open
