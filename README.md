Solarmanpv
==========

Tools to read information from www.solarmanpv.com/index_en.html, for example [link](http://www.solarmanpv.com/portal/Terminal/TerminalMain.aspx?pid=6543)

There are the following tools:
* a shell script; a proof of concept to show what is going on
* a python script that gives more beautiful output

Installation
------------

No installation needed; just run the file from the directory you want


Usage
-----

Shell script:

  $ ./solarmanpv-oneliner.sh
  
  [{"nowpower":"0.56 kW","daypower":"0.83 kWh","monthpower":"436.90 kWh","yearpower":"2.30 MWh","allpower":"4.54  MWh","lasttime":"Jul.29 10:12,GMT +2,2014","commissioned":"May.21,2013","capacity":"3.75 kW","installer":"Blabla","peakpower":"3.71 kW","efficiency":"2.41 kWh/kW/day","treesplanted":"12.43 <em style='font-size:16px'>trees</em>","co2":"4.54 <em style='font-size:16px'>ton</em>","income":"â¬1.05K"}]

Python script

$ ./solarmanpv.py

  the cookies are:
  Cookie ASP.NET_SessionId=025q0dvoxudruk45osuxi0uo for www.solarmanpv.com
  
  [{u'allpower': u'1.10 MWh',
    u'capacity': u'1.50 kW',
    u'co2': u"1.10 <em style='font-size:16px'>ton</em>",
    u'commissioned': u'Oct.20,2013',
    u'daypower': u'0.65 kWh',
    u'efficiency': u'2.40 kWh/kW/day',
    u'income': u'\u20ac252.68',
    u'installer': u"blabla",
    u'lasttime': u'Jul.29 10:13,GMT +1,2014',
    u'monthpower': u'138.99 kWh',
    u'nowpower': u'0.67 kW',
    u'peakpower': u'1.73 kW',
    u'treesplanted': u"3.00 <em style='font-size:16px'>trees</em>",
    u'yearpower': u'915.70 kWh'}]
    
  0.67 kW
  
  1.10 MWh




Thank you
---------

Thank you Petje (aka [Petski](https://github.com/petski)) for finding out the underlying solarmanpv mechanism.


