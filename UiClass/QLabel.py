import os
import sys

from PySide6.QtWidgets import *
from PySide6 import uic
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile

#https://doc.qt.io/qtforpython-6/tutorials/basictutorial/uifiles.html
#============================  class 설정 부분  =======================================
def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('QLabel.ui')
form_class = uic.loadUiType(form)[0]

class WindowClass( QMainWindow, form_class):
    def __init__(self):
        super( ).__init__( )
        self.setupUi(self)
#==========================  Signal & Setting 부분  ===================================
        # setAlignment [정렬]
        self.label_1.setAlignment(Qt.AlignLeft)
        self.label_2.setAlignment(Qt.AlignRight)
        self.label_3.setAlignment(Qt.AlignJustify)
        self.label_3.setAlignment(Qt.AlignVCenter)
        self.label_4.setAlignment(Qt.AlignCenter)

        # setText / setNum [입력]
        self.label_5.setText('Text')
        self.label_6.setNum(123)

        # setIndent [들여쓰기] / setMargin [여백]
        self.label_7.setAlignment(Qt.AlignLeft)
        self.label_7.setIndent(10)
        self.label_8.setAlignment(Qt.AlignHCenter)
        self.label_8.setMargin(6)

        # setTextFormat(TextFormat) [텍스트 포맷]
        self.label_9.setText('첫번째줄<br>두번째줄')
        self.label_9.setTextFormat(Qt.PlainText)
        self.label_10.setText('<span style="color : red">빨강</span>')
        self.label_10.setTextFormat(Qt.RichText)

        # setWorkWrap(bool) [자동 줄바꿈]
        self.label_11.setText('가나다라 마바사아 자차카타파하')
        self.label_11.setWordWrap(True)

        # setOpenExternalLinks [링크열기]
        self.label_12.setText("<a href=\"http://www.google.com\">구글링크</a>")
        self.label_12.setOpenExternalLinks(True)

        # setScaledContents [칸에 맞게 이미지 조정]
        pixmap=QPixmap("sun_blue.png")
        self.label_13.setPixmap(pixmap)
        self.label_14.setPixmap(pixmap)
        self.label_14.setScaledContents(True)
        print("hasScaledContents : "+str(self.label_14.hasScaledContents()))

        # setBuddy [오브젝트 연결]
        self.label_15.setText("&Name")
        self.label_15.setBuddy(self.line_15)
        self.label_16.setText("A&ge")
        self.label_16.setBuddy(self.line_16)

        # Signal들
        self.label_17.setText("<a href>label_17</a>")
        self.label_17.linkActivated.connect(self.fnc_clicked)
        self.label_17.linkHovered.connect(self.fnc_hovered)

        # setTextInteractionFlags [텍스트 상호작용]
        self.label_19.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse|Qt.TextEditable)
        self.btn_19.setText('Ctrl+G')
        self.btn_19.setShortcut('Ctrl+G')
        self.btn_19.clicked.connect(self.fnc_label_19)

        # clear [내용 삭제]
        self.btn_20.clicked.connect(self.fnc_label_20)
#===============================  Slot 부분   =========================================
    def fnc_clicked(self):
        self.label_18.setText('clicked')

    def fnc_hovered(self):
        self.label_18.setText('hovered')

    def fnc_label_19(self):
        self.label_19.setSelection(1,3)
        print("selectedText : "+self.label_19.selectedText())
        print("hasSelectedText : " + str(self.label_19.hasSelectedText()))

    def fnc_label_20(self):
        self.label_20.clear()
#==============================  app 실행 부분  =======================================
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass( )
    myWindow.show( )
    app.exec_( )