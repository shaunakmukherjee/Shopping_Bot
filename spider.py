# default program to scan webpages using python

import urllib
import urllib2
import webbrowser
 
data = urllib.urlencode({'q': 'Khaled'})
url = 'http://duckduckgo.com/html/' #small website given for reference
full_url = url + '?' + data
response = urllib2.urlopen(full_url)
with open("results.html", "w") as f:
    f.write(response.read())
 
webbrowser.open("results.html")
