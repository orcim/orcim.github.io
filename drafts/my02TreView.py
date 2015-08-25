#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
""" widgets definiti:

	- ctlEnter
	- addView
	- addTree
	- getRecord
	- myTreView  
	- myTreStore
	- myExpander
	- myExpField
	rev.140620 + myTreStore, addTree
	rev.140623 + myExpander, myExpField, treeView(expand, collapse)
	rev.140630 + printTreeStore, addField, myTreField
		-> addTree, myTreStore
	rev.140701 ~ myTreStore, myExpField
"""
#-----------------------------------------------------------------------------
# myModules
#-----------------------------------------------------------------------------
from my00init import *
from gi.repository import Pango
myRev = "(rev.140701)"

from myApp import MyWind
from my01Box import myViewObject, myBoxList, myFrame
from my02TxtView import myScrolled
#-----------------------------------------------------------------------------
# myApplet
#-----------------------------------------------------------------------------
def ctlEnter(obj, event, view):
	""" {ctrl+Enter}
	"""
	# intercetto solo ctrl+Enter
	if (event.state == Gdk.CONTROL_MASK) and (event.keyval== Gtk.keysyms.Return):
		# referenzio il modello (treeStore) e l'indice del record selezionato
		model, iter = view.get_selection().get_selected()
		# deve esistere un elemento selezionato
		if iter:
			# leggo il primo campo del record selezionato
			ele = model.get_value(iter, 0)
			print "hide id:",ele
			# elimino il record
			model.remove (iter)

#-----------------------------------------------------------------------------
def addView(tree, scro, *reco):
	""" aggiunge un record alla treeView 
		 e aggiorna lo scrool
	"""
	# leggo il modello
	stor = tree.get_model()
	# inserisco record dati
	pare = stor.append(reco)
	# scrollbar
	if scro != None:	
		# aggiorna lo scroll verticale
		vad = tree.get_vadjustment()
		vad.step_increment = 100.0 # altezza testo
		# #vad.value = vad.upper - vad.page_increment + vad.step_increment
		# vad.value += vad.step_increment * 2
		
		#scro.scroll_to_mark(stor.append(reco), 0)
		if 0:
			#print vad.step_increment, vad.page_increment, vad.page_size 
			print vad.value, vad.lower, vad.upper  

	return pare

#-----------------------------------------------------------------------------
def addTree(tree, scro, pare, *reco):
	""" aggiunge un record alla treeView 
		 e aggiorna lo scrool
	"""
	# leggo il modello
	stor = tree.get_model()
	# inserisco record dati
	pare = stor.append(pare, reco)
	# scrollbar
	if scro != None:
		# aggiorna lo scroll verticale
		vad = tree.get_vadjustment()
		vad.step_increment = 100.0 # altezza testo

	return pare

#-----------------------------------------------------------------------------
def addField(tree, scro=None, pare=None, colo=[], reco=[]):
	""" aggiunge un record alla treeView 
		 e aggiorna lo scrool
	"""
	# add color fields
	if colo == []:
		colo.append('#fafad2')
		colo.append('#fafac2')
	reco.extend(colo)

	# leggo il modello
	stor = tree.get_model()
	# inserisco record
	pare = stor.append(pare, reco)
	# scrollbar
	if scro != None:
		# aggiorna lo scroll verticale
		vad = tree.get_vadjustment()
		vad.step_increment = 100.0 # altezza testo

	return pare

#-----------------------------------------------------------------------------
def printTreeStore(stor):
	""" print all items of treeStore
	"""
	def printTreeRows(stor, treeiter, indent):
		""" print all items of treeStore
		"""
		while treeiter != None:
			print indent + str(stor[treeiter][:])
			# check next iter
			if stor.iter_has_child(treeiter):
				# get child
				child = stor.iter_children(treeiter)
				printTreeRows(stor, child, indent + "->")
			# next item
			treeiter = stor.iter_next(treeiter)

	rootiter = stor.get_iter_first()
	printTreeRows(stor, rootiter, "")

#-----------------------------------------------------------------------------
def getRecord(tree, path):
	""" ritorna i dati della riga selezionata
	"""
	# leggo il modello
	sto = tree.get_model()
	# prendo la riga
	ite = sto.get_iter(path)
	rec = []
	# legge la riga selezionata
	for ele in range(sto.get_n_columns()):
		# legge i campi della riga selezionata con 'ite'
		rec.append(sto.get_value(ite, ele))
	return rec
	
#-----------------------------------------------------------------------------
# myTreeView
#-----------------------------------------------------------------------------
def myTreView(name=["->", "Id", "->", "Name"], 
				call=None, data=['dati'],
				bord=1, font='Courier bold 9', 
				cCol=['white','gray','white','gray'], 
				widt=200, heig=100,
				shad=Gtk.SHADOW_ETCHED_IN, 
				poli=(Gtk.POLICY_AUTOMATIC, Gtk.POLICY_AUTOMATIC)):
	#item=, call=on_activated_makView):
	""" crea una TreeView

		-> name lista campi
		-> call funzione da eseguire su evento
		-> data dati da passare alla funzione
		-> bord margine esterno dello scroolbar
		-> font font da usare per le celle
		-> cCol lista colore di fondo delle colonne (name * N)
		-> widt ampiezza
		-> heig altezza
		-> shad tipo di cornice
			Gtk.SHADOW_NONE, Gtk.SHADOW_IN, Gtk.SHADOW_OUT, 
			Gtk.SHADOW_ETCHED_IN, Gtk.SHADOW_ETCHED_OUT
		-> poli politiche di visibilita delle barre di scorrimento
			(horizontal,vertical)
			POLICY_AUTOMATIC whether you need
			POLICY_ALWAYS leave the scrollbars
	"""
	#callback debug    
	def row_activated(widg, path, colu, *data):
		pass
		# leggo record selezionato 
		#  dal doppio click o dal enter
		# rec = getRecord(widg,path)
		
#listStore  
	if 0:  
		# costruisco il comando per l'istanza
		#  stor = Gtk.ListStore(gobject.TYPE_STRING, other..)
		cmd = "stor = Gtk.ListStore("
		for ele in name:
			# aggiungo il tipo
			cmd += str(type(ele))[7:10]+','
		cmd += ")"
		# istanzio
		exec(cmd)
	else:
		mode = [GObject.TYPE_STRING,]* (len(name))
		stor = Gtk.ListStore(*mode)
#treeView
	tree = Gtk.TreeView(stor)
	tree.show()
#callback    
	# in assenza di callback usa quella di debug
	if call == None:
		call = row_activated
	# callback su doppio click o enter
	tree.connect('row-activated', call)
	# aggiungo evento tastiera per intercettare ctrl+Enter
	tree.set_events(Gdk.EventMask.KEY_PRESS_MASK)
	# # associamo la callback all'evento
	# tree.connect("key-press-event", ctlEnter, tree)
#cellRender + viewColumn
	# aggiungo le colonne e le celle
	colu = []
	cell = []
	for ind, ele in enumerate(name):
		# qui bisognerebbe istanziare la cella
		#  in base al tipo!
	# istanzio cella di testo
		cel = Gtk.CellRendererText()
		# se non esistono colori 
		if cCol:
			# imposto i colori
			cel.set_property('cell-background', cCol[ind])
		if font:
			# imposto il font
			cel.set_property('font', font)
	# istanzio colonna
		col = Gtk.TreeViewColumn(ele, cel, text=ind)
		# crea un contorno (sembra non funzionare)
		col.set_spacing(10)
	# aggiungo la colonna alla tree
		tree.append_column(col)
	# reference
		# salvo il riferimento di colonna
		colu.append(col)
		# salvo il riferimento della cella
		cell.append(cel)
			
#myScrolled
	if shad != None:
		scro = myScrolled(obje=None, bord=bord, 
						  widt=widt, heig=heig, 
						  shad=shad, poli=poli)
		if 1:
			# titolo esterno allo scroll
			scro.add(tree)
		else:
			# titolo interno allo scroll
			scro.add_with_viewport(tree)
	else:
		scro = None
		
# <-
	#           0,    1,    2,    3        
	# tree, [stor, colu, cell, scro]
	return tree, [stor, colu, cell, scro]
#-----------------------------------------------------------------------------
def testTreView():
#myTreeView
	# ridefinisco la callback        
	def row_activated(widg, path, colu, *data):
		# leggo record selezionato 
		#  dal doppio click o dal enter
		rec = getRecord(widg, path)
		print rec
	#           0,    1,    2,    3        
	# tree, [stor, colu, cell, scro] (attenzione name,cCol, data devono coincidere!)
	obje, othe = myTreView(name=("id","nick",),
						   call=row_activated, data=[],
						   bord=1, font='Courier bold 9', 
						   cCol=['white','#c0c0c0'], 
						   #cCol=['white','yellow'], 
						   widt=400, heig=300, 
						   shad=Gtk.SHADOW_ETCHED_OUT, 
						   poli=(Gtk.POLICY_AUTOMATIC, Gtk.POLICY_AUTOMATIC))
	# If TRUE, hint to the theme engine to draw rows in alternating colors.
	obje.set_rules_hint(True)
	# reference
	colu = othe[1]
	cell = othe[2]
	scro = othe[3]
	# stor = othe[0]
	
#    # lo rendo ordinabile per riga via D&D
#    tree.set_reorderable(True)
#    # attivo la ricerca sul campo passato (ctrl+F)
#    tree.set_search_column(0)
	# attivo il sorting sulla colonna del campo passato
	colu[0].set_sort_column_id(0)
	colu[1].set_sort_column_id(1)
		# imposto attributi della cella
	# font
	cell[0].set_property('font', 'Sans bold 9')
	# edit
#    cell[0].set_property('editable', True )    
#    cell[0].connect('edited', on_edit_celRen, lisSto)

#add Data
	# inserisco N record
	num = 20
	for ele in range(num):
		addView(obje, scro, "%02d" %ele, "%03d" %(num-ele) )

# <-
	# tree, [stor, colu, cell, scro]
	return obje, othe

#-----------------------------------------------------------------------------
# myTreeStore
#-----------------------------------------------------------------------------
# (attenzione name,cCol,imag devono coincidere!)
def myTreStore(name=["->", "Id", "->", "Name"], 
				call=None, data=['dati'],
				bord=1, 
				font=['Courier bold 9'] * 4, 
				cCol=['white','gray','white','gray'], 
				imag=[None,] * 4,
				widt=200, heig=100,
				shad=Gtk.SHADOW_ETCHED_IN, 
				poli=(Gtk.POLICY_AUTOMATIC, Gtk.POLICY_AUTOMATIC)):
	#item=, call=on_activated_makView):
	""" crea una TreeView

		-> name lista campi
		-> call funzione da eseguire su evento
		-> data dati da passare alla funzione
		-> bord margine esterno dello scroolbar
		-> font font da usare per le celle
		-> cCol lista colore di fondo delle colonne
		-> iamg lista immagini
		-> widt ampiezza
		-> heig altezza
		-> shad tipo di cornice
			Gtk.SHADOW_NONE, Gtk.SHADOW_IN, Gtk.SHADOW_OUT, 
			Gtk.SHADOW_ETCHED_IN, Gtk.SHADOW_ETCHED_OUT
		-> poli politiche di visibilita delle barre di scorrimento
			(horizontal,vertical)
			POLICY_AUTOMATIC whether you need
			POLICY_ALWAYS leave the scrollbars
	"""
	# ridefinisco la callback        
	def row_activated(tree, path, colu, *data):
		# print widg, path, colu

		# leggo record selezionato 
		#  dal doppio click o dal enter
		# rec = getRecord(widg, path)
		# print rec

		# leggo record selezionato 
		#  dal doppio click o dal enter
		rec = getRecord(tree, path)
		# print rec, tree, path, colu

		# leggo il modello dei dati
		stor = tree.get_model()
		# leggo il riferimento della riga
		treeiter = stor.get_iter(path)
		if stor.iter_has_child(treeiter):
			# print "father"
			# collapse
			if tree.collapse_row(path):
				return
			# expand
			tree.expand_row(path,True)
		# else:
		# 	print "child"
		
#treeStore  
	mode = [GObject.TYPE_STRING,]* (len(name))
	stor = Gtk.TreeStore(*mode)
#treeView
	tree = Gtk.TreeView(stor)
	tree.show()
#callback    
	# in assenza di callback usa quella di debug
	if call == None:
		call = row_activated
	# callback su doppio click o enter
	tree.connect('row-activated', call)
	# aggiungo evento tastiera per intercettare ctrl+Enter
	tree.set_events(Gdk.EventMask.KEY_PRESS_MASK)
	# # associamo la callback all'evento
	# tree.connect("key-press-event", ctlEnter, tree)
#cellRender + viewColumn
	# aggiungo le colonne e le celle
	colu = []
	cell = []
	head = []
	for ind, ele in enumerate(name):
		# qui bisognerebbe istanziare la cella
		#  in base al tipo!
	# istanzio cella di testo
		cel = Gtk.CellRendererText()
		# se non esistono colori 
		if cCol:
			# imposto i colori
			cel.set_property('cell-background', cCol[ind])
		if font:
			# imposto il font
			cel.set_property('font', font[ind])
	# istanzio colonna
		col = Gtk.TreeViewColumn(ele)
		head.append(col)
		# image ?
		if imag[ind]:
			# imposto immagine
			pix = Gtk.CellRendererPixbuf()
			pix.set_property(imag[ind], Gtk.STOCK_OPEN)
			# inserisco campo
			col.pack_start(pix, False)
			col.set_attributes(pix)
		# campo testo
		col.pack_start(cel, 1)
		col.set_attributes(cel, text=ind)
		# crea un contorno (sembra non funzionare)
		col.set_spacing(10)
	# aggiungo la colonna alla tree
		tree.append_column(col)
	# reference
		# salvo il riferimento di colonna
		colu.append(col)
		# salvo il riferimento della cella
		cell.append(cel)
			
#myScrolled
	scro = myScrolled(obje=None, bord=bord, 
					  widt=widt, heig=heig, 
					  shad=shad, poli=poli)
	if 1:
		# titolo esterno allo scroll
		scro.add(tree)
	else:
		# titolo interno allo scroll
		scro.add_with_viewport(tree)
		
# <-
	#           0,    1,    2,    3    4    
	# tree, [stor, colu, cell, scro, head]
	return tree, [stor, colu, cell, scro, head]
#-----------------------------------------------------------------------------
def testTreStore():
#myTreeView
	def on_changed_treeSelection(selection, tree):
		"riconosco il cambio di selezione"
		if selection.get_mode() == Gtk.SELECTION_MULTIPLE:
			model, selec = selection.get_selected_rows()
			if selec:
				# ottengo il riferimento attraverso la posizione del dato
				iter = model.get_iter(selec[0])  
				#print 'multi:', selec
				for ele in selec:
					print ele[0] 
		else:
			model, selec = selection.get_selected()
			if selec:
				# ottengo la posizione del dato attraverso il riferimento
				path = model.get_path(selec)
				# print 'single:', selec

				rec = getRecord(tree, path)
				print rec

	#           0,    1,    2,    3     4   
	# tree, [stor, colu, cell, scro, head] (attenzione name,cCol,imag devono coincidere!)
	obje, othe = myTreStore(name=("id","nick",),
						   call=None, data=[],
						   bord=1, 
						   font=['Sans bold 9', 'Courier bold 9'], 
						   cCol=['white','#e0e0e0'], 
						   imag=[None,None], 
						   widt=400, heig=300, 
						   shad=Gtk.SHADOW_ETCHED_OUT, 
						   poli=(Gtk.POLICY_AUTOMATIC, Gtk.POLICY_AUTOMATIC))
	# If TRUE, hint to the theme engine to draw rows in alternating colors.
	obje.set_rules_hint(True)
	# reference
	stor = othe[0]
	colu = othe[1]
	cell = othe[2]
	scro = othe[3]

	# edit cell
	def on_edit_celRen(widg, path, newDat, stor):
		print path, newDat
		stor[path][1] = newDat
	# set property
	cell[1].set_property('editable', True )    
	# callback
	cell[1].connect('edited', on_edit_celRen, stor)

	# referenzio la selezione
	obj1 = obje.get_selection()
	# riconosco il cambio di selezione per visualizzare le selezionate
	obj1.connect('changed', on_changed_treeSelection, obje)

#add Data
	# inserisco N record
	num = 20
	# parent
	pare = None
	for ele in range(num):
		# pare = addTree(obje, scro, pare, "%02d" %ele, "%03d" %(ele) )
		pare1 = addTree(obje, scro, pare, "%02d" %ele, "%03d" %(ele) )
		if ele == 9:
			pare = pare1

	pare0 = addTree(obje, None, None, "Uffi", "1000" )
	pare1 = addTree(obje, None, pare0, "riUffi", "100" )
	pare2 = addTree(obje, None, pare1, "arciUffi", "200" )
	pareX = addTree(obje, None, pare1, "arciUffi", "300" )

# <-
	# tree, [stor, colu, cell, scro]
	return obje, othe

#-----------------------------------------------------------------------------
# myTreeField
#-----------------------------------------------------------------------------
def myTreField(name=("name","value"),
				call=None, data=['dati'],
				bord=1,
				font=['Luxi Mono 9', 'Sans 8'],
				size=[140, 180],
				widt=300, heig=400,
				shad=Gtk.SHADOW_ETCHED_IN, 
				poli=(Gtk.POLICY_AUTOMATIC, Gtk.POLICY_AUTOMATIC),
				nExp="Titolo"):
	""" crea una lista di campi da editare

		-> name lista campi
		-> call funzione da eseguire su evento
		-> data dati da passare alla funzione
		-> bord margine esterno dello scroolbar
		-> font font da usare per le celle
		-> cCol lista colore di fondo delle colonne
		-> iamg lista immagini
		-> widt ampiezza scrollbars
		-> heig altezza scrollbars
		-> shad tipo di cornice
			Gtk.SHADOW_NONE, Gtk.SHADOW_IN, Gtk.SHADOW_OUT, 
			Gtk.SHADOW_ETCHED_IN, Gtk.SHADOW_ETCHED_OUT
		-> poli politiche di visibilita delle barre di scorrimento
			(horizontal,vertical)
			POLICY_AUTOMATIC whether you need
			POLICY_ALWAYS leave the scrollbars
	"""

	# ridefinisco la callback        
	def row_activated(tree, path, colu, *data):
		# leggo record selezionato 
		#  dal doppio click o dal enter
		rec = getRecord(tree, path)
		# print rec, tree, path, colu

		# leggo il modello dei dati
		stor = tree.get_model()
		# leggo il riferimento della riga
		treeiter = stor.get_iter(path)
		if stor.iter_has_child(treeiter):
			# print "father"
			# collapse
			if tree.collapse_row(path):
				return
			# expand
			tree.expand_row(path,True)
		# else:
		# 	print "child"

#treeStore  
	mode = [GObject.TYPE_STRING,]* (len(name)*2)
	stor = Gtk.TreeStore(*mode)
#treeView
	tree = Gtk.TreeView(stor)
	tree.show()
#callback    
	# in assenza di callback usa quella di debug
	if call == None:
		call = row_activated
	# callback su doppio click o enter
	tree.connect('row-activated', call)
	# aggiungo evento tastiera per intercettare ctrl+Enter
	tree.set_events(Gdk.EventMask.KEY_PRESS_MASK)
	# # associamo la callback all'evento
	# tree.connect("key-press-event", ctlEnter, tree)	
	# active grid line
	tree.set_grid_lines(True)
	# hide column
	tree.set_headers_visible(False)

#cellRender + viewColumn
	# aggiungo le colonne e le celle
	colu = []
	cell = []
	head = []
	#First column's cell
	cel = Gtk.CellRendererText()
	cell.append(cel)
	cel.set_property('font', font[0])
	cel.set_property('background-set', True)
	# column 1
	col = Gtk.TreeViewColumn()
	colu.append(col)
	col.pack_start(cel, True)
	col.set_fixed_width(size[0])
	col.set_attributes(cel, text=0, background=2)
	tree.append_column(col)

	#Second column's cell
	cel = Gtk.CellRendererText()
	cell.append(cel)
	cel.set_property('font', font[1])
	cel.set_property('background-set', True)
	cel.set_property('editable', True )
	# column 2
	col = Gtk.TreeViewColumn()
	colu.append(col)
	col.pack_start(cel, True)
	col.set_fixed_width(size[1])
	col.set_attributes(cel, text=1, background=3)
	tree.append_column(col)

#myScrolled
	scro = myScrolled(obje=None, bord=bord, 
					  widt=widt, heig=heig, 
					  shad=shad, poli=poli)
	if 1:
		# titolo esterno allo scroll
		scro.add(tree)
	else:
		# titolo interno allo scroll
		scro.add_with_viewport(tree)

# myFather	
	# tree, scro=None, pare=None, colo=None, reco=[]
	pare = addField(tree=tree, colo=['#e0e0e0', '#e0e0e0'], reco=[nExp, ""] )

# <-
	# tree, [stor, colu, cell, scro, pare]
	return tree, [stor, colu, cell, scro, pare]
#-----------------------------------------------------------------------------
def testTreField():

	# tree, [stor, colu, cell, scro, pare]
	obje, othe = myTreField(name=("name","value"),
							call=None, data=['dati'],
							bord=1, 
							font=['Courier bold 9'] * 2, 
							size=[200, 100],
							widt=300, heig=400,
							shad=Gtk.SHADOW_ETCHED_IN, 
							poli=(Gtk.POLICY_AUTOMATIC, Gtk.POLICY_AUTOMATIC),
							nExp="Titolo", 
							)
	# reference
	tree = obje
	stor = othe[0]
	colu = othe[1]
	cell = othe[2]
	pare = othe[4]

#add Data
	# inserisco N record
	# tree, scro=None, pare=None, colo=None, reco=[]
	addField(tree=tree, pare=pare, reco=["Name", "wsm_0000"] )
	addField(tree=tree, pare=pare, reco=["Object Id", "0x3456"] )
	addField(tree=tree, pare=pare, reco=["Type", "Working Set"] )
	# visualizzo los store model	
	printTreeStore(stor)

# <-
	# tree, [stor, colu, cell, scro, pare]
	return tree, [stor, colu, cell, othe[3], pare]

#-----------------------------------------------------------------------------
# myExpander
#-----------------------------------------------------------------------------
def myExpander(name="Name", chil=None, spac=0, call=None, data=['dati'] ):
	""" crea un Expander

		-> name  nome label
		-> chil oggetto contenuto
		-> spac interspazio
		-> call funzione da eseguire su evento
		-> data dati da passare alla funzione
	"""
	#callback debug    
	def on_activated(widg, *data):
		print widg, data
		
#expander 
	obje = Gtk.Expander(label=name)
	obje.set_spacing(spac)	
	# obje.set_resize_toplevel(True)
	obje.show()
#callback    
	# in assenza di callback usa quella di debug
	if call == None:
		call = on_activated
	# callback su doppio click o enter
	obje.connect('activate', call)
	# obje.connect('notify::expanded', call)

	# aggiungo i figli
	if chil != None:
		obje.add(chil)
# <-
	# tree, [call]
	return obje, [call,]

#-----------------------------------------------------------------------------
def testExpander():
# myExpander

	from time import ctime

	#callback debug    
	def on_activated(widg, *data):
		res = widg.get_expanded()

		if res == False:
			# istanzio una label
			label = Gtk.Label(ctime())
			label.show()			
			# la inserisco
			widg.add(label)
		else:
			# rimuovo l'elemento
			widg.remove(widg.get_children()[0])
		
	obje, othe = myExpander(name="Name", chil=None, spac=0, call=on_activated, data=['dati'] )
	# obje.set_resize_toplevel(False)
	# obje.set_expanded(True)

# <-
	# tree, [call]
	return obje, othe

#-----------------------------------------------------------------------------
def myExpField(name=("name","value"),
				call=None, data=['dati'],
				font=['Luxi Mono 9', 'Sans 8'],
				size=[140, 180],
				cCol=['white','white'],
				nExp="Object", 
				dStr=[],
				oStr=0, ):
	""" crea una lista di campi da editare

		-> name lista campi
		-> call funzione da eseguire su evento
		-> data dati da passare alla funzione
		-> font font da usare per le celle
		-> size dimensione delle celle
		-> cCol colori di fondo delle colonne
		-> nExp nome expander
		-> dStr dati strutturati
		-> offs offset struttura
	"""
#treeView

	def ctlEnter(obj, event, view):
		""" {ctrl+Enter}
		"""
		# intercetto solo ctrl+Enter
		if (event.state == Gdk.CONTROL_MASK) and (event.keyval== Gtk.keysyms.Return):
			# referenzio il modello (treeStore) e l'indice del record selezionato
			model, iter = view.get_selection().get_selected()
			# deve esistere un elemento selezionato
			if iter:
				# leggo il primo campo del record selezionato
				ele = model.get_value(iter, 0)
				print "id:",ele

	#           0,    1,    2,    3        
	# tree, [stor, colu, cell, scro] (attenzione name,cCol,image devono coincidere!)
	obj1, oth1 = myTreView(name=name,
	# obj1, oth1 = myTreStore(name=name,
							call=call, data=data,
							font='Courier bold 9', 
							cCol=cCol, 
							widt=0, heig=0, 
							shad=None, 
							poli=(Gtk.POLICY_AUTOMATIC, Gtk.POLICY_AUTOMATIC))
	# If TRUE, hint to the theme engine to draw rows in alternating colors.
	obj1.set_rules_hint(True)
	# associamo la callback all'evento
	obj1.connect("key-press-event", ctlEnter, obj1)

	# reference
	tree = obj1
	stor = oth1[0]
	colu = oth1[1]
	cell = oth1[2]


	#-----------------------------------------------------------------------------
	def myCodInt(dStr, fiel="objId", data=1234):
		# integer value
		cod = 'dStr.dat.struc.%s = %s \n' %(fiel, data)
		exec(cod)

	def myCodStr(dStr, fiel="objId", data="data"):
		# integer value
		cod = 'dStr.dat.struc.%s = "%s" \n' %(fiel, data)
		exec(cod)

	# active grid line
	obj1.set_grid_lines(True)
	# hide column
	obj1.set_headers_visible(False)
	# font, size
	for ind, ele in enumerate(font):
		cell[ind].set_property('font', ele)
		colu[ind].set_fixed_width(size[ind])
	if ind == 1:
		# edit cell
		def on_edit_celRen(widg, path, newDat, stor, dStr, oStr):
			# print path, newDat, stor
			stor[path][1] = newDat

			# # view data fields
			# for ele in stor:
			# 	print ele[:]

			# read data from field structure
			try:
				nam, val, typ = dStr.dat.struc[int(path)+oStr]
				# (es: obj0.dat.struc.objId  = 1234)
				myCodInt(dStr, fiel=nam, data=newDat)
			except:
				nam, val = dStr.dat.struc[int(path)+oStr]
				# (es: obj0.dat.struc.value  = "1234")
				myCodStr(dStr, fiel=nam, data=newDat)
			print dStr

		# view structure

			# msg = ""
			# for nam, val, typ in dStr.dat.struc:
			# 	# 8 bit
			# 	if typ == 8:
			# 		msg +="%s:%.2x " %(nam, val)
			# 	# 16 bit
			# 	elif typ == 16:
			# 		msg +="%s:%.4x " %(nam, val)
			# 	# 32 bit
			# 	elif typ == 32:
			# 		msg +="%s:%.8x " %(nam, val)
			# print msg

		# set property
		cell[1].set_property('editable', True)  
		# callback
		cell[1].connect('edited', on_edit_celRen, stor, dStr, oStr)

# myExpander
	#callback debug    
	def on_activated(widg, *data):
		res = widg.get_expanded()
	# object
	obje, othe = myExpander(name=nExp, chil=obj1, spac=0, call=on_activated, data=['dati'] )
	# obje.set_resize_toplevel(False)
	obje.set_expanded(True)

# <-
	# expa, [tree, stor, colu, cell]
	return obje, [tree, stor, colu, cell]

#-----------------------------------------------------------------------------
def testExpField():

	#-----------------------------------------------------------------------------
	class Typ8(IterStructure): # typ=8 (Input String object)
	#-----------------------------------------------------------------------------
		_pack_ = 1
		_fields_ = [("objId",	c_uint16, 16), # 0
					("type",  	c_uint8 ,  8), # 2
					("width", 	c_uint16, 16), # 3
					("height", 	c_uint16, 16), # 5
					("bkgCol", 	c_uint8 ,  8), # 7
					("fonAtt", 	c_uint16, 16), # 8
					("inpAtt", 	c_uint16, 16), # 10
					("option", 	c_uint8 ,  8), # 12
					("varRef", 	c_uint16, 16), # 13
					("horJus", 	c_uint8 ,  8), # 15
					("length", 	c_uint8 ,  8)] # 16
	class Typ8a(Iter1Structure): # typ=8 (Input String object)
		_fields_ = [("value", 	c_char_p,   )] #  [chr * length]
	class Typ8b(IterStructure): # typ=8 (Input String object)
		_fields_ = [("enable", 	c_uint8 ,  8), # 
					("numMac", 	c_uint8 ,  8)] #
	class Typ8c(IterStructure): # typ=8 (Input String object)
		_fields_ = [("idEve", 	c_uint8 ,  8), # 0 
					("idMac", 	c_uint8 ,  8)] # 1

	#---------------------------------------------------------,
	# Typ 8,
	siz = [typ for nam, val, typ  in Typ8._fields_]
	siz = sum(siz)/8
	#
	class Uni8(Union):
		_fields_ = [("struc", Typ8),
					("data", c_uint8 * siz),]
	#
	class Obj8(object):
		def __init__(self):
			# attribute
			self.dat = Uni8()
		# display items & value (nam:%s val:%x)
		def __str__(self):
			return self.dat.struc.getItem(self.dat)
	# instance object
	obj0 = Obj8()
	# Data
	# objId:0000 type:00 bkgCol:01 select:01 actMsk:03e8 numObj:01 numMac:00 numLan:00
	obj0.dat.struc.objId  = 0x3456
	obj0.dat.struc.type   = 0x08
	obj0.dat.struc.widt   = 0x0200
	obj0.dat.struc.heig   = 0x003f
	obj0.dat.struc.bkgCol = 0x01
	obj0.dat.struc.fonAtt = 0x5294
	obj0.dat.struc.inpAtt = 0x0000
	obj0.dat.struc.option = 0x00
	obj0.dat.struc.varRef = 0x0000
	obj0.dat.struc.horJus = 0x00
	obj0.dat.struc.length = 0x05
	print obj0.dat.data[:]
	print obj0

	# expa, [tree, stor, colu, cell]
	obje, othe = myExpField(name=("name","value"),
							call=None, data=['dati'],
							font=['Courier 10', 'Sans 8'],
							size=[150, 200],
							cCol=['#fafad2','#fafac2'], 
							nExp="Object-1",
							dStr=obj0,
							oStr=-1, )
	# reference
	tree = othe[0]
	stor = othe[1]
	colu = othe[2]
	cell = othe[3]

#add Data
	# inserisco N record
	# (obje, scro, "", "")
	addView(tree, None, "Name", "wsm_0000" )
	addView(tree, None, "Object Id", "%d" %obj0.dat.struc.objId )
	addView(tree, None, "Type", "%d" %obj0.dat.struc.type )

	# Data Field
	# (obje, scro, pare, "", "")
	addView(tree, None, "Width", "%d" %obj0.dat.struc.width )
	addView(tree, None, "Height", "%d" %obj0.dat.struc.height )
	addView(tree, None, "Background Colour", "%d" %obj0.dat.struc.bkgCol )
	addView(tree, None, "Font Attributes", "%d" %obj0.dat.struc.fonAtt )
	addView(tree, None, "Input Attributes", "%d" %obj0.dat.struc.inpAtt )
	addView(tree, None, "Options", "%d" %obj0.dat.struc.option ) # [+]
	addView(tree, None, "Variable Reference", "%d" %obj0.dat.struc.varRef )
	addView(tree, None, "Horizontal Justif.", "%d" %obj0.dat.struc.horJus )
	addView(tree, None, "Length", "%d" %obj0.dat.struc.length )

# <-
	# expa, [tree, stor, colu, cell]
	return obje, [tree, stor, colu, cell]

#-----------------------------------------------------------------------------
def testExpField1():

	#---------------------------------------------------------,
	# Typ 8a,
	siz = 5

	class Typ8aX(Iter1Structure): # typ=8 (Input String object)
		_fields_ = [("value", c_char * siz)] #  [chr * length]
	#
	class UniStr(Union):
		_fields_ = [("struc", Typ8aX),
					("data", c_uint8 * siz),]
	#
	class ObjStr(object):
		def __init__(self):
			# attribute
			self.dat = UniStr()
		# display items & value (nam:%s val:%x)
		def __str__(self):
			# return "%s" %([ord(x) for x in self.dat.struc.value])
			# return self.dat.struc.value
			return self.dat.struc.getItem(self.dat)
	# instance object
	obj1 = ObjStr()
	# data
	obj1.dat.struc.value = "orcim"

	# expa, [tree, stor, colu, cell]
	obje, othe = myExpField(name=("name","value"),
							call=None, data=['dati'],
							font=['Courier 10', 'Sans 8'],
							size=[150, 200],
							cCol=['#fafad2','#fafac2'], 
							nExp="Object-1",
							dStr=obj1,
							oStr=0, )
	# reference
	tree = othe[0]
	stor = othe[1]
	colu = othe[2]
	cell = othe[3]

	# msg = [chr(x) for x in dat[1]["value"]]
	addView(tree, None, "String Value", "%s" %obj1.dat.struc.value ) # [+]

# <-
	# expa, [tree, stor, colu, cell]
	return obje, [tree, stor, colu, cell]

#-----------------------------------------------------------------------------
def myTry01():
	sys.exit()
		
#-----------------------------------------------------------------------------
# Main
#-----------------------------------------------------------------------------
if __name__ == "__main__":

	# istanza l'applicazione principale
	self = MyWind(width=350, height=300, title="myBox\ %s" %myRev, center=True, color="#b0b0b0")

	choi = 4
	
	if choi == 1:
		# tree, [stor, colu, cell, scro]
		obje, othe = testTreView()
		self.vBox.pack_start(child=othe[3], expand=False, fill=False, padding=0)
	elif choi == 2:
		# tree, [stor, colu, cell, scro, head]
		obje, othe = testTreStore()
		self.vBox.pack_start(child=othe[3], expand=False, fill=False, padding=0)
	elif choi == 3:
		# expa, [tree, stor, colu, cell]
		obje, othe = testExpander()
		self.vBox.pack_start(child=obje, expand=False, fill=False, padding=0)
	elif choi == 4:
		# expa, [tree, stor, colu, cell]
		obje, othe = testExpField()
		self.vBox.pack_start(child=obje, expand=False, fill=False, padding=0)
		obje, othe = testExpField1()
		self.vBox.pack_start(child=obje, expand=False, fill=False, padding=0)
	elif choi == 5:
		# tree, [stor, colu, cell, scro, pare]
		obje, othe = testTreField()
		self.vBox.pack_start(child=othe[3], expand=False, fill=False, padding=0)

	# cediamo il controllo alle Gtk
	Gtk.main()
