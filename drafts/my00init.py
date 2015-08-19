#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from __future__ import with_statement
""" lista oggetti definiti:
	
	- insLib, we_are_frozen, module_path
	- chaStockLabel, chaBackColor, myBeep, myNone, printD 
	- fixHexBas, hex2Flt, flt2Hex 
	- rev.140620 + myPickle, IterStructure 
	- rev 140701 + Keysyms
	- rev 140705 + Iter1Structure
"""
#-----------------------------------------------------------------------------
# Modules
#-----------------------------------------------------------------------------
# structures C
from ctypes import *
myRev = "(rev.140705)"

# system
# import warnings
# warnings.filterwarnings("ignore")
import os, sys
#import threading
#from glob import glob

# importa i moduli in modo dinamico (new style)
from gi.repository import Gtk, Gdk, GLib
from gi.repository import GObject 

# # gtk
# import gtk, gobject, pango
# ## Get Icons shown on buttons 
# settings = gtk.settings_get_default() 
# gtk.Settings.set_long_property(settings, "gtk-button-images", 1, "main") 

# time
from time import time, sleep, clock, localtime
# string
from string import atoi, atof
from math import pi, sin, cos, tan, log, radians

# # serializzazione
# try:
#     import cPickle as pickle
# except:
#     import pickle, dump, load 
#-----------------------------------------------------------------------------
# myDefines
#-----------------------------------------------------------------------------
# Enums
Gtk.ICON_SIZE_MENU = Gtk.IconSize.MENU
Gtk.ICON_SIZE_BUTTON = Gtk.IconSize.BUTTON
Gtk.JUSTIFY_LEFT = Gtk.Justification.LEFT
Gtk.JUSTIFY_RIGHT = Gtk.Justification.RIGHT
Gtk.POS_RIGHT = Gtk.PositionType.RIGHT
Gtk.POLICY_AUTOMATIC = Gtk.PolicyType.AUTOMATIC
Gtk.POLICY_ALWAYS = Gtk.PolicyType.ALWAYS
Gtk.SELECTION_BROWSE = Gtk.SelectionMode.BROWSE
Gtk.SELECTION_NONE = Gtk.SelectionMode.NONE
Gtk.SORT_ASCENDING = Gtk.SortType.ASCENDING
Gtk.SHADOW_NONE = Gtk.ShadowType.NONE
Gtk.SHADOW_IN = Gtk.ShadowType.IN
Gtk.SHADOW_OUT = Gtk.ShadowType.OUT
Gtk.SHADOW_ETCHED_IN = Gtk.ShadowType.ETCHED_IN
Gtk.SHADOW_ETCHED_OUT = Gtk.ShadowType.ETCHED_OUT
Gtk.STATE_NORMAL = Gtk.StateType.NORMAL
Gdk.BUTTON_PRESS = Gdk.EventType.BUTTON_PRESS
Gtk.TEXT_DIR_RTL = Gtk.TextDirection.RTL
Gdk.CONTROL_MASK = Gdk.ModifierType.CONTROL_MASK
Gtk.FILE_CHOOSER_ACTION_OPEN = Gtk.FileChooserAction.OPEN
Gtk.FILE_CHOOSER_ACTION_SAVE = Gtk.FileChooserAction.SAVE
Gtk.RESPONSE_CANCEL = Gtk.ResponseType.CANCEL
Gtk.RESPONSE_OK = Gtk.ResponseType.OK
Gtk.WIN_POS_CENTER = Gtk.WindowPosition.CENTER
Gtk.SELECTION_MULTIPLE = Gtk.SelectionMode.MULTIPLE
Gtk.TEXT_WINDOW_WIDGET = Gtk.TextWindowType.WIDGET

#-------------------------------------------------------------------
# gtk.keysyms
#-------------------------------------------------------------------
class Keysyms(object):
	pass
keysyms = Keysyms()
sys.modules['gtk.keysyms'] = keysyms
Gtk.keysyms = keysyms
for name in dir(Gdk):
	if name.startswith('KEY_'):
		target = name[4:]
		if target[0] in '0123456789':
			target = '_' + target
		value = getattr(Gdk, name)
		setattr(keysyms, target, value)

#-----------------------------------------------------------------------------
# Enviroment
#-----------------------------------------------------------------------------
def insLib(lib, deb=True):
	""" verifica e inserimento nel path """
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
if 0:
	print "myRoot", myRoot
	print "myFath", myFath
	print "myHome", myHome
# aggiungo il path delle mie librerie
insLib(myRoot+'/myLib',True)
#insLib(myRoot+'/myLib/myGtk',True)
insLib(myRoot+'/myLib/myProtocol',True)
#insLib(myRoot+'/myLib/myUtilities',True)
# insLib(myRoot+'/myWidg',True)

#-----------------------------------------------------------------------------
# myUtilities
#-----------------------------------------------------------------------------
def chaStockLabel(self,lab):
	" cambio nome alla label in una stock_id"
	al = self.get_children()[0]
	hb = al.get_children()[0]
	image, text = hb.get_children()
	text.set_text(lab)

#-----------------------------------------------------------------------------
def chaBackColor(obj=None, css="MyWind", col="#666666"):
	" cambio colore al background dell'oggetto"
	obj.set_name(css)
	# colore background
	style_provider = Gtk.CssProvider()
	css = "#%s {background-color: %s; }" %(css, col)
	# css = """
	# #MyWind {
	#     background-color: #F00;
	# }
	# """
	style_provider.load_from_data(css)
	Gtk.StyleContext.add_provider_for_screen(
		Gdk.Screen.get_default(), 
		style_provider,     
		Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
	)
	
#-----------------------------------------------------------------------------
def myBeep(fre=880, dly=100, tim=2):
	if sys.platform == 'win32':
		# sound
		from winsound import Beep
		" gestione suoni di sistema"
		for ele in xrange(tim):
			Beep(fre, dly)
			sleep(0.1)

#-----------------------------------------------------------------------------
def myNone(*args):
	pass

#-----------------------------------------------------------------------------
def fixHexBas(num, bas=16):
	""" fixed hex 
	"""
	msk = 2**(bas-1)
	# verifica se negativo
	if num & msk:
		num = -(msk - ( num & (msk -1) ))
	return num

#------------------------------------------------------------------------------
def hex2Flt(str):
	" converto da stringa hex a float (mantissa 24bit)" 
	from string import atoi
	num = atoi(str,16)
	" converto il formato esadecimale di un numero float"
	y = (((num & 0x7f800000) >> 23) - 0x7f)
	x = (((num & 0x007fffff) + 0x00800000) * 1.0 / 0x00800000) * 2**y
	if num & 0x80000000 > 0:
		x = -x
	return x

#------------------------------------------------------------------------------
def flt2Hex(num):
	" converto da float (mantissa 24bit) a stringa" 
	exp = 0
	man = 0
	sig = 0
	hex = 0
	
	if num < 0:
		num = -num
		sig = 0x80000000
	while True:
		if num >= 2:
			exp +=1
			num /=2.0
		elif num < 1:
			exp -=1
			num *=2.0
		else:
			break
	
	exp += 0x7f
	man = num * 0x00800000 - 0x00800000
	hex = sig | int(man) | (exp << 23)
	return ("%X" %hex)

#-----------------------------------------------------------------------------
def rad2deg(pha):
	""" convert Radians to Degrees
	"""
	return (pha * 180.0 / pi)
#-----------------------------------------------------------------------------
def deg2rad(pha):
	""" convert Degrees to Radians
	"""
	return (pha * pi / 180.0)

#-----------------------------------------------------------------------------
def printD(msg, att='\n'):
	sys.__stdout__.write(str(msg)+att)

#-----------------------------------------------------------------------------
def myTimeOut(tou, fun, *args):
	""" richiama callback ad ogni tick per N tou
		 passando gli argomenti
	"""
	# referenzio lo start
	tim = time()
	cou = 0
	# flag
	flg = True
	while flg:
		cou +=1
		# calcolo il tempo trascorso
		now = (time() - tim)
		if now > tou:
			# forzo l'uscita
			flg = False
		else:
			# chiamo la callback
			flg = fun(cou, *args)
			# (return=True fa scadere il tempo)
	return now < tou

#-----------------------------------------------------------------------------
def myPickle(obj=None, nam="mio.pkl"):
	""" obj==None => read  es: lObj=myPickle(nam="mio.pkl")
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
class Singleton(GObject.GObject):
#-----------------------------------------------------------------------------
	""" istanza con attributi in comune
	"""
	_instance = None
	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super(Singleton, cls).__new__(
								cls, *args, **kwargs)
		return cls._instance

#-----------------------------------------------------------------------------
class IterStructure(Structure):
#-----------------------------------------------------------------------------
	"rende la struttura iterabile"
	def __getitem__(self, i):
		if not isinstance(i, int):
			raise TypeError('subindices must be integers: %r' % i)
		# [name, value, type]
		return self._fields_[i][0], getattr(self, self._fields_[i][0]), self._fields_[i][2]

	def getItem(self, dat):
		msg = ""
		for nam, val, typ in dat.struc:
			# 8 bit
			if typ == 8:
				msg +="%s:%.2x " %(nam, val)
			# 16 bit
			elif typ == 16:
				msg +="%s:%.4x " %(nam, val)
			# 32 bit
			elif typ == 32:
				msg +="%s:%.8x " %(nam, val)
		return msg

#-----------------------------------------------------------------------------
class Iter1Structure(Structure):
#-----------------------------------------------------------------------------
	"rende la struttura iterabile"
	def __getitem__(self, i):
		if not isinstance(i, int):
			raise TypeError('subindices must be integers: %r' % i)
		# [name, value]
		return self._fields_[i][0], getattr(self, self._fields_[i][0])

	def getItem(self, dat):
		msg = ""
		for nam, val in dat.struc:
			msg +="%s:%s " %(nam, val)
		return msg

#-----------------------------------------------------------------------------
class myDialog(Gtk.Dialog):
#-----------------------------------------------------------------------------
	def __init__(self, parent, title="myDialog", msg="Vuoi Confermare?", 
					wid=3, hei=3, x=None, y=0):
		Gtk.Dialog.__init__(self, title, parent, 0,
			(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
			 Gtk.STOCK_OK, Gtk.ResponseType.OK))

		# window positions
		if x==None:
			self.set_position(Gtk.WindowPosition.CENTER)
		else:
			self.move(x, y)
		# size
		self.set_default_size(wid,hei)
		# referenzio il box
		box = self.get_content_area()
		# message
		label = Gtk.Label(msg)
		box.add(label)
		# visualizzo
		self.show_all()

#-----------------------------------------------------------------------------
# Main
#-----------------------------------------------------------------------------
if __name__ == "__main__":
	# ridefinisco la funzione per prova
	def myNone(*args):
		sleep(0.02)
		# stampo i dati passati e il tempo di esecuzione  
		print args, clock() 
		# True = continua l'esecuzione
		# False = ferma l'esecuzione (come fosse finita l'esecuzione in tempo!)
		return args[0]

	if 1:    
		cou = 0
		# tou, cal, *args (return=True fa scadere il tempo)
		res = myTimeOut(0.1, myNone, True, cou)
		# stampo il risultato
		print res

	if 0:
		# istanzio una dialog
		dial = myDialog(None, x=0, y=0)
		resp = dial.run()
		# response
		if resp == Gtk.ResponseType.OK:
			print("OK!")
		elif resp == Gtk.ResponseType.CANCEL:
			print("KO!")
		# close
		dial.destroy()

	if 0:
		dial = Gtk.MessageDialog(None, 0, Gtk.MessageType.WARNING,
			Gtk.ButtonsType.OK_CANCEL, "Vuoi Confermare?")
		# dial.move(0, 0)
		resp = dial.run()
		# response
		if resp == Gtk.ResponseType.OK:
			print("OK!")
		elif resp == Gtk.ResponseType.CANCEL:
			print("KO!")
		# close
		dial.destroy()
