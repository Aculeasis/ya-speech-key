# -*- coding: utf-8 -*-

import requests
import time


class Oops(Exception):
    pass


class APIKey:
    REQUEST_ERRORS = (requests.exceptions.HTTPError, requests.exceptions.RequestException)
    URL = 'https://translate.yandex.com'
    TARGET = 'SPEECHKIT_KEY:'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,ru;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'
    }

    def __init__(self, lifetime=3600, proxies=None):
        self._key = None
        self._lifetime = lifetime
        self._proxies = proxies
        self._by_expire = 0

    @property
    def key(self):
        if not self._key or self._rotten():
            self._get_key()
        return self._key

    def _rotten(self):
        return time.time() > self._by_expire

    def _get_key(self):
        key = self._extract()
        if not key:
            raise RuntimeError('API Key not extracted. Yandex change page?')
        self._by_expire = time.time() + self._lifetime
        self._key = key

    def _extract(self):
        try:
            response = requests.get(self.URL, headers=self.HEADERS, proxies=self._proxies)
        except self.REQUEST_ERRORS as e:
            raise RuntimeError(e)
        line = response.text
        if line.find('<title>Oops!</title>') > -1:
            raise Oops('Yandex blocked automated requests')
        end = 0
        result = None
        start = line.find(self.TARGET)
        if start > -1:
            start += len(self.TARGET)
            end = line.find(',', start)
        if start and end and start < end:
            result = line[start:end].strip(' \'')
        return result
