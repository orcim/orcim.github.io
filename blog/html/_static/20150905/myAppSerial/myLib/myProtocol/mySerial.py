#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" lista degli oggetti definiti:

	- printHex
	- MySerial

	Gestione di una connessione Seriale
	open()                  #open port
	close()                 #close port immediately
	setBaudrate(baudrate)   #change baudrate on an open port
	inWaiting()             #return the number of chars in the receive buffer
	read(size=1)            #read "size" characters
	write(s)                #write the string s to the port
	flushInput()            #flush input buffer, discarding all it's contents
	flushOutput()           #flush output buffer, abort output
	sendBreak()             #send break condition
	setRTS(level=1)         #set RTS line to specified logic level
	setDTR(level=1)         #set DTR line to specified logic level
	getCTS()                #return the state of the CTS line
	getDSR()                #return the state of the DSR line
	getRI()                 #return the state of the RI line
	getCD()                 #return the state of the CD line
"""

myRev = "(rev.150525)"
#-----------------------------------------------------------------------------
# Modules
#-----------------------------------------------------------------------------
from my00init import *

#------------------------------------------------------------------------------
# myDefines
#-----------------------------------------------------------------------------
def printHex(str):
	""" stampa caratteri non visibili in formato esadecimale"""
	mes = []
	for ch in str:
		if ch in printable:
			mes.append(ch)
		else:
			# rendo visibile il codice
			mes.append("(%02x)" %ord(ch))
			if ch == '\n':
				mes.append('\n')
	print "".join(mes)

#------------------------------------------------------------------------------
# myClass
#------------------------------------------------------------------------------
class MySerial(object):
	""" gestione di una comunicazione Seriale
		Attributi:
			ser
				- gestione Serial
			dlTx
				- ritardo tra un Tx ed un'altro
			cou
				- caratteri ricevuti
			buf
				- buffer di ricezione
		Metodi:
			close
				- Chiusura del socket
			chaSetting
				- configurazione della connessione
			sndChar
				- Invio di un char espresso come stringa es: '\n'
			sndString
				- Invio di una stringa 'str' (stringa ascii)
			rcvChar
				- Ricezione di un carattere (funzione non bloccante)
			rcvString
				- Ricezione di una N caratteri (funzione non bloccante)
			rcvStrTimeOut
				- Ricezione di N caratteri entro un certo tempo
	"""

	def __init__(self, por="/dev/ttyS", par=['1','115200','8','N','1'], ope=True, deb=False):
		""" Inizializzo il dispositivo
			@par    parametri di configurazione
			@ope    stabilisco se deve essere aperta la porta
		"""
		# referenzio il flag di Debug
		self.deb = deb
		self.ope = ope
		self.par = par
		self.por = por+par[0]
		# Gestione collegamento
		if self.ope:
			try:
				# provo ad aprire la connessione
				self.ser = serial.Serial(self.por)
				# configuro i parametri e provo apertura
				try:
					self.ser.close()
					self.ser.open()
					# set parameters
					self.chaSetting()
					# debug
					if self.deb:
						# ok
						print "%s now is open." %self.por
				except:
					self.ser = None
					# seriale gia' aperta
					print "%s port not opened!" %self.por
			except:
				# nessuna seriale presente
				self.ser = None
				# debug
				print "%s not present!" %self.por
				#sys.exit()
		else:
			# nessuna verifica di presenza device!
			self.ser = serial.Serial()
			#print self.ser
		# attributi
		self.dlTx = 0.002    # Delay from Tx to Tx
		#self.buf = ""

	def close(self):
		"""Chiusura del socket"""
		self.ser.close()
		# debug
		if self.deb:
			print "%s now is close." %self.por

	def __del__(self):
		"""Distruzione dell'oggetto"""
		try:
			self.close()
			del self.ser
		except:
			pass

	def chaSetting(self):
		""" configurazione della connessione """
		# uso parametri interno se non passati
		# forzo la chiusura  della connessione
		self.ser.close()
		self.ser.port = self.por
		self.ser.baudrate = atoi(self.par[1])
		self.ser.bytesize = atoi(self.par[2])
		self.ser.parity = self.par[3]
		self.ser.stopbits = atoi(self.par[4])
		try:
			self.ser.open()
		except:
			print "Problem to open the connection!!!"""
			print self.ser

	def sndByte(self, byt):
		""" Invio di 1 byte"""
		cha = "%c" %byt
		self.ser.write(cha)
		# ritardo tra un carattere e il successivo
		sleep(self.dlTx)
		if self.deb:
			# rendo visibile il codice
			cod = "\\x%02X" %ord(cha)
			print cod,

	def sndData(self, dat):
		""" Invio di sequenza di bytes"""
		# comando da inviare
		strCmd=""
		for byt in dat:
			strCmd+=("%c" %byt)
		# invio diretto perche' con 38400 c'e' la pausa di circa mSec
		#  che manda in time out il dispositivo
		self.ser.write(strCmd)
		if self.deb:
			for ele in dat:
				print "\\x%02X" %ele,
			print
		# qui bisognerebbe attendere almeno 4 time della velocita' di 1 byte
		#  a 9600
		#sleep(0.004)
		# a 38400
		sleep(0.001)

	def sndChar(self, cmd):
		""" Invio di 1 carattere espresso come stringa es: '\n' """
		for ele in cmd:
			cha = "%c" %ele
			self.ser.write(cha)
			# ritardo tra un carattere e il successivo
			sleep(self.dlTx)
		if self.deb:
			if cha == '\r':
				print "\n",
			else:
				print cha,

	def sndString(self, str):
		""" Invio di una stringa 'str' (stringa ascii) """
		#printHex(str)
		for ch in str:
			self.ser.write(ch)
			# ritardo tra un carattere e il successivo
			sleep(self.dlTx)
		# debug
		if self.deb:
			print "send:",
			printHex(str)

	def rcvByte(self):
		""" Ricezione di un byte (funzione non bloccante) """
		# verifico se c'e' qualcosa in ricezione
		cou = self.ser.inWaiting()
		if cou > 0:
			# prelievo un byte
			return self.ser.read(cou)
		else:
			return None

	def rcvChar(self):
		""" Ricezione di un carattere (funzione non bloccante) """
		return self.rcvByte()

	def rcvString(self, num=1):
		""" Ricezione di una N caratteri (funzione non bloccante) """
		# verifico quanti caratteri ci sono gia' nel buffer
		cou = self.ser.inWaiting()
		if cou > 0:
			if cou >= num:
				# provo la ricezione
				dat = self.ser.read(num)
			else:
				dat = self.ser.read(cou)
				# dati letti
				num = cou
		else:
			dat = None
			num = 0
		return (num, dat)

	def rcvDataTimeOut(self, num=1, tou=0.1):
		""" Ricezione di una sequenza di bytes entro un certo tempo
			Return:
				self.buf = caratteri acquisiti
		"""
		# svuoto buffer
		self.buf = ""
		# conteggio caratteri da ricevere
		self.cou = 0

		# referenzio lo start
		tim = clock()

		# flag
		flg = True
		while flg:
			# calcolo il tempo trascorso
			now = (clock() - tim)
			if now > tou:
				# forzo l'uscita
				flg = False
			# verifico la ricezione
			cou, dat = self.rcvString(num)
			if cou:
				# salvo i dati ricevuti
				self.buf += dat
				self.cou += cou
				if self.cou >= num:
					flg = False
		if now > tou:
			ret = False
		else:
			ret = True
		return (ret, self.buf)

	def rcvStrTimeOut(self, num=1, tou=0.1):
		""" Ricezione di N caratteri entro un certo tempo
			Return:
				self.buf = caratteri acquisiti
		"""
		return self.rcvDataTimeOut(num, tou)

#------------------------------------------------------------------------------
# myTry
#------------------------------------------------------------------------------
def myTry01a():

	# winzoz
	# "COM1"
	# 
	# Unix
	# "/dev/ttyUSB0"
	# "/dev/ttymxc0"
	# "/dev/ttyS0"

	por = "/dev/ttyUSB"
	par = ['0','115200','8','N','1']
	self = MySerial(por=por, par=par, ope=1, deb=1)
	self.ser = serial.Serial(self.por)
	# try:
	# 	self.ser.open()
	# 	print "serial opened"
	# except:
	# 	print "not opened!"

#------------------------------------------------------------------------------
def myTry01():

	# abilito il debug
	deb = 1
	# inizializzazione
	if 0:
#        por = "/dev/ttyS"
		por = "/dev/ttymxc"
		par = ['4','115200','8','N','1']
	else:
		por = "/dev/ttyUSB"
		# par = ['0','115200','8','N','1']
		par = ['0','9600','8','N','1']

	#  istanza di un seriale
	self = MySerial(por=por, par=par, ope=True, deb=deb)
	if self.ser:
		print "serial Ok"

		if 0:
			"invio dati"
			self.sndString("echo Ciao Mondo!\n")
			# # attendo per un certo timeOut un numero di caratteri
			# # (num=1, tou=0.1):
			# res,buf = self.rcvStrTimeOut(num=50, tou=0.1)
			# print "%s" %('timeOut:','ok:')[res], "chars receiver:",len(buf)
			# printHex(buf)
			# #print "%s" %buf
		if 0:
			# DTR -> reset
			# RTS -> cs
			# all high
			self.ser.setRTS(0)
			self.ser.setDTR(0)

		if 1:
			# reset low
			self.ser.setDTR(1)
			sleep(0.001)
			# reset high
			self.ser.setDTR(0)

		if 0:
			# cs low
			self.ser.setRTS(1)
			# tx Low
			# self.sndString("\x00")
			sleep(0.001)
			# cs high
			self.ser.setRTS(0)

		if 0:
			"controllo Handshake"
			print "Rts=1, Dtr=0"
			self.ser.setRTS(1)
			self.ser.setDTR(0)
			sleep(1)
			print "Rts=0, Dtr=1"
			self.ser.setRTS(0)
			self.ser.setDTR(1)
			sleep(1)
			print "Rts=1, Dtr=0"
			self.ser.setRTS(1)
			self.ser.setDTR(0)
			sleep(1)
			print "Rts=0, Dtr=0"
			self.ser.setRTS(0)
			self.ser.setDTR(0)
			sleep(1)
			print "Rts=1, Dtr=1"
			self.ser.setRTS(1)
			self.ser.setDTR(1)
			sleep(1)
		if 0:
			"ricezione dati"
			# vedi protocol
	else:
		print "Serial Ko"

#------------------------------------------------------------------------------
if __name__ == "__main__":

	# provo apertura seriale
	myTry01()

	# provo modbus Atto-D4 lettura parametri
#    myTry02()
