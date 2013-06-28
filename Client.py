from provapoly import *
import threading
import socket 
import re

addr=""



class Client(threading.Thread):
	def __init__(self,buff = 1024):
		threading.Thread.__init__(self)
		self.buff = buff 
		self=socket.socket()
		self.connect(("127.0.0.1",9999))
		while True:
			if (self.recv(buff))\r:
				print ("Server wrote:"+self.recv(buff))
			else:
				message=raw_input("Client >")
				#add regex
				if  (message.strip() == "exit" or message.strip() == "Exit"):
					self.close()
					quit()
				else:
					self.send(message)
					break


class Client_rec(threading.Thread):
	def __init__(self, s, buff=1024, nickname=""):
		threading.Thread.__init__(self)
		self.buff = buff
		self.s = s
		self.nickname = nickname
	
	def run(self):
		while True:
			message= s.recv(self.buff).strip()
			if (message == "exit"):
				s.close()	
				break
			else:
				print("Server wrote: " + message+ "\r")

	
	def run1(self):
		while True:
			message = raw_input("Client > ")
			s.send(message)


class Client_send(threading.Thread):
	def __init__self(self, s, buff = 1024):
		thread.Thread.__init__(self)
		self.s = s
		self.buff = buff
	
	def run(self):
		message = raw_input("Client > ")
		s.send(message)


		



if __name__ =="__main__":
	s=socket.socket()
	s.connect(("127.0.0.1",9999))
	c=Client_rec(s,1024,"Pippo")
	c.start()
	c.run1()	









