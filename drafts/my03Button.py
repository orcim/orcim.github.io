#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
""" widgets definiti:

    - myButton       - myButList
    - myButFrame     - myButFraList
    - myButSwitch    - myButSwiList    
    - myButSwiFrame  - myButSwiFraList    
    
"""
myRev = "(rev.140525)"
#-----------------------------------------------------------------------------
# myModules
#-----------------------------------------------------------------------------
from my00init import *
from gi.repository import Pango

from myApp import MyWind
from my01Box import myViewObject, myBoxList, myFrame
#-----------------------------------------------------------------------------
# myButton
#-----------------------------------------------------------------------------
def myButton(name='my_Button', 
             icon=Gtk.STOCK_OK, 
             call=None, data=['dati']):
    """ crea un bottone con associato una icona e una etichetta
        alla premuta del bottone viene eseguita la callback associata
    
        -> name nome associato alla label
        -> icon tipo di icona associata
        -> call funzione da eseguire su evento
        -> data dati da passare alla funzione
    """
    #callback debug    
    def on_clicked(widg, *data):
        print "a", widg.props.label, data
#button
    # istanzio un bottone
    butt = Gtk.Button(stock=icon)
    # lo rendo visibile
    butt.show()
    # confermo l'immagine attuale
    butt.props.image = butt.get_image()
    # modifico la label passata
    butt.props.label = name
    
    # in assenza di callback usa quella di debug
    if call == None:
        call = on_clicked
    butt.connect('clicked', call, *data)
# <-        
    return butt, call
#-----------------------------------------------------------------------------
def testButton():
#myButton
    # ridefinisco la callback        
    def on_clicked(widg, *data):
        print "b", widg.props.label, data
    # butt, call
    obje, othe = myButton(name='my_Button', 
                          icon=Gtk.STOCK_YES, 
                          call=on_clicked, data=[])
# <-
    return obje

#-----------------------------------------------------------------------------
# myButton List
#-----------------------------------------------------------------------------
def myButList(name=["_Read","_Write","_Defau"], 
              icon=Gtk.STOCK_NO,
              call=None, data=['dati'],
              tBox='v', aBox=[False, False, 1]):
    #callback debug
    def on_clicked(widg, ind, *data):
        print "a", ind, data
    # in assenza di callback uso quella di debug
    if call == None:
        call = on_clicked

    # funzione che istanzia oggetti tipo
    def myList(ind):
#myButton        
        # butt,call
        return myButton(name[ind], icon, 
                        call, [ind, data])
#myBoxList
    # xBox, [butt,call] * N
    obje, othe = myBoxList(name=name, tBox=tBox, 
                           aBox=aBox, func=myList)
# <-
    return obje, othe
#-----------------------------------------------------------------------------
def testButList():
#myButList    
    # ridefinisco la callback
    def on_clicked(widg, ind, *data):
        print "b", ind, data
    # xBox, [butt,call] * N
    obje, othe = myButList(name=["_Read","_Write","_Defau"], 
                           icon=Gtk.STOCK_NO,
                           call=on_clicked, data=[],
                           tBox='v', aBox=[False, False, 1])
    # cambio icona al primo bottone
    othe[0][0].props.image = Gtk.Image.new_from_stock(Gtk.STOCK_YES, Gtk.ICON_SIZE_BUTTON)
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
# myButFrame
#-----------------------------------------------------------------------------
def myButFrame(name='my_Button', 
               icon=Gtk.STOCK_OK, 
               call=None, data=['dati'],
               bFra=1, sFra=Gtk.SHADOW_ETCHED_OUT, 
               tFra='v', aFra=[False, False, 1]):
    """ crea un bottone con associato una icona in un frame con etichetta
        alla premuta del bottone viene eseguita la funzione associata
    
        -> name nome associato al frame label
        -> icon tipo di icona associata
        -> call funzione da eseguire su evento
        -> data dati da passare alla funzione
        -> bFra bordo riservato all'esterno
        -> sFra tipo di cornice
        -> tFra tipo di contenitore v/h 
        -> aFra attributi del contenitore
    """
    #callback debug    
    def on_clicked(widg, *data):
        print "a", data
#button
    # istanzio un bottone
    butt = Gtk.Button(stock=icon)
    # lo rendo visibile
    butt.show()
    # confermo l'immagine attuale
    butt.props.image = butt.get_image()
    # elimino la label del bottone
    butt.props.label = ""
#myFrame
    #fram, [labe, xBox]
    obje, othe = myFrame(name, butt, 'black', bFra, sFra, tFra, aFra)
    
    # in assenza di callback usa quella di debug
    if call == None:
        call = on_clicked
    butt.connect('clicked', call, *data)
# <-
    #fram, [labe, xBox, butt, call]        
    return obje, [othe[0], othe[1], butt, call]
#-----------------------------------------------------------------------------
def testButFrame():
#myButFrame
    # ridefinisco la callback        
    def on_clicked(widg, *data):
        print "b", data
    # fram, [labe, xBox, butt, call]
    obje, othe = myButFrame(name='myButFrame', 
                            icon=Gtk.STOCK_OK, 
                            call=on_clicked, data=[],
                            bFra=1, sFra=Gtk.SHADOW_ETCHED_OUT, 
                            tFra='v', aFra=[False, False, 1])
# <-
    return obje

#-----------------------------------------------------------------------------
# myButFraList
#-----------------------------------------------------------------------------
def myButFraList(name=["Read","Write","Default"], 
                 icon=Gtk.STOCK_YES,
                 call=None, data=['dati'],
                 bFra=1, sFra=Gtk.SHADOW_ETCHED_OUT, 
                 tFra='v', aFra=[False, False, 1],
                 tBox='h', aBox=[False, False, 1]):
    #callback debug
    def on_clicked(widg, ind, *data):
        print "a", ind, data
    # in assenza di callback uso quella di debug
    if call == None:
        call = on_clicked

    # funzione che istanzia oggetti tipo
    def myList(ind):
#myButFrame
        # fram, [labe, xBox, butt, call]
        return myButFrame(name[ind], icon,
                          call, [ind, data],
                          bFra, sFra, tFra, aFra)
#myBoxList
    # xBox, [fram, [labe, xBox, butt, call]] * N
    obje, othe = myBoxList(name=name, tBox=tBox, 
                           aBox=aBox, func=myList)
# <-
    return obje, othe
#-----------------------------------------------------------------------------
def testButFraList():
#myButFraList    
    # ridefinisco la callback
    def on_clicked(widg, ind, *data):
        print "b", ind, data
    # xBox, [fram, [labe, xBox, butt, call]] * N
    obje, othe = myButFraList(name=["Read","Write","Default"], 
                              icon=Gtk.STOCK_NO,
                              call=on_clicked, data=[],
                              bFra=1, sFra=Gtk.SHADOW_ETCHED_OUT, 
                              tFra='v', aFra=[False, False, 1],
                              tBox='h', aBox=[False, False, 1])
    # cambio icona al primo bottone
    othe[0][1][2].props.image = Gtk.Image.new_from_stock(Gtk.STOCK_YES, Gtk.ICON_SIZE_BUTTON)

    #debug
    myViewObject(obje, othe)
# <-
    return obje

#-----------------------------------------------------------------------------
# myButSwitch
#-----------------------------------------------------------------------------
def myButSwitch(name=['my_ButSwitch',None], 
                icon=[Gtk.STOCK_NO, Gtk.STOCK_YES],
                call=None, data=['dati'],
                func=[None, None]):
    """ crea un bottone con 2 stati, ad ogni stato e'
         associata una icona e una label
         
        -> name nomi associati alle icone
        -> icon tipo di icone associate
        -> call funzione da eseguire su evento
        -> data dati da passare alla funzione
        -> func funzioni associate allo stato dello switch
    """
    #callback debug    
    def on_clicked(widg, *data):
        "widg e' il riferimento dell'istanza"
        al = widg.get_children()[0] # alignment
        hb = al.get_children()[0]   # hbox
        image, text = hb.get_children()
        #
        if image.get_stock()[0] == widg.icon[0]:
            # switch On
            widg.props.image = Gtk.Image.new_from_stock(widg.icon[1], Gtk.ICON_SIZE_BUTTON)
            # update status
            widg.stat = 1
            if widg.func[0]:
                widg.func[0](*data)
            try:
                if widg.labe[1] != None:
                    widg.props.label = widg.labe[1]
            except:
                pass
        else:
            # switch Off
            widg.props.image = Gtk.Image.new_from_stock(widg.icon[0], Gtk.ICON_SIZE_BUTTON)
            # update status
            widg.stat = 0
            if widg.func[1]:
                widg.func[1](*data)
            widg.props.label = widg.labe[0]
#button
    # istanzio un bottone
    butt = Gtk.Button(stock=icon[0])
    # reference icon
    butt.icon = icon
    # reference name
    butt.labe = name
    # reference function
    butt.func = func
    # reference status
    butt.stat = 0
    # lo rendo visibile
    butt.show()
    # modifico la label
    butt.props.image = butt.get_image()
    butt.props.label = name[0]
    
    # in assenza di callback usa quella di debug
    if call == None:
        call = on_clicked
    # passo il riferimento dell'oggetto stesso "butt"
    butt.connect('clicked', call, *data)
# <-        
    return butt,call
#-----------------------------------------------------------------------------
def testButSwitch():
#myButSwitch
    #ridefinisco le funzioni
    def buttOn(*data):
        print "On  adesso %s!" %data[0]
    def buttOff(*data):
        print "Off adesso %s!" %data[1]
    # butt,call
    obje, othe = myButSwitch(name=['_Off','_On',], 
                             icon=[Gtk.STOCK_NO, Gtk.STOCK_YES],
                             call=None, data=['sono acceso','sono spento'],
                             func=[buttOn, buttOff]) 
# <-
    return obje

#-----------------------------------------------------------------------------
# myButSwiList
#-----------------------------------------------------------------------------
def myButSwiList(name=[["_Echo",],["_Lf",],["_Cr",],["_Debug"],], 
                 icon=[Gtk.STOCK_NO, Gtk.STOCK_YES],
                 call=None, data=['dati'],
                 func=[None, None],
                 tBox='v', aBox=[False, False, 1]):

    # funzione che istanzia oggetti tipo
    def myList(ind):
    #myButSwitch
        # butt,call
        return myButSwitch(name[ind], icon, 
                           call, [ind, data],
                           func)
#myBoxList
    # xBox, [butt,call] * N
    obje, othe = myBoxList(name=name, tBox=tBox, 
                           aBox=aBox, func=myList)
# <-
    return obje, othe
#-----------------------------------------------------------------------------
def testButSwiList():
#myButSwitch    
    #function debug
    def buttOn(ind, *data):
        print " On", ind
    def buttOff(ind, *data):
        print "Off", ind
    # xBox, [butt,call] * N
    obje, othe = myButSwiList(name=[["_Echo"],["_Lf"],["_Cr"],["_Debug"],], 
                              icon=[Gtk.STOCK_NO, Gtk.STOCK_YES],
                              call=None, data=['dati'],
                              func=[buttOn, buttOff],
                              tBox='h', aBox=[False, False, 1])
#myFrame    
    # fram,[labe,xBox]
    obj1, oth1 = myFrame(name='myButSwitch', obje=obje, colo='black',
                         bord=2, shad=Gtk.SHADOW_ETCHED_OUT,
                         tBox='v' )
    #debug
    myViewObject(obje, othe)
# <-
    return obj1

#-----------------------------------------------------------------------------
# myButSwitch
#-----------------------------------------------------------------------------
def myButSwiFrame(name='myButSwitFrame', 
                  icon=[Gtk.STOCK_NO, Gtk.STOCK_YES],
                  call=None, data=['dati'],
                  func=[None, None],
                  bFra=1, sFra=Gtk.SHADOW_ETCHED_OUT, 
                  tFra='h', aFra=[False, False, 1]):
    """ crea un bottone con 2 stati all'interno di un frame,
         ad ogni stato e' associata una icona e una label
         
        -> name nomi associati alle label dei frame
        -> icon tipo di icone associate
        -> call funzione da eseguire su evento
        -> data dati da passare alla funzione
        -> func funzioni associate allo stato dello switch
        -> bFra bordo riservato all'esterno
        -> sFra tipo di cornice
        -> tFra tipo di contenitore v/h 
        -> aFra attributi del contenitore
    """
    #callback debug    
    def on_clicked(widg, *data):
        "widg e' il riferimento dell'istanza"
        al = widg.get_children()[0] # alignment
        hb = al.get_children()[0]   # hbox
        image, text = hb.get_children()
        #
        if image.get_stock()[0] == widg.icon[0]:
            # switch On
            widg.props.image = Gtk.Image.new_from_stock(widg.icon[1], Gtk.ICON_SIZE_BUTTON)
            # update status
            widg.stat = 1
            if widg.func[0]:
                widg.func[0](*data)
        else:
            # switch Off
            widg.props.image = Gtk.Image.new_from_stock(widg.icon[0], Gtk.ICON_SIZE_BUTTON)
            # update status
            widg.stat = 0
            if widg.func[1]:
                widg.func[1](*data)
#button
    # istanzio un bottone
    butt = Gtk.Button(stock=icon[0])
    # reference icon
    butt.icon = icon
    # reference name
    butt.labe = name
    # reference function
    butt.func = func
    # reference status
    butt.stat = 0
    # lo rendo visibile
    butt.show()
    # modifico la label
    butt.props.image = butt.get_image()
    butt.props.label = ""
#myFrame
    #fram,[labe,xBox]
    fram,othe = myFrame(name, butt, 'black', bFra, sFra, tFra, aFra)

    # in assenza di callback usa quella di debug
    if call == None:
        call = on_clicked
    # passo il riferimento dell'oggetto stesso "butt"
    butt.connect('clicked', call, *data)
# <-        
    #fram, [labe, xBox, butt, call]        
    return fram, [othe[0], othe[1], butt, call]
#-----------------------------------------------------------------------------
def testButSwiFrame():
#myButton
    # ridefinisco le funzioni
    def buttOn(*data):
        print "Adesso %s!" %data[0]
    def buttOff(*data):
        print "Adesso %s!" %data[1]
    # fram, [labe,xBox,butt,call]
    obje, othe = myButSwiFrame(name='myButSwitFrame', 
                               icon=[Gtk.STOCK_NO, Gtk.STOCK_YES],
                               call=None, data=['sono acceso','sono spento'],
                               func=[buttOn, buttOff],
                               bFra=1, sFra=Gtk.SHADOW_ETCHED_OUT, 
#                               tFra='h', aFra=[False, False, 1])
                               tFra='h', aFra=[True, True, 1])
# <-
    return obje

#-----------------------------------------------------------------------------
# myButSwitFramList
#-----------------------------------------------------------------------------
def myButSwiFraList(name=["Read","Write","Default"], 
                    icon=[Gtk.STOCK_NO, Gtk.STOCK_YES],
                    call=None, data=['dati'],
                    func=[None, None],
                    bFra=1, sFra=Gtk.SHADOW_ETCHED_OUT, 
                    tFra='v', aFra=[False, False, 1],
                    tBox='h', aBox=[False, False, 1]):
    # funzione che istanzia oggetti tipo
    def myList(ind):
    #myButSwiFrame
        # fram, [labe, xBox, butt, call]
        return myButSwiFrame(name[ind], icon,
                             call, [ind, data], func, 
                             bFra, sFra, tFra, aFra)
#myBoxList
    # xBox, [fram, [labe, xBox, butt, call]] * N
    obje, othe = myBoxList(name=name, tBox=tBox, 
                           aBox=aBox, func=myList)
# <-
    return obje, othe
#-----------------------------------------------------------------------------
def testButSwiFraList():
#myButSwiFrame    
    # ridefinisco le funzioni
    def buttOn(ind, data):
        print data[0], ind
    def buttOff(ind, data):
        print data[1], ind
    # xBox, [fram, [labe, xBox, butt, call]] * N
    obje, othe = myButSwiFraList(name=["Read","Write","Default"], 
                                 icon=[Gtk.STOCK_NO, Gtk.STOCK_YES],
                                 call=None, data=["adesso sono acceso","adesso sono spento"],
                                 func=[buttOn, buttOff],
                                 bFra=1, sFra=Gtk.SHADOW_ETCHED_OUT, 
                                 tFra='v', aFra=[False, False, 1],
                                 tBox='h', aBox=[False, False, 1])
    #debug
    myViewObject(obje, othe)
# <-
    return obje

#-----------------------------------------------------------------------------
def myTry01():
    sys.exit()

#-----------------------------------------------------------------------------
# Main
#-----------------------------------------------------------------------------
if __name__ == "__main__":
    choi = 11
    
    if choi == 1:
        obje = testButton()
    elif choi == 2:
        obje = testButFrame()
    elif choi == 3:
        obje = testButSwitch()
    elif choi == 4:
        obje = testButSwiFrame()

    elif choi == 11:
        obje = testButList()
    elif choi == 12:
        obje = testButFraList()
    elif choi == 13:
        obje = testButSwiList()
    elif choi == 14:
        obje = testButSwiFraList()
        
    # istanza l'applicazione principale
    self = MyWind(width=None, height=800, title="myBox\ %s" %myRev, center=True, color="#b0b0b0")
    self.vBox.pack_start(child=obje, expand=False, fill=False, padding=0)
    # cediamo il controllo alle gtk
    Gtk.main()
