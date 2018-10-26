# cording: utf-8


import pygame.mixer
import time
import sys
import glob
from random import shuffle

mplist = glob.glob("soundfile/*.mp3")
print(mplist)

pygame.mixer.init()
#pygame.mixer.music.load("soundfile/roll-finish1.mp3")

pastime = time.time()
print(pastime)


itr = 0

while True:
	try:
		pygame.mixer.music.load(mplist[itr%2])
		pygame.mixer.music.play(1)
		time.sleep(5)
		pygame.mixer.music.stop()
		itr = itr + 1
	except KeyboardInterrupt:
		sys.exit(0)

sys.exit()
