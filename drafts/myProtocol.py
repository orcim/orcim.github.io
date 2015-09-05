#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
	- myParser
	- MyProtocol
	
	120316 in assenza di seriale la virtualizza con l'istruzione 'print'
	140310 passaggio port
	150529 default ['\r','\n']
	150529 ricezione binaria
"""
myRev = "(rev.150529)"

""" Protocollo Seriale
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

#-----------------------------------------------------------------------------
# myModules
#-----------------------------------------------------------------------------
from my00initProt import *

from mySerial import MySerial
#-----------------------------------------------------------------------------
# myDefine
#-----------------------------------------------------------------------------
def myParser(self, parsResp=[]):
#    # lista dei parametri da controllare
#    self.parsResp = parsResp
	
	# prototipo scansione stringhe da controllare 
	def pars00(data):
		""" parsing con stringa completa
		"""
		# lista dei parametri da controllare
		for ele in parsResp:
			if data == ele[1]:
				# qui bisognerebbe chiamare la callback dei dati parsati ele[1]
				# interrompe il ciclo perche' l'ha parsato!
				return True

	# lista dei loopback da eseguire
#    self.pars = [pars00,]
	self.pars = []
	
	def myParser0(*args):
		data = args[0]
		# print data received
		self.wriTg(data+'\n',"bluWhi")
		# scan di tutti i parsing da eseguire
		for par in self.pars:
			res = par(data)
			# interrompe il ciclo perche' l'ha trovato!
			if res:
				return True
		# False interrompe il ciclo di loop
		return False
	return myParser0
	
#-----------------------------------------------------------------------------
# myClass
#-----------------------------------------------------------------------------
class MyProtocol(GObject.GObject):
#-----------------------------------------------------------------------------
	""" Gestione Protocollo Seriale
		- acqAscii            accumulo dati ascii ricevuti nel buffer 
		- acqBinary           accumulo dati binary ricevuti nel buffer 
		- loop                acquisizione dati dal device
		- sendListCommands    invio lista comandi
		- sendFileCommands    invio file comandi
		- wriTg               stdout compatibile con le Gtk 
		- chkDevice           controllo comunicazione col device
		- insLoop             inserimento permanente del loop di ricezione
	"""
	def __init__(self, ser=None, sta='', sto=['\r','\n'],
				 hex=False, buf=None, wri=None, cal=None):
		self.sta = sta          # codice di inizio pacchetto
		self.asc = True
#attributi
		self.sto = sto          # stop
		self.ser = ser          # riferimento della connessione seriale
		self.cha = ''           # dato ricevuto
		self.buf = []           # buffer di accumulo dati
		self.str = ""           # string data
		self.hex = hex          # enable view hex code ascii
		self.hid = False        # enable view not printable
		self.err = True         # error timeOut
		self.loo = True         # loop di attesa
		self.brd = True         # display broadcast
		self.datRx = None       # data Rx
		self.calBk1 = cal       # callback 
		self.res = False        # response callback
		self.kSleep = 0.06      # delay between commands 
#protocol body
		self.cmd = 'R'          # comando da eseguire
		self.tar = 'VE'         # target interessato
		self.dat = []           # dati acquisiti
#protocol system
		self.coun = 0           # counter (caratteri ricevuti)
		self.couHex = 0         # counter (caratteri ricevuti in hex)
		self.lstCmd = []        # list send comand

		if self.ser.ser:
			pass
		else:    
			# simula il seriale    
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
				self.buf.append(self.cha)
			else:
				self.buf.append(data)

	def acqBinary(self, data):
		""" accumulo dati binary ricevuti nel buffer """
		self.couHex += 1
		# rendo visibile il codice
		self.cha = "%02x," %ord(data)
		# self.buf.append(data)
		self.buf.append(self.cha)
			# split line
		if self.couHex % 32 == 0:
			self.buf.append('\n')

	def loopPro(self):
		""" acquisizione dati dal device con protocollo """
		if self.ser:
			# acquisizione dati
			buff = self.ser.rcvChar()
			print "non implementato!"
# #ascii terminal
# 			if self.asc:
# 				if not buff:
# 					self.datRx = None
# 					sleep(0.001)
# 				else:
# 					for data in buff:
# 						self.datRx = data
# 						self.coun += 1
# 						# accumulate data solo printabili in self.buf
# 						self.acqAscii(data)
# 						# start
# 						if data == self.sta:
# 							self.coun = 0
# 							self.buf = [self.sta]
# 						# end
# 						elif data in self.sto:
# 							# chiamo la callback
# 							if self.calBk1:
# 								self.str = "".join(self.buf)
# 								self.res = self.calBk1(self.str)
# 							# end process
# 							self.buf = []
# 							self.coun = 0
# 			else:
# 				print "no binary!"
		# continua Idle
		return True

	def loop(self):
		""" acquisizione dati dal device """
		if self.ser:
			# acquisizione dati
			buff = self.ser.rcvChar()
#ascii terminal
			if self.asc:
				if not buff:
					self.datRx = None
					sleep(0.001)
				else:
					for data in buff:
						self.datRx = data
						self.coun += 1
						# accumulate data solo printabili in self.buf
						self.acqAscii(data)
						# print "rx ascii!"

					# parsing
					# if data in self.sto:
					if 1:
						# chiamo la callback
						if self.calBk1:
							self.res = self.calBk1("".join(self.buf))
						# end process
						self.buf = []
						self.coun = 0
			else:
#binary terminal
				if not buff:
					self.datRx = None
					sleep(0.001)
				else:
					for data in buff:
						self.datRx = data
						self.coun += 1
						# accumulate data solo printabili in self.buf
						self.acqBinary(data)
						# print "rx bin!"

					if 1:
						# chiamo la callback
						if self.calBk1:
							self.res = self.calBk1("".join(self.buf))
						# end process
						self.buf = []
						self.coun = 0

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
			sleep(self.kSleep)
	
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
		if self.sta == '':
			# referenzio il metodo che inserisco nel loop di Idle
			self.idPro = GObject.idle_add(self.loop)
		else:
			# referenzio il metodo che inserisco nel loop di Idle
			self.idPro = GObject.idle_add(self.loopPro)

	# simula la textView    
	def wriTg(self, msg, tag):
		print tag, msg,
	
#-----------------------------------------------------------------------------
# myTry
#-----------------------------------------------------------------------------
def try01(self, msg=['rra0004*',]):
	""" invio comando e visualizzo i dati ricevuti nel buffer seriale
	"""
	# invio un comando
	self.sendListCommands(msg)
	# attendo un numero di caratteri per un certo timeOut
	res,buf = self.ser.rcvStrTimeOut(num=50, tou=0.3)
	print "%s" %('timeOut:','ok:')[res], "chars receiver:",len(buf)
	# visualizzo buffer seriale
	print "buf:", self.ser.buf
#-----------------------------------------------------------------------------
def try02(msg="rra0004*"):
	""" invio comando e acquisisco i dati via protocollo
	"""
	def myTry(*args):
		print 'data', args
		return True
	# cambio il loop back del seriale
	self.calBk1 = myTry 
	# invio un comando
	self.sendListCommands([msg,])
	#self.ser.sndString('#010207RRA1000')
	# tou, cal, *args (return=False fa scadere il tempo)
	myTimeOut(0.1, self.loop)
	# stampo il risultato del parser
	print self.res

#-----------------------------------------------------------------------------
# Main
#-----------------------------------------------------------------------------
if __name__ == "__main__":

	""" inizializza la seriale col protocollo
	"""
#configuration    
	if 1:
		# dev = "/dev/ttyS"
		dev = "/dev/ttymxc"
		# port, baudrate, bytesize, parity, stopbits, timeout, xonxoff, rtscts, dsrdtr
		cfg = ['4', '9600', '8', 'N', '1', None, False, False, False]
	else:
		dev = "/dev/ttyUSB"
		cfg = ['0', '115200', '8', 'N', '1', None, False, False, False]
	# fil="init.pkl", par=None, ope=True, deb=False
	obj = MySerial(por=dev, par=cfg, deb=1)
	if obj.ser:
		print "device Ok"
		#myProtocolSpring
		# ser=None, deb=False, sta='#', max=80, ide=1, hex=False, buf=None, wri=None, cal=None
		self = MyProtocol(ser=obj, sta='')
		#Parsing    
		myPars = myParser(self)
		# cambio la lista di loopback del device
		self.calBk1 = myPars
	else:
		print "device Ko"
		sys.exit()
	
	choi = 4
	if choi == 0:
		pass
	if choi == 1:
		# invio comando e visualizzo i dati ricevuti nel buffer seriale
		try01(self, msg=['echo $PATH',])
		
	elif choi == 2:
		# invio comando e acquisisco i dati via protocollo
		try02()
		
	elif choi == 3:
		# stringhe valide per il parsing
		pars = []
		pars.append(("#rra0000*","Read   Version: XXX ver 0.1 del 08/03/2012 10.22"))
		pars.append(("#rra0004*","Read   Ram/Par:1111"))
		# attivo il mio parsing
		self.calBk1 = myParserDefine(self, pars) 
		# invio dei comandi
		self.sendListCommands(['rra0000*',])
		# tou, cal, *args (return=True fa scadere il tempo)
		# 0.02=ok 0.01=ko
		myTimeOut(0.05, self.loop)
		print self.res

	elif choi == 4:
		from string import atof
		from time import localtime
		# inserimento permanente del loop di ricezione
		# self.dev.insLoop()

		def myLocParser(*args):
			if 0:
				print args
			else:
				ite = args[0].split(',')
				if ite:
					# print ite

					if ite[0] == "$GPRMC":
						# <1>,<2>,<3>,<4>,<5>,<6>,<7>,<8>,<9>,<10>,<11>,<12>*hh
						dat = "%s" %ite[9][:6]
						print "dat:%s/%s/%s" %(dat[:2],dat[2:4],dat[4:]), 
						tim = "%s" %ite[1][:6]
						print "tim:%s.%s.%s" %(tim[:2],tim[2:4],tim[4:])
						drc = atof(ite[8])
						print "dir:%5.1f" %(drc)

					if ite[0] == "$GPGGA":
						# <1>,<2>,<3>,<4>,<5>,<6>,<7>,<8>,<9>,M,<10>,M,<11>,<12>*hh
						lat = atof(ite[2][:2])
						lat += atof(ite[2][2:]) / 60.0
						lon = atof(ite[4][:3])
						lon += atof(ite[4][3:]) /60.0
						print "lat:%.6f lon:%.6f" %(lat, lon)
						alt = atof(ite[11])
						print "alt:%6.1f" %(alt)
						qua = int(ite[6])
						print "qua:%d" %(qua)
						sat = int(ite[7])
						print "sat:%02d" %(sat)

					if ite[0] == "$GPVTG":
						# ,<1>,T,<2>,M,<3>,N,<4>,K,<5>*hh
						vel = atof(ite[7])
						print "vel:%6.1f" %(vel)

					if ite[0] == "$GPGSA":
						# ,<1>,<2>,<3>,<3>,<3>,<3>,<3>,<3>,<3>,<3>,<3>,<3>,<3>,<3>,<4>,<5>,<6>*hh
						mod = "%s" %ite[1]
						print "mod:%s" %mod 
						dop = "%4.1f" %atof(ite[15])
						print "dop:%s" %dop

			return True
		self.calBk1 = myLocParser

		while True:
			self.loop()
