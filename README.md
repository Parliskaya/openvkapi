# openvkapi

![](https://komarev.com/ghpvc/?username=Parliskaya)
<a href='https://pypi.org/project/openvk/'>
    <img src='https://img.shields.io/pypi/v/openvk.svg' alt='Documentation Status' />
</a>  
A modern, easy to use API wrapper for OpenVK written in Python.

## Installing

```
pip install openvk==1.5
```


## Quick Example
```python
from openvk import openvkapi
from openvk import messages


client = openvkapi.auth('youre@gmail.com', 'password')
user_id = 1010
messages.send(client, user_id, 'Hello world!')
```

## Links
[Documentation](https://github.com/Parliskaya/openvkapi/wiki/openvkapi-Documentation)  
[Telegram chat](https://t.me/ovkapi)   
[Author in OpenVK](https://openvk.su/ucinka)  
[LeenzeryDev](https://github.com/leenzerydev)   
[LuneeDev](https://github.com/luneedev)   
[.NET version](https://github.com/LyStudios/OpenVkNetApi)  
