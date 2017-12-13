from matplotlib import pyplot
from pymongo import *
client = MongoClient("mongodb://admin:admin@ds021182.mlab.com:21182/c4e")
db = client.get_default_database()

base = db['customers']
cust = base.find()
c_wom = 0
c_ads = 0
c_events = 0
for i in cust:
    if i['ref']=="events":
        c_events += 1
    elif i['ref'] == "ads":
        c_ads += 1
    else:
        c_wom += 1
print(" Word of mouth : ",c_wom)
print("Events :",c_events)
print("Ads :",c_ads)

labels =["Word of mouth ","Events","Ads",]
colors =["blue","#7D3C98","red"]
data = [c_wom,c_events,c_ads]

pyplot.axis("equal")
pyplot.pie(data, labels=labels, colors=colors , shadow = True)
pyplot.show()
