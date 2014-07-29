#!/usr/bin/env python

from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import cookielib
import json
from pprint import pprint
import sys

debug = False	# set to True if you want more output

pid = '6666'

if len(sys.argv) < 2:
	sys.stderr.write('Usage: sys.argv[0] <pid>')
	print "... I'm assuming pid", pid
else:
	pid = sys.argv[1]

#Create a CookieJar object to hold the cookies
cj = cookielib.CookieJar()
#Create an opener to open pages using the http protocol and to process cookies.
opener = build_opener(HTTPCookieProcessor(cj), HTTPHandler())

#create a request object to be used to get the page.
req = Request('http://www.solarmanpv.com/portal/Terminal/TerminalMain.aspx?pid=')
f = opener.open(req)
#html = f.read()

if debug:
	#Check out the cookies
	print "the cookies are: "
	for cookie in cj:
	    print cookie

req = Request('http://www.solarmanpv.com/portal/AjaxService.ashx?ac=upTerminalMain&psid=' + pid)
html = opener.open(req).read()
result = json.loads(html)

#print results
if debug:
	pprint(result)

print "NowPower is", result[0][u'nowpower']
print "AllPower is", result[0][u'allpower']


