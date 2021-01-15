"""
We want to use Python and an HTML parser called BeautifulSoup
to visit websites (NPR News) and extract their article titles, 
article url and the article text. Then we will perform rudimentary 
sentiment analysis on the article text.
"""

from bs4 import BeautifulSoup
import urllib3

#4
def Summary(article):
    """
    a very basic summary of the articles, based on the 
    listing of 15 most frequently occuring article words.
   
    """
    D = {}
    S = set()
    with open("stopwords.txt", "r") as f:
        for line in f:
            word = line.replace("\n", "")
            S.add(word)
    art = article.lower()
    art = art.replace('.', "")
    art = art.replace(',', "")
    art = art.replace('"', "")
    art = art.replace('?', "")
    art = art.replace("!", "")
    A   =  art.split(" ") # entire article to a list of words
    for word in A:
        if word not in S and word != "":
            if word not in D:
                D[word] = 1
            else:
                D[word] += 1 
    E = sorted(D.items(), key = lambda x: x[1], reverse=True) #sort dictionary according to value
    print("15 most frequent words:")
    for i in range(15):
        print(E[i][0])
#3
def SentimentAnalysis(article):
    """
    an extremely basic sentinment analysis of the articles, 
    based on the word comparisons and word frequencies.
    """

    pos_sentiment_cnt = 0
    neg_sentiment_cnt = 0
    neut_sentiment_cnt = 0
    P = set()
    N = set()
    S = set()
    with open("positivesentimentwords.txt", "r") as f:
        for line in f:
            word = line.replace("\n", "")
            P.add(word)

    with open("negativesentimentwords.txt", "r") as f:
        for line in f:
            word = line.replace("\n", "")
            N.add(word)

    with open("stopwords.txt", "r") as f:
        for line in f:
            word = line.replace("\n", "")
            S.add(word)

    art = article.lower()
    art = art.replace('.', "")
    art = art.replace(',', "")
    art = art.replace('"', "")
    art = art.replace('?', "")
    art = art.replace("!", "")
    A = set(art.split(" ")) # entire article to a set of words
    B = set([word for word in A if word not in S])
    pos_sentiment_cnt = len(B.intersection(P))
    neg_sentiment_cnt = len(B.intersection(N))
    print("positive sentiment (in %)",  100*pos_sentiment_cnt/len(B))
    print("negative sentiment (in %)",  100*neg_sentiment_cnt/len(B))
#2
def GetArticleText(art_url):    
    http = urllib3.PoolManager()
    requested = http.request('GET', art_url)
    B = BeautifulSoup(requested.data.decode('utf-8'), 'lxml')
    Btmp = B.find('div', {'id': 'storytext'})
    T = Btmp.get_text().replace("\n", "")
    return T
 
#1    
def ScrapeNPR():
    http = urllib3.PoolManager()
    npr_url = "https://www.npr.org/sections/news/"
    requested = http.request('GET', npr_url)
    B = BeautifulSoup(requested.data.decode('utf-8'), 'lxml')
    # for a better display of the html file, use print(B.prettify())
    Articles = B.find_all('h2', attrs = {'class' : 'title'})
    for meta_art in Articles:  # each article
        title = meta_art.find('a').string # extracts the title of the article inside the <a > hyperlink/anchor
        art_url = meta_art.find('a')['href'] # extracts the url of the article  
        article = GetArticleText(art_url)
        print(title)
        print(art_url)
        SentimentAnalysis(article)
        Summary(article)
        print("-----------------")
        

def main():
    ScrapeNPR()

main()