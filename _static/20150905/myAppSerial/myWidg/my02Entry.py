#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" lista degli oggetti definiti:

	- myEntry        - myEntList
	- myEntLabel     - myEntLabList
	- myEntFrame     - myEntFraList
"""

myRev = "(rev.150527)"
#-----------------------------------------------------------------------------
# Modules
#-----------------------------------------------------------------------------
from my00init import *
from gi.repository import Pango

#-----------------------------------------------------------------------------
# myModules
#-----------------------------------------------------------------------------
from myWind import MyWind #(contiene my00initGtk)
from my01Box import myViewObject, myBox, myBoxList, myFrame
from my02Label import myLabel

#-----------------------------------------------------------------------------
# myEntry
#-----------------------------------------------------------------------------
def myEntry(name='myText', 
			numb=None, 
			call=None, data=['dati']):
	""" crea una entry text di una certa dimensione 'numb'
		con un testo di default 'text'
		
		-> name testo da inserire nella entry
		-> numb numero massimo di caratteri visibili 
		-> call funzione da eseguire su evento
		-> data dati da passare alla funzione
	"""
	#callback debug    
	def on_activate(widg, *data):
		print "a", widg.get_text()
#entry
	# istanzio una Entry
	entr = Gtk.Entry()
	entr.show()
	# referenzio l'istanza
	entr.iden = str(entr.weak_ref)[-11:-1]
	# imposto massima lunghezza visibile in caratteri
	if numb == None:
		entr.set_width_chars(len(name))
	else:
		# max visible characters
		entr.set_width_chars(numb)
		# max entry digit
		#entr.set_max_length(numb)
		#entr.set_sensitive_length(False)
	entr.set_text(str(name))
	
	# in assenza di callback usa quella di debug
	if call == None:
		call = on_activate
	entr.connect("activate", call, *data)	
# <-        
	return entr, call
#-----------------------------------------------------------------------------
def testEntry():
#myEntry
	# ridefinisco la callback        
	def on_activate(widg, *data):
		print "b", widg.get_text(), data
	# entr, call
	entr, call = myEntry(name='myEntry',
						 numb=None, 
						 call=on_activate, data=["i miei dati",])
# <-
	return entr

#-----------------------------------------------------------------------------
# myEntryList
#-----------------------------------------------------------------------------
def myEntList(name=["One","Two","Three"], 
			  numb=None, 
			  call=None, data=['dati'],
			  tBox='v', aBox=[False, False, 1]):
	#callback debug
	def on_activate(widg, ind, *data):
		print "a", widg
		print ind, data
		
	# in assenza di callback uso quella di debug
	if call == None:
		call = on_activate

	# funzione che istanzia oggetti tipo
	def myList(ind):
#myEntry
		# entr, call
		return myEntry(name[ind], numb, 
					   call, [ind, data])
#myBoxList
	# xBox, [entr, call] * N
	obje, othe = myBoxList(name=name, tBox=tBox, 
						   aBox=aBox, func=myList)
# <-
	return obje, othe
#-----------------------------------------------------------------------------
def testEntList():
#myEntList    
	# ridefinisco la callback
	def on_activate(widg, ind, *data):
		pass
		print "b", "%05s" %widg.get_text(), ind, data
	# xBox, [entr, call] * N
	obje, othe = myEntList(name=["One","Two","Three"], 
						   numb=6, 
						   call=on_activate, data=[],
						   tBox='h', aBox=[False, False, 1] )
#myFrame    
	# fram,[labe,xBox]
	obj1, oth1 = myFrame(name='myEntry', obje=obje, colo="black",
						 bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
						 tBox='v' )
	#debug
	myViewObject(obje, othe)
# <-
	return obj1

#-----------------------------------------------------------------------------
# myEntryLabel
#-----------------------------------------------------------------------------
def myEntLabel(name='myText', 
			   numb=None,
			   call=None, data=['dati'],
			   nLab='Label', cLab="#333",
			   tLab='h', aLab=[False, False, 1]):
	""" crea una entry text di una certa dimensione 'numb'
		con un testo di default 'text' con associata una
		label alla riga o colonna
		  
		-> name testo da inserire nella entry
		-> numb numero massimo di caratteri visibili 
		-> call funzione da eseguire su evento
		-> data dati da passare alla funzione
		-> nLab nome etichetta 
		-> cLab colore etichetta 
		-> tLab tipo contenitore etichetta v/h 
		-> aLab attributi contenitore etichetta 
	"""
#myEntry
	# entr, call
	entr,call = myEntry(name=name,
			  			numb=numb, 
			  			call=call, data=data)
#myLabel
	if cLab == None:
		cLab=Gdk.color_parse('blue')
	# labe
	labe = myLabel(name=nLab, 
					leng=len(nLab)+1, prea=' ', post=' ', 
					font='Courier 10', 
					colo=cLab)
#xBox   
	xBox = myBox(tLab)
	#child, expand=True, fill=True, padding=0
	xBox.pack_start(labe, *aLab)
	xBox.pack_start(entr, *aLab)	
# <-        
	return xBox, [entr, call, labe]
#-----------------------------------------------------------------------------
def testEntLabel():
#myEntLabel
	# ridefinisco la callback        
	def on_activate(widg, *data):
		print "b", widg.get_text(), data
	# xBox, [entr, call, labe]
	obje, othe = myEntLabel(name='myText', 
							numb=None,
							call=on_activate, data=[],
							nLab='Label', cLab="#333",
							tLab='h', aLab=[False, False, 1])
# <-
	return obje

#-----------------------------------------------------------------------------
# myEntryLabelList
#-----------------------------------------------------------------------------
def myEntLabList(name=["One","Two","Three"], 
				 numb=None, 
				 call=None, data=['dati'],
				 nLab=['Label01','Label02','Label03'], cLab="#333",
				 tLab='h', aLab=[False, False, 1],
				 tBox='h', aBox=[False, False, 1],):
	#callback debug
	def on_activate(widg, ind, *data):
	  print "a", widg
	  print ind, data
		
	# in assenza di callback uso quella di debug
	if call == None:
	  call = on_activate

	# funzione che istanzia oggetti tipo
	def myList(ind):
#myEntLabel
		# xBox, [entr, call, labe]
		return myEntLabel(name[ind], numb,
						  call, [ind, data],
						  nLab[ind], cLab,
						  tLab, aLab)
#myBoxList
	# xBox, [xBox, [entr, call, labe]] * N
	obje, othe = myBoxList(name=name, tBox=tBox, 
						   aBox=aBox, func=myList)
# <-
	return obje, othe
#-----------------------------------------------------------------------------
def testEntLabList():
#myEntLabList    
	# ridefinisco la callback
	def on_activate(widg, ind, *data):
		print "b", "%05s" %widg.get_text(), ind, data
	# xBox, [xBox, [entr, call, labe]] * N
	obje, othe = myEntLabList(name=["One","Two","Three"], 
							  numb=6, 
							  call=on_activate, data=[],
							  nLab=['Label01','Label02','Label03'], cLab="#333",
							  tLab='h', aLab=[False, False, 1],
							  tBox='v', aBox=[False, False, 1],)
#myFrame    
	# fram,[labe,xBox]
	obj1, oth1 = myFrame(name='myEntLabList', obje=obje, colo='black',
						 bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
						 tBox='v' )
	#debug
	myViewObject(obje, othe)
# <-
	return obj1

#-----------------------------------------------------------------------------
# myEntryFrame
#-----------------------------------------------------------------------------
def myEntFrame(name='myText', 
			   numb=None,
			   call=None, data=['dati'],
			   nFra='Label', cFra='black', bFra=1, sFra=Gtk.SHADOW_ETCHED_OUT, 
			   tFra='v', aFra=[False, False, 1]):
	""" crea una entry text di una certa dimensione 'numb'
		con un testo di default 'text' inserita in un frame
		
		-> name testo da inserire nella entry
		-> call funzione da eseguire su evento
		-> data dati da passare alla funzione
		-> numb numero massimo di caratteri visibili 
		-> nFra nome del frame 
		-> cFra colore nome del frame 
		-> bFra bordo riservato all'esterno
		-> sFra tipo di cornice
		-> tFra tipo di contenitore v/h 
		-> aFra attributi del contenitore
	"""    
#myEntry
	entr,call = myEntry(name=name,
						numb=numb,
						call=call, data=data)
#myFrame
	#fram, [labe, xBox]
	fram,othe = myFrame(nFra, entr, cFra, bFra, sFra, tFra, aFra)
	# <-
	#fram, [labe, xBox, entr, call]        
	return fram, [othe[0], othe[1], entr, call]
#-----------------------------------------------------------------------------
def testEntFrame():
#myEntFrame
	# ridefinisco la callback        
	def on_activate(widg, *data):
		pass
		print "b", data
	#fram, [labe, xBox, entr, call]        
	obje, othe = myEntFrame(name='myText', 
							numb=6,
							call=on_activate, data=[],
							nFra='myEntFrame', cFra='black', bFra=1, sFra=Gtk.SHADOW_ETCHED_OUT, 
							tFra='v', aFra=[False, False, 1])
# <-
	return obje

#-----------------------------------------------------------------------------
# myEntryFramelList
#-----------------------------------------------------------------------------
def myEntFraList(name=["One","Two","Three"], 
				 numb=None, 
				 call=None, data=['dati'],
				 nFra=['Label01','Label02','Label03'], 
				 cFra='black',
				 bFra=1, sFra=Gtk.SHADOW_ETCHED_OUT, 
				 tFra='v', aFra=[False, False, 1],
				 tBox='h', aBox=[False, False, 1]):
	#callback debug
	def on_activate(widg, ind, *data):
		print "a", 
		print ind, data
		
	# in assenza di callback uso quella di debug
	if call == None:
		call = on_activate

	# funzione che istanzia oggetti tipo
	def myList(ind):
#myEntFram
		#fram, [labe, xBox, entr, call]
		return myEntFrame(name[ind], numb,
						  call, [ind, data],
						  nFra[ind], cFra, bFra, sFra, 
						  tFra, aFra)
#myBoxList
	# xBox, [fram, [labe, xBox, entr, call]] * N        
	obje, othe = myBoxList(name=name, tBox=tBox, 
						   aBox=aBox, func=myList)
# <-
	return obje, othe
#-----------------------------------------------------------------------------
def testEntFraList(debu=0):
#myEntFraList    
	# ridefinisco la callback
	def on_activate(widg, ind, *data):
		print "b", "%05s" %widg.get_text(), ind, data
	# xBox, [fram, [labe, xBox, entr, call]] * N        
	obje, othe = myEntFraList(name=["One","Two","Three"], 
							  numb=None, 
							  call=on_activate, data=[],
							  nFra=['Label01','Label02','Label03'],
							  cFra='black', 
							  bFra=1, sFra=Gtk.SHADOW_ETCHED_OUT, 
							  tFra='v', aFra=[False, False, 1],
							  tBox='h', aBox=[False, False, 1])
#myFrame    
	# fram,[labe,xBox]
	obj1, oth1 = myFrame(name='myEntryFrame', obje=obje, colo='black',
						 bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
						 tBox='v' )
	#debug
	myViewObject(obje, othe)
# <-
	return obj1

#-----------------------------------------------------------------------------
# myTry
#-----------------------------------------------------------------------------
def myTry01():
  sys.exit()
	
#-----------------------------------------------------------------------------
# Main
#-----------------------------------------------------------------------------
if __name__ == "__main__":

	# test arguments
	if len(sys.argv) == 1:
		# no arguments (scelgo io)
		choi = 13
	else:
		# get first argument (scelta esterna)
		choi = int(sys.argv[1])

	# oggetti singoli 
	if choi == 1:
		obje = testEntry()
	elif choi == 2:
		obje = testEntLabel()
	elif choi == 3:
		obje = testEntFrame()

	elif choi == 11:
		obje = testEntList()
	elif choi == 12:
		obje = testEntLabList()
	elif choi == 13:
		obje = testEntFraList()
		
	# istanza l'applicazione principale
	self = MyWind(width=None, height=800, title="myEntry %s" %myRev, center=True, color="#b0b0b0")
	self.vBox.pack_start(child=obje, expand=False, fill=False, padding=0)

	# cediamo il controllo alle gtk
	Gtk.main()
