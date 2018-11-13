### Extracts Yandex Speech API key from translate page
[![PyPI version](https://img.shields.io/pypi/v/ya-speech-key.svg)](https://pypi.org/project/ya-speech-key)
[![Python versions](https://img.shields.io/badge/python-2.7%20|%203.4%2B-blue.svg)](https://github.com/Aculeasis/ya-speech-key)
[![Build Status](https://travis-ci.org/Aculeasis/ya-speech-key.svg?branch=master)](https://travis-ci.org/Aculeasis/ya-speech-key)

This API key can be used for Yandex SpeechKit Cloud API. No guarantees, Yandex can break it at any time.

### Install
`pip install ya-speech-key`

### Usage
```python
from ya_speech_key import APIKey

key = APIKey()
print(key.key)
```

`lifetime` set key update interval in seconds. Default `3600`.

`proxies` sets proxies in [requests format](http://docs.python-requests.org/en/master/user/advanced/#proxies). Default `None`.

```python
key = APIKey(lifetime=3600, proxies=None)
```
