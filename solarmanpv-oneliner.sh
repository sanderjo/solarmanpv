#!/bin/sh

curl --silent --cookie-jar /tmp/cookies -o /dev/null 'http://www.solarmanpv.com/portal/Terminal/TerminalMain.aspx?pid=6067' && \
curl --cookie "ASP.NET_SessionId=`awk ' END { print $NF }' /tmp/cookies`"  'http://www.solarmanpv.com/portal/AjaxService.ashx?ac=upTerminalMain&psid=6067'

