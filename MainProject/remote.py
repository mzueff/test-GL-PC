#!/usr/bin/python
# -*- coding: utf-8 -*-

# Config
# key_func=i2c_code,Lirc_key_name_by_Lir.conf
#
#
#

debug=0

# адрес микросхемы расширителя портов
extaddr=0x20

# Порт GPIO где слушаем прерывание
PIN_INT=25

# Возвращает при всех отпущенных кнопках
key_return=0xff

#

# имя секции описывающей пульт в lircd.conf
section='JVC'

#кнопки с фиксацией
mute=0xbf,'KEY_MUTE'

# Кнопки без фиксации (имя=адрес,имя в Lircd.conf,время удержания в 1/10 сек)
volup=0xdf,'KEY_VOLUMEUP',10
voldown=0xef,'KEY_VOLUMEDOWN',0
chup=0xf7,'KEY_UP',0
chdown=0xfb,'KEY_DOWN',0
ptt=0x7f,'PTT',0
# import libraries
import smbus as smbus
import RPIO
from time import *
import sys
import lcddriver
import string
import os
import socket
import mpd


sock = socket.socket()

#from subprocess import Popen, PIPE

#configure I2C bus for functions
i2c = smbus.SMBus(1)

# Инициируем LCD
lcd = lcddriver.lcd()
lcd.lcd_display_string('  Media System  ', 1)
lcd.lcd_display_string('     Started    ', 2)


# MPD
client = mpd.MPDClient()
client.connect("localhost", 6600) # подключаемся к серверу



# Remote Section

# Настраиваем порт на прием прерываний
RPIO.setup(PIN_INT, RPIO.IN, pull_up_down=RPIO.PUD_DOWN)

def vol_chg(key):
	    #lcd.lcd_clear()
	    c=0
	    if key == 'volup':
		fst_str="   Volume  UP   "
		mot=" Volume +"
		key_addr=volup[0]
		pause=volup[2]
	    if key == 'voldown':
		fst_str="  Volume  DOWN  "
		mot=" Volume -"
		key_addr=voldown[0]
		pause=voldown[2]
	    if key == 'chup':
		fst_str="   Channel UP   "
		mot=" Ch +"
		key_addr=chup[0]
		pause=chup[2]
	    if key == 'chdown':
		fst_str="  Channel DOWN  "
		mot=" Ch -"
		key_addr=chdown[0]
		pause=chdown[2]
	    
	    if key == 'ptt':
		fst_str=" Intercom Trnsm "
		mot=" Int PTT"
		key_addr=ptt[0]
		pause=ptt[2]
	    
	    lcd.lcd_display_string(fst_str, 1)
	    lcd.lcd_display_string('                ', 2)

# Отрабатывается по приходу прерывания
def gpio_callback(gpio_id, val):
    #Читаем адрес нажатой кнопки
    try:
       key_addr = i2c.read_byte( extaddr )
       if (debug == 1):
	   print gpio_id, val, 'READ! At address 0x{0:2x} READ 0x{1:2x}'.format( extaddr, key_addr )
    except IOError :
       if (debug == 1):
           print 'PCF8574 Device not found at I2C address 0x{1:2x}'.format( extaddr, key_addr )
           error = 1


    if key_addr != key_return:
        # Обрабатываем одиночные нажатые кнопки
	if key_addr == volup[0]:
	    c=0
	    state=i2c.read_byte( extaddr )
	    while state == volup[0]:
		state=i2c.read_byte( extaddr )
		vol_chg('volup')
		print val, c, "Volume UP"
		c+=1
		sleep(0.2)
	elif key_addr == voldown[0]:
	    c=0
	    state=i2c.read_byte( extaddr )
	    while state == voldown[0]:
		state=i2c.read_byte( extaddr )
		vol_chg('voldown')
		print val, c, "Volume DOWN"
		c+=1
		sleep(0.2)
	elif key_addr == chup[0]:
	    if val != 1:
		vol_chg('chup')
		print val, "Channel UP"
	    else:
		print val
	elif key_addr == chdown[0]:
	    vol_chg('chdown')
	    print val, "Channel DOWN"
	elif key_addr == ptt[0]:
	    vol_chg('ptt')
	    print val, "Intercom Trans"

	elif key_addr == mute[0]:
	    print "Mute"
	    #lcd.lcd_display_string("Tun: Select Src", 1)
	    #lcd.lcd_display_string("CH: Change Fold", 2)

# Обрабатываем комбинации нажатых кнопок

	if key_addr == (mute[0] & volup[0]):
	    s=client.status()
	    if s['state'] != 'play':
		print "STATUS Stop"
		#if s['playlistlength']==0:
		client.clear()
		client.load('radio')
		print "Load default playlist: Radio"
		client.play()
	    else:
		client.next()
	    sleep(0.2)
	    s=client.currentsong()
	    if 'name' in s:
		print s['name']
		fst=s['name']
	    else:
		print 'none'
		fst='                '
	    if 'title' in s:
		print s['title']
		snd=s['title']
	    else:
		print 'none'
		snd='                '
	    lcd.lcd_display_string(fst, 1)
	    lcd.lcd_display_string(snd, 2)

#	    if station == '':
#		os.system("mpc play")
	#    for i in range(len(station)):
	#        print station[i]
	#        stat+=station[i]
	#    stat='303'+stat
	#    sock.connect(('localhost', 9090))
	#    sock.send('303'+stat)
	#    sock.close()
	elif key_addr == (mute[0] & voldown[0]) and val == 0:
	    s=client.status()
	    if s['state'] != 'play':
		print "STATUS Stop",s['playlistlength']
		#if s['playlistlength'] < 1:
		print "Load default playlist: Radio"
		client.clear()
		client.load('radio')
		client.play()
	    else:
		client.previous()
	    sleep(0.2)
	    s=client.currentsong()
	    if 'name' in s:
		print s['name']
		fst=s['name']
	    else:
		print 'none'
		fst='                '
	    if 'title' in s:
		print s['title']
		snd=s['title']
	    else:
		print 'none'
		snd='                '
	    lcd.lcd_display_string(fst, 1)
	    lcd.lcd_display_string(snd, 2)
	    #stat='303'+stat
	    #sock.connect(('localhost', 9090))
	    #stat='303'+stat
	    #sock.send(stat)
	    #sock.close()
    else:
	if (debug == 1):
	    print 'All Keys released. READ ', key_addr
	
	lcd.lcd_display_string("TUN: Volume Chg", 1)
	lcd.lcd_display_string("CH: Track Selec", 2)
    
#    sleep(0.22)

# Вызов обработчика прерываний
#RPIO.add_interrupt_callback(PIN_INT, gpio_callback, pull_up_down=RPIO.PUD_UP, threaded_callback=True, debounce_timeout_ms=100)
RPIO.add_interrupt_callback(PIN_INT, gpio_callback, pull_up_down=RPIO.PUD_UP, threaded_callback=False, debounce_timeout_ms=50)

# Ждем прихода прерывания
RPIO.wait_for_interrupts()
