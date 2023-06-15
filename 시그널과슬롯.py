#시그널과 슬롯 (Signal & Slot) - https://wikidocs.net/22020
#다이얼 위젯으로 조절한 값을 화면에 출력하는 프로그램을 만들어 보겠습니다.
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLCDNumber, QDial, QVBoxLayout

#다이얼을 움직이면 그 값에 맞춰서 LCD에 숫자가 표시됩니다.
class MyApp(QWidget):

    def __init__(self):
         #super( ) 메서드는 부모 클래스를 상속받는 메서드인데 super( ).__init__( )를 통해 부모 클래스의 초기값을 호출하게 됩니다.
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        self.setLayout(vbox)
# valueChanged 시그널을 lcd의 display 슬롯에 연결합니다. display 슬롯은 숫자를 받아서 QLCDNumber 위젯에 표시하는 역할을 합니다.
        dial.valueChanged.connect(lcd.display)

        self.setWindowTitle('Signal and Slot')
        self.setGeometry(300, 300, 200, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())