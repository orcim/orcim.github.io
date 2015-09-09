#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" lista degli oggetti definiti:

	- myRadButton      
	- myRadButList
	- myRadButLisLabel
"""

myRev = "(rev.150904)"
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
# myRadioButton
#-----------------------------------------------------------------------------
def myRadButton(name='myRadButton', 
				chil=None, valu=0, 
				call=None, data=['dati']):
	""" crea un bottone di tipo radio
		alla premuta del bottone viene eseguita la callback associata

		-> name nome associato alla label
		-> chil widget di riferimento
		-> valu indica il valore selezionato
		-> call funzione da eseguire su evento
		-> data dati da passare alla funzione        
	"""
	#callback debug    
	def on_clicked(widg, *data):
		# descrivo solo quello attivato
		try:
			if widg.get_active():
				print data[0]
		except:
			pass
#radioButton
	# istanzio un bottone
	butt = Gtk.RadioButton(name)
	# lo rendo visibile
	butt.show()
	# attivo il button
	butt.set_active(valu)

	# in assenza di callback usa quella di debug
	if call == None:
		call = on_clicked
	butt.connect('clicked', call, *data)
# <-
	return butt, call
#-----------------------------------------------------------------------------
def testRadButton():
#radButton
	# ridefinisco la callback        
	def on_clicked(widg, *data):
		# descrivo solo quello attivato
		try:
			if widg.get_active():
				print data[0]
		except:
			pass
	# butt, call
	obje, othe = myRadButton(name='primo', 
							chil=None, valu=False, 
							call= on_clicked, data=['myRadio',])
#myFrame    
	# fram,[labe,xBox]
	obj1, oth1 = myFrame(name='myRadioButton', obje=obje, colo='black',
						 bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
						 tBox='v' )
	#debug
	myViewObject(obje, [othe])
# <-
	return obj1

#-----------------------------------------------------------------------------
# myRadioButtonList
#-----------------------------------------------------------------------------
def myRadButList(name=["One","Two","Three"], 
				 chil=None, valu=0, 
				 call=None, data=['dati'],
				 tBox='h', aBox=[False, False, 1]):
	#callback debug
	def on_clicked(widg, ind, *data):
		ena = widg.get_active()
		if ena:
			print "a", "%05s" %widg.props.label.replace('_',''), 
			print ind, data 
		
	# in assenza di callback uso quella di debug
	if call == None:
		call = on_clicked

	# funzione che istanzia oggetti tipo
	def myList(ind):
#myRadButton
		# butt,[call,]
		return myRadButton(name=name[ind], 
						   chil=chil, valu=False, 
						   call=call, data=[ind, data])
#myBoxList
	# xBox, [butt,call] * N
	obje, othe = myBoxList(name=name, tBox=tBox, 
						   aBox=aBox, func=myList)
	# prendo come capogruppo la prima istanza
	gro = othe[0][0].get_group()
	for ele in othe[1:]:
		# imposto il capogruppo alle altre istanze
		ele[0].join_group(gro[0])
	# rendo attivo il button
	if type(valu) == type(1):
		othe[valu][0].set_active(True)
# <-
	return obje, othe
#-----------------------------------------------------------------------------
def testRadButList():
#myRadButton    
	# ridefinisco la callback
	def on_clicked(widg, ind, *data):
		ena = widg.get_active()
		if ena:
			print "b", "%05s" %widg.props.label.replace('_',''), 
			print ind, data 
	# xBox, [butt,call] * N
	obje, othe = myRadButList(name=["One","Two","Three"], 
							  chil=None, valu=1, 
							  call=on_clicked, data=[],
							  tBox='h', aBox=[False, False, 1])
#myFrame    
	# fram,[labe,xBox]
	obj1, oth1 = myFrame(name='select', obje=obje, colo='black',
						 bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
						 tBox='v' )
	#debug
	myViewObject(obje, othe)
# <-
	return obj1

#-----------------------------------------------------------------------------
# myRadioButtonListLabel
#-----------------------------------------------------------------------------
def myRadButLisLabel(name=["One","Two","Three"], 
					 chil=None, valu=False, 
					 call=None, data=['dati'],
					 nLab='Label', cLab=None,
					 tBox='h', aBox=[False, False, 1]):
	"""     nLab name
			cLab color
	"""

	#callback debug
	def on_clicked(widg, ind, *data):
		ena = widg.get_active()
		if ena:
			print "a", "%05s" %widg.props.label.replace('_',''),
			print ind, data 
		
	# in assenza di callback uso quella di debug
	if call == None:
		call = on_clicked

	# funzione che istanzia oggetti tipo
	def myList(ind):
#myRadButton
		# butt, call
		return myRadButton(name=name[ind], 
						   chil=chil, valu=False, 
						   call=call, data=[ind, data])
#myBoxList
	# xBox, [butt, call] * N
	obje, othe = myBoxList(name=name, tBox=tBox, 
						   aBox=aBox, func=myList)
	# prendo come capogruppo la prima istanza
	gro = othe[0][0].get_group()
	for ele in othe[1:]:
		# imposto il capogruppo alle altre istanze
		ele[0].join_group(gro[0])
	# rendo attivo il button
	if type(valu) == type(1):
		othe[valu][0].set_active(True)
#myLabel
	if cLab == None:
		cLab='blue'
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
def testRadButLisLabel():
#radButton    
	# ridefinisco la callback
	def on_clicked(widg, ind, *data):
		ena = widg.get_active()
		if ena:
			print "b", "%05s" %widg.props.label.replace('_',''), 
			print ind, data 
	# xBox, [labe, [butt, call] * N]
	obje, othe = myRadButLisLabel(name=["One","Two","Three"], 
								  chil=None, valu=2, 
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
		obje = testRadButton()
	elif choi == 2:
		obje = testRadButList()
	elif choi == 3:
		obje = testRadButLisLabel()
		
	# istanza l'applicazione principale
	self = MyWind(width=None, height=800, title="myBox\ %s" %myRev, center=True, color="#b0b0b0")
	self.vBox.pack_start(child=obje, expand=False, fill=False, padding=0)
	# cediamo il controllo alle gtk
	Gtk.main()
