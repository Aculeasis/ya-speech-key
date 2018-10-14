# -*- coding: utf-8 -*-

import requests
import time
import random


class APIKey:
    REQUEST_ERRORS = (requests.exceptions.HTTPError, requests.exceptions.RequestException)
    URLS = [
        'translate.yandex.ru', 'translate.yandex.ua', 'translate.yandex.by',
        'translate.yandex.kz', 'ceviri.yandex.com.tr', 'translate.yandex.com'
            ]
    TARGET = 'SPEECHKIT_KEY:'

    def __init__(self, lifetime=3600):
        self._key = None
        self._lifetime = lifetime
        self._by_expire = 0

    @property
    def key(self):
        if not self._key or self._rotten():
            self._get_key()
        return self._key

    def _rotten(self):
        return time.time() > self._by_expire

    def _get_key(self):
        key = None
        for target in self.URLS:
            key = self._extract('https://{}'.format(target))
            if not key:
                time.sleep(random.random())
            else:
                break
        if not key:
            raise RuntimeError('API Key not extracted. Yandex change page?')
        self._by_expire = time.time() + self._lifetime
        self._key = key

    def _extract(self, url):
        try:
            response = requests.get(url)
        except self.REQUEST_ERRORS as e:
            raise RuntimeError(e)
        line = response.text
        end = 0
        result = None
        start = line.find(self.TARGET)
        if start > -1:
            start += len(self.TARGET)
            end = line.find(',', start)
        if start and end and start < end:
            result = line[start:end].strip(' \'')
        return result
