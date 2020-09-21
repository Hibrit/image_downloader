from os import listdir
from os.path import join

from requests import get


def path_pick(path, extension, name):
    download_dir = join('downloads', path[1:])
    return join(download_dir, f'{name}.{extension}')


def dwn_img(url, path, name):
    r = get(url, stream=True)
    extension = url.split('.')[-1]
    path = path_pick(path, extension, name)

    if r.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
