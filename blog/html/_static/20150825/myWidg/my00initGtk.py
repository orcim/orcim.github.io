#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" lista oggetti definiti:
	
	- chaStockLabel, chaBackColor
	- myDialog
"""

myRev = "(rev.150824)"
#-----------------------------------------------------------------------------
# Modules
#-----------------------------------------------------------------------------
from my00init import *


#-----------------------------------------------------------------------------
# Gtk2 = Gtk3 (retrocompatibilità)
#-----------------------------------------------------------------------------
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

#-----------------------------------------------------------------------------
# myDefine
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
# myClass
#-----------------------------------------------------------------------------
class myDialog(Gtk.Dialog):
	""" Dialog di supporto
		 quando si vuol interagire velocemente con l'utente
	"""
	def __init__(self, parent=None, title="myDialog", mesg="Vuoi Confermare?", 
					width=3, heigth=3, x=None, y=0, icon=True):
		Gtk.Dialog.__init__(self, title, parent, 0,
			(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
			 Gtk.STOCK_OK, Gtk.ResponseType.OK))

		# abilita le icone che per default sono nascoste
		if icon:
			# prendeo la referenza degli oggetti presenti
			for obj in self.action_area.get_children():
				# abilito la vista dell'immagine
				obj.set_always_show_image (True)

		# se x è presente voglio scegliere la posizione del nostro dialog
		if x==None:
			# altrimenti la centro nella dimensione del nostro schermo
			self.set_position(Gtk.WindowPosition.CENTER)
		else:
			self.move(x, y)
		# imposto la dimensione
		self.set_default_size(width,heigth)
		# prendo la referenza del box interno
		box = self.get_content_area()
		# istanzio una label per il message
		label = Gtk.Label(mesg)
		# e la inserisco
		box.add(label)
		# visualizzo il tutto
		self.show_all()
#-----------------------------------------------------------------------------
def testMyDialog():
	# istanzio una dialog
	dial = myDialog(parent=None, title="myDialog", mesg="Vuoi Confermare?", 
			width=3, heigth=3, x=None, y=0, icon=True)
	# avvio l'esecuzione
	resp = dial.run()
	# attendo la risposta
	if resp == Gtk.ResponseType.OK:
		print("OK")
	elif resp == Gtk.ResponseType.CANCEL:
		print("Cancel")
	# distruggo l'istanza
	dial.destroy()

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

	if choi == 1:
		"test myDialog"
		testMyDialog()
