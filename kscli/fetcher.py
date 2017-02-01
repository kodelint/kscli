import requests
from bs4 import BeautifulSoup
from fabric.colors import yellow as yellow
from download import download_prep
from utils import pptable, error
import ast
from utils import generate_url


try:
    xrange_ = xrange
except NameError:
    xrange_ = range


def fetch(category, ssl, page, search):
    if search == True:
        url = generate_url(category, page, flag=True)
    else:
        url = generate_url(category, page, flag=False)

    source_code = requests.get(url, verify=ssl)
    plain_text = source_code.text.encode('utf-8')
    soup = BeautifulSoup(plain_text, "lxml")

    torrent_name = []
    torrent_seeds = []
    torrent_size = []
    torrent_leechers = []
    torrent_megent = []
    sno = []

    for i in soup.findAll('table', {'class': 'data'}):
        for j in i('a', {'class': 'cellMainLink'}):
            torrent_name.append(j.get_text())

        for j in i('td', {'class': 'nobr center'}):
            torrent_size.append(j.get_text())

        for j in i('td', {'class': 'green center'}):
            torrent_seeds.append(j.get_text())

        for j in i('td', {'class': 'red lasttd center'}):
            torrent_leechers.append(j.get_text())

        for j in i('div', {'data-sc-paramas': 'magnet'}):
            torrent_megent.append(j.get_text())

        for j in i('div', {'class' : 'none'}):
             k = ast.literal_eval(j.get('data-sc-params'))
             torrent_megent.append(k['magnet'])

        for i in xrange_(8):
            for j in xrange_(25):
                sno.append(j + 1)

    decorative_combine = zip(sno, torrent_name, torrent_size, torrent_seeds, torrent_leechers)
    combine = zip(sno, torrent_name, torrent_size, torrent_seeds, torrent_leechers, torrent_megent)

    return decorative_combine, combine


def get_naughty(ssl, page):
    category = 'xxx'
    pp_torrents, torrents = fetch(category, ssl, page, search=False)
    naughty = []
    for i in xrange_(len(pp_torrents)):
        naughty.append(pp_torrents[i])

    print (yellow('\nLATEST MOVIE TORRENTS\n'))
    pptable(naughty)
    download_prep(torrents)


def get_movies(ssl, page):
    category = 'movies'
    pp_torrents, torrents = fetch(category, ssl, page, search=False)
    movies = []
    for i in xrange_(len(pp_torrents)):
        movies.append(pp_torrents[i])

    print (yellow('\nLATEST MOVIE TORRENTS\n'))
    pptable(movies)
    download_prep(torrents)


def get_new(ssl, page):
    category = 'new'
    pp_torrents, torrents = fetch(category, ssl, page, search=False)
    new = []
    for i in xrange_(len(pp_torrents)):
        new.append(pp_torrents[i])
    print (yellow('\nLATEST TORRENTS\n'))
    pptable(new)
    download_prep(torrents)


def get_tv(ssl, page):
    category = 'tv'
    pp_torrents, torrents = fetch(category, ssl, page, search=False)
    tv = []
    for i in xrange_(len(pp_torrents)):
        tv.append(pp_torrents[i])

    print (yellow('\nLATEST TV TORRENTS\n'))
    pptable(tv)
    download_prep(torrents)


def get_music(ssl, page):
    category = 'music'
    pp_torrents, torrents = fetch(category, ssl, page, search=False)
    music = []
    for i in xrange_(len(pp_torrents)):
        music.append(pp_torrents[i])

    print (yellow('\nLATEST MUSIC TORRENTS\n'))
    pptable(music)
    download_prep(torrents)


def get_apps(ssl, page):
    category = 'applications'
    pp_torrents, torrents = fetch(category, ssl, page, search=False)
    apps = []
    for i in xrange_(len(pp_torrents)):
        apps.append(pp_torrents[i])

    print (yellow('\nLATEST APPLICATION TORRENTS\n'))
    pptable(apps)
    download_prep(torrents)


def get_books(ssl, page):
    category = 'books'
    pp_torrents, torrents = fetch(category, ssl, page, search=False)
    books = []
    for i in xrange_(len(pp_torrents)):
        books.append(pp_torrents[i])

    print (yellow('\nLATEST BOOKS TORRENTS\n'))
    pptable(books)
    download_prep(torrents)


def lets_search(sobj, ssl, page):
    pp_torrents, torrents = fetch(sobj, ssl, page, search=True)
    result = []
    if len(pp_torrents) <= 1:
        result = pp_torrents
    else:
        for i in xrange_(len(pp_torrents)):
            result.append(pp_torrents[i])

    print (yellow('SEARCH RESULT FOR : ') + sobj + '\n')
    pptable(result)
    download_prep(torrents)
