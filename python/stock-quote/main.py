import requests
import urllib2
from xml.etree import ElementTree as etree
import feedparser
import re
from bs4 import BeautifulSoup

ticker = "BLK"
print("executing")

def get_stock_data(ticker):
    r = requests.get("http://finance.yahoo.com/webservice/v1/symbols/" + ticker + "/quote?format=json&view=%E2%80%8C%E2%80%8Bdetail")
    return r.json()

def ifttt_stockquote(phrase):
    print phrase
    report = {}
    report["value1"] = phrase
    r = requests.post("https://maker.ifttt.com/trigger/single/with/key/dD37h2LH22FMQNR83Ur-Fl", data=report)    
    return r

def event_handler(event,context):
    if event['clickType']=='SINGLE':
        print "Detected SINGLE press"
        print("getting data for " + ticker)
        data = get_stock_data(ticker)
        price = data['list']['resources'][0]['resource']['fields']['price']
        price = str(round(float(price),2))
        change = data['list']['resources'][0]['resource']['fields']['chg_percent']
        change = float(change)
        move = ""
        if (change < -1.0) :
            move = "It has gone down a lot, by "
        elif (change < -.25) :
            move = "It is down for the day, by "
        elif (change > 1.0) :
            move = "It's having a big day, up "
        elif (change > 0.25) :
            move = "It's having a strong day, up "
        else :
            move = "Not much movement today. It has changed "
               
        change = str(round(float(change),2))

        print("sending to IFTTT : " + ticker + "|" + price + "|" + change)
        message = "The current price of ticker " + ticker + " is " + price + " dollars. " + \
            move + change + " percent from the previous close. Goodbye. "
        r = ifttt_stockquote(message)

    elif event['clickType']=='DOUBLE':
        print "Detected DOUBLE press"
        blk_file = urllib2.urlopen('https://www.blackrockblog.com/feed/')
        #convert to string:
        blk_data = blk_file.read()
        #close file because we dont need it anymore:
        blk_file.close()

        #entire feed
        blk_root = etree.fromstring(blk_data)
        item = blk_root.findall('channel/item')

        stories = "Here are the three latest stories from the Blackrock blog: "
        num = 1

        for entry in item:
            #get description
            stories += " Number " + str(num) + ". "
            stories += entry.findtext('description')
            if num == 3:
                break
            num += 1

        stories += " Go to blackrock blog dot com to read the full stories. Goodbye"
        print("sending to IFTTT : " + stories)
        r = ifttt_stockquote(stories)

    elif event['clickType']=='LONG':
        print "Detected LONG press"
    # get first 2 stories from BLK Engineering blog

        feed = feedparser.parse('http://rockthecode.io/feed')
        message = "Here is the the latest story from the Blackrock Engineering blog: "
        for i in range(0,1):
            message += feed['entries'][i].title
            html = feed['entries'][i].content
            soup = BeautifulSoup(html[0]['value'],"html5lib")
            text = soup.get_text()
            match = re.search(r'MEETUP SUMMARY(.*)TECH-',text,re.DOTALL)
            message += match.group(1)

        message += " Go to rock the code dot I O to read the full stories. Go BlackRock Engineers. Goodbye"
        r = ifttt_stockquote(message)

    else:
        print "Event type not handled"

## test code
test_event = { "clickType": "SINGLE" }
test_context = {}
#event_handler(test_event,test_context)

print("Done")

