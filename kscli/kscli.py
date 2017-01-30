# -*- coding: utf-8 -*-
"""kickass.

Usage:
  kscli
  kscli [--no_verifyssl=<boolean>][-m | -t | -a | -s | -l | -g | -p | -b | -x | -M | -T | -A | -S | -B | -G | -P | -X]
  kscli -h | --help
  kscli --version

Options:
  -h, --help               Show this screen.
  --version                Show version.
  --no_verifyssl           Change SSL setting in request package [default: True]
  -m, --movies             Show latest Movie torrents
  -t, --tv                 Show latest TV torrents
  -s, --songs              Show latest Music torrents
  -g, --games              Show lates Game Torrents
  -p, --apps               Show latest Application Torrents
  -b, --books              Show latest Book Torrents
  -x, --naughty            Show latest XXX Torrents
"""

import sys
import requests
import os
from fetcher import get_movies, get_tv, get_new, get_books, get_music, get_naughty, get_apps, get_books, lets_search
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import argparse
from utils import print_version
from fabric.colors import red as red

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def main():
    os.environ['COLUMNS'] = '120'
    parser = argparse.ArgumentParser(description='kscli (KickAss Cli utility)', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    kickass = parser.add_mutually_exclusive_group(required=False)
    kickass.add_argument('-n', '--new', action='store_true', help='Gets the latest torrents from kickasstorrents.to, sorted by seeders')
    kickass.add_argument('-m', '--movies', action='store_true', help='Gets the latest movie from kickasstorrents.to, sorted by seeders')
    kickass.add_argument('-t', '--tv', action='store_true', help='Gets the latest tv show from kickasstorrents.to, sorted by seeders')
    kickass.add_argument('-a', '--apps', action='store_true', help='Gets the latest apps from kickasstorrents.to, sorted by seeders')
    kickass.add_argument('-b', '--books', action='store_true', help='Gets the latest books from kickasstorrents.to, sorted by seeders')
    kickass.add_argument('-x', '--naughty', action='store_true', help='Gets the latest naughty stuff from kickasstorrents.to, sorted by seeders')
    kickass.add_argument('-s', '--music', action='store_true', help='Gets the latest music from kickasstorrents.to, sorted by seeders')
    kickass.add_argument('-S', '--search', action='store', help='Search results from kickasstorrents.to, sorted by seeders')
    kickass.add_argument('-v', '--version', action='store_true', help='Kickass Version')
    sslopts = parser.add_argument_group('SSL verification toggle')
    sslopts.add_argument('--no_verifyssl', action='store_true', default=True, required=False, help='Toggle for SSL verification')
    kickassargs = parser.parse_args()
    ssl = True

    if kickassargs.no_verifyssl:
        ssl = False
    if kickassargs.movies:
        get_movies(ssl)
    elif kickassargs.tv:
        get_tv(ssl)
    elif kickassargs.new:
        get_new(ssl)
    elif kickassargs.apps:
        get_apps(ssl)
    elif kickassargs.books:
        get_books(ssl)
    elif kickassargs.naughty:
        get_naughty(ssl)
    elif kickassargs.music:
        get_music(ssl)
    elif kickassargs.search:
        lets_search(kickassargs.search, ssl)
    elif kickassargs.version:
        print_version()
        pass
    else:
        print(red("You got the wrong option bro..."))
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()