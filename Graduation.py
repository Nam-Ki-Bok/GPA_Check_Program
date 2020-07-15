import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import mysql.connector

box_list = []  # 성적입력 combo_box
class_list = []  # 성적입력 할 과목
table_name = []  # input 에서 사용 할 테이블 이름

my_db = mysql.connector.connect(
  host="localhost",
  user="user_name",
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

        insert_1_1_action = QAction(QIcon('insert.png'), '1-1', self)
        insert_1_1_action.setShortcut('alt+1')
        insert_1_1_action.triggered.connect(self.insert_1_1)

        insert_1_2_action = QAction(QIcon('insert.png'), '1-2', self)
        insert_1_2_action.setShortcut('alt+2')
        insert_1_2_action.triggered.connect(self.insert_1_2)

        insert_2_1_action = QAction(QIcon('insert.png'), '2-1', self)
        insert_2_1_action.setShortcut('alt+3')
        insert_2_1_action.triggered.connect(self.insert_2_1)

        insert_2_2_action = QAction(QIcon('insert.png'), '2-2', self)
        insert_2_2_action.setShortcut('alt+4')
        insert_2_2_action.triggered.connect(self.insert_2_2)

        insert_3_1_action = QAction(QIcon('insert.png'), '3-1', self)
        insert_3_1_action.setShortcut('alt+5')
        insert_3_1_action.triggered.connect(self.insert_3_1)

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
        insert_score.addAction(insert_1_1_action)
        insert_score.addAction(insert_1_2_action)
        insert_score.addAction(insert_2_1_action)
        insert_score.addAction(insert_2_2_action)
        insert_score.addAction(insert_3_1_action)

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
        widget.appendPlainText(check.replace('_', '-') + ' 성적 조회\n')
        widget.appendPlainText('교과목명\t\t\t\t\t이수구분\t\t\t\t학점\t\t등급')
        widget.appendPlainText('-------------------------------------------------------------------------------'
                               '----------------------------------------------------------------------------')
        application_credit = 0  # 신청학점
        acquisition_credit = 0  # 취득학점
        average_grade = self.cal_average_credit(my_result)

        for idx, cur in enumerate(my_result):
            class_name = str(cur[1])
            classification = str(cur[2])
            credit = str(cur[3])
            grade = str(cur[4])
            application_credit += int(credit)
            acquisition_credit += int(credit)
            if idx == 0:
                if len(class_name) <= 8:
                    output = class_name + '\t\t\t\t\t' + classification + '\t\t\t\t' + credit + '\t\t' + grade
                else:
                    output = class_name + '\t\t\t\t' + classification + '\t\t\t\t' + credit + '\t\t' + grade
            else:
                if len(class_name) <= 8:
                    output = '\n' + class_name + '\t\t\t\t\t' + classification + '\t\t\t\t' + credit + '\t\t' + grade
                else:
                    output = '\n' + class_name + '\t\t\t\t' + classification + '\t\t\t\t' + credit + '\t\t' + grade
            widget.appendPlainText(output)

        widget.appendPlainText('-------------------------------------------------------------------------------'
                               '----------------------------------------------------------------------------\n')
        widget.appendPlainText('신청학점 : ' + str(application_credit) + '\t\t\t\t\t취득학점 : ' + str(acquisition_credit) +
                               '\t\t\t\t\t평균평점 : ' + str(average_grade)[:4])
        widget.setGeometry(25, 40, 950, 435)
        widget.show()

    def cal_average_credit(self, my_result):
        sum = 0
        p_cnt = 0
        for cur in my_result:
            if cur[4] == 'A+':
                sum += 4.5
            elif cur[4] == 'A0':
                sum += 4.0
            elif cur[4] == 'B+':
                sum += 3.5
            elif cur[4] == 'B0':
                sum += 3.0
            elif cur[4] == 'C+':
                sum += 2.5
            elif cur[4] == 'C0':
                sum += 2.0
            elif cur[4] == 'D+':
                sum += 1.5
            elif cur[4] == 'D0':
                sum += 1.0
            elif cur[4] == 'P':
                p_cnt += 1

        return sum / (len(my_result) - p_cnt)


    def insert_info(self, check):
        table_name.clear()
        table_name.append(check)
        widget = QPlainTextEdit(self)
        widget.setReadOnly(True)
        query = 'SELECT * FROM ' + check
        my_cur.execute(query)
        my_result = my_cur.fetchall()
        widget.appendPlainText(check.replace('_', '-') + ' 성적 입력\n')
        widget.appendPlainText('교과목명\t\t\t\t\t이수구분\t\t\t\t학점\t\t등급')
        widget.appendPlainText('-------------------------------------------------------------------------------'
                               '----------------------------------------------------------------------------')
        for idx, cur in enumerate(my_result):
            class_name = str(cur[1])
            classification = str(cur[2])
            credit = str(cur[3])
            if idx == 0:
                if len(class_name) <= 8:
                    output = class_name + '\t\t\t\t\t' + classification + '\t\t\t\t' + credit
                else:
                    output = class_name + '\t\t\t\t' + classification + '\t\t\t\t' + credit
            else:
                if len(class_name) <= 8:
                    output = '\n' + class_name + '\t\t\t\t\t' + classification + '\t\t\t\t' + credit
                else:
                    output = '\n' + class_name + '\t\t\t\t' + classification + '\t\t\t\t' + credit
            widget.appendPlainText(output)

        widget.appendPlainText('-------------------------------------------------------------------------------'
                               '----------------------------------------------------------------------------\n')
        widget.setGeometry(25, 40, 950, 435)
        widget.show()

        self.init_combo_box(my_result)

    def init_combo_box(self, my_result):
        y = 89
        box_list.clear()
        class_list.clear()
        for cur in my_result:
            class_list.append(cur[0])
            cur = QComboBox(self)
            cur.addItem('A+')
            cur.addItem('A0')
            cur.addItem('B+')
            cur.addItem('B0')
            cur.addItem('C+')
            cur.addItem('C0')
            cur.addItem('D+')
            cur.addItem('D0')
            cur.addItem('F')
            cur.addItem('FA')
            cur.addItem('P')
            cur.addItem('NP')
            cur.move(900, y)
            cur.setFixedSize(60, 60)
            cur.show()
            box_list.append(cur)

            y += 32

        insert_btn = QPushButton(self)
        insert_btn.setText('입력')
        insert_btn.setFixedSize(60, 30)
        insert_btn.move(900, y + 30)
        insert_btn.show()
        insert_btn.clicked.connect(self.input_data)

    def input_data(self):
        grade_list = [val.currentText() for val in box_list]
        for idx, val in enumerate(grade_list):  # UPDATE 1_1 SET 등급 = 'A+' WHERE id = 1;
            query = 'UPDATE ' + str(table_name[0]) + ' SET 등급 = \'' + val + '\' WHERE id = ' + str(idx + 1)
            print(query)
            my_cur.execute(query)
            my_db.commit()

    def insert_1_1(self):
        self.insert_info('1_1')

    def insert_1_2(self):
        self.insert_info('1_2')

    def insert_2_1(self):
        self.insert_info('2_1')

    def insert_2_2(self):
        self.insert_info('2_2')

    def insert_3_1(self):
        self.insert_info('3_1')

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
