from os import access
import socket
pl="ip adresleri: "
bl="açık portlar: "
file=open("ip.txt","r")
ips=file.read()
file.close()
for ip in ips.splitlines():
    print(ip)
    for port in range(1,25):
        try:
            soket=socket.socket()
            soket.connect((str(ip),int(port)))
            banner=soket.recv(1024)
            bl.append(banner)
            pl.append(str(port))
            soket.close()
            print(port)
            print(banner)
            if "SSH" in str(banner):
                print("sistem linux veya başka bir cihaz olabilir")
                log=str(ip)+"\n"
                dosya=open("linux.txt","a")
                dosya.write(log)
                dosya.close()
        except:
            pass
print(pl)
print(bl)
