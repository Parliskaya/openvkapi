# openvkapi

![](https://komarev.com/ghpvc/?username=Parliskaya)   
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
