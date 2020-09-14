from os import mkdir
from os.path import abspath, dirname, exists, join
from threading import Thread

from requests_html import HTMLSession

from image_downloader import dwn_img

URL = 'https://wallpapercave.com'


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


def foo(term, name):
    d = Downloader(URL, term, name)
    d.run()


t1 = Thread(target=foo, args=(
    '/binding-of-isaac-desktop-wallpapers', 'binding-of-isaac-1'))
t2 = Thread(target=foo, args=(
    '/the-binding-of-isaac-wallpapers', 'binding-of-isaac-2'))
t3 = Thread(target=foo, args=('/dark-wallpapers', 'dark'))
t4 = Thread(target=foo, args=('/dark-anime-desktop-wallpapers', 'dark-anime'))
t5 = Thread(target=foo, args=('/dark-gaming-wallpapers', 'dark-gaming'))
t6 = Thread(target=foo, args=('/wallpaper-arch-linux', 'arch-1'))
t7 = Thread(target=foo, args=('/arch-linux-wallpaper', 'arch-2'))
t8 = Thread(target=foo, args=('/ciri-wallpapers', 'ciri'))
t9 = Thread(target=foo, args=(
    '/the-witcher-3-wild-hunt-hd-wallpapers', 'witcher-1'))
t10 = Thread(target=foo, args=('/the-witcher-4k-hd-wallpapers', 'witcher-2'))
t11 = Thread(target=foo, args=('/yennefer-wallpapers', 'yennefer'))
t12 = Thread(target=foo, args=(
    '/the-witcher-triss-merigold-desktop-wallpapers', 'triss'))


ts = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12]

for t in ts:
    t.deamon = True
    t.start()

for t in ts:
    t.join()
