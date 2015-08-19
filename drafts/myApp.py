#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" lista degli oggetti definiti:

	- myWind
	- myApp 		(150807)
	- myBox1 		(150807)
	- myFrame1 		(150807)
"""

myRev = "(rev.150807)"

#-----------------------------------------------------------------------------
# Modules
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# myModules
#-----------------------------------------------------------------------------
from my00init import *

#-----------------------------------------------------------------------------
# myDefines
#-----------------------------------------------------------------------------
def myBox1(tBox='v', homo=False, spac=0):
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
def myFrame1(name='myFrame', obje=None, colo='blue',
			bord=2, shad=Gtk.SHADOW_ETCHED_OUT, 
			tBox='v', aBox=[False, False, 1],
			xtBox='', xaBox=[False, False, 1],
			deb=False ):
	""" crea una cornice con un titolo
	
		-> name nome associato alla label della cornice
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

	# nasconde il bordo e il nome del frame
	if not deb:
		bord=0
		aBox=[False, False, 0]
		name = ""
		shad = Gtk.SHADOW_NONE

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
	xBox = myBox1(tBox)
	fram.add(xBox)
#object
	if obje != None:
		#child, expand=True, fill=True, padding=1
		xBox.pack_start(obje, *aBox)

#myBox (esterno)
	if (xtBox == 'v') or (xtBox == 'h'):  
		yBox = myBox1(xtBox)
		#child, expand=True, fill=True, padding=1
		yBox.pack_start(fram, *xaBox)
# <-
		return yBox, [labe, xBox, fram]
	else:    
# <-
		return fram, [labe, xBox]
	
#-----------------------------------------------------------------------------
# myClass
#-----------------------------------------------------------------------------
class MyApp(Gtk.Window):
	""" + window (self)                                                   
	"conf                                       .------------------------.
	"0001 - aBox            (h application)     | application            |
	"0002   - gBox            (h global)        |   .--------------------.
	"0004   - mBox            (v main)          |   | g | m | menu       |
	"0008     - uBox            (h menu)        |   | l | a .------------.
	"0010     - bBox            (v body)        |   | o | i | body       |
	"0020     - sBox            (h status)      |   | b | n |            |
	"                                           |   | a |   .------------.
	"                                           |   | l |   | status     |
	"                                           .---.---.----------------.
	"""	
	def __init__(self, width=None, height=400, title="myApp", 
					center=True, color="#bbbbbb", conf=0x003f, deb=0):
		super(MyApp, self).__init__()
		# imposto il nome dell'oggetto uguale al titolo
		self.set_name(title)

		self.width = width
		self.height = height
		# imposta il titolo dell'applicazione
		self.set_title(title)
		# dimensione
		if width != None:
			self.resize(width, height)
		# posizione
		if center:
			self.set_position(Gtk.WindowPosition.CENTER)

		# callback di uscita
		self.connect("delete-event", Gtk.main_quit)
		# intercettiamo la tastiera
		self.connect("key_press_event", self.doKeyPress)

		# attributes
		homo=False
		spac=0 
		expa=False
		fill=False
		padd=1
		bord=2
		colo="#333333"

#aBox (application)
		# fram,[labe,xBox]
		aObj, oth1 = myFrame1(name='application', obje=None, colo=colo,
							 bord=bord, shad=Gtk.SHADOW_IN,
							 # [expand=True, fill=True, padding=1]
							 tBox='h', aBox=[expa, fill, padd],
							 deb=deb )
		self.aBox = oth1[1]

#gBox (aBox/global)
		# fram,[labe,xBox]
		gObj, oth1 = myFrame1(name='global', obje=None, colo=colo,
							 bord=bord, shad=Gtk.SHADOW_IN,
							 # [expand=True, fill=True, padding=1]
							 tBox='h', aBox=[expa, fill, padd],
							 deb=deb )
		self.gBox = oth1[1]

#mBox (aBox/main)
		# fram,[labe,xBox]
		mObj, oth1 = myFrame1(name='main', obje=None, colo=colo,
							 bord=bord, shad=Gtk.SHADOW_IN,
							 # [expand=True, fill=True, padding=1]
							 tBox='v', aBox=[expa, fill, padd],
							 deb=deb )
		self.mBox = oth1[1]

#uBox (mBox/menu)
		# fram,[labe,xBox]
		uObj, oth1 = myFrame1(name='menu', obje=None, colo=colo,
							 bord=bord, shad=Gtk.SHADOW_IN,
							 # [expand=True, fill=True, padding=1]
							 tBox='h', aBox=[expa, fill, padd],
							 deb=deb )
		self.uBox = oth1[1]

#bBox (mBox/body)
		# fram,[labe,xBox]
		bObj, oth1 = myFrame1(name='body', obje=None, colo=colo,
							 bord=bord, shad=Gtk.SHADOW_IN,
							 # [expand=True, fill=True, padding=1]
							 tBox='v', aBox=[expa, fill, padd],
							 deb=deb )
		self.bBox = oth1[1]

#sBox (mBox/status)
		# fram,[labe,xBox]
		sObj, oth1 = myFrame1(name='status', obje=None, colo=colo,
							 bord=bord, shad=Gtk.SHADOW_IN,
							 # [expand=True, fill=True, padding=1]
							 tBox='h', aBox=[expa, fill, padd],
							 deb=deb )
		self.sBox = oth1[1]

		if conf == 0x003f: # all
			self.xBox = myBox1("v")
			self.add(self.xBox)
			# insert object in application (app, glo, mai, men, bod, sta)
			self.xBox.pack_start(child=aObj, expand=True, fill=True, padding=padd) # 0001
			self.aBox.pack_start(child=gObj, expand=expa, fill=fill, padding=padd) # 0002
			self.aBox.pack_start(child=mObj, expand=True, fill=True, padding=padd) # 0004
			self.mBox.pack_start(child=uObj, expand=expa, fill=fill, padding=padd) # 0008
			self.mBox.pack_start(child=bObj, expand=True, fill=True, padding=padd) # 0010
			self.mBox.pack_start(child=sObj, expand=expa, fill=fill, padding=padd) # 0020
		elif conf == 0x003e: # no application
			self.xBox = myBox1("h")
			self.add(self.xBox)
			# insert object in application (glo, mai, men, bod, sta)
			self.xBox.pack_start(child=gObj, expand=expa, fill=fill, padding=padd) # 0002
			self.xBox.pack_start(child=mObj, expand=True, fill=True, padding=padd) # 0004
			self.mBox.pack_start(child=uObj, expand=expa, fill=fill, padding=padd) # 0008
			self.mBox.pack_start(child=bObj, expand=True, fill=True, padding=padd) # 0010
			self.mBox.pack_start(child=sObj, expand=expa, fill=fill, padding=padd) # 0020
		elif conf == 0x0036: # no application, menu
			self.xBox = myBox1("h")
			self.add(self.xBox)
			# insert object in application (glo, mai, bod, sta)
			self.xBox.pack_start(child=gObj, expand=expa, fill=fill, padding=padd) # 0002
			self.xBox.pack_start(child=mObj, expand=True, fill=True, padding=padd) # 0004
			self.mBox.pack_start(child=bObj, expand=True, fill=True, padding=padd) # 0010
			self.mBox.pack_start(child=sObj, expand=expa, fill=fill, padding=padd) # 0020
		elif conf == 0x0016: # no application, menu, status
			self.xBox = myBox1("h")
			self.add(self.xBox)
			# insert object in application (glo, mai, bod)
			self.xBox.pack_start(child=gObj, expand=expa, fill=fill, padding=padd) # 0002
			self.xBox.pack_start(child=mObj, expand=True, fill=True, padding=padd) # 0004
			self.mBox.pack_start(child=bObj, expand=True, fill=True, padding=padd) # 0010
		elif conf == 0x0012: # no application, main, menu, status
			self.xBox = myBox1("h")
			self.add(self.xBox)
			# insert object in application (glo, bod)
			self.xBox.pack_start(child=gObj, expand=expa, fill=fill, padding=padd) # 0002
			self.xBox.pack_start(child=bObj, expand=True, fill=True, padding=padd) # 0010
		elif conf == 0x003c: # no application, global
			self.xBox = myBox1("h")
			self.add(self.xBox)
			# insert object in application (mai, men, bod, sta)
			self.xBox.pack_start(child=mObj, expand=True, fill=True, padding=padd) # 0004
			self.mBox.pack_start(child=uObj, expand=expa, fill=fill, padding=padd) # 0008
			self.mBox.pack_start(child=bObj, expand=True, fill=True, padding=padd) # 0010
			self.mBox.pack_start(child=sObj, expand=expa, fill=fill, padding=padd) # 0020
		elif conf == 0x0038: # no application, global, main
			self.xBox = myBox1("v")
			self.add(self.xBox)
			# insert object in application (men, bod, sta)
			self.xBox.pack_start(child=uObj, expand=expa, fill=fill, padding=padd) # 0008
			self.xBox.pack_start(child=bObj, expand=True, fill=True, padding=padd) # 0010
			self.xBox.pack_start(child=sObj, expand=expa, fill=fill, padding=padd) # 0020
		elif conf == 0x0030: # no application, global, main, menu
			self.xBox = myBox1("v")
			self.add(self.xBox)
			# insert object in application (bod, sta)
			self.xBox.pack_start(child=bObj, expand=True, fill=True, padding=padd) # 0010
			self.xBox.pack_start(child=sObj, expand=expa, fill=fill, padding=padd) # 0020
		elif conf == 0x0010: # no application, global, main, menu, status
			self.xBox = myBox1("v")
			self.add(self.xBox)
			# insert object in application (bod)
			self.xBox.pack_start(child=bObj, expand=True, fill=True, padding=padd) # 0010
		elif conf == 0x0000: # no application, global, main, menu, body, status
			self.bBox = myBox1("v")
			self.add(self.bBox)
			# insert object in application ()

		if color:
			# change background color to Class
			chaBackColor(obj=self, css=title, col=color)
		# visualizza il tutto
		self.show_all()

	def doKeyPress(self, widget, event):
		# intercetto ctrl
		if (event.state == Gdk.ModifierType.CONTROL_MASK):
			#print "Ctrl", Gdk.keyval_name(event.keyval)
			pass
		else:
			# leggo il tasto premuto
			keyname = Gdk.keyval_name(event.keyval)
			#print "the button %s was pressed" % keyname
			if keyname == "Escape":
				Gtk.main_quit()

#-----------------------------------------------------------------------------
class MyWind(Gtk.Window):
	""" + window (self)                         .------------------------.
	"     - vBox                                | vertical               |
	"       - hBox                              |   .--------------------.
	"                                           |   | horizontal         |
	"                                           |   |                    |
	"                                           .---.--------------------.
	"""
	def __init__(self, width=None, height=400, title="myWind", center=True, color=""):
		super(MyWind, self).__init__()
		# imposto il nome dell'oggetto uguale al titolo
		self.set_name(title)

		self.title = title
		self.width = width
		self.height = height
		# imposta il titolo dell'applicazione
		self.set_title(self.title)
		# dimensione
		if width != None:
			self.resize(width, height)
		# posizione
		if center:
			self.set_position(Gtk.WindowPosition.CENTER)

		# callback di uscita
		self.connect("delete-event", Gtk.main_quit)
		# intercettiamo la tastiera
		self.connect("key_press_event", self.doKeyPress)

		#vBox (application)
		self.vBox = Gtk.VBox(homogeneous=False, spacing=0)
		self.add(self.vBox)
		#hBox (application)
		self.hBox = Gtk.HBox(homogeneous=False, spacing=0)
		self.vBox.pack_start(child=self.hBox, expand=False, fill=False, padding=0)

		if color:
			# change background color to Class
			chaBackColor(obj=self, css=title, col=color)
		# visualizza il tutto
		self.show_all()

	def doKeyPress(self, widget, event):
		# intercetto ctrl
		if (event.state == Gdk.ModifierType.CONTROL_MASK):
			#print "Ctrl", Gdk.keyval_name(event.keyval)
			pass
		else:
			# leggo il tasto premuto
			keyname = Gdk.keyval_name(event.keyval)
			#print "the button %s was pressed" % keyname
			if keyname == "Escape":
				Gtk.main_quit()

#-----------------------------------------------------------------------------
# myTry
#-----------------------------------------------------------------------------
def myTry01():
	# istanza l'applicazione 
	#  width=None, height=400, title="myApp", center=True
	self = MyWind(title="myWind")

	# attributes
	colo="#333333"
	bord=2 			# external
	expa=False
	fill=False
	padd=1 			# internal
	deb=True

#aBox (application)
	# fram,[labe,xBox]
	aObj, oth1 = myFrame1(name='application', obje=None, colo=colo,
						bord=bord, shad=Gtk.SHADOW_IN,
						tBox='h', aBox=[expa, fill, padd],
						#xtBox='h', xaBox=[expa, fill, padd],
						deb=deb )
	self.aBox = oth1[1]

	# inserimento nel contenitore
	self.vBox.pack_start(child=aObj, expand=False, fill=False, padding=0)

#gBox (aBox/global)
	# fram,[labe,xBox]
	gObj, oth1 = myFrame1(name='global', obje=None, colo=colo,
						bord=bord, shad=Gtk.SHADOW_IN,
						tBox='h', aBox=[expa, fill, padd],
						#xtBox='h', xaBox=[expa, fill, padd],
						deb=deb )
	self.gBox = oth1[1]

	# inserimento nel contenitore
	self.vBox.pack_start(child=gObj, expand=False, fill=False, padding=0)

#-----------------------------------------------------------------------------
def myTry02():
	""" + window (self)                                                   
	"conf                                       .------------------------.
	"0001 - aBox            (h application)     | application            |
	"0002   - gBox            (h global)        |   .--------------------.
	"0004   - mBox            (v main)          |   | g | m | menu       |
	"0008     - uBox            (h menu)        |   | l | a .------------.
	"0010     - bBox            (v body)        |   | o | i | body       |
	"0020     - sBox            (h status)      |   | b | n |            |
	"                                           |   | a |   .------------.
	"                                           |   | l |   | status     |
	"                                           .---.---.----------------.
	"""	
	# istanza l'applicazione 
	self = MyApp(width=400, height=400, title="myApp", 
					center=True, color="#bbbbbb", conf=0x003f, deb=1)

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

	if choi == 1:   # (MyWind)
		# draw window
		myTry01()
	elif choi == 2: # (MyApp) 
		# draw application
		myTry02()

	# avvia applicazione
	Gtk.main()
