from setuptools import setup
setup(name='kscli',
      packages=['kscli'],
      version='0.1.0',
      description='Download torrents from kickasstorrents.to directly through terminal',
      author='Satyajit Roy',
      license='MIT',
      author_email='kodelint@gmail.com',
      url='http://github.com/kodelint/kscli',
      download_url = 'http://github.com/alyakhtar/mypackage/tarball/1.1.5',
      entry_points='''
               [console_scripts]
               katastrophe=kscli:main
           ''',
      install_requires=[
          'beautifulsoup4','tabulate','requests','lxml','argparse','bencode','bitstring','fabric','ConfigParser'
      ],
      keywords=['torrent', 'download', 'kickasstorrents.to'], )
