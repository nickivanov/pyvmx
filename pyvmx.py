#!/usr/bin/python
"""
pyvmx.py -- A Python 2.6 script to automatically edit VMWare .vmx files. 

Copyright 2013 Nick Ivanov

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import print_function

# python stuff
import os
import sys
import getopt
import shutil


USAGE="""

This is %s

Python 2.6 script to automatically edit VMWare .vmx files. 

Usage:

	%s [options] <input_file> [<edit_file>]
	
Both <input_file> and <edit_file> contain the key/value pairs in the format
compatible with the shell variable declaration:

	key = "value"
	
If a key from <edit_file> is found in <input_file>, its value is updated with
the one from <edit_file>. If the key is not found in <input_file>, the pair is
appended at the end. The order of lines in <input_file> is otherwise preserved.
If <edit_file> is not present, the entries are read from the standard input.
	
Options:

	-b, --backup	
		
		Create a backup file before overwriting <input_file>. The backup file 
		name is derived from <input_file> by adding a "~".
		
	-o <filename>, --output	<filename> 
	
		Instead of updating <input_file>, write the merged entries to <filename>
		
	-h, --help
	
		Show this help.
	 

""" % (__file__,__file__)

"""
Read a VMX file or STDIN; store key/value pairs in a dict.
Keep a separate list of keys to preserve their order
"""

def read_vmx(filename):
	#vmxdict = OrderedDict()
	# would have used OrderedDict if I had Python 2.7...
	# so I'll have to do with a list of keys and a dict
	lkeys = [] # this is to preserve the key order
	dpairs = dict()
	if filename == '':
		fvmx = sys.stdin
	else:
		fvmx = open(filename)
		
	try:
		with fvmx:
			for line in fvmx.readlines():
				if line.startswith('#'): # it's a comment
					key = line.rstrip() # trim the new line character
					val = ''
				else:
					pair = line.split('=',1) 	# split just once, in case there are equal signs in the value
					key = pair[0].strip()
					val = pair[1].strip().strip('"') 	# value surrounded by double quotes; keep leading/trailing spaces within the value
					
				lkeys.append(key)
				dpairs[key] = val
				
	except IOError as e:
		print ("I/O error %d while reading %s: %s" % (e.errno,  filename, e.strerror))
	except :
		print ("Unexpected error reading %s: %s"%(filename,sys.exc_info()[0]))
		exit(-100)
	 
		
	else:   
		return (lkeys,dpairs)
		
	finally:
		fvmx.close()

"""
Write key/value pairs to a file
"""
def print_vmx(lkeys, dpairs, ofile):
	try:
		with open(ofile, 'w') as fvmx:
			for k in lkeys:
				if k.startswith('#'): # comment
					fvmx.write (k+'\n')
				else:
					fvmx.write ('%s = "%s"\n'%(k,dpairs[k]))
	except IOError as e:
		print ("I/O error %d while writing %s: %s" % (e.errno,  ofile, e.strerror))	
	finally:
		fvmx.close()			

""" 
    Merge dnewpairs into dpairs. New keys from dnewpairs will be added at the
    end of lkeys and returned -- to keep the line order intact
"""

def merge_vmx(lkeys, dpairs, lnewkeys, dnewpairs):
	for newkey in lnewkeys: # should keep the order
		if not newkey in dpairs: # append new key
			lkeys.append(newkey)
		dpairs[newkey] = dnewpairs[newkey]
			
	return (lkeys, dpairs)

""" Main program """

if __name__ != '__main__':
	print("Don't import me -- I'm not what you think I am!")
	exit()

   
# check arguments

infile = ''
editfile = ''
do_backup=False

try:
	(opts,trail) = getopt.getopt(sys.argv[1:], "hbo:",["help","backup","output="])
except getopt.GetoptError:
	print("\nInvalid arguments\n\n" + USAGE)
	exit(-1)
	
if len(trail) < 1: # must have the input file
	print("\nMissing arguments\n\n" + USAGE)
	exit(-1)
	
infile=trail[0] # must be the first non-option argument
if infile == '' or not os.path.isfile(infile): # bail out early
	print ("Cannot find file '%s'; exiting"%infile)
	exit()

if len(trail) > 1 and trail[1] != '': # input new entries from file
	editfile = trail[1]
	if not os.path.isfile(editfile): 
		print ("Cannot find file '%s'; exiting"%editfile)
		exit()

outfile = infile
for (opt,arg) in opts:
	if opt in ('-h', '--help'):
		print (USAGE)
		exit()
	elif opt in ('-b', '--backup'): 
		do_backup = True
	elif opt in ('-o', '--output'):
		outfile = arg
			
# if the output file is the same as input and backup is requested, do it
if outfile==infile and do_backup:
	try:
		shutil.copyfile(infile,infile+"~")
		print ("Backup file created: %s"%(infile+"~"))
	except IOError as e:
		print ("I/O error %d while backing up %s: %s" % (e.errno,  infile, e.strerror))
		exit(-1)
elif outfile!=infile and do_backup: # does not make sense; issue warning
	print ("Output file is different from input file; what do you need the backup for?")
		
			
(lkeys,dpairs) = read_vmx(infile)
(lnewkeys,dnewpairs) = read_vmx(editfile) # will fall back to stdin if file is not specified

(lkeys,dpairs) = merge_vmx(lkeys, dpairs, lnewkeys, dnewpairs)

print_vmx(lkeys,dpairs, outfile)

print ("Wrote %s"%outfile)

