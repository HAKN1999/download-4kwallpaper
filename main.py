#!/usr/bin/python3

from requests_html import HTMLSession
from time import sleep
import requests
import wget
import re
import os


class Images:
    def __init__(self):
        self.session = HTMLSession()
        self.parent_dir = os.getcwd()

    def target_website(self, url):
        self.regex(url)
        response = self.session.get(url)
        flex_box = response.html.find('.flexbox_item')
        for pages in flex_box:
            for page in pages.find('a'):
                for link in page.links:
                    # print(link)
                    self.download(link)

        # if found download reset by peer
        if len(self.list_broken_link) > 0:
            self.error_download(self.list_broken_link)

    def create_folder(self, directory):
        self.path = os.path.join(self.parent_dir, directory)
        try:
            os.makedirs(self.path)
        except:
            print('Folder created!')

    def regex(self, url):
        r = re.findall(r"https://4kwallpaper.wiki/(.*).html", url)
        directory = r[0]
        self.create_folder(directory)
        print(f'Active on {self.directory}')

    def download(self, url):
        self.list_broken_link = list()
        try:
            os.chdir(self.path)
        except Exception as e:
            print(e)

        # handel download reset by peer
        try:
            wget.download(url)
        except Exception as e:
            print(f'ConnectionResetError {url}\n')
            self.list_broken_link.append(url)

    def error_download(self, link_broken):
        # download again if found reset download
        if len(list_broken_link) > 0:
            [self.download(i) for i in self.list_broken_link]


url = ['https://4kwallpaper.wiki/taokaka-wallpapers.html',
       'https://4kwallpaper.wiki/sharingan-eyes-wallpapers.html', 'https://4kwallpaper.wiki/chibi-wallpapers.html', 'https://4kwallpaper.wiki/stella-glow-wallpapers.html']

img = Images()
[img.target_website(i) for i in url]
