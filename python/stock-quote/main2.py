import requests
import urllib2
from xml.etree import ElementTree as etree

ticker = "BLK"
print("executing")

def get_stock_data(ticker):
    r = requests.get("http://finance.yahoo.com/webservice/v1/symbols/" + ticker + "/quote?format=json&view=%E2%80%8C%E2%80%8Bdetail")
    return r.json()

def ifttt_stockquote(phrase):
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
        change = data['list']['resources'][0]['resource']['fields']['chg_percent']

        print("sending to IFTTT : " + ticker + "|" + price + "|" + change)
        message = "The current price of " + ticker + " is " + price + " dollars. " + \
            "It has changed " + change + "percent from the previous close"
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

        stories += " Go to www dot blackrock blog dot com to read the full stories. Goodbye"
        print("sending to IFTTT : " + stories)
        r = ifttt_stockquote(stories)

    else:
        print "Event type not handled"

## test code
test_event = { "clickType": "DOUBLE" }
test_context = {}
#event_handler(test_event,test_context)

print("Done")

