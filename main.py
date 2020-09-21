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
        self.threads = []

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
        current_name = 1
        for tag in image_tags:
            t = Thread(target=dwn_img, args=(
                f'{self.URL}{tag.attrs["src"]}', join(self.PATH, 'downloads', self.TERM), current_name))
            self.threads.append(t)
            current_name += 1
            # TODO : write dwn_img() func
            # ! be carefull if img exists don't download
            # ! try to multi thread this

        for t in self.threads:
            t.deamon = True
            t.start()

        for t in self.threads:
            t.join()
        print(f'[+] Finished downloading {self.TERM}')


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
    '/the-witcher-triss-merigold-desktop-wallpapers',
    '/ciri-wallpapers',
    '/ciri-desktop-wallpapers',
    '/ciri-and-geralt-wallpapers',
    '/geralt-and-ciri-the-witcher-4k-wallpapers',
    '/dark-red-wallpaper-hd',
    '/wallpaper-dark-red'

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
