# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as fh:
    long_description = fh.read()

with open('version') as fh:
    version = fh.read().splitlines()[0]

setup(
    name='ya-speech-key',
    version=version,
    packages=['ya_speech_key'],
    url='https://github.com/Aculeasis/ya-speech-key',
    license='MIT',
    author='Aculeasis',
    author_email='amilpalimov2@ya.ru',
    description='Extracts Yandex Speech API key from translate page',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=["requests"],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
        'Topic :: Software Development :: Libraries',
    ],
)
