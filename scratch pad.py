####################################################################################################
##
## BY: UTKAARSH SIINGH
## MADE WITH PYQT5 & QTDESIGNER
## V:1.0.0
##
####################################################################################################

from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QTextEdit, QMessageBox, QColorDialog, QFontDialog, QFileDialog)
from PyQt5.QtCore import (Qt, QDir)
from PyQt5.QtGui import (QFont, QIcon)
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
import sys, os

openfile = ""

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(691, 592)
        self.setWindowTitle("Scratch Pad")
        self.setWindowIcon(QIcon("scratch_pad.ico"))

        self.vbox = QVBoxLayout()
        self.label = QLabel("New Document")
        self.vbox.addWidget(self.label)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Segoe UI", 10))
        self.label.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.466, x2:1, y2:0.472, stop:0 rgba(255, 0, 127, 255), stop:1 rgba(85, 0, 127, 255));\n"
"border-radius:8px;\n"
"color: rgb(255, 255, 255);")

        self.textEdit = QTextEdit()
        self.textEdit.setFont(QFont("Ubuntu Mono", 12))
        self.vbox.addWidget(self.textEdit)

        self.hbox = QHBoxLayout()
        
        self.new_button = QPushButton()
        self.new_button.clicked.connect(self.click_new)
        self.new_button.setIcon(QIcon("new.ico"))
        self.new_button.setText("New")
        self.new_button.setFont(QFont("Segoe UI", 10))
        self.new_button.setStyleSheet(u"background-color: rgb(203, 203, 203);\n"
        "border-radius:8px;")
        self.hbox.addWidget(self.new_button)
        
        self.open_button = QPushButton()
        self.open_button.clicked.connect(self.click_open)
        self.open_button.setIcon(QIcon("open.ico"))
        self.open_button.setText("Open")
        self.open_button.setFont(QFont("Segoe UI", 10))
        self.open_button.setStyleSheet(u"background-color: rgb(203, 203, 203);\n"
        "border-radius:8px;")
        self.hbox.addWidget(self.open_button)

        self.save_button = QPushButton()
        self.save_button.clicked.connect(self.click_save)
        self.save_button.setIcon(QIcon("save.ico"))
        self.save_button.setText("Save")
        self.save_button.setFont(QFont("Segoe UI", 10))
        self.save_button.setStyleSheet(u"background-color: rgb(203, 203, 203);\n"
        "border-radius:8px;")
        self.hbox.addWidget(self.save_button)

        self.font_button = QPushButton()
        self.font_button.clicked.connect(self.click_font)
        self.font_button.setIcon(QIcon("font.ico"))
        self.font_button.setText("Font")
        self.font_button.setFont(QFont("Segoe UI", 10))
        self.font_button.setStyleSheet(u"background-color: rgb(203, 203, 203);\n"
        "border-radius:8px;")
        self.hbox.addWidget(self.font_button)

        self.color_button = QPushButton()
        self.color_button.clicked.connect(self.click_color)
        self.color_button.setIcon(QIcon("color.ico"))
        self.color_button.setText("Color")
        self.color_button.setFont(QFont("Segoe UI", 10))
        self.color_button.setStyleSheet(u"background-color: rgb(203, 203, 203);\n"
        "border-radius:8px;")
        self.hbox.addWidget(self.color_button)

        self.print_button = QPushButton()
        self.print_button.clicked.connect(self.click_print)
        self.print_button.setIcon(QIcon("print.ico"))
        self.print_button.setText("Print")
        self.print_button.setFont(QFont("Segoe UI", 10))
        self.print_button.setStyleSheet(u"background-color: rgb(203, 203, 203);\n"
        "border-radius:8px;")
        self.hbox.addWidget(self.print_button)

        self.print_preview_button = QPushButton()
        self.print_preview_button.clicked.connect(self.click_print_preview)
        self.print_preview_button.setIcon(QIcon("print_preview.ico"))
        self.print_preview_button.setText("Print Preview")
        self.print_preview_button.setFont(QFont("Segoe UI", 10))
        self.print_preview_button.setStyleSheet(u"background-color: rgb(203, 203, 203);\n"
        "border-radius:8px;")
        self.hbox.addWidget(self.print_preview_button)

        self.exit_button = QPushButton()
        self.exit_button.clicked.connect(self.click_exit)
        self.exit_button.setIcon(QIcon("exit.ico"))
        self.exit_button.setText("Exit")
        self.exit_button.setFont(QFont("Segoe UI", 10))
        self.exit_button.setStyleSheet(u"background-color: rgb(203, 203, 203);\n"
        "border-radius:8px;\n"
        "color:red;")
        self.hbox.addWidget(self.exit_button)
        
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)

    def click_new(self):
        self.message = QMessageBox.question(self, "Confirm", "Are you sure that you want to create a new .txt file ?", QMessageBox.Yes | QMessageBox.No)
        if self.message == QMessageBox.Yes:
            self.message2 = QMessageBox.question(self, "Confirm", "Do you want to save the file ?", QMessageBox.Yes | QMessageBox.No)
            if self.message2 == QMessageBox.Yes:
                self.click_save()
                self.textEdit.setText("")
            else:
                pass
        else:
            pass
        self.label.setText("New Document")

    def click_open(self):
        global openfile
        try:
            openfile, _ = QFileDialog.getOpenFileName(self, 'Open File', "", "Text File (*.txt)")
            with open(openfile, "r") as f:
                lines = f.read()
            self.textEdit.setText(lines)
            self.label.setText(openfile)
        except Exception as e:
            pass

    def click_save(self):
        global openfile
        if len(openfile) == 0:
            savefile, _= QFileDialog.getSaveFileName(self, 'Save File', "", "Text File (*.txt)")
            self.text = self.textEdit.toPlainText()

            try:
                with open(savefile, "w") as f:
                    f.write(self.text)
                self.label.setText(savefile)
            except:
                pass
        
        elif len(openfile) > 0:
            with open(openfile, "w") as f:
                self.text = self.textEdit.toPlainText()
                f.write(self.text)
        

    def click_font(self):
        textfont, ok = QFontDialog.getFont()

        if ok:
            self.textEdit.setFont(textfont)

    def click_color(self):
        self.color = QColorDialog.getColor()
        self.textEdit.setTextColor(self.color)

    def click_print(self):
        self.printer = QPrinter(QPrinter.HighResolution)
        self.dialog = QPrintDialog(self.printer)

        if self.dialog.exec_() == QPrintDialog.Accepted:
            self.textEdit.print_(self.printer)

    def click_print_preview(self):
        self.printer = QPrinter(QPrinter.HighResolution)
        self.priviewDialog = QPrintPreviewDialog(self.printer)
        self.priviewDialog.paintRequested.connect(self.print_preview)
        self.priviewDialog.exec_()

    def print_preview(self):
        self.textEdit.print_(self.printer)

    def click_exit(self):
        self.close()

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
