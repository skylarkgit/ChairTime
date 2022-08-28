import urllib.request
import os


def download(filename, url):
    urllib.request.urlretrieve(url,filename)
    
def exists(filename):
    return os.path.exists(filename)