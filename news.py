
import requests
from bs4 import BeautifulSoup
print 'Headlines ...'
news = []
url = 'http://feeds.feedburner.com/NdtvNews-TopStories'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
for i in soup.find_all('item'):
    news.append(i.find('title').text)
for i in news[:3]:
    print i
print '------'
