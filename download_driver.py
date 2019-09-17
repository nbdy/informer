from os import system, makedirs
from os.path import isfile, isdir
from sys import platform


def get_for_current_os():
    if platform.startswith("linux"):
        return ["https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_linux64.zip",
                ]
    elif platform.startswith("win"):
        return ["https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_win32.zip",
                ]
    elif platform.startswith("mac"):
        return ["https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_mac64.zip",
                ]


def download(path, url):
    if not isdir(path):
        makedirs(path)
    z = url.split("/")[-1]
    if not isfile(path + z):
        c = "cd " + path + ";wget " + url + ";unzip " + z + ";rm " + z
        system(c)


def main():
    system('if [ ! -d "driver" ]; then mkdir driver/; fi')
    for u in get_for_current_os():
        download("driver/", u)


if __name__ == '__main__':
    main()
