# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify the url
quote_page = 'http://quotes.toscrape.com/random'

# query the website and return the html to the variable page
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find('span', attrs={'class': 'text'})
print name_box.text.strip()

author_box = soup.find('small', attrs={'class': 'author'})
print 'By ' + author_box.text.strip()