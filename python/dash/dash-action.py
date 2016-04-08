from scapy.all import *
def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)
    if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
      if pkt[ARP].hwsrc == 'f0:27:2d:1b:26:58': # Dash button
        print "Dash button pressed!"
      else:
        print "ARP Probe from unknown device: " + pkt[ARP].hwsrc
print sniff(prn=arp_display, filter="arp", store=0)
