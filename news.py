
import requests
from bs4 import BeautifulSoup
print 'Headlines ...'
news = []
url = 'http://zeenews.india.com/rss/india-national-news.xml'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
for i in soup.find_all('item'):
    news.append(i.find('title').text)
for i in news[:5]:
    print i
print '------'
