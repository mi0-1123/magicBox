# -*- coding: utf-8 -*-

import pygame.mixer
import serial
import time
import sys
import glob
import random

BLUETOOTH = '/dev/ttyAMA0'
#BLUETOOTH = '/dev/ttyS0'
RATE = 9600


if __name__ == '__main__':

	myserial = serial.Serial(BLUETOOTH, RATE, timeout=1)	
	mplist = glob.glob("soundfile/comp/*.mp3")
	rollist = glob.glob("soundfile/roll/*.mp3")
	pygame.mixer.init()
#	print mplist.__class__.__name__
	num = len(mplist)
	rollen = len(rollist)
#	print "listlen",num
	count = 0
	flg=False

	while True:
#		time.sleep(0.5)
		try:
			print "count",count
			count += 1
#			itr = random.choice(range(num))
#			myserial.write( "0,1,1,9")

			strmsg=myserial.readline()
			print "get",strmsg
#			print "strmsg class is ",strmsg.__class__.__name__
			if len(strmsg) is not 0:
				vallist = strmsg.split(",")
				vallistint=[]
				for i in vallist:
					tmp1 = i.replace('\n','')
					tmp2 = tmp1.replace('\r','')
					vallistint.append(int(tmp2))
				
				print "castint",vallistint

#				if  vallistint[1] and vallistint[2]:
				if  vallistint[2]:
					if	not pygame.mixer.music.get_busy():
							th = random.choice(range(rollen))
							pygame.mixer.music.load(rollist[th])
							pygame.mixer.music.play()
							flg = True
							itr = random.choice(range(num))
				if flg and vallistint[3] > -43:
					pygame.mixer.music.load(mplist[itr])
					pygame.mixer.music.play()
					flg = False

		except KeyboardInterrupt:
			sys.exit(0)
