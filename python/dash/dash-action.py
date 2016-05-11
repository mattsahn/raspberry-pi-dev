from scapy.all import *
from requests import post

# Home Assistant API URL to trigger event
url = 'http://localhost:8123/api/events/dash_button_pressed'
headers = {'x-ha-access': '',
           'content-type': 'application/json'}
##json_data = {"entity_id": "script.arrive_home"}

def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)
    if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
      #if pkt[ARP].hwsrc == 'f0:27:2d:1b:26:58': # Dash button
      if pkt[ARP].hwsrc == '74:c2:46:e5:8c:43': # Dash button
        print "Dash button pressed!"
        ## call HA API
        response = post(url, headers=headers)
        print "API called"
        print(response.text)
        print "got API response"
      else:
        print "ARP Probe from unknown device: " + pkt[ARP].hwsrc
print sniff(prn=arp_display, filter="arp", store=0)
