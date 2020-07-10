import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import mysql.connector


my_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Skarlqhr1!"
)

my_cur = my_db.cursor()
my_cur.execute('USE Kibok_Class')

main_html = "<font color=\"Lime\", size=\"10\">";


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        widget = QPlainTextEdit(self)
        widget.setReadOnly(True)
        widget.appendHtml(main_html + '졸업 할 수 있을까 ...?')
        widget.setGeometry(25, 40, 950, 435)
        widget.show()

        find_1_1_action = QAction(QIcon('pencil.png'), '1-1', self)
        find_1_1_action.setShortcut('Ctrl+1')
        find_1_1_action.triggered.connect(self.find_1_1)

        find_1_2_action = QAction(QIcon('pencil.png'), '1-2', self)
        find_1_2_action.setShortcut('Ctrl+2')
        find_1_2_action.triggered.connect(self.find_1_2)

        find_2_1_action = QAction(QIcon('pencil.png'), '2-1', self)
        find_2_1_action.setShortcut('Ctrl+3')
        find_2_1_action.triggered.connect(self.find_2_1)

        find_2_2_action = QAction(QIcon('pencil.png'), '2-2', self)
        find_2_2_action.setShortcut('Ctrl+4')
        find_2_2_action.triggered.connect(self.find_2_2)

        find_3_1_action = QAction(QIcon('pencil.png'), '3-1', self)
        find_3_1_action.setShortcut('Ctrl+5')
        find_3_1_action.triggered.connect(self.find_3_1)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        insert_score = menubar.addMenu('성적입력')

        score_search = menubar.addMenu('학점조회')
        score_search.addAction(find_1_1_action)
        score_search.addAction(find_1_2_action)
        score_search.addAction(find_2_1_action)
        score_search.addAction(find_2_2_action)
        score_search.addAction(find_3_1_action)

        check_graduation = menubar.addMenu('졸업조건체크')

        self.setWindowTitle('졸업 할 수 있을까 ?')
        self.setGeometry(450, 300, 1000, 500)
        self.show()

    def find_1_1(self):
        print('1-1 학기 학점 조회 함수 실행')
        widget = QPlainTextEdit(self)
        widget.setReadOnly(True)
        widget.appendPlainText('1-1 학기 학점 조회 함수 실행')
        widget.setGeometry(25, 40, 950, 435)
        widget.show()

    def find_1_2(self):
        print('1-2 학기 학점 조회 함수 실행')
        widget = QPlainTextEdit(self)
        widget.setReadOnly(True)

        my_cur.execute('SELECT * FROM 1_2')
        my_result = my_cur.fetchall()

        widget.appendPlainText('1-2 학기 학점 조회 함수 실행\n')
        for cur in my_result:
            widget.appendPlainText(str(cur[2]))
        widget.setGeometry(25, 40, 950, 435)
        widget.show()

    def find_2_1(self):
        print('2-1 학기 학점 조회 함수 실행')
        widget = QPlainTextEdit(self)
        widget.setReadOnly(True)
        widget.appendPlainText('2-1 학기 학점 조회 함수 실행')
        widget.setGeometry(25, 40, 950, 435)
        widget.show()

    def find_2_2(self):
        print('2-2 학기 학점 조회 함수 실행')
        widget = QPlainTextEdit(self)
        widget.setReadOnly(True)
        widget.appendPlainText('2-2 학기 학점 조회 함수 실행')
        widget.setGeometry(25, 40, 950, 435)
        widget.show()

    def find_3_1(self):
        print('3-1 학기 학점 조회 함수 실행')
        widget = QPlainTextEdit(self)
        widget.setReadOnly(True)
        my_cur.execute('SELECT * FROM 3_1')
        my_result = my_cur.fetchall()
        widget.appendPlainText('3-1 학기 학점 조회 함수 실행\n')
        for cur in my_result:
            widget.appendPlainText(str(cur[2]))
        widget.setGeometry(25, 40, 950, 435)
        widget.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())