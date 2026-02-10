# Web Scraper Templates

## Basic Scraper Template
import requests
from bs4 import BeautifulSoup

class BasicScraper:
    def __init__(self, url):
        self.url = url
        self.content = None

    def fetch(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.content = response.content
        else:
            raise Exception('Failed to fetch page')

    def parse(self):
        if not self.content:
            raise Exception('Content not fetched')
        soup = BeautifulSoup(self.content, 'html.parser')
        return soup

## Example Usage
# scraper = BasicScraper('http://example.com')
# scraper.fetch()
# soup = scraper.parse()