#!/usr/bin/env python

print 'Checking GitHub API Status...'

# Load appropriate HTTP libs
try:
    from urllib.request import Request, urlopen, HTTPError, URLError     # Python 3
    from urllib.parse import urlparse, urlsplit
except:
    from urllib2 import Request, urlopen, HTTPError, URLError            # Python 2
    from urlparse import urlparse, urlsplit
    
# Build Request Object
url = 'https://status.github.com/api/status.json'
print 'Checking url \'' + str(url) + '\''
request = Request(url)

# Check the response
try:
    response = urlopen(request)
    body = json.load(response)   
    print str(body)
except HTTPError as e:
    print 'ERROR: HTTPError Exception thrown; ' + str(e)
    sys.exit(code)
except URLError as e:
    print 'ERROR: URLError Exception thrown; ' + str(e)
    sys.exit(code)
else:
    print 'GitHub API Check PASSED'