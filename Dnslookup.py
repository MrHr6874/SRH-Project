'''#from libs.colors import *
from bs4 import BeautifulSoup
import urllib3
from gooey import Gooey
import argparse
import re
@Gooey
def GetArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", dest="Website", help="Please enter a website URL")
    arguments = parser.parse_args()
    if not arguments.Website:
        parser.error("[-] Please specify a valid URL")
    else:
        return arguments

def validateUrl():
    url_input = GetArguments
    pattern = re.compile(r'\bwww.\b')
    
    if pattern.match(url_input) is None :
        url_input = 'www.'+url_input    
    http = urllib3.PoolManager()
    
    try:
        url = http.request('GET', 'http://'+url_input)
    except urllib3.exceptions.HTTPError:
        print('Please Enter a Valid URL(www.example.com)')
        validateUrl()
    else:
        return url_input

# DNS Lookup

def dns_lookup(url_input):
    http = urllib3.PoolManager()
    url = http.request('GET','https://api.hackertarget.com/dnslookup/?q='+url_input).data
    soup = BeautifulSoup(url, 'lxml')
    print(soup.p.string)


url_input = validateUrl()
dns_lookup(url_input)'''