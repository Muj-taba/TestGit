## update the lines
import cv2
import numpy as np
import time
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
from PyQt5.uic import loadUiType
from os import path
from PyQt5.QtWidgets import *



FORM_CLASS,_ = loadUiType(path.join(path.dirname(__file__),"hu.ui"))
FORM_CLASS2, _ = loadUiType(path.join(path.dirname(__file__), "gallery.ui"))


class Main(QMainWindow,FORM_CLASS):
    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.select)
        self.pushButton_2.clicked.connect(self.cloze)
        self.window2 = gallery()
        self.pushButton_3.clicked.connect(self.galleryy)

    def galleryy(self):
            self.window2.show()

    def select(self):
        if self.radioButton.isChecked():
            self.video()

        if self.radioButton_2.isChecked():
            self.image()



    def image(self):
        cap = cv2.VideoCapture(0)  # video capture source camera (Here webcam of laptop)
        ret, frame = cap.read()  # return a single frame in variable `frame`


        while (True):
            cv2.imshow('img2', frame)  # display the captured image
            if cv2.waitKey(1) & 0xFF == ord('y'):  # save on pressing 'y'
                cv2.imwrite('c1.png', frame)
                cv2.destroyAllWindows()
                break

        cap.release()


    def video(self):



        cap = cv2.VideoCapture(1)

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

        while (cap.isOpened()):

            ret, frame = cap.read()

            if ret == True:
                frame = cv2.flip(frame, 0)

                # write the flipped frame
                out.write(frame)

                cv2.imshow('Huda', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        # Release everything if job is finished
        cap.release()
        out.release()
        cv2.destroyAllWindows()

    def cloze(self):
        cv2.destroyWindow()

class gallery(QMainWindow, FORM_CLASS2):
    def __init__(self, parent=None):
        super(gallery, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)



def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()