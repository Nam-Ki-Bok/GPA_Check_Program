import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import mysql.connector


my_db = mysql.connector.connect(
  host="localhost",
  user="my_name",
  password="my_password"
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
        self.setFixedSize(1000, 500)
        self.show()

    def print_info(self, check):

        widget = QPlainTextEdit(self)
        widget.setReadOnly(True)
        query = 'SELECT * FROM ' + check
        my_cur.execute(query)
        my_result = my_cur.fetchall()
        widget.appendPlainText(check.replace('_', '-'))
        widget.appendPlainText('\n교과목명\t\t\t\t\t이수구분\t\t\t\t학점\t\t등급')
        widget.appendPlainText('-------------------------------------------------------------------------------'
                               '----------------------------------------------------------------------------')
        application_credit = 0  # 신청학점
        acquisition_credit = 0  # 취득학점
        for cur in my_result:
            class_name = str(cur[0])
            classification = str(cur[1])
            credit = str(cur[2])
            application_credit += int(credit)
            if len(class_name) <= 8:
                output = class_name + '\t\t\t\t\t' + classification + '\t\t\t\t' + credit
            else:
                output = class_name + '\t\t\t\t' + classification + '\t\t\t\t' + credit
            widget.appendPlainText(output)

        widget.appendPlainText('-------------------------------------------------------------------------------'
                               '----------------------------------------------------------------------------\n')
        widget.appendPlainText('신청학점 : ' + str(application_credit) + '\t\t\t\t\t취득학점 : ' + str(acquisition_credit) +
                               '\t\t\t\t\t평균평점 : ')
        widget.setGeometry(25, 40, 950, 435)
        widget.show()

    def find_1_1(self):
        self.print_info('1_1')

    def find_1_2(self):
        self.print_info('1_2')

    def find_2_1(self):
        self.print_info('2_1')

    def find_2_2(self):
        self.print_info('2_2')

    def find_3_1(self):
        self.print_info('3_1')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())