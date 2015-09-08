#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" lista degli oggetti definiti:

	- MyProtocol	
"""

""" Esempio di un Protocollo Seriale
/*====================================*/
/*= define PROTOCOL Header           =*/
/*====================================*/
// Preamble + Start + Source Address + Destination Address + Lenght
//
// Pre + Sta + Src + Des + Len
// 1     1     2     2     2  (ascii mode)
// 1     1     1     1     1  (binary mode)
//
// Pre    Preamble      (for rs485)
//        0xff
//
// Sta    Start tx
//        '#'           (ascii mode)
//
// Sto    Stop tx
//        '\n'          (ascii mode)
//
"""

myRev = "(rev.150906)"
#-----------------------------------------------------------------------------
# Modules
#-----------------------------------------------------------------------------
from my00init import *

# importa i moduli in modo dinamico (new style)
from gi.repository import Gtk, Gdk, GLib
from gi.repository import GObject 

#-----------------------------------------------------------------------------
# myModules
#-----------------------------------------------------------------------------
from mySerial import MySerial

#-----------------------------------------------------------------------------
# myDefine
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# myClass
#-----------------------------------------------------------------------------
class MyProtocol(object):
	""" Gestione Protocollo Seriale
		- acqAscii            accumulo dati ascii ricevuti nel buffer 
		- acqBinary           accumulo dati binary ricevuti nel buffer 
		- loop                acquisizione dati dal device
		- sendListCommands    invio lista comandi
		- sendFileCommands    invio file comandi
		- wriTg               stdout compatibile con le Gtk 
		- insLoop             inserimento permanente del loop di ricezione
	"""
	def __init__(self, ser=None, sta='', sto=['\r','\n'], hex=False, cal=None):
		self.sta = sta          # codice di inizio pacchetto
		self.asc = True
#attributi
		self.sto = sto          # stop
		self.ser = ser          # riferimento istanza seriale
		self.cha = ''           # dato ricevuto
		self.buf = []           # buffer di accumulo dati ricevuti
		self.str = ""           # string data
		self.hex = hex          # enable view hex code ascii
		self.hid = False        # enable view not printable
		self.err = True         # error timeOut
		self.loo = True         # loop di attesa
		# self.end = True         # fine loop
		self.brd = True         # display broadcast
		self.dat = None         # data Rx di supporto
		self.cal = cal          # callback 
		self.res = False        # response callback
		self.slp = 0.06         # delay between commands 
#protocol body
		self.cmd = 'R'          # comando da eseguire
		self.tar = 'VE'         # target interessato
		self.dat = []           # dati acquisiti
#protocol system
		self.cou = 0            # counter (caratteri ricevuti)
		self.couHex = 0         # counter (caratteri ricevuti in hex)
		self.lstCmd = []        # list send comand

		# verifica se esiste l'istanza del device seriale
		if self.ser.ser:
			pass
		else:    
			# simula 2 metodi per virtualizzare una seriale    
			def sndString(str):
				print str
			self.ser.sndString = sndString
			def rcvChar():
				return None
			self.ser.rcvChar = rcvChar

	def acqAscii(self, data):
		""" accumulo dati ascii ricevuti nel buffer """
		if self.hex:
			self.couHex += 1
			self.cha = "%02x," %ord(data)
			self.buf.append(self.cha)
			# split line
			if self.couHex % 32 == 0:
				self.buf.append('\n')
		else:
			if not data in printable:
				# rendo visibile il codice
				if data == '\n':
					self.cha = data
					if self.hid:
						self.cha += '\\n'
				elif data == '\r':
					self.cha = data
					if self.hid:
						self.cha += '\\r'
				elif self.hid:
					self.cha = '.'
				# accumlo dato Rx
				self.buf.append(self.cha)
			else:
				# accumlo dato Rx
				self.buf.append(data)

	def acqBinary(self, data):
		""" accumulo i dati binari ricevuti nel buffer """
		self.couHex += 1
		# rendo visibile il codice
		self.cha = "%02x," %ord(data)
		self.buf.append(self.cha)
		if self.couHex % 32 == 0:
			self.buf.append('\n')

	def loop(self):
		""" acquisizione dati dal device """
		if self.ser:
			# acquisizione dati
			buff = self.ser.rcvByte()
			if not buff:
				self.dat = None
				sleep(0.001)
			else:
				for data in buff:
					self.dat = data
					self.cou += 1
					# start
					if data == self.sta:
						self.cou = 0
						self.buf = []
					else:
				#ascii terminal
						if self.asc:
							# accumula dati solo printabili nel buffer
							self.acqAscii(data)
				#binary terminal
						else:
							# accumula dati binari nel buffer
							self.acqBinary(data)

					# parser
					if data in self.sto:

					# forzo il parser continuo per avere una risposta 
					#  in tempo reale nella visualizzazione della GUI futura.
					# if 1: 
						# chiamo la callback (il paser)
						if self.cal:
							self.res = self.cal("".join(self.buf))
						# end process
						self.buf = []
						self.cou = 0
						break
		# continua Idle
		return True

	def sendListCommands(self, data, log=1):
		""" send Commands
		"""
		for cmnd in data:
			if self.asc:
				# print "ascii"
				cmd = self.sta + cmnd + self.sto[0]
			else:
				# print "binary"
				cmd = cmnd
			# send comand
			self.ser.sndString(cmd)
			# update comand send
			self.lstCmd.append(cmd[:-1])
			if log:
				# view comand in log
				self.wriTg(cmd,"greWhi")
			sleep(self.slp)
	
	def sendFileCommands(self, name, loop=None):
		""" send file Commands
		"""
		# lettura file
		for ele in (line.rsplit(None,0) for line in open(name)):
			# verifico che non sia una lista vuota
			if ele:
				# invio comando
				self.sendCommands(ele)
			if loop:
				loop()

	def insLoop(self):
		""" attivazione permanente del loop di ricezione
		"""
		# referenzio il metodo che inserisco nel loop di Idle
		self.idPro = GObject.idle_add(self.loop)

	# simula la textView    
	def wriTg(self, msg, tag):
		print tag, msg,
	
#-----------------------------------------------------------------------------
# myTry
#-----------------------------------------------------------------------------
def myTry01(deb=1):

	# inizializzazione in base al S.O.
	if sys.platform == 'win32':
		# Windows (numerazione parte da 1)
		por = "COM"
		par = ['1','115200','8','N','1']
	else:
		# Unix  (numerazione parte da 0)	
		#por = "/dev/ttyS"
		#por = "/dev/ttymxc"
		por = "/dev/ttyUSB"
		par = ['0','115200','8','N','1']

	# definisco il parser
	def myParser(*args):		
		print 'parser:', args
		# mantiene il loop attivo (esce solo per timeOut!)
		return True

	#  istanza di un seriale
	dev = MySerial(por=por, par=par, ope=1, deb=deb)
	if dev.ser:
		print "device Ok"
		self = MyProtocol(ser=dev, sta='*', sto=['\r','\n'], hex=0, cal=None)
		# attivo il parser
		self.cal = myParser
		return self
	else:
		print "device Ko"
		sys.exit()

#-----------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
if __name__ == "__main__":

	# test arguments
	if len(sys.argv) == 1:
		# no arguments (scelgo io)
		choi = 1
	else:
		# get first argument (scelta esterna)
		choi = int(sys.argv[1])

	if choi == 1:
		# test: istanza un device
		self = myTry01(1)
		# invio un comando
		self.sendListCommands(["cmd_1",])

		# tou, cal, *args
		print "time: %f" %myTimeOut(0.01, self.loop)
