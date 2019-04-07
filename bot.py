# -*- coding: utf-8 -*-

import itchat
import os
import requests
import logging
import time
import yaml
import json
import base64
from pydub import AudioSegment
from itchat.content import *

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

config = {}
with open('config.yml', 'r') as f:
    config = yaml.safe_load(f)
if any (key not in config for key in ['host', 'port', 'validate']):
    logging.error("配置文件格式有误，程序将退出！")
    exit(1)
url = '{}:{}/chat'.format(config['host'], config['port'])

def convert_mp3_to_wav(mp3_path):
    """ 
    将 mp3 文件转成 wav

    :param mp3_path: mp3 文件路径
    :returns: wav 文件路径
    """
    target = mp3_path.replace(".mp3", ".wav")
    if not os.path.exists(mp3_path):
        logging.critical("文件错误 {}".format(mp3_path))
        return None
    AudioSegment.from_mp3(mp3_path).export(target, format="wav")
    return target        

@itchat.msg_register([RECORDING])
def download_files(msg):
    if msg.toUserName == 'filehelper':
        logging.info('received voice {}'.format(msg))
        msg.download(msg.fileName)
        wav = convert_mp3_to_wav(msg.fileName)
        with open(wav, 'rb') as f:
            data = base64.b64encode(f.read())
        param = {
            'validate': config['validate'],
            'type': 'voice',
            'voice': data,
            'uuid': str(int(time.time()))
        }
        r = requests.post(url, data=param)
        r.encoding = 'utf-8'
        try:
            resp = r.json()['resp']
            msg.user.send('wukong: %s' % (resp))
        except Exception as e:
            logging.error(e)
        finally:
            if os.path.exists(msg.fileName):
                os.remove(msg.fileName)
            if os.path.exists(wav):
                os.remove(wav)

@itchat.msg_register(TEXT)
def text_reply(msg):
    if msg.toUserName == 'filehelper' and not msg.text.startswith('wukong: '):
        logging.info('received text {}'.format(msg.text))
        param = {
            'validate': config['validate'],
            'type': 'text',
            'query': msg.text,
            'uuid': str(int(time.time()))
        }
        r = requests.post(url, data=param)
        r.encoding = 'utf-8'
        try:
            resp = r.json()['resp']
            msg.user.send('wukong: %s' % (resp))
        except Exception as e:
            logging.error(e)

itchat.auto_login(enableCmdQR=2, hotReload=True)
itchat.run(True)
