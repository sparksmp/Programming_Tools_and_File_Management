"""
We want to use Python and an HTML parser called BeautifulSoup
to visit websites (UIC News) and extract their article dates, titles, 
article url and the article text. 
"""


from bs4 import BeautifulSoup
import urllib3

my_word = "the"
def TheCount(article):
    for word in alpha:
        D[c] = 0
    for c in article:
        if c in alpha:
            D[c] += 1
    return D

def GetArticleText(art_url):    
    http = urllib3.PoolManager()
    requested = http.request('GET', art_url)
    B = BeautifulSoup(requested.data.decode('utf-8'), 'lxml')
    Btmp = B.find('div', {'class': 'pf-content'})
    art_text = Btmp.get_text().replace("\n", "")
    return art_text
   
def ScrapeUICNews():
    #this only gets the FIRST srticle on the site - firstArticle funct
    http = urllib3.PoolManager()
    uic_news_url = "https://today.uic.edu/uicnews/section/uic-news/"
    requested = http.request('GET', uic_news_url)
    B = BeautifulSoup(requested.data.decode('utf-8'), 'lxml')
    #print(B) # for a basic HTML content
    #print(B.prettify()) # for a better/neater display of the HTML content
    Articles = B.find_all('div', attrs = {'class' : 'news-release-info clearfix'})
    firstArticle = Articles[0]  # only consider the first article
    title = firstArticle.find('a').string # extracts the title of the article inside the <a > hyperlink/anchor
    art_url = firstArticle.find('a')['href'] # extracts the url of the article  
    article = GetArticleText(art_url)
    D = ArticleLetterCount(article)
    print(D)
    
def main():
    ScrapeUICNews()

main()
