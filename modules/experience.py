#!/usr/bin/env python3
import os
import yaml
import voice
import webbrowser
from telnetlib import Telnet
import subprocess

def switch(group):
    if group == "wintele":
        return [{
		'user': 'TrialRooT',
        'password':'GrinWin2021'
		}]
    elif group == "golden":
        return [{
		'user': 'grin',
        'password':'grin!1306!'
		}]
    elif group == "golden_server":
        return [{
		'user': 'grin',
        'password':'fuckgolden1306!'
		}]    
   



def load_file(filename):
    with open(filename, encoding='utf-8') as f: 
        file = yaml.safe_load(f) 
        return file

def ssh_connect(*query):
		print('Enter your host: ')
		host = input()
		os.system(f'ssh -i id_rsa grin@{host}')

def ssh2_connect(*query):
    test = load_file('configs/device_list.yaml')
    key1 = ''.join(query).split()[1]
    key2 = [x for x in test]

    if key1 not in  key2:
        voice.speaker('айпи нету в базе')
    else:	
        ip = test[key1][0]['ip']
        name = test[key1][1]['name']
        group = test[key1][2]['group']
        print(name)
        try:
            for sw in switch(group):
                login = sw['user']
                os.system(f'.\\applications\MXterm.exe -newtab "ssh -l {login} {ip}"')
        except:
            voice.speaker('айпи не доступен')
            pass
		


def show_list_device(*query):
    test = load_file('configs/device_list.yaml')
    for t in test:
        print(f'ключ: {t}\n значение: {test[t]}')



def telnet_connect(*query, **kargs):
    test = load_file('configs/device_list.yaml')
    key1 = ''.join(query).split()[1]
    key2 = [x for x in test]

    if key1 not in  key2:
        voice.speaker('айпи нету в базе')
    else:	
        ip = test[key1][0]['ip']
        name = test[key1][1]['name']
        group = test[key1][2]['group']
        print(name)
        try:
            
            with Telnet(ip, 23) as tn:
                tn.write(switch(group)['user'].encode('ascii') + b"\n")
                tn.write(switch(group)['password'].encode('ascii') + b"\n")
                tn.interact()
        except:
            voice.speaker('айпи не доступен')
            pass
            		


def browser(*query):
	query = ' '.join(query)
	webbrowser.open(f'http://www.google.com/search?q={query}')

def passive(*query):
		'''Функция заглушка при простом диалоге с ботом'''
		pass        
	