import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import mysql.connector

box_list = []  # 성적입력 combo_box
class_list = []  # 성적입력 할 과목
table_name = []  # input 에서 사용 할 테이블 이름
non_data = []  # input 에서 non_class data 담을 리스트

my_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
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

        insert_non_action = QAction(QIcon('insert.png'), '비교과', self)
        insert_non_action.setShortcut('alt+0')
        insert_non_action.triggered.connect(self.insert_non)

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

        find_non_action = QAction(QIcon('pencil.png'), '비교과', self)
        find_non_action.setShortcut('Ctrl+0')
        find_non_action.triggered.connect(self.find_non)

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
        insert_score.addAction(insert_non_action)
        insert_score.addAction(insert_1_1_action)
        insert_score.addAction(insert_1_2_action)
        insert_score.addAction(insert_2_1_action)
        insert_score.addAction(insert_2_2_action)
        insert_score.addAction(insert_3_1_action)

        score_search = menubar.addMenu('학점조회')
        score_search.addAction(find_non_action)
        score_search.addAction(find_1_1_action)
        score_search.addAction(find_1_2_action)
        score_search.addAction(find_2_1_action)
        score_search.addAction(find_2_2_action)
        score_search.addAction(find_3_1_action)

        cond_check_action = QAction(QIcon('pencil.png'), '실행', self)
        cond_check_action.setShortcut('Ctrl+-')
        cond_check_action.triggered.connect(self.cond_check)

        check_graduation = menubar.addMenu('졸업조건체크')
        check_graduation.addAction(cond_check_action)

        self.setWindowTitle('졸업 할 수 있을까 ?')
        self.setGeometry(450, 300, 1000, 500)
        self.setFixedSize(1000, 500)
        self.show()

    def cond_check(self):
        semester = ['1_1', '1_2', '2_1', '2_2', '3_1', '3_2', '4_1', '4_2']
        major_must = 0  # 전공필수
        major_sel = 0  # 전공선택
        must = 0  # 교양필수
        select1 = 0  # 교선1
        select2 = 0  # 교선2
        basic = 0  # 학문기초교양

        widget = QPlainTextEdit(self)
        widget.setReadOnly(True)

        for cur in semester:
            try:
                query = 'SELECT 이수구분, 학점 FROM ' + cur
                my_cur.execute(query)
                my_result = my_cur.fetchall()
                for val in my_result:
                    if val[0] == '전필':
                        major_must += val[1]
                    elif val[0] == '전선':
                        major_sel += val[1]
                    elif val[0] == '교필':
                        must += val[1]
                    elif val[0] == '교선1':
                        select1 += val[1]
                    elif val[0] == '교선2':
                        select2 += val[1]
                    elif val[0] == '기교':
                        basic += val[1]
            except:
                pass

        widget.appendPlainText('-------------------------------------------------------------------------------'
                               '----------------------------------------------------------------------------')
        major_must_text = '\t\t\t전공필수 : {} / 37'.format(major_must)
        if major_must < 37:
            major_must_text += ' \t{} 학점 부족 !!!'.format(37 - major_must)
        else:
            major_must_text += '\t조건 충족 !!!'
        widget.appendPlainText(major_must_text)

        major_sel_text = '\n\t\t\t전공선택 : {} / 35'.format(major_sel)
        if major_sel < 35:
            major_sel_text += '\t{} 학점 부족 !!!'.format(35 - major_sel)
        else:
            major_sel_text += '\t조건 충족 !!!'
        widget.appendPlainText(major_sel_text)

        must_text = '\n\t\t\t교양필수 : {} / 11'.format(must)
        if must < 11:
            must_text += '\t{} 학점 부족 !!!'.format(11 - must)
        else:
            must_text += '\t조건 충족 !!!'
        widget.appendPlainText(must_text)

        select1_text = '\n\t\t\t교양선택1 : {} / 15'.format(select1)
        if select1 < 15:
            select1_text += '\t{} 학점 부족 !!!\t\t3분야 이상 수강 필수 !!!'.format(15 - select1)
        else:
            select1_text += '\t조건 충족 !!! 3분야 이상 수강 확인 요망 !!!'
        widget.appendPlainText(select1_text)

        select2_text = '\n\t\t\t교양선택2 : {}'.format(select2) + '\t\t\t\t다른 이수구분 학점 모두 만족 후 나머지 학점 채울 것 !!!'
        widget.appendPlainText(select2_text)

        basic_text = '\n\t\t\t기초교양 : {}'.format(basic)
        if basic < 9:
            basic_text += '\t{} 학점 부족 !!!'.format(9 - basic)
        else:
            basic_text += '\t\t조건 충족 !!!'
        widget.appendPlainText(basic_text)


        widget.appendPlainText('-------------------------------------------------------------------------------'
                               '----------------------------------------------------------------------------')

        query = 'SELECT * FROM non_class'
        my_cur.execute(query)
        my_result = my_cur.fetchall()

        vol = my_result[0][1]  # 세종사회봉사
        west = my_result[0][2]  # 서양
        east = my_result[0][3]  # 동양
        ew = my_result[0][4]  # 동서양
        science = my_result[0][5]  # 과학사
        toeic = my_result[0][6]

        vol_text = '\t\t\t세종사회봉사 : ' + vol
        widget.appendPlainText(vol_text)

        west_text = '\n\t\t\t서양의역사와사상 : {} / 4'.format(west)
        widget.appendPlainText(west_text)

        east_text = '\n\t\t\t동양의역사와사상 : {} / 2'.format(east)
        widget.appendPlainText(east_text)

        ew_text = '\n\t\t\t동서양의문학 : {} / 3'.format(ew)
        widget.appendPlainText(ew_text)

        science_text = '\n\t\t\t과학사 : {} / 1'.format(science)
        widget.appendPlainText(science_text)

        toeic_text = '\n\t\t\t토익 : {} / 700'.format(toeic)
        widget.appendPlainText(toeic_text)

        widget.appendPlainText('-------------------------------------------------------------------------------'
                               '----------------------------------------------------------------------------')

        widget.setGeometry(25, 40, 950, 435)
        widget.show()

    def print_non_info(self):
        widget = QPlainTextEdit(self)
        widget.setReadOnly(True)
        query = 'SELECT * FROM non_class'
        my_cur.execute(query)
        my_result = my_cur.fetchall()
        widget.appendPlainText('비교과\n')
        widget.appendPlainText('-------------------------------------------------------------------------------'
                               '----------------------------------------------------------------------------\n')
        text1 = '\t\t\t\t      세종사회봉사 : ' + str(my_result[0][1]) + '\n'
        text2 = '\t\t\t\t      서양의역사와사상 : ' + str(my_result[0][2]) + '권\n'
        text3 = '\t\t\t\t      동양의역사와사상 : ' + str(my_result[0][3]) + '권\n'
        text4 = '\t\t\t\t      동서양의 문학 : ' + str(my_result[0][4]) + '권\n'
        text5 = '\t\t\t\t      과학사상 : ' + str(my_result[0][5]) + '권\n'
        text6 = '\t\t\t\t      토익 : ' + str(my_result[0][6]) + '점\n'
        widget.appendPlainText(text1)
        widget.appendPlainText(text2)
        widget.appendPlainText(text3)
        widget.appendPlainText(text4)
        widget.appendPlainText(text5)
        widget.appendPlainText(text6)
        widget.appendPlainText('-------------------------------------------------------------------------------'
                               '----------------------------------------------------------------------------\n')
        widget.setGeometry(25, 40, 950, 435)
        widget.show()

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

    def insert_non_info(self):
        widget = QPlainTextEdit(self)
        widget.setReadOnly(True)
        widget.appendPlainText('-------------------------------------------------------------------------------'
                               '----------------------------------------------------------------------------\n')
        widget.appendPlainText('\t\t\t\t      세종사회봉사 : \n')
        widget.appendPlainText('\t\t\t\t      서양의역사와사상 : \n')
        widget.appendPlainText('\t\t\t\t      동양의역사와사상 : \n')
        widget.appendPlainText('\t\t\t\t      동서양의 문학 : \n')
        widget.appendPlainText('\t\t\t\t      과학사상 : \n')
        widget.appendPlainText('\t\t\t\t      토익 : \n')
        widget.appendPlainText('-------------------------------------------------------------------------------'
                               '----------------------------------------------------------------------------\n')
        widget.setGeometry(25, 40, 950, 435)
        widget.show()

        vol = QLineEdit(self)
        vol.move(480, 78)
        vol.setFixedSize(30, 20)
        vol.show()
        non_data.append(vol)

        west = QLineEdit(self)
        west.move(480, 108)
        west.setFixedSize(30, 20)
        west.show()
        non_data.append(west)

        east = QLineEdit(self)
        east.move(480, 138)
        east.setFixedSize(30, 20)
        east.show()
        non_data.append(east)

        ew = QLineEdit(self)
        ew.move(480, 168)
        ew.setFixedSize(30, 20)
        ew.show()
        non_data.append(ew)

        science = QLineEdit(self)
        science.move(480, 198)
        science.setFixedSize(30, 20)
        science.show()
        non_data.append(science)

        toeic = QLineEdit(self)
        toeic.move(480, 228)
        toeic.setFixedSize(30, 20)
        toeic.show()
        non_data.append(toeic)

        insert_btn = QPushButton(self)
        insert_btn.setText('입력')
        insert_btn.setFixedSize(60, 30)
        insert_btn.move(700, 300)
        insert_btn.show()
        insert_btn.clicked.connect(self.input_non_data)

    def input_non_data(self):
        vol = non_data[0].text()
        west = non_data[1].text()
        east = non_data[2].text()
        ew = non_data[3].text()
        science = non_data[4].text()
        toeic = non_data[5].text()

        query = 'UPDATE non_class SET 세종사회봉사 = \'' + vol + '\' WHERE id = 1'
        my_cur.execute(query)
        print(query)
        my_db.commit()

        query = 'UPDATE non_class SET 서양 = \'' + west + '\' WHERE id = 1'
        my_cur.execute(query)
        print(query)
        my_db.commit()

        query = 'UPDATE non_class SET 동양 = \'' + east + '\' WHERE id = 1'
        my_cur.execute(query)
        print(query)
        my_db.commit()

        query = 'UPDATE non_class SET 동서양 = \'' + ew + '\' WHERE id = 1'
        my_cur.execute(query)
        print(query)
        my_db.commit()

        query = 'UPDATE non_class SET 과학사 = \'' + science + '\' WHERE id = 1'
        my_cur.execute(query)
        print(query)
        my_db.commit()

        query = 'UPDATE non_class SET 토익 = \'' + toeic + '\' WHERE id = 1'
        my_cur.execute(query)
        print(query)
        my_db.commit()

    def insert_non(self):
        self.insert_non_info()

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

    def find_non(self):
        self.print_non_info()

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