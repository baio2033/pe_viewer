import sys, os
from struct import *
import pefile

def usage():
	print("[+] Usage\n")
	print("python", sys.argv[0], "<PE File>")

def menu(peFile): 
	print '###############################################'                                      
	print ('''

  ____  _____         _                        
 |  _ \| ____| __   _(_) _____      _____ _ __ 
 | |_) |  _|   \ \ / / |/ _ \ \ /\ / / _ \ '__|
 |  __/| |___   \ V /| |  __/\ V  V /  __/ |   
 |_|   |_____|   \_/ |_|\___| \_/\_/ \___|_|   
                                               
''')
	print '###############################################\n'

	print "1) DOS HEADER Info"
	print "2) NT HEADER Info"
	print "3) FILE HEADER Info"
	print "4) OPTIONAL HEADER Info"
	print "5) SECTION HEADER Info"
	print "6) dump result to file"
	print "7) exit"

	s = int(raw_input('\nselect job > '))

	if s == 1:
		view_dos_header(peFile)
	elif s == 2:
		view_nt_header(peFile)
	elif s == 3:
		view_file_header(peFile)
	elif s == 4:
		view_optional_header(peFile)
	elif s== 5:
		view_section_header(peFile)
	elif s == 6:
		dump(peFile)
	elif s == 7:
		sys.exit()

def view_dos_header(peFile):
	dos_h = peFile.DOS_HEADER
	print "\n"
	print(dos_h)
	print "\n"

def view_nt_header(peFile):
	nt_h = peFile.NT_HEADERS
	print "\n"
	print(nt_h)
	print "\n"

def view_file_header(peFile):
	file_h = peFile.FILE_HEADER
	print "\n"
	print(file_h)
	print "\n"

def view_optional_header(peFile):
	option_h = peFile.OPTIONAL_HEADER
	print "\n"
	print(option_h)
	print "\n"

def view_section_header(peFile):
	for section in peFile.sections:
		print "\n"
		print(section)
	print "\n"

def dump(peFile):
	dump = peFile.dump_info()
	output = open("dump.txt", "w")
	output.write(str(dump))
	output.close()

	print "\n[+] dump file created!\n"
	print "[+] Path : " + os.getcwd() + "/dump.txt\n\n"

if __name__ == "__main__":
	if len(sys.argv) < 2:
		usage()
		sys.exit()

	fileName = sys.argv[1]
	peFile = pefile.PE(fileName)

	while True:		
		menu(peFile)