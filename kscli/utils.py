from fabric.colors import red, yellow, green
from tabulate import tabulate
import os

def print_version():
    from ConfigParser import ConfigParser
    BASE_PATH = os.path.dirname(os.path.realpath(__file__))
    CONFIG_FILE = os.path.join(BASE_PATH, '..', 'setup.cfg')
    config = ConfigParser()
    config.read(CONFIG_FILE)
    version = config.get("bumpversion", "current_version")
    print version

def info(msg):
    """
    :param: message i.e. any message
    :return: message with color
    """
    header = green('Info:: ')
    print(header + yellow(msg))


def error(msg):
    """
    :param: message i.e. any message
    :return: message with color
    """
    header = red('Error:: ')
    print(header + yellow(msg))


def pptable(resultset):
    """
    :param::dump: Get all the data
    :return::prints: Prints the data tablulate manaer
    """
    if not resultset:
        error('ResultSet Nothing Found !!!')
        exit()
    else:
        headers = [green('INDEX'), green('NAME'), green('SIZE'), green('SEEDS'), green('LEECHERS'), green('MEGNET')]
        print(tabulate(dump, headers, tablefmt='psql', numalign="center"))


def which(program):
    """
    :param: program: i.e. docker, python etc
    :return: fullpath:  full path for the given binary
    """
    import os

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


def generate_url(obj, page, flag):
    """
    :param:: obj: search object
    :parama:: flag: True or False
    :parama:: page: Page no.
    :return:: url:  Generate the URL
    """
    if page is not None:
        if flag:
            link = 'https://kickasstorrents.to/usearch/' + obj + '/' + str(page) + '/'
        elif flag is False and obj == 'new':
            link = 'https://kickasstorrents.to/' + obj + '/' + str(page) + '/'
        else:
            link = 'https://kickasstorrents.to/' + obj + '/' + str(page) + '/'
    else:
        if flag:
            link = 'https://kickasstorrents.to/usearch/' + obj + '/'
        elif flag is False and obj == 'new':
            link = 'https://kickasstorrents.to/' + obj + '/'
        else:
            link = 'https://kickasstorrents.to/' + obj + '/'

    return link
