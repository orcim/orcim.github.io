#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" lista oggetti definiti:
	
	- insLib, we_are_frozen, module_path
	- myPath, myNone, printD, myPickle
	- myTimeOut
"""

#myRev = "(rev.150906)"
#-----------------------------------------------------------------------------
# Modules
#-----------------------------------------------------------------------------
# structures C
from ctypes import *

# system
# import warnings
# warnings.filterwarnings("ignore")
import os, sys
#import threading
#from glob import glob

# time
from time import time, sleep, clock, localtime
# string
from string import atoi, atof
# from math import pi, sin, cos, tan, log, radians

# # serializzazione
# try:
#     import cPickle as pickle
# except:
#     import pickle, dump, load 

#-----------------------------------------------------------------------------
# Enviroment
#-----------------------------------------------------------------------------
def insLib(lib, deb=True):
	""" Inserisce nel path la libreria passata 
	"""
	# verifica se gia' presente
	if lib not in sys.path:
		# aggiungo in prima posizione
		sys.path.insert(0, lib)
	else:
		if deb:
			print "gia' presente:", lib

#-----------------------------------------------------------------------------
def we_are_frozen():
	"""Returns whether we are frozen via py2exe.
	This will affect how we find out where we are located."""
	return hasattr(sys, "frozen")

#-----------------------------------------------------------------------------
def module_path():
	# verifico il sitema operativo
	if sys.platform != 'win32':
		return os.getcwd()
	else:
		""" This will get us the program's directory,
		even if we are frozen using py2exe"""
		if we_are_frozen():
			return os.path.dirname(unicode(sys.executable, sys.getfilesystemencoding( )))
		return os.path.dirname(unicode(__file__, sys.getfilesystemencoding( )))
			
#-----------------------------------------------------------------------------
def myPath(path):
	# elimino la current path per comodita' visiva
	myFath = os.getcwd()
	if path.find(myFath) == 0:
		path = path[len(myFath)+1:]
	return path

#-----------------------------------------------------------------------------
# ricavo l'ambiente
myRoot = module_path()
myFath, myHome = os.path.split(myRoot)

#-----------------------------------------------------------------------------
# myDefine
#-----------------------------------------------------------------------------
def myNone(*args):
	pass

#-----------------------------------------------------------------------------
# caratteri stampabili
printable=list("'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ")

#-----------------------------------------------------------------------------
def printD(msg, att='\n'):
	""" forzo scrittura nella standard out
		 server quando lo stdout e' reinderizzato e si vuole
		 inviare comunque vero stdout di default
	"""
	sys.__stdout__.write(str(msg)+att)

#-----------------------------------------------------------------------------
def myPickle(obj=None, nam="mio.pkl"):
	""" Serializzazione degli oggetti.
		obj==None => read  es: lObj=myPickle(nam="mio.pkl")
		obJ!=None => write es: myPickle(obj=["prova",1,[1,2,3]], nam="new.pkl")
	"""
	# provo l'importazione del modulo piu' veloce
	#  altrimenti ripiego in quello standard
	try:
		import cPickle as pickle
	except:
		import pickle
	
	if obj != None:
		# write
		pickle.dump(obj, open(nam,'w'))
	else:
		# read
		return pickle.load(open(nam,'r'))

#-----------------------------------------------------------------------------
def myTimeOut(tou, cal, *args):
	""" richiamo il metodo 'cal' passando gli argomenti '*args'
		esco dal metodo 'myTimeOut' per tempo scaduto o se 
		la funzione 'cal' ritorna

	"""
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
		else:
			# chiamo la callback
			# (flg=False fa uscire dal loop immediatamente)
			flg = cal(*args)
# <- ritorna il tempo passato
	return now
#-----------------------------------------------------------------------------
def testTimeOut():

	def myParser(*args):
		print 'data', args
		return args[0]
	# tou, cal, *args (False fa uscire dal loop immediatamente)
	print "time: %f" %myTimeOut(0.1, myParser, False, "Ciao!")

#-----------------------------------------------------------------------------
# Main
#-----------------------------------------------------------------------------
if __name__ == "__main__":

	# test arguments
	if len(sys.argv) == 1:
		# no arguments (scelgo io)
		choi = 2
	else:
		# get first argument (scelta esterna)
		choi = int(sys.argv[1])

	if choi == 1:
		"test enviroment"
		print "myRoot:", myRoot
		print "myFath:", myFath
		print "myHome:", myHome
	elif choi == 2:
		testTimeOut()
