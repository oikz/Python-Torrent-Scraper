from bs4 import BeautifulSoup
import requests
url = 'https://rarbg.to/torrents.php?category=27;28&search=dying+light&order=seeders&by=DESC'
response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, "lxml")

print(soup.prettify())



#hoge = tree.xpath('//td[@class="lista"//@align="left"]//a/text()')
#hoge = tree.xpath('//a[1]/@href')
#hoge = tree.xpath('/html/body/table[3]/tbody/tr/td[2]/div/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td[2]/a')
#hoge = tree.xpath('//*[@onmouseout="return nd();"]/@href')
#hoge = tree.xpath('/html/body/main/div/div/div/div[3]/div[1]/table/tbody/tr[1]/td[1]/a[2]/@href')
#hoge = tree.xpath('//td[@class="coll-1 name"]/@href')
#print(hoge)
#print(tree)
#soup = BeautifulSoup(tree, 'html.parser')
#print(soup.prettiffy())
#tree.xpath('//div[@class="content"]//a[@class="name"]/@href')
#//div[@class='image']/a[1]/@href

#pageContent=requests.get('https://en.wikipedia.org/wiki/List_of_Olympic_medalists_in_judo')
#tree = html.fromstring(pageContent.content)

#goldWinners=tree.xpath('//*[@id="mw-content-text"]/table/tr/td[2]/a[1]/text()')
#silverWinners=tree.xpath('//*[@id="mw-content-text"]/table/tr/td[3]/a[1]/text()')
#bronzeWinner we need rows where there's no rowspan - note XPath
#bronzeWinners=tree.xpath('//*[@id="mw-content-text"]/table/tr/td[not(@rowspan=2)]/a[1]/text()')
#medalWinners=goldWinners+silverWinners+bronzeWinners