from os import mkdir
from os.path import abspath, dirname, exists, join

from requests_html import HTMLSession

from image_downloader import dwn_img


class Downloader():
    def __init__(self, url, term, name):
        self.URL = url
        self.TERM = term
        self.NAMING_TERM = name
        self.PATH = dirname(abspath(__file__))
        self.session = HTMLSession()

    def create_dwn_if_not_exists(self):
        if not exists(join(self.PATH, 'downloaded')):
            mkdir('downloaded')
        else:
            print('[+] Folder already exists.')

    def run(self):
        self.create_dwn_if_not_exists()

        response = self.session.get(f'{self.URL}{self.TERM}')

        image_tags = response.html.find('.wpimg', first=False)

        for tag in image_tags:
            dwn_img(f'{self.URL}{tag.attrs["src"]}', join(
                self.PATH, 'downloaded', self.NAMING_TERM))
            # TODO : write dwn_img() func
            #! be carefull if img exists don't download
            #! try to multi thread this


d = Downloader('https://wallpapercave.com', '/ciri-wallpapers', 'ciri')
d.run()
