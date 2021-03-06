# -*- coding: utf-8 -*-
from util.hook import cmd
import time
import os
import requests

home_path =  '/home/pi'

# TODO 相対path
kyoshitsu_path = home_path + 'music/kyoshitsu.mp3'

# TODO not exist
coffee_host = os.getenv('COFFEE_HOST')

@cmd('coffee_run')
def coffee_run(bot):
    try:
        bot.say('おいしいコーヒーを入れますね')
        time.sleep(4)
        requests.get(coffee_host + '/coffee/0')
        time.sleep(5)
        play_music(kyoshitsu_path)
    except requests.exceptions.ConnectionError:
        bot.say('働きたくないでござる')

@cmd("coffee_stop")
def coffee_stop(bot):
    try:
        requests.get(coffee_host + '/coffee/1')
        bot.say('コーヒーをちゅうだんしました')
    except requests.exceptions.ConnectionError:
        bot.say('働きたくないでござる')

def play_music(bot, path):
    bot.stop_say()
    print(" ".join(['mplayer', '-volume', '100', path]))
    time.sleep(1)
    subprocess.Popen(['mplayer', '-volume', '100', path])
