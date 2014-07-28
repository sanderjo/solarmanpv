#!/bin/sh

# in this case, get the raw information for pid=5432; fill out your own

curl --silent --cookie-jar /tmp/cookies -o /dev/null 'http://www.solarmanpv.com/portal/Terminal/TerminalMain.aspx' && \
curl --cookie "ASP.NET_SessionId=`awk ' END { print $NF }' /tmp/cookies`"  'http://www.solarmanpv.com/portal/AjaxService.ashx?ac=upTerminalMain&psid=5432'

