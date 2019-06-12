import urllib.request
import json
import codecs

#locu_api = 'at_6NouiZ1qvJE8NIyLbs3nmzhUQAPDU'

url = 'https://api.macaddress.io/v1?apiKey=at_6NouiZ1qvJE8NIyLbs3nmzhUQAPDU&output=json&search=44:38:39:ff:ef:57'
#pramas['search']=Macadd

json_obj = urllib.request.urlopen(url)
reader = codecs.getreader("utf-8")
data = json.load(reader(json_obj))
#print (data)
#print company address

print ("company Name is " +data['vendorDetails']['companyName']);
print ("comapany Address is " +data['vendorDetails']['companyAddress']);
