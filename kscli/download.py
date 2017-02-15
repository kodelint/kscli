from fabric.colors import green as green, red as red, yellow as yellow
import sys
import os
from utils import error, info, which


def download(mlink):
    exe_path = which('webtorrent')
    if exe_path is None:
        print(red("\nError:: ") + yellow("`webtorrent` is not installed, can't download torrent"))
        print(red("Error:: ") + yellow("please run `npm install webtorrent` to install `webtorrent`"))
    else:
        try:
            os.system("/usr/local/bin/webtorrent --out ~/Downloads/ download " + mlink)
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))


def download_prep(data):
    print('\n')
    sno = raw_input(green('Enter Torrent No to download or q to quit : '))
    if sno == 'q' or sno == 'quit':
        sys.exit(0)
    else:
        if 0 <= int(sno) <= 30:
            for record in data:
                if record[0] == int(sno):
                    info("Downloading : " + yellow(record[1]))
                    download(record[5])
        else:
            error("INVALID INDEX")
