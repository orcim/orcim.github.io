#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys

#-----------------------------------------------------------------------------
# Main
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    # suddivido la cartella dal nome del file                
    path = os.getcwd()
    par, cur = os.path.split(path)
    print "*** start from", par, cur

    # directory da escludere
    myExcl = ["z", ]

    lisDir=[] 
    lisFil=[] 

    def walkTree(dir, lisDir=[], lisFil=[]):
        """ 
        """
        # lettura delle cartelle presenti
        for name in os.listdir(dir):
            # associo il nome al path
            path = os.path.join(dir, name)
            # verifica se e' una cartella
            if os.path.isdir(path):
                temp = path.split('/')
                for ele in myExcl:
                    if ele in temp:
                        continue
                    print path
                    # aggiungo cartella alla lista
                    lisDir.append(path)
                    # vado in profondita' (ricorsivo)
                    walkTree(path, lisDir, lisFil)
            else:
                if name.endswith(".pyc"):
                    os.system('rm %s' %path)
                    print "delete -> %s" %name
                # aggiungo file alla lista
                lisFil.append(name)

    # from current
    walkTree(path, lisDir, lisFil)
    # for ele in lisDir:
    #     print os.path.split(ele)
    #print lisFil
                
