#!/usr/bin/env python3 
import yaml
TRIGGERS = {'TRIGGERS': ['лиса','алиса','иса','алис','alice']}  
data_set = {
'TRIGGERS': ['лиса','алиса','иса','алис','alice'],   
'открой сервер': ['ssh_connect коннекчусь к железке'],
'запусти сервак': ['ssh_connect введи домен и мы на месте'],
'запусти браузер': ['browser запускаю браузер'],
'открой браузер': ['browser интернет активирован'],
'интернет открой': ['browser открываю браузер'],
'посмотреть фильм': ['browser сейчас открою браузер'],
'расскажи анекдот':['passive Вчера помыл окна, теперь у меня рассвет на два часа раньше...'],
'работаешь':['passive как видишь'],
}

with open('configs/triggers.yaml', 'w', encoding='utf-8') as fout: 
    yaml.dump(TRIGGERS, fout, indent=4, default_flow_style=False, allow_unicode=True) 

with open('configs/triggers.yaml', encoding='utf-8') as fin: 
    load_file = yaml.safe_load(fin) 

print(load_file)
