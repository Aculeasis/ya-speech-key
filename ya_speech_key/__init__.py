# -*- coding: utf-8 -*-

import requests
import time


class APIKey:
    REQUEST_ERRORS = (requests.exceptions.HTTPError, requests.exceptions.RequestException)
    URL = 'https://translate.yandex.ru'
    TARGET = 'SPEECHKIT_KEY:'

    def __init__(self, lifetime=3600):
        self._key = None
        self._lifetime = lifetime
        self._by_expire = 0

    @property
    def key(self):
        if not self._key or self._rotten():
            self._extract()
        return self._key

    def _rotten(self):
        return time.time() > self._by_expire

    def _extract(self):
        try:
            response = requests.get(self.URL)
        except self.REQUEST_ERRORS as e:
            raise RuntimeError(e)
        line = response.text
        end = 0
        result = None
        start = line.find(self.TARGET)
        if start:
            start += len(self.TARGET)
            end = line.find(',', start)
        if start and end and start < end:
            result = line[start:end].strip(' \'')
        if not result:
            raise RuntimeError('API Key not extracted. Yandex change page?')
        self._by_expire = time.time() + self._lifetime
        self._key = result
