
"""
We want to use Python and an HTML parser called BeautifulSoup
to visit websites (UIC News) and extract their article dates, titles, 
article url and the article text. 
"""


from bs4 import BeautifulSoup
import urllib3

#2
def GetArticleText(art_url):    
    http = urllib3.PoolManager()
    requested = http.request('GET', art_url)
    B = BeautifulSoup(requested.data.decode('utf-8'), 'lxml')
    Btmp = B.find('div', {'class': 'pf-content'})
    art_text = Btmp.get_text().replace("\n", "")
    return art_text
 
#1      
def ScrapeUICNews():
    http = urllib3.PoolManager()
    uic_news_url = "https://today.uic.edu/uicnews/section/uic-news/"
    requested = http.request('GET', uic_news_url)
    B = BeautifulSoup(requested.data.decode('utf-8'), 'lxml')
    #print(B) # for a basic HTML content
    #print(B.prettify()) # for a better/neater display of the HTML content
    Articles = B.find_all('div', attrs = {'class' : 'news-release-info clearfix'})
    for meta_art in Articles:
        date = meta_art.find('p').getText() # finds the first paragraph occurrence and returns its text component
        title = meta_art.find('a').string # extracts the title from the url anchor
        art_url = meta_art.find('a')['href'] # extracts the url of the article
        print(date)
        print(title)  
        print(art_url)
        article = GetArticleText(art_url)
        print(article)
        print("--------------")
def main():
    ScrapeUICNews()

main()
