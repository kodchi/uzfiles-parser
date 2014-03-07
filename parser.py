import sys
import urllib2
import os 
import re
from BeautifulSoup import BeautifulSoup

print "working..."

#http://uzfiles.com/mp3.php?artist=Ahror%20Usmonov&lang=Uzbek&letter=A 
url = sys.argv[1]
if len(sys.argv) > 2:
	page_num = sys.argv[2]
else:
	page_num = 0

# url = "http://uzfiles.com/mp3.php?artist=Abbos%20Kosimov&lang=Uzbek&letter=A"
file_name = url.split('artist=')[1].split('&lang')[0].replace('%20', ' ') + '.html'
i = 0
link = ""
links =  ""

for i in range(0, int(page_num)):
    url = sys.argv[1] + '&page=' + str(i) + '&sort=id%20desc'
    html = urllib2.urlopen(url).read()
    pages = re.findall("class\=['\"]posts['\"] href=['\"]file_details\.php\?read=(\d+)", html)
    for page in pages:
        down_page = "http://uzfiles.com/file_details.php?read=" + str(page)
        soup = BeautifulSoup(urllib2.urlopen(down_page).read())
        file_path = soup.find("input", attrs={"name": "filepath1"})
        if not file_path:
            continue
        file_path = file_path['value']
        host = soup.find("input", attrs={"name": "host"})['value']
        link = "http://www.%s.com/%s" % (host, file_path)
        print link
        link = link.encode('utf-8')
        links += '<br />' + '<a href="' + link + '" target="_blank">' + link + '</a>' 
        i += 1
f = open(file_name, 'w')
f.write(links)
f.close()
print os.getcwd() + os.sep + file_name
# os.system("firefox " + os.getcwd() + file_name)
