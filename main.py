# memasukkan encrypt extended vigenere cypher ke RC4
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap
from rc4 import *
from extended_vigenere import * 

class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        loadUi("extended.ui", self)
        self.label_6.setText("Modified RC4")
        self.exp.clicked.connect(self.Export)
        self.encrypt.clicked.connect(self.Encrypt)
        self.decrypt.clicked.connect(self.Decrypt)
        self.exp_2.clicked.connect(self.Export_2)

    def Encrypt (self) :
        output = []
        text = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        fileloc = self.textEdit_4.toPlainText()

        if text == '':
            bin_data = open(fileloc, 'rb').read()
            string = bin_data.decode('latin1')
            enc = rc4Encode(string,key)
            encode = ex_vigenereEncode(enc, key)
        else :
            enc = rc4Encode(text,key)
            encode = ex_vigenereEncode(enc,key)            
        output = ''.join(encode)    
        self.textBrowser.setText(str(output))
    
    def Decrypt (self):
        output = []
        text = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        fileloc = self.textEdit_4.toPlainText()

        if text == '':
            bin_data = open(fileloc, 'rb').read()
            string = bin_data.decode('latin1')
            decode = ex_vigenereDecode(string, key)
            dec = rc4Encode(decode,key)
        else :
            decode = ex_vigenereDecode(text,key)  
            dec = rc4Encode(decode,key) 
        output = ''.join(dec)    
        self.textBrowser_2.setText(str(output))

    def Export (self):
        key = self.textEdit_2.toPlainText()
        path = self.textEdit_4.toPlainText()
        text = self.textEdit.toPlainText()
        filetype = self.textEdit_3.toPlainText()
        fileName = "hasil." + filetype
        if text == '':
            bin_data = open(path, 'rb').read()
            string = bin_data.decode('latin1')
            decode = ex_vigenereDecode(string, key)
            dec = rc4Encode(decode,key)
        else :
            decode = ex_vigenereDecode(text,key)  
            dec = rc4Encode(decode,key) 
        dec = "" . join(dec)
        with open(fileName, 'wb') as f: 
            f.write(dec.encode('latin1'))

    def Export_2 (self):
        key = self.textEdit_2.toPlainText()
        fileloc = self.textEdit_4.toPlainText()
        text = self.textEdit.toPlainText()
        if text == '':
            bin_data = open(fileloc, 'rb').read()
            string = bin_data.decode('latin1')
            enc = rc4Encode(string,key)
            encode = ex_vigenereEncode(enc, key)
        else :
            enc = rc4Encode(text,key)
            encode = ex_vigenereEncode(enc,key)
        en = "" . join(encode)
        with open('encrypt', 'wb') as f: 
            f.write(en.encode('latin1'))


# string = 'haigais'
# key = 'hqwertfdkcmrl;sf23bl;;[weq232324vvxvvbdfge]'
# c = rc4Encode(string,key)
# print (c)
# a = ex_vigenereEncode(c, key)
# print(a)
# b = ex_vigenereDecode(a,key)
# print(b)
# f = rc4Decode(b,key)
# print(f)

app = QApplication(sys.argv)
welcome = Menu()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(700)
widget.setFixedWidth(900)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Bye - bye")