from os import listdir
from os.path import join

from requests import get

download_dir = ''


def path_pick(path, extension):
    global download_dir
    c = 1
    download_dir, name = '/'.join(path.split('/')[:-1]), path.split('/')[-1]

    while f'{name}-{c}' in [i.split('.')[0] for i in listdir(download_dir)]:
        c += 1

    return join(download_dir, f'{name}-{c}.{extension}')


def dwn_img(url, path):
    r = get(url, stream=True)
    extension = url.split('.')[-1]
    path = path_pick(path, extension)

    if r.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
        print(f'[+] Finished downloading {path.split("/")[-1]}')
