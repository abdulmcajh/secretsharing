from provapoly import *
from DH import *
import threading
import socket 
import re



dh_object_client=DiffieHellman()
addr=""
server_pubk=0
common_key=0

class Client(threading.Thread):
	def __init__(self,buff = 3000):
		threading.Thread.__init__(self)
		self.buff = buff 
		self=socket.socket()
		self.connect(("127.0.0.1",9999))
		while True:
			if (self.recv(buff)):
				print ("Server wrote:"+self.recv(buff))
			else:
				message=raw_input("Client >")
				if  (message.strip() == "exit" or message.strip() == "Exit"):
					self.close()
					quit()
				else:
					self.send(message)
					break


class Client_rec(threading.Thread):
	def __init__(self, s, buff=3000, nickname=""):
		threading.Thread.__init__(self)
		self.buff = buff
		self.s = s
		self.nickname = nickname
	
	def run(self):
		global server_pubk
		global common_key
		global dh_object_client		
		a=0
		while True:
			message = s.recv(self.buff).strip()
			if ("Server pubk:" in message):
				a=long(message.strip("Server pubk:")[0:])
				print "SERVER PUB KEY IN CLIENT RUN REC"+str(a)
				common_key=dh_object_client.genKey(a)
				print hexlify(dh_object_client.key)
			if (message == "exit" or message == "Exit"):
				s.close()	
				quit()
				break
			else:
				print("Server wrote: " + message+ "\r")

	
	def run1(self):
		global dh_object_client
		global common_key
		s.send("Client pubk:"+str(dh_object_client.publicKey))
		print "CLIENT PUB KEY IN CLIENT RUN SEND "+str(dh_object_client.publicKey)
		while True:
			message = raw_input("Client > ")
			s.send(message)


class Client_send(threading.Thread):
	def __init__self(self, s, buff = 3000):
		thread.Thread.__init__(self)
		self.s = s
		self.buff = buff
	
	def run(self):
		message = raw_input("Client > ")
		s.send(message)


		



if __name__ =="__main__":
#	print dh_object_client.publicKey
#	dh_object_client.genKey(server_pubk)
	#dh_object_client.getKey()
	#print "Client pub key" + str(dh_object_client.publicKey)
	#print "Shared key" + str(DH.dh_object_client.getKey())
	#print(dh_object_client.genSecret(long(server_pubk)))
	s=socket.socket()
	s.connect(("127.0.0.1",9999))
	c=Client_rec(s,3000,"Pippo")
	c.start()
	c.run1()
	
	









