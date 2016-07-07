import feedparser
import re
from bs4 import BeautifulSoup

feed = feedparser.parse('http://rockthecode.io/feed')

posts = []
for i in range(0,2):
    print feed['entries'][i].title
    print ""
    html = feed['entries'][i].content
    soup = BeautifulSoup(html[0]['value'],"html5lib")
    text = soup.get_text()
    match = re.search(r'MEETUP SUMMARY(.*)TECH-',text,re.DOTALL)
    print match.group(1)

print "done"

