import urllib2 
from multiprocessing.dummy import Pool as ThreadPool

pool = ThreadPool()

urls = [ 'http://www.yahoo.com', 'http://www.reddit.com' ]
results = pool.map(urllib2.urlopen, urls)
pool.close()
pool.join()
print results
