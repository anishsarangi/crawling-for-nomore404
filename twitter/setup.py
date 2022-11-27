from setuptools import setup, find_packages

setup(
    name="twitter-archiver",
    version="0.3.7",
    author="Kenji Nagahashi",
    author_email="kenji@archive.org",
    packages=find_packages(),
    install_requires=[
        'gevent',
        #'tornado',
        # tweetstream available on PyPI looks different from what we
        # depend on.
        #'tweetstream==0.2.0',
        'ujson',
        'configobj',
        'oauth2',
        'kafka-python',
        'PyYAML>=5',
        'warctools',
        'twitter-stream.py'
    ],
    scripts=[
        'archivestream.py',
        'kafkastream.py',
        'tweetwarc.py'
        ],
    zip_safe=False
    )

