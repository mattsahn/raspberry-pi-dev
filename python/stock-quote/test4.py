from googlefinance import getQuotes

import json
r = getQuotes('BLK')
print r
print r[0]['LastTradeWithCurrency']
