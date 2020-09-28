#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
#Here comes the section to allow multiple string to be filtered for.
#Apart of the solution below a suggestion for more "Pythongic" way: using dictionary, where key=strings to filter for, and value=names fits for the filter
	filterfor=input ('What should be the text to filter for? ')
	filterforTitle = '\n' + filterfor + ':\n'
	fout.write(filterforTitle)
	namelist_filterfor=[filterfor+':']
#String to be filtered for with apostrophy fails. Solution should be below
#just toe below: other special characters should be allowed. 
	specchar = filterfor.find('\'')
	if specchar >-1:
		print ('Try a text without aphostrophe!')
		exit()
	print('\nNames fitting the condition from:', fname)
	fhand.seek(0,0)
	for line in fhand:
		line = line.rstrip()
		if 'Please indicate your name' in line: continue 
		#print ('This is the point where it starts to pharse for each line')
		if line.find(filterfor) >-1:
			splitted = line.split(',')
			splittedStr = ''.join(map(str, splitted[-1:])) + '\n'
			print(splittedStr)
			fout.write(splittedStr)
			namelist_filterfor.append(splittedStr)
	print (namelist_filterfor)
	filternum = filternum-1
fout.close()
