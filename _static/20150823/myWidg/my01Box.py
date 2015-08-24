#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" lista degli oggetti definiti:

	- myViewObject
	- myBox     - myBoxList
	- myFrame   - myFraList
	- myEvent   - myEveList
"""

myRev = "(rev.150823)"
#-----------------------------------------------------------------------------
# Modules
#-----------------------------------------------------------------------------
from my00init import *
from gi.repository import Pango

#-----------------------------------------------------------------------------
# myModules
#-----------------------------------------------------------------------------
from myWind import MyWind

#-----------------------------------------------------------------------------
# myDefines
#-----------------------------------------------------------------------------
def myViewObject(obje, othe):
	print " obje:", obje
	# view objects
	for ind, ele in enumerate(othe):
		print "row%02d:" %ind, ele

#-----------------------------------------------------------------------------
# myBox
#-----------------------------------------------------------------------------
def myBox(tBox='v', homo=False, spac=0):
	""" crea un contenitore del tipo richiesto
	
		-> tBox tipo di contenitore v/h 
		-> homo tipo omogeneita'
		-> spac spazio da mantenere intorno all'oggetto
	"""
	if tBox == 'v':
		# creo un Vertical Box
		xBox = Gtk.VBox(homo,spac)
	elif tBox == 'h':
		# creo un Horizontal Box
		xBox = Gtk.HBox(homo,spac)
	xBox.show()
# <-
	return xBox
#-----------------------------------------------------------------------------
def testBox():
#myBox    
	xBox = myBox('h', homo=False, spac=0)
	#child, expand=True, fill=True, padding=1
	#xBox.pack_start(obje, False, False, 1)
	
	# inserisco alcuni oggetti
	for ele in ("yellow","blue","green","red","brown"):
	# labels
		labe = Gtk.Label(" I am %s" %ele)
		labe.show()
	# events
		# istanzio l'oggetto
		eBox = Gtk.EventBox()
		# lo rendo visibile
		eBox.show()
		# imposto il colore di sfondo
		eBox.modify_bg(Gtk.STATE_NORMAL, Gdk.color_parse(ele))
	# xBox
		# inerisco nei contenitori
		eBox.add(labe)
		#child, expand=True, fill=True, padding=1
		xBox.pack_start(eBox, False, False, 1)
#myFrame    
	# fram, [labe, xBox]
	fram, othe = myFrame(name='Box', obje=xBox, colo='black',
						bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
						tBox='v', aBox=[False, False, 1] )
# <-
	return fram

#-----------------------------------------------------------------------------
# myBoxList
#-----------------------------------------------------------------------------
def myBoxList(name=["Obj1","Obj2"],
			  tBox='v', aBox=[False, False, 1], 
			  func=None):
	# istanzio il contenitore
	xBox = myBox(tBox)
	listObj = []
	for ind, ele in enumerate(name):
		# istanza gli oggetti
		obje,othe = func(ind)
		listObj.append([obje,othe])
		#child, expand=True, fill=True, padding=0
		xBox.pack_start(obje, *aBox)
# <-
	return xBox, listObj
#-----------------------------------------------------------------------------
def testBoxList():
#myBoxList
	# funzione che istanzia gli oggetti tipo
	def myList(ind, *para):
		# istanzio una label
		labe = Gtk.Label(nam[ind])
		# la rendo visibile
		labe.show()
		# imposto il colore
		labe.modify_fg(Gtk.STATE_NORMAL, Gdk.color_parse(col[ind]))
		# <-
		return labe, None

	# define attributes
	nam = ("Obj1","Obj2","Obj3")
	col = ('blue','green','red')            
	# xBox, listObj
	obje, othe = myBoxList(name= nam,
						   tBox='h', aBox=[False, False, 1], 
						   func=myList)
	#debug
	myViewObject(obje, othe)
# <-
	return obje

#-----------------------------------------------------------------------------
# myFrame
#-----------------------------------------------------------------------------
def myFrame(name='myFrame', obje=None, colo='blue',
			bord=2, shad=Gtk.SHADOW_ETCHED_OUT, 
			tBox='v', aBox=[False, False, 1],
			xtBox='', xaBox=[False, False, 1],
			):
	""" crea una cornice con un titolo
	
		-> name nome associato alla label
		-> obje oggetto da inserire
		-> colo colore label
		-> bord bordo riservato all'esterno
		-> shad tipo di cornice
			Gtk.SHADOW_NONE, Gtk.SHADOW_IN, Gtk.SHADOW_OUT, 
			Gtk.SHADOW_ETCHED_IN, Gtk.SHADOW_ETCHED_OUT
		-> tBox tipo di contenitore v/h interno 
		-> aBox attributi del contenitore interno
		-> xtBox tipo di contenitore v/h esterno 
		-> xaBox attributi del contenitore esterno
	"""
#frame
	if name != "":
		name = " "+name+" "
	fram = Gtk.Frame(label=name)
	# la rendo visibile
	fram.show()
	# imposto il bordo (esterno)
	fram.set_border_width(bord)
	fram.set_shadow_type(shad)
#label
	# referenzio la label della Frame
	labe = fram.get_label_widget()
	# attivo il markup
	labe.set_markup("<b>%s</b>" %name)
	# imposto il colore
	labe.modify_fg(Gtk.STATE_NORMAL, Gdk.color_parse(colo))
#myBox (interno)
	xBox = myBox(tBox)    
	fram.add(xBox)
#object
	if obje != None:
		#child, expand=True, fill=True, padding=1
		xBox.pack_start(obje, *aBox)

#myBox (esterno)
	if (xtBox == 'v') or (xtBox == 'h'):  
		yBox = myBox(xtBox)
		#child, expand=True, fill=True, padding=1
		yBox.pack_start(fram, *xaBox)
# <-
		return yBox, [labe, xBox, fram]
	else:    
# <-
		return fram, [labe, xBox]
#-----------------------------------------------------------------------------
def testFrame():
#label
	if 0:
		lab1 = None
	else:
		#str
		lab1 = Gtk.Label()
		# uso il markup
		lab1.set_markup(' <b>prova</b> ')
		# la rendo visibile
		lab1.show()
		# imposto il colore
		lab1.modify_fg(Gtk.STATE_NORMAL, Gdk.color_parse('blue'))
#myFrame    
	# fram,[labe,xBox]
	obje, othe = myFrame(name='myFrame', obje=lab1, colo='#f000f0',
						bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
						tBox='v', aBox=[False, False, 10])
# <-
	return obje

#-----------------------------------------------------------------------------
# myFraList
#-----------------------------------------------------------------------------
def myFrameList(name=["frame00","frame01"], colo='black',
				oFra=None, bFra=2, sFra=Gtk.SHADOW_ETCHED_OUT, 
				tFra='v', aFra=[False, False, 1],
				tBox='v', aBox=[False, False, 1]):
	# funzione che istanzia oggetti tipo
	def myList(ind):
#myFrame
		#fram,[labe,xBox]
		print "=>", colo[ind]
		return myFrame(name[ind], oFra, colo, bFra, sFra, tFra)
#myBoxList
	# xBox, [fram,[labe,xBox]] * N
	obje, othe = myBoxList(name=name, tBox=tBox, 
						   aBox=aBox, func=myList)
# <-
	return obje, othe
#-----------------------------------------------------------------------------
def testFraList():
#myFraList
	# xBox, [fram,[labe,xBox]] * N
	obje, othe = myFrameList(name=["frame00","frame01"], colo='black',
							oFra=None, bFra=2, sFra=Gtk.SHADOW_ETCHED_OUT, 
							tFra='v', aFra=[False, False, 1],
							tBox='v', aBox=[False, False, 5])
	#debug
	myViewObject(obje, othe)
# <-
	return obje

#-----------------------------------------------------------------------------
# myEvent
#-----------------------------------------------------------------------------
def myEvent(name="myEvent", 
			colo='yellow', font='Courier 10', 
			call=None, data=[]):
	""" crea un contenitore sensibile agli eventi con una label al suo interno
	 
		-> name nome associato alla label
		-> colo colore assegnato
		-> font font usato per il testo
		-> call funzione da eseguire su evento
		-> data dati da passare alla funzione
	"""
	#callback debug
	def on_clicked(widg, *data):
		print widg
#eventBox
	# istanzio l'oggetto
	eBox = Gtk.EventBox()
	# lo rendo visibile
	eBox.show()
	# associo un attributo
	eBox.status = [0]
	# imposto il colore di fondo
	eBox.modify_bg(Gtk.STATE_NORMAL, Gdk.color_parse(colo))
	# in assenza di callback uso quella di debug
	if call == None:
		call = on_clicked
	eBox.connect('button-release-event', call, *data)
#label
	if name:
		# istanzio l'oggetto
		labe = Gtk.Label(name)
		# lo rendo visibile
		labe.show()
		# imposto un font
		labe.modify_font(Pango.FontDescription(font))
		# aggiungo l'oggetto
		eBox.add(labe)
	else:
		labe = None
# <-
	return eBox, [labe, call]
#-----------------------------------------------------------------------------
def testEvent():
	# ridefinisco la callback 
	def on_clicked(widg, *data):
		msg = widg.get_child().get_text()
		if msg == 'statusOn_':
			widg.status[0] = 0
			widg.modify_bg(Gtk.STATE_NORMAL, Gdk.color_parse("red"))
			widg.get_child().set_text('statusOff')
		else:
			widg.modify_bg(Gtk.STATE_NORMAL, Gdk.color_parse("green"))
			widg.get_child().set_text('statusOn_')
			widg.status[0] = 1
		print ("Off","On")[widg.status[0]]
	# eBox,[labe,call]
	obje, othe = myEvent(name="statusOn_", 
						 colo='yellow', font='Courier 10', 
						 call=on_clicked, data=[])
#myFrame    
	# fram,[labe,xBox]
	obj1, oth1 = myFrame(name='myEvent', obje=obje, colo='black',
						bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
						tBox='v' )
# <-
	return obj1

#-----------------------------------------------------------------------------
# myEveList
#-----------------------------------------------------------------------------
def myEveList(name=["event00","event01"], 
			  cEve='yellow', fEve='Courier 10',
			  call=None, data=[],
			  tBox='v', aBox=[False, False, 1]):
	#callback debug
	def on_clicked(widg, eve, ind, *data):
		print "event%02d" %ind
	# in assenza di callback uso quella di debug
	if call == None:
		call = on_clicked
		
	# funzione che istanzia oggetti tipo
	def myList(ind):
#myEvent
		# eBox, [labe,call]
		return myEvent(name[ind], 
					   cEve, fEve, call, [ind, data])
#myBoxList
	# xBox, [eBox, [labe,call]] * N
	obje, othe = myBoxList(name=name, tBox=tBox, 
						   aBox=aBox, func=myList)
# <-
	return obje, othe
#-----------------------------------------------------------------------------
def testEveList():
#myEvent
	# xBox, [eBox, [labe,call]] * N
	obje, othe = myEveList(name=["event00","event01","event02"], 
						   cEve='yellow', fEve='Courier 10',
						   call=None, data=[],
						   tBox='v', aBox=[False, False, 1])
	# cambio colore di fondo della seconda riga
	othe[1][0].modify_bg(Gtk.STATE_NORMAL, Gdk.color_parse("green"))
#myFrame    
	# fram,[labe,xBox]
	obj1, oth1 = myFrame(name='myEvent', obje=obje, colo='black',
						bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
						tBox='v' )
	#debug
	# myViewObject(obje, othe)
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
		choi = 1
	else:
		# get first argument (scelta esterna)
		choi = int(sys.argv[1])

	# oggetti singoli	
	if choi == 1:
		obje = testBox()
	elif choi == 2:
		obje = testFrame()
	elif choi == 3:
		obje = testEvent()

	# lista di oggetti
	elif choi == 11:
		obje = testBoxList()
	elif choi == 12:
		obje = testFraList()
	elif choi == 13:
		obje = testEveList()

	# istanza l'applicazione principale
	self = MyWind(width=None, height=800, title="myBox", center=True, color="#aaaaaa")
	self.vBox.pack_start(child=obje, expand=False, fill=False, padding=0)

	# cediamo il controllo alle gtk
	Gtk.main()
