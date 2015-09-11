#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" lista degli oggetti definiti:

	- myApp
"""

myRev = "(rev.150909)"
#-----------------------------------------------------------------------------
# Modules
#-----------------------------------------------------------------------------
from my00init import *
from my00initGtk import *

#-----------------------------------------------------------------------------
# myModules
#-----------------------------------------------------------------------------
from myWind import myBox1, myFrame1

#-----------------------------------------------------------------------------
# myDefines
#-----------------------------------------------------------------------------

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
					center=True, color="#bbbbbb", conf=0x003f, show=0):
		super(MyApp, self).__init__()

		# referenzio gli attributi passati
		self.title = title
		self.width = width
		self.height = height

		# imposta il titolo dell'applicazione
		self.set_title(self.title)
		# imposto il nome dell'oggetto uguale al titolo
		self.set_name(title.split()[0]) #150827

		# ridimensiono se viene passato almeno l'ampiezza
		if width != None:
			self.resize(width, height)
		# se richiesto centro la posizione
		if center:
			self.set_position(Gtk.WindowPosition.CENTER)

		# callbacks di uscita da eventi
		self.connect("delete-event", Gtk.main_quit)
		# intercettiamo la tastiera
		self.connect("key_press_event", self.doKeyPress)

		# se passato cambio colore
		if color:
			# change background color to Class
			chaBackColor(obj=self, css=self.get_name(), col=color) #150827

		# abilita la propria visualizzazione
		self.show()

		# attributi comuni ai vari contenitori
		homo = False
		spac = 0 
		expa = False
		fill = False
		padd = 1
		bord = 2
		colo = "#333333"

#aBox (application)
		# fram,[labe,xBox]
		aObj, oth1 = myFrame1(name='application', obje=None, colo=colo,
							 bord=bord, shad=Gtk.SHADOW_IN,
							 # [expand=True, fill=True, padding=1]
							 tBox='h', aBox=[expa, fill, padd],
							 show=show )
		self.aBox = oth1[1]

#gBox (aBox/global)
		# fram,[labe,xBox]
		gObj, oth1 = myFrame1(name='global', obje=None, colo=colo,
							 bord=bord, shad=Gtk.SHADOW_IN,
							 # [expand=True, fill=True, padding=1]
							 tBox='h', aBox=[expa, fill, padd],
							 show=show )
		self.gBox = oth1[1]

#mBox (aBox/main)
		# fram,[labe,xBox]
		mObj, oth1 = myFrame1(name='main', obje=None, colo=colo,
							 bord=bord, shad=Gtk.SHADOW_IN,
							 # [expand=True, fill=True, padding=1]
							 tBox='v', aBox=[expa, fill, padd],
							 show=show )
		self.mBox = oth1[1]

#uBox (mBox/menu)
		# fram,[labe,xBox]
		uObj, oth1 = myFrame1(name='menu', obje=None, colo=colo,
							 bord=bord, shad=Gtk.SHADOW_IN,
							 # [expand=True, fill=True, padding=1]
							 tBox='h', aBox=[expa, fill, padd],
							 show=show )
		self.uBox = oth1[1]

#bBox (mBox/body)
		# fram,[labe,xBox]
		bObj, oth1 = myFrame1(name='body', obje=None, colo=colo,
							 bord=bord, shad=Gtk.SHADOW_IN,
							 # [expand=True, fill=True, padding=1]
							 tBox='v', aBox=[expa, fill, padd],
							 show=show )
		self.bBox = oth1[1]

#sBox (mBox/status)
		# fram,[labe,xBox]
		sObj, oth1 = myFrame1(name='status', obje=None, colo=colo,
							 bord=bord, shad=Gtk.SHADOW_IN,
							 # [expand=True, fill=True, padding=1]
							 tBox='h', aBox=[expa, fill, padd],
							 show=show )
		self.sBox = oth1[1]

# scelta della configurazione desiderata
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
def testMyApp():
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
	self = MyApp(width=400, height=400, title="myApp %s" %myRev, 
					center=True, color="#bbbbbb", conf=0x003f, show=1) #150827
	return self

#-----------------------------------------------------------------------------
# myTry
#-----------------------------------------------------------------------------
def myTry01():
	testMyApp()

#-----------------------------------------------------------------------------
def myTry02():

	from my02TxtView import myTxtView

	self = testMyApp()

#myFraScrTexView
	#          0,   1,   2,   3,   4,    5,    6,       7 
	# fram,[labe,xBox,buff,text,cTag,clear,write,writeTag]
	fram,othe = myTxtView(name='logBuffer', colo="black",
							widt=400, heig=400, 
							font="courier 9", edit=False, 
							left=1, righ=1, bord=3,
							bFra=1, sFra=Gtk.SHADOW_ETCHED_OUT, tFra='v' )
	# insert object in apllication
	self.bBox.pack_start(fram, False, False, 1)
	
	# referenzio gli attributi
	self.cTag = othe[4]
	# referenzio i metodi
	self.clear = othe[5]
	self.write = othe[6] # *msg
	self.wriTg = othe[7] # str="", tag="blaWhi"
	
	# redirect sul proprio buffer text
	sys.stdout = self

	# scrivo qualcosa col colore di default
	self.write('ciao mondo')
	# cambio colore al volo
	self.wriTg(' crudele\n', "redWhi")    

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
		# draw Applications (MyApp)
		myTry01()
	elif choi == 2:
		# draw Applications (MyApp)
		myTry02()

	# avvia applicazione
	Gtk.main()
