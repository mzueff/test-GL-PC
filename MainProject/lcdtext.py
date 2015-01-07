#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep


# На входе:
# номер значение
# 1     способ вывода
# 2     длительность вывода
# 3     действие по таймауту
#

# Текст для вывода
text="012345"

# Способ вывода
# 1 В строку 1
# 2 В строку 2
# 3 В строку 1 с прокруткой
# 4 В строку 2 с прокруткой
# 5 В строку 1 по сентру
# 6 В строку 2 по центру
style=6

# Длительность вывода
# 0 постоянно
# 1-10 сек
timeout=0

# Замена после таймаута
# 1 предыдушей строкой 1
# 2 предыдущей строкой 2
# 3 часами
out=3


def out(string):
 import lcddriver
 #lcd = lcddriver.lcd()

 style=int(string[0:1])
 timeout=int(string[1:2])
 out=int(string[2:3])
 text=string[3:]
 print "Style=", style,"Timeout=",timeout,"Out=",out,"Text=",text

 # Пустая строка
 c=0
 space=''
 while c<16:
    space+=' '
    c+=1

 # Вывод
 if style==1 or style==2:
    if style==1:
	num=1
    elif style==2:
	num=2
    string=text+space[:16-len(text)]
    #lcd.lcd_display_string(string, num)


 # Прокрутка
 if style==3 or style==4:
    if style==3:
	num=1
    else:
	num=2
    c=1
    c2=1
    while c<=len(text):
	c1=16-c
	if(c1>=0):    
	    string = space[:c1] + text[:c]
            print string
	else:
	    string = text[c2:16+c2]
	    c2+=1
	c+=1
        print "String=", string
	lcd.lcd_display_string(string, num)
	sleep(0.1)

 # По центру
 if style==5 or style==6:
    if style==5:
	num=1
    else:
	num=2
    start=int(round((16-len(text))/2))
    end=int(round((16-len(text))/2)+len(text))
    string=space[:int(round((16-len(text))/2))]+text+space[end:]
    print string, end, len(string)
    #lcd.lcd_display_string(string, num)

 print "Text=",string,len(string)
 return string,num