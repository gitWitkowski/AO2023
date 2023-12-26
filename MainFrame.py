#!/usr/bin/env python

from GUI import GUI
import wx

class MainFrame(GUI):
    def __init__( self, parent ):
        GUI.__init__(self, None)
        self.image = None # instance variable for wx.Image 

    # method repainting loaded image on wxPanel_image
    def onPaint(self, imageToPaint):
        # create ClientDC and clear panel 
        dc = wx.ClientDC(self.wxPanel_image)
        dc.Clear()

        # wxPanel_image width and height
        (w,h) = self.wxPanel_image.GetSize()
        
        # image width and height
        (img_w,img_h) = imageToPaint.GetSize()
        
        # shift from top left corner to center image
        shiftX = 0
        shiftY = 0

        # max image height and space on left and right
        if (img_h/img_w) > (h/w):
            # rescale image
            imageToPaint = imageToPaint.Rescale(int(img_w / img_h * h), h)
            # adjust shift
            shiftX = (w - imageToPaint.GetWidth()) / 2

        # max image width and space on top and bottom
        else:
            # rescale image
            imageToPaint = imageToPaint.Rescale(w, int(img_h / img_w * w))
            # adjust shift
            shiftY = (h - imageToPaint.GetHeight()) / 2

        # convert image to bitmap and draw it on wxPanel_image
        dc.DrawBitmap(imageToPaint.ConvertToBitmap(),int(shiftX),int(shiftY))

    def wxButton_loadFileOnButtonClick( self, event ):
        print("wxButton_loadFile")
        # trzeba zaimplementowac zaladowanie obrazka z pliku do jakiejs zmiennej
        # mozna tez od razy wyswietlic zaladowany obrazek na przygotowanym panelu (wxPanel_image)

        # open file dialog window, allow to select only .jpg and .png files
        fileDialog = wx.FileDialog(self, "Open image file", wildcard="JPG and PNG files (*.jpg;*.png)|*.jpg;*.png", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        # close dialog window if user has changed mind
        if fileDialog.ShowModal() == wx.ID_CANCEL:
            return

        # get path to file
        pathname = fileDialog.GetPath()

        try:
            # load image to file
            self.image = wx.Image(pathname, wx.BITMAP_TYPE_ANY)
            # draw image on wxPanel_image
            self.onPaint(self.image.Copy())
        except IOError:
            wx.LogError("Cannot open file!")

    # method to repaint loaded image whenever wxPanel_image size changes
    def wxPanel_imageOnSize( self, event ):
        # call onPaint method only when image is loaded
        if self.image != None:
            self.onPaint(self.image.Copy())

    def wxButton_OCROnButtonClick( self, event ):
        print("wxButton_OCR")
        # trzeba zaimplementowac cale dzialanie OCR
        # po sczytaniu znakow/tekstu z obrazka mozna go wpisac do read-only panelu tekstowego (textCtrl_outputText) 

    def wxButton_copyOnButtonClick( self, event ):
	    print("wxButton_copy")
        # ten przycisk jest tylko po to, zeby po wcisnieciu go zawartosc panelu tekstowego (textCtrl_outputText) zostala przekopiowana do schowka