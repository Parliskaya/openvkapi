# openvkapi

![](https://komarev.com/ghpvc/?username=Parliskaya)
<a href='https://openvkapi.readthedocs.io/ru/latest/?badge=latest'>
    <img src='https://readthedocs.org/projects/openvkapi/badge/?version=latest' alt='Documentation Status' />
</a>
<a href='https://pypi.org/project/openvk/'>
    <img src='https://img.shields.io/pypi/v/openvk.svg' alt='Documentation Status' />
</a>  
A modern, easy to use API wrapper for OpenVK written in Python.

## Installing

```python
pip install openvk
```


## Quick Example
```python
from openvk import openvkapi
from openvk import messages


client = openvkapi.auth('youre@gmail.com', 'password')
messages.send(client, user_id, 'Hello world!')
```

## Links
[Documentation](http://openvkapi.readthedocs.io/)  
[Author to OpenVK](https://openvk.su/parlis)
