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

myRev = "(rev.150906)"
#-----------------------------------------------------------------------------
# Modules
#-----------------------------------------------------------------------------
from my00init import *
import serial

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
			- ser 			istanza seriale
			- dlTx 			ritardo tra un invio ed un'altro
			- cou 			caratteri ricevuti
			- buf 			buffer di ricezione
		Metodi:
			- close			chiusura del socket
			- chaSetting	configurazione parametri
			- sndChar		invio di un char espresso come stringa es: '\n'
			- sndString		invio di una stringa es: 'str' (stringa ascii)
			- rcvChar		ricezione di un carattere (funzione non bloccante)
			- rcvString		ricezione di una N caratteri (funzione non bloccante)
			- rcvStrTimeOut	ricezione di N caratteri entro un certo tempo
	"""

	def __init__(self, por="/dev/ttyS", par=['1','115200','8','N','1'], ope=True, deb=False):
		""" Inizializzo il dispositivo
			-> por    tipo device (dipende dal S.O.)
			-> par    parametri di configurazione
			-> ope    stabilisco se deve essere aperta la connessione
		"""
		# referenzio il flag di Debug
		self.deb = deb
		self.ope = ope
		self.par = par
		self.por = por+par[0]
		# Gestione apertura collegamento
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
				if self.deb:
					print "%s not present!" %self.por
					#sys.exit()
		# nessuna verifica di presenza device!
		else:
			self.ser = serial.Serial()
		# ritardo tra un invio e il successivo
		self.dlTx = 0.002    

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
		"""Configurazione parametri """
		# forzo la chiusura per inizializzare i nuovi parametri
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
		""" Invio 1 byte"""
		cha = "%c" %byt
		self.ser.write(cha)
		# ritardo tra un invio e il successivo
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
		# Non uso sndByte per evitare il ritardo self.dlTx
		self.ser.write(strCmd)
		if self.deb:
			for ele in dat:
				print "\\x%02X" %ele,
			print
		sleep(0.001)

	def sndChar(self, cmd):
		""" Invio di 1 carattere espresso come stringa es: '\n' """
		for ele in cmd:
			cha = "%c" %ele
			self.ser.write(cha)
			# ritardo tra un invio e il successivo
			sleep(self.dlTx)
		if self.deb:
			if cha == '\r':
				print "\n",
			else:
				print cha,

	def sndString(self, str):
		""" Invio di una stringa 'str' (stringa ascii) """
		for ch in str:
			self.ser.write(ch)
			# ritardo tra un invio e il successivo
			sleep(self.dlTx)
		# debug
		if self.deb:
			print "send:",
			printHex(str)

	def rcvByte(self):
		""" Ricezione di N bytes (funzione non bloccante) """
		# verifico se c'e' qualcosa in ricezione
		cou = self.ser.inWaiting()
		if cou > 0:
			# prelievo un byte
			return self.ser.read(cou)
		else:
			return None

	# alias di rcvByte
	def rcvChar(self):
		""" Ricezione di N bytes (funzione non bloccante) """
		return self.rcvByte()

	def rcvString(self, num=1):
		""" Attesa di N bytes (funzione non bloccante) """
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
			<- self.buf = caratteri acquisiti
		"""
		# pilisco il buffer prima della ricezione
		self.buf = ""
		# contatore caratteri da ricevere
		self.cou = 0

		# referenzio lo start per il tOut
		tim = clock()

		# flag
		flg = True
		while flg:
			# calcolo il tempo trascorso
			now = (clock() - tim)
			if now > tou:
				# forzo l'uscita (tempo scaduto)
				flg = False
			# verifico dati in ricezione
			cou, dat = self.rcvString(num)
			if cou:
				# salvo i dati ricevuti
				self.buf += dat
				self.cou += cou
				if self.cou >= num:
					flg = False
		# ritorno False se è scaduto il tempo
		if now > tou:
			ret = False
		# ritorno True se ho ricevuto tutti i dati
		else:
			ret = True
		return (ret, self.buf)

	# alias di rcvDataTimeOut
	def rcvStrTimeOut(self, num=1, tou=0.1):
		""" Ricezione di N caratteri entro un certo tempo
			<- self.buf = caratteri acquisiti
		"""
		return self.rcvDataTimeOut(num, tou)

#------------------------------------------------------------------------------
# myTry
#------------------------------------------------------------------------------
def myTry01():

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

	#  istanza di un seriale
	self = MySerial(por=por, par=par, ope=1, deb=1)
	if self.ser:
		# init DTR/RTS
		if 0:
			# set to low
			self.ser.setDTR(1)
			sleep(0.01)
			# set to high
			self.ser.setDTR(0)
			self.ser.setRTS(0)

		print "serial open: OK!"
		return self 

	else:
		print "Serial not found!"
		return None

#------------------------------------------------------------------------------
def myTry02():
	self = myTry01()
	if self:
		# invio una stringa
		self.sndString("Ciao mondo!\n")
		# attendo (num) N caratteri entro (tou) un tempo
		res,buf = self.rcvStrTimeOut(num=50, tou=0.01)
		print "%s" %('timeOut:','ok:')[res], "chars receiver:",len(buf)
		print "buf:",
		# visualizza anche i caratteri speciali
		printHex(buf)
		# print "%s" %buf

#-----------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
if __name__ == "__main__":

	# test arguments
	if len(sys.argv) == 1:
		# no arguments (scelgo io)
		choi = 2
	else:
		# get first argument (scelta esterna)
		choi = int(sys.argv[1])

	if choi == 1:
		# test apertura seriale
		myTry01()
	elif choi == 2:
		# test
		myTry02()

