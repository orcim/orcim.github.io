#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" widgets definiti:

	- myChkButton      
	- myChkButList
	- myChkButLisLabel
"""

myRev = "(rev.150903)"
#-----------------------------------------------------------------------------
# Modules
#-----------------------------------------------------------------------------
from my00init import *
from gi.repository import Pango

#-----------------------------------------------------------------------------
# myModules
#-----------------------------------------------------------------------------
from myWind import MyWind #(contiene my00initGtk)
from my01Box import myViewObject, myBoxList, myFrame
from my02Label import myLabel

#-----------------------------------------------------------------------------
# myCheckButton
#-----------------------------------------------------------------------------
def myChkButton(name='my_ChkButton', 
				valu=True, colo=None, 
				call=None, data=['dati']):
	""" crea un bottone di tipo check
		alla premuta del bottone viene eseguita la callback associata
	
		-> name nome associato alla label
		-> valu valore da associare
		-> colo colore assegnato al bottone
		-> call funzione da eseguire su evento
		-> data dati da passare alla funzione
	"""
	#callback debug
	def on_clicked(widg, *data):
		ena = widg.get_active()
		print "a) %s is %s" % (data, ("OFF", "ON")[ena])
		# change color
		#labe = widg.get_child()
		if widg.colo != None:
			if ena:
				widg.modify_fg(Gtk.STATE_NORMAL, Gdk.color_parse('green'))
				#labe.modify_fg(Gtk.STATE_NORMAL, Gdk.color_parse('green'))
			else:
				widg.modify_fg(Gtk.STATE_NORMAL, Gdk.color_parse('red'))
				#labe.modify_fg(Gtk.STATE_NORMAL, Gdk.color_parse('red'))

#chkButton    
	# istanzio l'oggetto
	butt = Gtk.CheckButton(name)
	# lo rendo visibile
	butt.show()
	# assegno il valore
	butt.set_active(valu)
	# assegno colore
	butt.colo = colo
	if colo != None:
		butt.modify_fg(Gtk.STATE_NORMAL, Gdk.color_parse(colo))
		
	# in assenza di callback usa quella di debug
	if call == None:
		call = on_clicked
	butt.connect('clicked', call, *data)
# <-
	return butt, call
#-----------------------------------------------------------------------------
def testChkButton():
#myChkButton
	# ridefinisco la callback        
	def on_clicked(widg, name, *data):
		ena = widg.get_active()
		print "b) %s is %s" % (name, ("OFF", "ON")[ena])
	# butt, call
	obje, othe = myChkButton(name='my_ChkButton', 
							 valu=True, colo='black', 
							# call= on_clicked, data=['myCheck',])
							 call= None, data=['myCheck',])
#myFrame    
	# fram,[labe,xBox]
	obj1, oth1 = myFrame(name='prova', obje=obje, colo='black',
						 bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
						 tBox='v' )
	#debug
	myViewObject(obje, [othe])
# <-
	return obj1

#-----------------------------------------------------------------------------
# myCheckButtonList
#-----------------------------------------------------------------------------
def myChkButList(name=["One","Two","Three"], 
				 valu=False, colo=None, 
				 call=None, data=['dati'],
				 tBox='h', aBox=[False, False, 1]):
	#callback debug
	def on_clicked(widg, ind, *data):
		ena = widg.get_active()
		print "a",
		print ind, data, ("OFF", "ON")[ena]
		
	# in assenza di callback uso quella di debug
	if call == None:
		call = on_clicked

	# funzione che istanzia oggetti tipo
	def myList(ind):
#myChkButton        
		# butt, [call,]
		return myChkButton(name=name[ind], 
							valu=False, colo=None, 
							call=call, data=[ind, data])
#myBoxList
	# xBox, [butt, call] * N
	obje, othe = myBoxList(name=name, tBox=tBox, 
						   aBox=aBox, func=myList)
# <-
	return obje, othe
#-----------------------------------------------------------------------------
def testChkButList():
#myChkButton    
	# ridefinisco la callback
	def on_clicked1(widg, ind, *data):
		ena = widg.get_active()
		print "%05s" %widg.props.label.replace('_',''), "is", ("OFF", "ON")[ena]
	# xBox, [butt, call] * N
	obje, othe = myChkButList(name=["Uno","Due","Tre"], 
							  valu=False, colo=None, 
							  call=on_clicked1, data=['uffi'],
							  tBox='h', aBox=[False, False, 1])
#myFrame    
	# fram,[labe,xBox]
	obj1, oth1 = myFrame(name='myButton', obje=obje, colo='black',
						 bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
						 tBox='v' )
	#debug
	myViewObject(obje, othe)
# <-
	return obj1

#-----------------------------------------------------------------------------
# myCheckButtonListLabel
#-----------------------------------------------------------------------------
def myChkButLisLabel(name=["One","Two","Three"], 
					 valu=False, colo=None, 
					 call=None, data=['dati'],
					 nLab='Label', cLab=None,
					 tBox='h', aBox=[False, False, 1]):
	"""     nLab name
			cLab color
	"""

	#callback debug
	def on_clicked(widg, ind, *data):
		ena = widg.get_active()
		print "a",
		print ind, data, ("OFF", "ON")[ena]
		
	# in assenza di callback uso quella di debug
	if call == None:
		call = on_clicked

	# funzione che istanzia oggetti tipo
	def myList(ind):
#myChkButton        
		# butt, call
		return myChkButton(name=name[ind], valu=False, colo=None, 
							call=None, data=[ind, data])
#myBoxList
	# xBox, [butt, call] * N
	obje, othe = myBoxList(name=name, tBox=tBox, 
						   aBox=aBox, func=myList)
#myLabel
	if cLab == None:
		cLab= 'blue'
	#name='myLabel', leng=0, prea=' ', post='', font='Arial 10', colo=Gdk.color_parse('black')
	labe = myLabel(name=nLab, 
				   leng=len(nLab)+1, prea=' ', post=' ', 
				   font='Courier 10', 
				   colo=cLab)
	# inserisco la label nella list degli oggetti
	othe.insert(0,[labe])
	# inserisco la label in testa alla box
	#child, expand=True, fill=True, padding=0
	obje.pack_start(labe, False, False, 0)
	obje.reorder_child(labe, 0)
# <-
	return obje, othe
#-----------------------------------------------------------------------------
def testChkButLisLabel():
#myChkButLisLabel    
	# ridefinisco la callback
	def on_clicked(widg, ind, *data):
		ena = widg.get_active()
		#print "b", widg, ind, idata
		print "%05s" %widg.props.label.replace('_',''), "is", ("OFF", "ON")[ena]
	# xBox, [labe, [butt, call] * N]
	obje, othe = myChkButLisLabel(name=["One","Two","Three"], 
								  valu=False, colo=None, 
								  call=on_clicked, data=[],
								  nLab='Label', cLab=None,
								  tBox='h', aBox=[False, False, 1])
#myFrame    
	# fram,[labe,xBox]
	obj1, oth1 = myFrame(name='myButton', obje=obje, colo='black',
						 bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
						 tBox='v' )
	#debug
	myViewObject(obje, othe)
# <-
	return obj1

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
		choi = 3
	else:
		# get first argument (scelta esterna)
		choi = int(sys.argv[1])

	if choi == 1:
		obje = testChkButton()
	elif choi == 2:
		obje = testChkButList()
	elif choi == 3:
		obje = testChkButLisLabel()
		
	# istanza l'applicazione principale
	self = MyWind(width=None, height=800, title="myChkButton %s" %myRev, center=True, color="#b0b0b0")
	self.vBox.pack_start(child=obje, expand=False, fill=False, padding=0)
	# cediamo il controllo alle gtk
	Gtk.main()
