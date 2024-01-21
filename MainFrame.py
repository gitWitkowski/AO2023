#!/usr/bin/env python

from GUI import GUI
import wx
from DataLoader import load_data_from_csv, load_mnist_data, combine_datasets, split_data
from NeuralNetwork import create_neural_network, configure_model, train_model, evaluate_model, load_saved_model
from ImageProcessing import load_and_process_image, predict_text_from_image
from Constants import MODEL_DIRECTORY, MODEL_FULL_PATH
import os

class MainFrame(GUI):
    def __init__(self, parent):# Now these functions can be accessed directly when importing the ImageProcessing package.
        GUI.__init__(self, None)
        self.image = None  # instance variable for wx.Image
        self.image_path = None
        self.model = self.load_or_create_model()  # Load existing model or create a new one

    def load_or_create_model(self):
        if os.path.exists(MODEL_FULL_PATH):
            print("Loading existing model: " + MODEL_FULL_PATH)
            loaded_model = load_saved_model(MODEL_FULL_PATH)
        else:
            print("Creating a new model...")
            new_model = self.create_new_model()
            if not os.path.exists(MODEL_DIRECTORY):
                os.makedirs(MODEL_DIRECTORY)
            new_model.save(MODEL_FULL_PATH)
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

        # open file dialog window, allow to select only .png files
        fileDialog = wx.FileDialog(self, "Open image file", wildcard="PNG files (*.png)|*.png",
                                   style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        # close dialog window if user has changed mind
        if fileDialog.ShowModal() == wx.ID_CANCEL:
            return

        # get path to file
        self.image_path = fileDialog.GetPath()
        try:
            # load image to file
            self.image = wx.Image(self.image_path, wx.BITMAP_TYPE_ANY)
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
        if self.image is not None:
            cropped_chars = load_and_process_image(self.image_path)
            if cropped_chars:
                predicted_text = predict_text_from_image(cropped_chars, self.model)
                self.textCtrl_outputText.SetValue(predicted_text)

    def wxButton_copyOnButtonClick(self, event):
        print("wxButton_copy")
        # open the clipboard and write content of textCtrl_outputText into it
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(wx.TextDataObject(self.textCtrl_outputText.GetValue()))
            wx.TheClipboard.Close()

        wx.MessageBox("Tekst został skopiowany do schowka.", "Sukces", wx.OK | wx.ICON_INFORMATION)