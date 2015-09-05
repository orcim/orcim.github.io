#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" lista degli oggetti definiti:

	- myApp

"""
from my00init import *

myRev = "(rev.150529)"
#-----------------------------------------------------------------------------
# Modules
#-----------------------------------------------------------------------------
# import cairo
# import math

#-----------------------------------------------------------------------------
# myModules
#-----------------------------------------------------------------------------
# structures C
from ctypes import *
from myApp import MyWind
#-----------------------------------------------------------------------------
# myDefines
#-----------------------------------------------------------------------------
# comunication
# from mySerial import MySerial
# from myProtocol import MyProtocol, myParser
# canBus
from myDevice import MyDevice

#-----------------------------------------------------------------------------
def myNone(*args):
	pass

#-----------------------------------------------------------------------------
# myClass
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# myTry
#-----------------------------------------------------------------------------
def myTry01(por="0", dev="/dev/ttyUSB", baud='115200'):
	""" receiver & transmission
	"""

	from my01Box import myFrame
	from my02TxtView import myScrTexVieFrame    
	from my02Entry import myEntFrame, myEntList
	from my02Label import myLabFrame
	from my03Button import myButton, myButFrame
	from my03ChkButton import myChkButton
#myFraScrTexView
	#          0,   1,   2,   3,   4,    5,    6,       7 
	# fram,[labe,xBox,buff,text,cTag,clear,write,writeTag]
	fram,othe = myScrTexVieFrame(name='logBuffer', colo="black",
								widt=400, heig=400, 
								font="courier 9", edit=False, 
								left=1, righ=1, bord=3,
								bFra=1, sFra=Gtk.SHADOW_ETCHED_OUT, tFra='v' )
	# insert object in apllication
	self.vBox.pack_start(fram, False, False, 1)
	
	# referenzio gli attributi
	self.cTag = othe[4]
	# referenzio i metodi
	self.clear = othe[5]
	self.write = othe[6] # *msg
	self.wriTg = othe[7] # str="", tag="blaWhi"
	
	# redirect sul proprio buffer text
	sys.stdout = self

##############################################################################
#myFrame (Rx Buffer)
	# fram,[labe,xBox]
	obje, othe = myFrame(name='Rx buffer', obje=None, colo='black',
						bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
						tBox='h', aBox=[False, False, 10])
	# referenzio l'oggetto
	self.boxBuf = othe[1]
	# change background color to Class
	chaBackColor(obj=obje, css="boxBuf", col="#a0a0a0")

	# insert object in application
	self.vBox.pack_start(obje, False, False, 1)

#myChkButton (enable Rx)
	# ridefinisco la callback        
	def on_clicked(widg, name, *data):
		pass
	# butt, call
	obje, othe = myChkButton(name='Ena', 
							valu=True, colo='black', 
							call= on_clicked, data=['-',])
	# referenzio l'oggetto
	self.chkEna = obje
	# fram,[labe,xBox]
	obj1, oth1 = myFrame(name='Rx', obje=obje, colo='black',
						 bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
						 tBox='h' )
	# insert object in application
	self.boxBuf.pack_start(obj1, False, False, 1)

#myLabFrame (counter Rx data)
	#fram, [labe, lFrm, xBox]
	obje, othe = myLabFrame(name='0', 
							leng=len('0')+1, prea=' ', post='', 
							font='Arial 10', 
							colo='blue',
							nFra='Rx.data', cFra='black', bFra=1, sFra=Gtk.SHADOW_ETCHED_OUT, 
							tFra='h', aFra=[False, False, 1])
	# referenzio l'oggetto
	self.labRcv = othe[0]
	# insert object in application
	self.boxBuf.pack_start(obje, False, False, 1)

#myButton (clear buffer)
	# ridefinisco la callback        
	def on_clicked(widg, *data):
		self.clear()
		# frame ricevuti
		self.couRcv = 0
		self.couSnd = 0
		self.labRcv.set_text(" %d" %self.couRcv)
		self.labSnd.set_text(" %d" %self.couSnd)
	# fram, [labe, xBox, butt, call]
	obje, othe = myButFrame(name="buffer", 
							icon=Gtk.STOCK_OK, 
							call=on_clicked, data=[],
							bFra=1, sFra=Gtk.SHADOW_ETCHED_OUT, 
							tFra='v', aFra=[False, False, 1])
	# imposto la label
	othe[2].props.label = "clear"    
	# insert object in application
	self.boxBuf.pack_start(obje, False, False, 1)

#myChkButton (view Hid)
	# ridefinisco la callback        
	def on_clicked(widg, name, *data):
		if widg.get_active():
			self.dev0.prot.hid = 1
		else:
			self.dev0.prot.hid = 0
	# butt, call
	obje, othe = myChkButton(name='view', 
							valu=0, colo='black', 
							call= on_clicked, data=['-',])
	# referenzio l'oggetto
	self.chkHid = obje
	# fram,[labe,xBox]
	obj1, oth1 = myFrame(name='Hide', obje=obje, colo='black',
						 bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
						 tBox='h' )
	# insert object in application
	self.boxBuf.pack_start(obj1, False, False, 1)

#myChkButton (view Hex)
	# ridefinisco la callback        
	def on_clicked(widg, name, *data):
		if widg.get_active():
			self.dev0.prot.hex = 1
		else:
			self.dev0.prot.hex = 0
	# butt, call
	obje, othe = myChkButton(name='view', 
							valu=0, colo='black', 
							call= on_clicked, data=['-',])
	# referenzio l'oggetto
	self.chkHex = obje
	# fram,[labe,xBox]
	obj1, oth1 = myFrame(name='Hex', obje=obje, colo='black',
						 bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
						 tBox='h' )
	# insert object in application
	self.boxBuf.pack_start(obj1, False, False, 1)

##############################################################################
#myFrame (Tx Commands)
	# fram,[labe,xBox]
	obje, othe = myFrame(name='Tx commands', obje=None, colo='black',
						bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
						tBox='h', aBox=[False, False, 10])
	# referenzio l'oggetto
	self.boxCmd = othe[1]
	# change background color to Class
	chaBackColor(obj=obje, css="boxCmd", col="#a0a0a0")
	
	# insert object in application
	self.vBox.pack_start(obje, False, False, 1)

#myChkButton (tx)
	# ridefinisco la callback        
	def on_clicked(widg, name, *data):
		pass
	# butt, call
	obje, othe = myChkButton(name='Ena', 
							valu=True, colo='black', 
							call= on_clicked, data=['-',])
	# referenzio l'oggetto
	self.chkTx = obje
	# fram,[labe,xBox]
	obj1, oth1 = myFrame(name='Tx', obje=obje, colo='black',
						 bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
						 tBox='h' )
	# insert object in application
	self.boxCmd.pack_start(obj1, False, False, 1)

#myLabFrame (counter Tx data)
	#fram, [labe, lFrm, xBox]
	obje, othe = myLabFrame(name='0', 
							leng=len('0')+1, prea=' ', post='', 
							font='Arial 10', 
							colo='blue',
							nFra='Tx.data', cFra='black', bFra=1, sFra=Gtk.SHADOW_ETCHED_OUT, 
							tFra='h', aFra=[False, False, 1])
	# referenzio l'oggetto
	self.labSnd = othe[0]
	# insert object in application
	self.boxCmd.pack_start(obje, False, False, 1)

	self.cmdDev = None
#myButton (send file)
	# ridefinisco la callback        
	def on_clicked(widg, *data):
		self.cmdDev = stpFile("data/"+self.entCmdSerial.get_text())
		# print self.cmdDev.nam, self.cmdDev.dly, self.cmdDev.hnd

		# read first line
		val = self.cmdDev.next()
		if val != False:
			val = stpCnv(val)
			# send first line
			# self.dev0.prot.sendListCommands([val,], log=0)
			self.bufDev = val[:]

			# background work
			GObject.idle_add(stpCmd, self.cmdDev, self.dev0)

	# fram, [labe, xBox, butt, call]
	obje, othe = myButFrame(name="file.tx", 
							icon=Gtk.STOCK_OK, 
							call=on_clicked, data=[],
							bFra=1, sFra=Gtk.SHADOW_ETCHED_OUT, 
							tFra='v', aFra=[False, False, 1])
	# imposto la label
	othe[2].props.label = "send"    
	# insert object in application
	self.boxCmd.pack_start(obje, False, False, 1)

#myEntFrame (cmd Serial)
	# ridefinisco la callback        
	def on_activate(widg, *data):
		data_str = widg.get_text()
		# Binary
		if self.chkBin.get_active():
			if len(data_str) % 2 != 0:
				print "Entry format: ff0091"
				data_str = ""
			else:
				# split string to substring with lenght = 2 
				data = [data_str[i:i+2] for i in range(0, len(data_str), 2)]
				# print data
				data_str = []
				for ele in data:
					data_str.append("%c" %atoi(ele,16))
		# Ascii
		else:
			# CR	
			if self.chkCR.get_active():
				data_str += '\r'
			# LF
			if self.chkLF.get_active():
				data_str += '\n'
			# convert to list
			data_str = [data_str,]

		# send data
		if data_str:
			# print data_str
			# self.dev0.prot.sendListCommands(data_str, log=0)
			self.bufDev = data_str[:]

	#fram, [labe, xBoxcmdB, entr, call]        
	obje, othe = myEntFrame(name='', 
							numb=29,
							call=on_activate, data=[],
							nFra='cmd.Serial', bFra=1, sFra=Gtk.SHADOW_ETCHED_OUT, 
							tFra='h', aFra=[False, False, 1])
	# referenzio l'oggetto
	self.entCmdSerial = othe[2]
	# insert object in application
	self.boxCmd.pack_start(obje, False, False, 1)

#myChkButton (enable CR)
	# ridefinisco la callback        
	def on_clicked(widg, name, *data):
		pass
	# butt, call
	obje, othe = myChkButton(name='Ena', 
							valu=1, colo='black', 
							call= on_clicked, data=['-',])
	# referenzio l'oggetto
	self.chkCR = obje
	# fram,[labe,xBox]
	obj1, oth1 = myFrame(name='CR', obje=obje, colo='black',
						 bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
						 tBox='h' )
	# insert object in application
	self.boxCmd.pack_start(obj1, False, False, 1)

#myChkButton (enable LF)
	# ridefinisco la callback        
	def on_clicked(widg, name, *data):
		pass
	# butt, call
	obje, othe = myChkButton(name='Ena', 
							valu=1, colo='black', 
							call= on_clicked, data=['-',])
	# referenzio l'oggetto
	self.chkLF = obje
	# fram,[labe,xBox]
	obj1, oth1 = myFrame(name='LF', obje=obje, colo='black',
						 bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
						 tBox='h' )
	# insert object in application
	self.boxCmd.pack_start(obj1, False, False, 1)

#myChkButton (enable Binary)
	# ridefinisco la callback        
	def on_clicked(widg, name, *data):
		self.dev0.prot.asc = not widg.get_active()
		# print self.dev0.prot.asc
	# butt, call
	obje, othe = myChkButton(name='Ena', 
							valu=0, colo='black', 
							call= on_clicked, data=['-',])
	# referenzio l'oggetto
	self.chkBin = obje
	# fram,[labe,xBox]
	obj1, oth1 = myFrame(name='Bin', obje=obje, colo='black',
						 bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
						 tBox='h' )
	# insert object in application
	self.boxCmd.pack_start(obj1, False, False, 1)

#myChkButton (enable Debug)
	# ridefinisco la callback        
	def on_clicked(widg, name, *data):
		self.dev0.mySer.deb = widg.get_active()
	# butt, call
	obje, othe = myChkButton(name='Ena', 
							valu=0, colo='black', 
							call= on_clicked, data=['-',])
	# referenzio l'oggetto
	self.chkDeb = obje
	# fram,[labe,xBox]
	obj1, oth1 = myFrame(name='Deb', obje=obje, colo='black',
						 bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
						 tBox='h' )
	# insert object in application
	self.boxCmd.pack_start(obj1, False, False, 1)

#myChkButton (enable RTS)
	# ridefinisco la callback        
	def on_clicked(widg, name, *data):
		if widg.get_active():
			self.dev0.mySer.ser.setRTS(1)
		else:
			self.dev0.mySer.ser.setRTS(0)
	# butt, call
	obje, othe = myChkButton(name='On', 
							valu=1, colo='black', 
							call= on_clicked, data=['-',])
	# referenzio l'oggetto
	self.chkRts = obje
	# fram,[labe,xBox]
	obj1, oth1 = myFrame(name='Rts', obje=obje, colo='black',
						 bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
						 tBox='h' )
	# insert object in application
	self.boxCmd.pack_start(obj1, False, False, 1)

#myChkButton (enable DTR)
	# ridefinisco la callback        
	def on_clicked(widg, name, *data):
		if widg.get_active():
			self.dev0.mySer.ser.setDTR(1)
		else:
			self.dev0.mySer.ser.setDTR(0)
	# butt, call
	obje, othe = myChkButton(name='On', 
							valu=1, colo='black', 
							call= on_clicked, data=['-',])
	# referenzio l'oggetto
	self.chkDtr = obje
	# fram,[labe,xBox]
	obj1, oth1 = myFrame(name='Dtr', obje=obje, colo='black',
						 bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
						 tBox='h' )
	# insert object in application
	self.boxCmd.pack_start(obj1, False, False, 1)

##############################################################################
# Device

	# istanza del bus
	# self.dev0 = MyDevice("0", "/dev/ttyACM", baud='115200')
	self.dev0 = MyDevice(por, dev, baud)
	if not self.dev0.mySer.ser:
		printD("device not present!")
	else:
		# re-imposta il titolo dell'applicazione
		self.set_title(self.title + " %s" %self.dev0.mySer.por)
		print self.dev0.mySer.par

	self.dev0.couErr = 0

	self.debLog = 1
	self.bufDev = 0
	self.couRcv = 0
	self.couSnd = 0
	self.couFil = 0
	self.namFil = ""
	self.start = time()
	def devRx(self):
		if self.chkEna.get_active():
			# ricevo dati
			try:
				# lettura dati
				data = self.dev0.read()
				if data:
					# aggiorno bytes ricevuti
					self.couRcv += len(data)
					self.labRcv.set_text(" %d" %self.couRcv)
					# # stampa i dati
					# if self.dev0.myPars.flgTx:
					# 	print "->", data
					# else:
					# 	print "<-", data

					# print data,
					self.write(data)
					# clear data rx
					self.dev0.myPars.data = None

			except Exception,err:
				if "DEV read error" in err:
					pass
				else:
					self.dev0.couErr += 1
					print "err:", self.dev0.couErr, err
		sleep(0.001)
		# rimane attivo
		return True

	# referenzio il metodo che inserisco nel loop di Idle
	self.rxDev = GObject.idle_add(devRx, self)

	def devTx(self):
		# invio dati
		try:
			# send parameters
			if self.bufDev:

				# print data_str
				self.dev0.prot.sendListCommands(self.bufDev, log=0)
				self.bufDev = []

				self.couSnd +=1
				self.labSnd.set_text(" %d" %self.couSnd)
				# delay richiesta ritardata
				#GLib.timeout_add(300, reqPar, self)
			else:
				pass

		except:
			if self.debLog:
				print("MyDevice write Frame error")

		# visualizzo tempo trascorso
		# print "tim:%s" %(time() - self.start)

		sleep(0.001)
		# rimane attivo
		return True

	# referenzio il metodo che inserisco nel loop di Idle
	self.txDev = GObject.idle_add(devTx, self)

#-----------------------------------------------------------------------------
# myGenerators
#-----------------------------------------------------------------------------
def stpFile(nam="data/cmdCanBus.cmd"):
	"send file one by one line"
	self.namFil = nam
	try:
		hnd = file(self.namFil,"r")
		for ele in hnd:
			yield ele
	except:
		print "file not found!"
		yield False

#-----------------------------------------------------------------------------
def stpCmd(obj=None, dev=None):
	"send next line"
	try:
		while 1:
			val = obj.next()
			# print val,

			# convert value
			val = stpCnv(val)
			# dev.prot.sendListCommands([val,], log=0)
			self.bufDev = val[:]
			return True
	# evita l'eccezzione
	except StopIteration:
		return False

#-----------------------------------------------------------------------------
def stpCnv(val=None):
	"convert value"
	if self.namFil[-4:] == ".bin":
		# remove CR,LF
		val = val.strip('\r\n')
		# check format
		if len(val) % 2 != 0:
			print "Entry format: ff0091"
			val = ""
		else:
			# split string to substring with lenght = 2 
			data = [val[i:i+2] for i in range(0, len(val), 2)]
			# print data
			val = []
			for ele in data:
				val.append("%c" %atoi(ele,16))
			val = "".join(val)
	return [val,]

#-----------------------------------------------------------------------------
# Main
#-----------------------------------------------------------------------------
if __name__ == "__main__":

	choi = 0

	if choi == 0:
		# istanza l'applicazione principale
		self = MyWind(width=800, height=500, title="myTerminal %s" %myRev, center=True, color="#b0b0b0")
		# rx & tx isobus
		myTry01(por="0", dev="/dev/ttyUSB", baud='115200')
		# avvia applicazione
		Gtk.main()
	elif choi == 1:
		# istanza l'applicazione principale
		self = MyWind(width=800, height=500, title="myTerminal %s" %myRev, center=True, color="#b0b0b0")
		# rx & tx isobus
		myTry01(por="1", dev="/dev/ttyUSB", baud='115200')
		# avvia applicazione
		Gtk.main()
