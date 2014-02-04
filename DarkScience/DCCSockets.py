#DCC Jan 2014 Python Sockets
# Kurtisebear

import socket
import sys
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
remote_ip = socket.gethostbyname("directus.darkscience.net")
s.connect((remote_ip, 6789))
message = "GET / HTTP/1.1\r\n\r\n"
s.send(message)
content = ""
while 1:
    buf = s.recv(1000)
    if not buf:
        break
    content+=buf


content = content.split("<p>")[1]
content = re.sub ("[^0123456789x]","",content)
content = content.replace('x', '*')
answer = eval(content)
print answer
clength = str(answer)
clength = len(clength) + 7


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
remote_ip = socket.gethostbyname("directus.darkscience.net")
s.connect((remote_ip, 6789))
message = "POST / HTTP/1.1\r\nContent-Type: application/x-www-form-urlencoded\r\ncontent-length: " + str(clength) + "\r\n" + "answer=" + str(answer) + "\r\n\r\n"
print message

s.send(message)

content1 = ""



print content1
# print "---"
# print content

