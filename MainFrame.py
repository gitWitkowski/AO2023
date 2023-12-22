#!/usr/bin/env python

from GUI import GUI

class MainFrame(GUI):
    def __init__( self, parent ):
        GUI.__init__(self, None)

    def wxButton_loadFileOnButtonClick( self, event ):
        print("wxButton_loadFile")
        # trzeba zaimplementowac zaladowanie obrazka z pliku do jakiejs zmiennej
        # mozna tez od razy wyswietlic zaladowany obrazek na przygotowanym panelu (wxPanel_image)

    def wxButton_OCROnButtonClick( self, event ):
        print("wxButton_OCR")
        # trzeba zaimplementowac cale dzialanie OCR
        # po sczytaniu znakow/tekstu z obrazka mozna go wpisac do read-only panelu tekstowego (textCtrl_outputText) 

    def wxButton_copyOnButtonClick( self, event ):
	    print("wxButton_copy")
        # ten przycisk jest tylko po to, zeby po wcisnieciu go zawartosc panelu tekstowego (textCtrl_outputText) zostala przekopiowana do schowka