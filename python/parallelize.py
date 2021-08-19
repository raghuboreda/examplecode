import urllib.request
urls = ['http://finance.yahoo.com']
for url in urls:
    u = urllib.request.urlopen(url)
    print(u)
