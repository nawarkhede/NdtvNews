import requests
import json
from bs4 import BeautifulSoup

print 'Weather ...'
url = 'http://api.openweathermap.org/data/2.5/weather?q=Mumbai,in&appid=51802c40fcf278769218f282d61d324e&units=metric'
data = requests.get(url)
data = json.loads(data.content)
print '%s -> Min %s - Max %s | humidity %s ' % (data['name'],
                                                data['main']['temp_min'],
                                                data['main']['temp_max'],
                                                data['main']['humidity'])


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
