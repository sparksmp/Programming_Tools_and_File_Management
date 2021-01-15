from bs4 import BeautifulSoup
import urllib3

def countTHE(article):
    count = 0
    art = article.lower()
    art = art.replace('.', "")
    art = art.replace(',', "")
    art = art.replace('"', "")
    art = art.replace('?', "")
    art = art.replace("!", "")
    A   =  art.split(" ")
    for word in A:
        if word == "the":
            count += 1
    return count

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
