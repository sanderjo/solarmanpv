#!/usr/bin/env python

from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import cookielib
import json
from pprint import pprint

pid = '6067'


#Create a CookieJar object to hold the cookies
cj = cookielib.CookieJar()
#Create an opener to open pages using the http protocol and to process cookies.
opener = build_opener(HTTPCookieProcessor(cj), HTTPHandler())

#create a request object to be used to get the page.
req = Request('http://www.solarmanpv.com/portal/Terminal/TerminalMain.aspx?pid=')
f = opener.open(req)
#html = f.read()

#Check out the cookies
print "the cookies are: "
for cookie in cj:
    print cookie

req = Request('http://www.solarmanpv.com/portal/AjaxService.ashx?ac=upTerminalMain&psid=' + pid)
html = opener.open(req).read()
result = json.loads(html)
#print result
pprint(result)
print result[0][u'nowpower']
print result[0][u'allpower']


