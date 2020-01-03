import telepot
import time
from telepot.loop import MessageLoop
import requests
from time import gmtime, strftime
from datetime import datetime
import os


def handle(msg):
        chat_id = msg['chat']['id']
        command = msg['text']

        print ('Received:')
        print(command)

        if command == '/lampe3':
                #making ip request to your interruptor
                requests.get('http://the_local_ip_of_your_tasmota/cm?cmnd=Power%20TOGGLE')
                bot.sendMessage(chat_id, str("la lampe du salon a bien change d'etat"))
                
        if command == '/date':
                #just for fun, it's to test if the raspberry is not shut down
                temps = strftime("%d-%m-%Y %H:%M:%S")
                bot.sendMessage(chat_id, str(temps))
                
        if command == '/photo':
                #ask for making a photo, then saving it in '/home/pi/photo/' and its name is the date and the hour of when it's has been taken
                hour = strftime("%d-%m-%Y_%H.%M.%S")
                os.system('fswebcam -r 1280x720 -S 3 --jpeg 50 --save /home/pi/photo/img_{}.jpg'.format(hour))
                bot.sendPhoto(chat_id, photo=open('/home/pi/photo/img_{}.jpg'.format(hour), 'rb'))
                bot.sendMessage(chat_id, str('Date : {}'.format(hour)))
                
        if command == '/bonjour':
                #same as '/date', it's a test sentence
                bot.sendMessage(chat_id, str("Salut gros"))
                
        if command == '/video5':
                #taking a video of 5 seconds
                #-t = combien de temps de video, en seconde
                hour = strftime("%d-%m-%Y_%H.%M.%S")
                os.system('avconv -t 5 -f video4linux2 -r 30 -s 1280x720 -i /dev/video0 /home/pi/videos/video_{}.avi'.format(hour))
                bot.sendVideo(chat_id, video=open('/home/pi/videos/video_{}.avi'.format(hour)))
                bot.sendMessage(chat_id, str('Date : {}'.format(hour)))
                
        if command == '/video60':
                #video of 60 seconds
                hour = strftime("%d-%m-%Y_%H.%M.%S")
                os.system('avconv -t 60 -f video4linux2 -r 30 -s 1280x720 -i /dev/video0 /home/pi/videos/video_{}.avi'.format(hour))
                bot.sendVideo(chat_id, video=open('/home/pi/videos/video_{}.avi'.format(hour)))
                bot.sendMessage(chat_id, str('Date : {}'.format(hour)))
                
        if command == '/video5min':
                #5minutes
                hour = strftime("%d-%m-%Y_%H.%M.%S")
                os.system('avconv -t 300 -f video4linux2 -r 30 -s 1280x720 -i /dev/video0 /home/pi/videos/video_{}.avi'.format(hour))
                bot.sendVideo(chat_id, video=open('/home/pi/videos/video_{}.avi'.format(hour)))
                bot.sendMessage(chat_id, str('Date : {}'.format(hour)))


bot = telepot.Bot('YOUR TOKEN')
print(bot.getMe())

while 1:
        time.sleep(10)

