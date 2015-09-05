
#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" lista degli oggetti definiti:

	- 150529 init
"""
myRev = "(rev.150529)"

#-----------------------------------------------------------------------------
# Modules
#-----------------------------------------------------------------------------
# import cairo
# import math

#-----------------------------------------------------------------------------
# myModules
#-----------------------------------------------------------------------------
from my00init import *

# structures C
from ctypes import *
#-----------------------------------------------------------------------------
# myDefines
#-----------------------------------------------------------------------------
# comunication
from mySerial import MySerial
from myProtocol import MyProtocol, myParser

#-----------------------------------------------------------------------------
class MyParser:

	def __init__(self, interface="usb0"):
		self.data = None
		self.flgTx = False

	def parser(self, *args):
		"parsing"
		# print "args:", args

		self.data = args[0][:]

		# ite = args[0].split(',')
		# if ite:
		# 	if ite[0] == "":
		# 		pass 
		# 	else:
		# 		dat = ite[0].split()
		# 		# for debug 
		# 		print "NoPars:", dat
		# 		self.data = dat

				# # 3, 4, 6, 8,9,...
				# if dat[0][:3] == "CAN":
				# 	if dat[1] == "->":
				# 		self.flgTx = True
				# 	else:
				# 		self.flgTx = False
				# 	self.frame.can_id = atoi(dat[3], 16)
				# 	if dat[4] == "X":
				# 		self.frame.can_id |= 0x80000000
				# 	self.frame.can_dlc = atoi(dat[6], 16)
				# 	for x in xrange(self.frame.can_dlc):
				# 		self.frame.data[x] = atoi(dat[8+x], 16)

				# else:
				# 	self.frame.can_dlc = 0
				# 	print "NoPars:", ite
		return True

#-----------------------------------------------------------------------------
# myClass
#-----------------------------------------------------------------------------
class MyDevice:

	def __init__(self, interface="0", port="/dev/ttyACM", baud='115200'):

		# Serial
		# por = "/dev/ttyACM"
		# por = "/dev/ttyUSB"
		por = port
		cha = interface
		# port, baudrate, bytesize, parity, stopbits, timeout, xonxoff, rtscts, dsrdtr
		cfg = [cha, baud, '8', 'N', '1', None, False, False, False]
		# fil="init.pkl", par=None, ope=True, deb=False
		obj = MySerial(por=por, par=cfg, deb=0)
		self.mySer = obj	# => self.prot.ser
		if self.mySer.ser:
			print "device present!"
		# Protocol
			# ser=None, sta='', sto=['\r','\n'],hex=False, buf=None, wri=None, cal=None
			prot = MyProtocol(ser=obj, sta='', sto=['',])
			self.prot = prot
		#Parsing    
			# myPars = myParser(self.prot)
			# self.prot.calBk1 = myPars
			# cambio la lista di loopback del device
			self.myPars = MyParser()
			self.prot.calBk1 = self.myPars.parser
			# attivo protocollo sul loop principale
			# self.prot.insLoop()

			# check Open
			if self.mySer.ope:
				print "device Ok"
			else:
				print "device not open!"

		
	def read(self):
		"""
		Low-level function
		"""	
		data = None		
		if self.mySer.ser:
			# acquire serial data
			self.prot.loop()
			data = self.myPars.data
		return data

	def write(self, data):
		"""
		Low-level function
		"""
		if self.mySer.ser:
			# send data
			self.send(data)

	def send(self, data):
		# print len(data_str)
		# send value (aggiunge un LF)
		self.prot.sendListCommands([data,], log=0)

#-----------------------------------------------------------------------------
# Main
#-----------------------------------------------------------------------------
if __name__ == "__main__":

	choi = 1

	if choi == 1:
		# istanza del bus
		usb0 = MyDevice("0", "/dev/ttyUSB")
