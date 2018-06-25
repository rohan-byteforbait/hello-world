import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    sum=0
    print('Retrieving', address)
    uh = urllib.request.urlopen(address)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    #print(data.decode())
    tree = ET.fromstring(data)

    comment = tree.findall('.//count')
    for lst in comment:
        #name = comment[lst].find('name').text
        count = (lst).text
        print( 'count', count)
        sum=int(count)+sum
    print(sum)
