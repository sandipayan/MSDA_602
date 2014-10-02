__author__ = 'sandipayannandi'


from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()



import urllib2

dict={}


api_key = "e9eac5f806f369c012f19aa40bafba3e3efc8b4a"
url = "http://www.cnn.com/2014/10/01/politics/secret-service-director-resigns/index.html?hpt=hp_t1"
url = "http://access.alchemyapi.com/calls/url/URLGetRankedKeywords?apikey=%s&url=%s&outputMode=xml" % (api_key,url)
xml_op = urllib2.urlopen(url).read()
#print xml_op

f = open('xml_op.xml', 'w')
print >> f, xml_op
f.close()

from xml.dom import minidom
xmldoc = minidom.parse('xml_op.xml')


reflist = xmldoc.getElementsByTagName('keyword')


for i in range(1,len(reflist)):
    dict[reflist[i].childNodes[1].firstChild.data.encode('ASCII')] = reflist[i].childNodes[3].firstChild.data.encode('ASCII')



dict_sorted= sorted([(value,key) for (key,value) in dict.items()] , reverse=True  )

for i in range(0,10):
    print dict_sorted[i]




























