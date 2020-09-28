#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Ez a script a kovetkezo celbol keszult: 
Amikor valaszok vannak egy tablaban, es azt szeretnénk tudni, hogy:
- egy bizonyos választ ki adott.
- A válaszokon belül is előfordulhatnak vesszők és az egyes kérdések válaszai is vesszővel elválasztottak. 
Tábla előkészítése: 
- Ez a srcipt Ubuntu-n így futtatható: $ python Respfilter_multiple_str_write.py
- Ez a script és az inputként használt file is ugyanabban a mappában legyen.
- A válaszadó neve az utolsó oszlopban legyen. 
Eredmények: 
- A Terminal-os is láthatók
- De különben egy hónap-nap-óra-perc-másodperc nevü .txt file-ba is kiexportálja, abba a könyvtárba, ahol futtatunk.
.csv-re és .txt-re is működik.

"""

from datetime import datetime
nowtime = datetime.now()
timestampStr = nowtime.strftime(' %m-%d-%H-%M-%S')
fname=input ('Enter the file name to search through: ')
try:
	fhand = open(fname)
except:
	print('File cannot be opened:', fname)
	exit()
filternum = input ('How many texts do you want to filter for? ')
try: 
	filternum = int(filternum)
except:
	print ('Please give a number next time!')
	exit()

fout = open(timestampStr, 'w')
fout.write(fname)
fout.write(timestampStr)
while filternum > 0:
#itt jon az a resz, hogy tobb valasz is egyszerre szamlalhato:
#1-tobb szurest lehetne directory-ban is tarolni, ahol key=filter, value=nevek
	filterfor=input ('What should be the text to filter for? ')
	filterforTitle = '\n' + filterfor + ':\n'
	fout.write(filterforTitle)
	namelist_filterfor=[filterfor+':']
#Aposztrófos szöveggel egyelőre elhasal, valami mód kellene annak vizsgálatára
	specchar = filterfor.find('\'')
	if specchar >-1:
		print ('Try a text without aphostrophe!')
		exit()
	print('\nNames fitting the condition from:', fname)
	fhand.seek(0,0)
	for line in fhand:
		line = line.rstrip()
		if 'Please indicate your name' in line: continue 
		#print ('Ezutan valogat a feltetelnek megfelelo sorra')
		if line.find(filterfor) >-1:
			splitted = line.split(',')
			splittedStr = ''.join(map(str, splitted[-1:])) + '\n'
			print(splittedStr)
			fout.write(splittedStr)
			namelist_filterfor.append(splittedStr)
	print (namelist_filterfor)
	filternum = filternum-1
fout.close()