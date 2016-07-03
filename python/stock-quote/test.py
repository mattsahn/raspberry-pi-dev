import urllib2
from xml.etree import ElementTree as etree
blk_file = urllib2.urlopen('https://www.blackrockblog.com/feed/')
#convert to string:
blk_data = blk_file.read()
#close file because we dont need it anymore:
blk_file.close()

#entire feed
blk_root = etree.fromstring(blk_data)
item = blk_root.findall('channel/item')

stories = "Here are the latest stories from the Blackrock blog: "
num = 1

for entry in item:   
    #get description
    stories += " Number " + str(num) + ". "
    stories += entry.findtext('description')  
    num += 1

stories += " Go to www dot blackrock blog dot com to read the full stories. Goodbye"
print stories
