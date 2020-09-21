from os import listdir
from os.path import join

from requests import get


def path_pick(path, extension):
    c = 1
    print(path)
    download_dir = join('downloads', path[1:])
    print(download_dir)
    while f'{c}' in [i.split('.')[0] for i in listdir(download_dir)]:
        c += 1

    return join(download_dir, f'{c}.{extension}')


def dwn_img(url, path):
    r = get(url, stream=True)
    extension = url.split('.')[-1]
    path = path_pick(path, extension)

    if r.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
        print(f'[+] Finished downloading {path.split("/")[-1]}')
