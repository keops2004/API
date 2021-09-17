#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 14:30:33 2021

@author: nabucodonosor
"""
import requests
import json
		


datos = {'placa': 'MJWLBQY',
    'fecha': '2021-08-17 15:00:51	0.0',
    'posicion': 'P1C2D1',
    'tipo': 'automovil',
    'match': 0
}
path = 'http://127.0.0.1:5000/api/v1.0/placa/'


resp = requests.post(path, json=datos)
print(resp.text)

KEY = '123447a47f563e90fe2db0f56b1b17be62378e31b7cfd3adc776c59ca4c75e2fc512c15f69bb38307d11d5d17a41a7936789'
USER = '2gbnhf5'
headers = {'x-access-token': KEY,'x-access-user':USER}
resp = requests.get(path, headers = headers)
print(resp.text)

resp = requests.get(path)
print(resp.text)


black = {'placanegra': 'AD125LK',
    'fechanegra': '2021-08-14 12:09:22',
    'status': 'Infraccion'
}
black_path = 'http://127.0.0.1:5000/api/v1.0/black'

resp_black = requests.post(black_path,  headers = headers,json=black)
print(resp_black)
print(resp_black.text)

resp = requests.get(black_path)
print(resp.text)

path = 'http://127.0.0.1:5000/api/v1.0/user/'
datos = {'usuario': 'YO',
             'key': 'jnsdds63'
}
resp = requests.post(path, json=datos)
print(resp.text)

resp = requests.get(path)
print(resp.text)











