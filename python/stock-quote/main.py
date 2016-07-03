import requests

ticker = "BLK"
print("executing")

def get_stock_data(ticker):
    r = requests.get("http://finance.yahoo.com/webservice/v1/symbols/" + ticker + "/quote?format=json&view=%E2%80%8C%E2%80%8Bdetail")
    return r.json()

def ifttt_stockquote(ticker, price, change):
    report = {}
    report["value1"] = ticker
    report["value2"] = price
    report["value3"] = change 
    r = requests.post("https://maker.ifttt.com/trigger/single/with/key/dD37h2LH22FMQNR83Ur-Fl", data=report)    
    return r

def event_handler(event,context):
    print("getting data for " + ticker)
    data = get_stock_data(ticker)
    price = data['list']['resources'][0]['resource']['fields']['price']
    change = data['list']['resources'][0]['resource']['fields']['chg_percent']

    print("sending to IFTTT : " + ticker + "|" + price + "|" + change)
    r = ifttt_stockquote(ticker, price, change)
    print r.headers

print("Done")

