#!/usr/bin/env python

from GUI import GUI
import wx
from DataLoader import load_data_from_csv, load_mnist_data, combine_datasets, split_data
from NeuralNetwork import create_neural_network, configure_model, train_model, evaluate_model, load_model
from ImageProcessing import load_and_process_image, predict_text_from_image
import os

class MainFrame(GUI):
    def __init__(self, parent):# Now these functions can be accessed directly when importing the ImageProcessing package.
        GUI.__init__(self, None)
        self.image = None  # instance variable for wx.Image
        self.model = self.load_or_create_model()  # Load existing model or create a new one

    def load_or_create_model(self):
        model_file = 'saved_model.h5'  

        if os.path.exists(model_file):
            print("Loading existing model...")
            loaded_model = load_model(model_file)
        else:
            print("Creating a new model...")
            loaded_model = self.create_new_model()
            loaded_model.save(model_file)  

        return loaded_model

    def create_new_model(self):
        features_letters, labels_letters = load_data_from_csv()
        X_train_mnist, y_train_mnist, X_test_mnist, y_test_mnist = load_mnist_data()
        combined_features, combined_labels = combine_datasets(features_letters, labels_letters, X_train_mnist,
                                                              y_train_mnist)
        X_train, X_test, y_train, y_test = split_data(combined_features, combined_labels)

        model = create_neural_network()
        model = configure_model(model)
        model = train_model(model, X_train, y_train, X_test, y_test)

        return model
    # method repainting loaded image on wxPanel_image
    def onPaint(self, imageToPaint):
        # create ClientDC and clear panel 
        dc = wx.ClientDC(self.wxPanel_image)
        dc.Clear()

        # wxPanel_image width and height
        (w, h) = self.wxPanel_image.GetSize()

        # image width and height
        (img_w, img_h) = imageToPaint.GetSize()

        # shift from top left corner to center image
        shiftX = 0
        shiftY = 0

        # max image height and space on left and right
        if (img_h / img_w) > (h / w):
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
        dc.DrawBitmap(imageToPaint.ConvertToBitmap(), int(shiftX), int(shiftY))

    def wxButton_loadFileOnButtonClick(self, event):
        print("wxButton_loadFile")
        # trzeba zaimplementowac zaladowanie obrazka z pliku do jakiejs zmiennej
        # mozna tez od razy wyswietlic zaladowany obrazek na przygotowanym panelu (wxPanel_image)

        # open file dialog window, allow to select only .jpg and .png files
        fileDialog = wx.FileDialog(self, "Open image file", wildcard="JPG and PNG files (*.jpg;*.png)|*.jpg;*.png",
                                   style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

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
    def wxPanel_imageOnSize(self, event):
        # call onPaint method only when image is loaded
        if self.image is not None:
            self.onPaint(self.image.Copy())

    def wxButton_OCROnButtonClick(self, event):
        print("wxButton_OCR")
        # trzeba zaimplementowac cale dzialanie OCR
        # po sczytaniu znakow/tekstu z obrazka mozna go wpisac do read-only panelu tekstowego (textCtrl_outputText) 

    def wxButton_copyOnButtonClick(self, event):
        print("wxButton_copy")
    # ten przycisk jest tylko po to, zeby po wcisnieciu go zawartosc panelu tekstowego (textCtrl_outputText) zostala przekopiowana do schowka
