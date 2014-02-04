
import whois
import time

with open("domains.txt", 'r') as f:
	for line in f:
		w = whois.whois(line)
		print line
		print w
		print "\n"
		time.sleep(1)


#w = whois.whois('google.com')

#print w 

#FILE = open("domains.txt", 'r')
#for f in FILE:
#	LINE = FILE.readline()
#	print LINE
