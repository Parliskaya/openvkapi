# openvkapi

![](https://komarev.com/ghpvc/?username=Parliskaya)
<a href='https://pypi.org/project/openvk/'>
    <img src='https://img.shields.io/pypi/v/openvk.svg' alt='Documentation Status' />
</a>  
A modern, easy to use API wrapper for OpenVK written in Python.

## Installing

```
pip install openvk==0.0.8
```


## Quick Example
```python
from openvk import openvkapi
from openvk import messages


client = openvkapi.auth('youre@gmail.com', 'password')
messages.send(client['token'], user_id, 'Hello world!')
```

## Links
[Documentation](https://github.com/Parliskaya/openvkapi/wiki/openvkapi-Documentation)  
[Author to OpenVK](https://openvk.su/parlis)
