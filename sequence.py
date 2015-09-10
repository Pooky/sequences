#!/usr/bin/env python

import textwrap
import sys

stringToSearch = ""


''' Find sequence '''

def comparePatternAndString(pattern, string):
	
	string = string.lower()
	pattern = pattern.lower()

	#print string + "-----" + pattern

	res = string.find(pattern)
	#print res
	return res	

def appendToFile(string):
	
	string = string.rstrip()

	with open(fileName + ".out", "a") as file:
		file.write(string + "\n")

def fillWithCharacters(number, string):
	
	output = ""
	for i in range(0, number):
		output += "~"
	
	output += string
	
	return textwrap.wrap(output,61)

def processPattern(pattern):
	## goign trought patterns			
	print pattern
	pos = comparePatternAndString(pattern, stringToSearch)
	if pos < 0:
		print "Position not found"
	else:
		print "POSITION: " + str(pos)
		outputForFile = fillWithCharacters(pos, pattern)
		for x in outputForFile:
			appendToFile(x)

def main():
	
	global stringToSearch
	main_sequence = False
	pattern = None
	last_pattern = None
	pattern_sequence = False

	with open(fileName, "r") as file:
		for line in file:
			
			# main sequence
			if ">" in line and "|CDS" in line:
				main_sequence = True
				appendToFile(line)			
			elif ">" in line:
				main_sequence = False
				
				if pattern != None:
					processPattern(pattern)

				pattern = "" # new Pattern
				print "FOUND NEW PATTERN : " + line
				appendToFile(line)
			
			if main_sequence and ">" not in line:
				stringToSearch += line.rstrip()
				appendToFile(line)
			elif ">" not in line:
				pattern += line.rstrip() 	
		# Process last pattern
		if pattern != None:
			processPattern(pattern)

	
			#print line + " ----- " + str(main_sequence)	
	
	
	#print stringToSearch


if len(sys.argv) < 1 :
	print "No input file. EXIT"	
	exit();

fileName = sys.argv[1]

main()

