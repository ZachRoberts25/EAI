import urllib2
import re
import math

def websiteCrawler(numberOfWebsites):
    if numberOfWebsites < 26:
        if numberOfWebsites <= 0:
            print "Please enter a number greater than 0"
        array1 = []
        body = urllib2.urlopen("http://www.alexa.com/topsites/global;0").read()
        array = re.findall("href=\"/siteinfo/.*", body)
        i = 0
        while i < len(array):
            x = array[i].split("href=\"/siteinfo/")
            y = x[1].split("\">")
            array1.append(y[0])
            i += 1

        return array1[:numberOfWebsites]
    else:
        array1 = []
        numberOfPages = math.ceil(numberOfWebsites/25.0)
        i = 0
        while i < numberOfPages:
            url = "http://www.alexa.com/topsites/global;" + str(i)
            body = urllib2.urlopen(url).read()
            array = re.findall("href=\"/siteinfo/.*", body)
            z = 0
            while z < len(array):
                x = array[z].split("href=\"/siteinfo/")
                y = x[1].split("\">")
                array1.append(y[0])
                z += 1
            i += 1
        return array1[:numberOfWebsites]
print websiteCrawler(26)
