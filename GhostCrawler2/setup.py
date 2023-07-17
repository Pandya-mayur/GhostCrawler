# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='GhostCrawler',
    version="1.0",
    packages=find_packages(),
    author="megadose",
    install_requires=["requests","argparse","termcolor","tqdm", "html5lib","bs4","PySocks"],
    description="OnionSearch is a script that scrapes urls on different .onion search engines.",
    include_package_data=True,
    url='https://github.com/Pandya-mayur/GhostCrawler',
    entry_points = {'console_scripts': ['GhostCrawler2 = GhostCrawler2.core:scrape']},
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
