import requests
import re
import urllib

#target_url = 'https://www.geeksforgeeks.org'


class Crawler:
    def __init__(self, url):
        self.target_url = url
        self.target_links = []
        self.isCrawling = False

    def extract_links_from(self, url):
        response = requests.get(url)
        response = response.text.replace('\'', '"')
        pattern = 'href[ ]{0,1}=[ ]{0,1}"([^\"]{0,})"'
        return re.findall(pattern, response, re.I)

    def crawl(self, url=None):
        if url is None:
            url = self.target_url
        href_links = self.extract_links_from(url)
        for link in href_links:
            link = urllib.parse.urljoin(url, link)
            if '#' in link:
                link = link.split("#")[0]

            if self.target_url in link and link not in self.target_links:
                self.target_links.append(link)
                while self.isCrawling:
                    try:
                        print(link)
                        self.crawl(link)
                    except KeyboardInterrupt:
                        self.isCrawling = False
                        return