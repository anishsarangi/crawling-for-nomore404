from setuptools import setup, find_packages

setup(
    name="twitter-archiver",
    version="0.3.6",
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
        'oauth2-utf8==1.5.170',
        'kafka-python',
        'PyYAML',
        'warctools',
        ],
    scripts=[
        'archivestream.py',
        'kafkastream.py',
        'tweetwarc.py'
        ],
    zip_safe=False
    )

