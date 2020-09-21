from os import mkdir
from os.path import abspath, dirname, exists, join
from threading import Thread

from requests_html import HTMLSession

from image_downloader import dwn_img

URL = 'https://wallpapercave.com'


class Downloader():
    def __init__(self, url, term):
        self.URL = url
        self.TERM = term
        self.PATH = dirname(abspath(__file__))
        self.session = HTMLSession()

    def create_dwn_if_not_exists(self):
        if not exists(join(self.PATH, 'downloads')):
            mkdir('downloads')
        else:
            print('[+] Folder already exists.')

        if not exists(join(self.PATH, 'downloads', self.TERM[1:])):
            mkdir(join('downloads', self.TERM[1:]))
        else:
            print('[+] Folder already exists.')

    def run(self):
        self.create_dwn_if_not_exists()

        response = self.session.get(f'{self.URL}{self.TERM}')

        image_tags = response.html.find('.wpimg', first=False)

        for tag in image_tags:
            dwn_img(f'{self.URL}{tag.attrs["src"]}', join(
                self.PATH, 'downloads', self.TERM))
            # TODO : write dwn_img() func
            #! be carefull if img exists don't download
            #! try to multi thread this


def foo(term):
    d = Downloader(URL, term)
    d.run()


to_dwn_list = [
    '/binding-of-isaac-desktop-wallpapers',
    '/the-binding-of-isaac-wallpapers',
    '/dark-wallpapers',
    '/dark-anime-desktop-wallpapers',
    '/dark-gaming-wallpapers',
    '/wallpaper-arch-linux',
    '/arch-linux-wallpaper',
    '/ciri-wallpapers',
    '/the-witcher-3-wild-hunt-hd-wallpapers',
    '/the-witcher-4k-hd-wallpapers',
    '/yennefer-wallpapers',
    '/the-witcher-triss-merigold-desktop-wallpapers'
]

ts = []

for i in to_dwn_list:
    t = Thread(target=foo, args=(i,))
    ts.append(t)

for t in ts:
    t.deamon = True
    t.start()

for t in ts:
    t.join()
