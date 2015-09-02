#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" lista degli oggetti definiti:

    - myLabel
    - myLabList
    - myLabFrame
"""

myRev = "(rev.150827)"
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

#-----------------------------------------------------------------------------
# myLabel
#-----------------------------------------------------------------------------
def myLabel(name='myLabel', 
            leng=0, prea=' ', post='', 
            font='Curier 10', 
            colo='black'):
    """ crea una label con attributi stabiliti
    
        -> name nome associato alla label
        -> leng lunghezza di formattazione
        -> prea preambolo di formattazione
        -> post post (aggiunto dopo la label)
        -> font font usato per il testo
        -> colo colore assegnato
    """
#label
    # istanzio una label
    labe = Gtk.Label()
    # la rendo visibile
    labe.show()
    #labe.set_alignment(0,0.5)
    if leng > 0:
        name = name.rjust(leng,prea)
    name += post
    # imposto la label
    labe.set_markup(name)
    # imposto un font
    labe.modify_font(Pango.FontDescription(font))
    # imposto il colore
    labe.modify_fg(Gtk.STATE_NORMAL, Gdk.color_parse(colo))
# <-        
    return labe
#-----------------------------------------------------------------------------
def testLabel():
#myLabel
    # labe
    labe = myLabel(name='prova', 
                   leng=len('prova')+5, prea='.', post='', 
                   font='Arial 10', 
                   colo='blue')
# <-
    return labe

#-----------------------------------------------------------------------------
# myLabel List
#-----------------------------------------------------------------------------
def myLabList(name=["_Read","_Write","_Defau"], 
              leng=0, prea=' ', post='', 
              font='Courier 10', 
              colo='black',
              tBox='v', aBox=[False, False, 1]):
    # funzione che istanzia oggetti tipo
    def myList(ind):
#myLabel
        # labe
        obje = myLabel(name[ind], leng, 
                       prea, post, font, colo)
        return obje, None
#myBoxList
    # xBox, [labe, None] * N
    obje, othe = myBoxList(name=name, tBox=tBox, 
                           aBox=aBox, func=myList)
# <-
    return obje, othe
#-----------------------------------------------------------------------------
def testLabList():
#myLabList    
    # xBox, [labe, None] * N
    obje, othe = myLabList(name=["Read","Write","Default"], 
                           leng=7, prea=' ', post=':', 
                           font='Courier 10', 
                           colo='brown',
                           tBox='v', aBox=[False, False, 1])
    # cambio colore alla seconda label
    othe[1][0].modify_fg(Gtk.STATE_NORMAL, Gdk.color_parse("green"))
#myFrame    
    # fram,[labe,xBox]
    obj1, oth1 = myFrame(name='myLabel', obje=obje, colo='black',
                         bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
                         tBox='v' )
    #debug
    myViewObject(obje, othe)
# <-
    return obj1

#-----------------------------------------------------------------------------
# myLabFrame
#-----------------------------------------------------------------------------
def myLabFrame(name='myLabel', 
            leng=0, prea=' ', post='', 
            font='Curier 10', 
            colo=Gdk.color_parse('black'),
            nFra='Label', cFra='black', bFra=1, sFra=Gtk.SHADOW_ETCHED_OUT, 
            tFra='v', aFra=[False, False, 1]):
    """ crea una label con attributi stabilit
    
        -> name nome associato alla label
        -> leng lunghezza di formattazione
        -> prea preambolo di formattazione
        -> post post (aggiunto dopo la label)
        -> font font usato per il testo
        -> colo colore assegnato
        -> nFra nome del frame 
        -> cFra colore nome del frame 
        -> bFra bordo riservato all'esterno
        -> sFra tipo di cornice
        -> tFra tipo di contenitore v/h 
        -> aFra attributi del contenitore
    """
#myLabel
    # labe
    labe = myLabel(name=name, 
                   leng=leng, prea=prea, post=post, 
                   font=font, colo=colo)
#myFrame
    #fram, [labe, xBox]
    fram,othe = myFrame(nFra, labe, cFra, bFra, sFra, tFra, aFra)
    # <-
    #fram, [labe, lFrm, xBox]        
    return fram, [labe, othe[0], othe[1]]
#-----------------------------------------------------------------------------
def testLabFrame():
#myLabFrame
    #fram, [labe, lFrm, xBox]
    obje, othe = myLabFrame(name='myText', 
                            leng=len('myText')+5, prea='.', post='', 
                            font='Arial 10', 
                            colo='blue',
                            nFra='Label', cFra="blue", bFra=1, sFra=Gtk.SHADOW_ETCHED_OUT, 
                            tFra='v', aFra=[False, False, 1])
# <-
    return obje

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
        choi = 2
    else:
        # get first argument (scelta esterna)
        choi = int(sys.argv[1])

    if choi == 1:
        obje = testLabel()
    elif choi == 2:
        obje = testLabList()
    elif choi == 3:
        obje = testLabFrame()

    # istanza l'applicazione principale
    self = MyWind(width=None, height=800, title="myLabel %s" %myRev, center=True, color="#b0b0b0")
    self.vBox.pack_start(child=obje, expand=False, fill=False, padding=0)

    # cediamo il controllo alle gtk
    Gtk.main()
