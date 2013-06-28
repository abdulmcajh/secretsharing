from provapoly import *
import threading
import socket
import re
import time


addr=""
sharers=[]

class Dealer_rec(threading.Thread):
	def __init__(self,socket,buff=1024,nickname=None):
		threading.Thread.__init__(self)
		self.socket = socket
		self.buff = buff
		self.nickname = nickname
	def run(self):
		global addr
		
		while True:
			message = str(self.socket.recv(self.buff).strip())
			if message is None:
				break
			elif message == "1":
				sharers.append(addr)
				self.socket.send("I'll send you the share soon \r")
				print(sharers)
			elif (message.strip()=="exit" or message.strip()=="Exit"):
				self.socket.close()
				exit()
			print("Received"+"    "+message+"from"+" "+str(addr[0])+","+str(addr[1])+"\r")


class Dealer_send(threading.Thread):
	def __init__(self,socket,buff=1024):
		threading.Thread.__init__(self)
		self.socket=socket
		self.buff = buff
	
	
	def run(self):
		number=0
		u=True
		self.socket.send("Type 1 if you want to share a secret with me \n")
		while True:
			message=raw_input("Server >")
			if message.strip() == "exit":
				self.socket.close()
				quit()
			self.socket.send(message+"\n")
		




def startdealer():
	while True:
		a=[]
		global addr
		s=socket.socket()
		s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		s.bind(("192.168.100.63",9999))
		s.listen(100)
		con,addr = s.accept()
		a.append(addr)
		print("Connection from {0}".format(addr))
		print(a)
		dealer = Dealer_rec(con, 3000, "Dealer")
		dealer1 = Dealer_send(con,3000)
		dealer.start()
		dealer1.start()



if __name__ =="__main__":
	startdealer()









