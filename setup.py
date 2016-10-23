from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='xianc',
    version='0.1.1',

    description='A set of crawlers for Xian',
    long_description=long_description,


    url='https://github.com/Kuba77/Xian-C',

    author='Jakub Chronowski',
    author_email='jakub@chronow.ski',

    license='MIT',


    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: XIAN Collaborators',
        'Topic :: Software Development :: Database',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7'
    ],

    keywords='xian crawler',
    packages=['xianc', 'xianc.wikitravel', 'xianc.wikitravel.spiders'],

    install_requires=[
        'pyasn1==0.1.9',
        'Scrapy==1.2.0',
        'redis==2.10.5',
        'rq==0.6.0',
        'rq-scheduler==0.7.0',
        'xiandb'
    ],
    dependency_links=[
        'https://github.com/Kuba77/Xian-DB/tarball/master#egg=xiandb'
    ]
)
