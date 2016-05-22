
from lxml import html
import requests


def scrapmovie(link,n):
    """
    This function scrapes out the name and summary of the ith movie from the list of movie and saves as 'i.txt'

    """
    page = requests.get(link)
    tree = html.fromstring(page.text)

    xp1 = '//*[@id="main"]/div/span/div/div/div[2]/table/tbody/tr[%d]/td[2]/a/text()' %n
    xp2 = '//*[@id="main"]/div/span/div/div/div[2]/table/tbody/tr[%d]/td[2]/a/@href' %n
    movie_name = tree.xpath(xp1)
    try:
        mvi = str(movie_name[0].encode('ascii','ignore'))
    except:
        pass
    links = tree.xpath(xp2)
    print mvi
    print links
    link = 'http://www.imdb.com' + links[0]

    flenm =  "res/%d.txt"%n
    f = open(flenm, "w" )
    f.write(mvi+'\n\n')
    k = link.rfind("/")
    link = link[:k] + '/synopsis?ref_=tt_stry_pl'
    print link
    page = requests.get(link)
    tree = html.fromstring(page.text)
    cast = tree.xpath('//*[@id="swiki.2.1"]/text()')
    print cast
    for i in cast:
        try:
            f.write(str(i)+'\n')
        except:
            pass
    print "done"
    f.write('\n\n')
    f.close()


def scrapmovies(link,n):
    """
    This function is provided with n the number of movies to be scraped from the boxoffice
    page of the IMDB website. The initiates everything.

    """
    for i in range(1,n+1):
        scrapmovie(link,i)

response = input("Please enter the number of movies to be scraped : ")
scrapmovies('http://www.imdb.com/chart/top?ref_=cht_ql_2',int(response))
f.close()

