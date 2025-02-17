# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'myForm.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(748, 429)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 741, 421))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.function = QLabel(self.tab)
        self.function.setObjectName(u"function")
        self.function.setGeometry(QRect(230, 10, 361, 41))
        font = QFont()
        font.setPointSize(20)
        self.function.setFont(font)
        self.a = QLabel(self.tab)
        self.a.setObjectName(u"a")
        self.a.setGeometry(QRect(40, 60, 151, 41))
        font1 = QFont()
        font1.setPointSize(14)
        self.a.setFont(font1)
        self.b = QLabel(self.tab)
        self.b.setObjectName(u"b")
        self.b.setGeometry(QRect(330, 60, 151, 41))
        self.b.setFont(font1)
        self.start = QLineEdit(self.tab)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(190, 70, 113, 22))
        self.end = QLineEdit(self.tab)
        self.end.setObjectName(u"end")
        self.end.setGeometry(QRect(480, 70, 113, 22))
        self.epsilonLabel = QLabel(self.tab)
        self.epsilonLabel.setObjectName(u"epsilonLabel")
        self.epsilonLabel.setGeometry(QRect(230, 110, 151, 41))
        self.epsilonLabel.setFont(font1)
        self.epsilon = QLineEdit(self.tab)
        self.epsilon.setObjectName(u"epsilon")
        self.epsilon.setGeometry(QRect(330, 120, 113, 22))
        self.extremus = QTextEdit(self.tab)
        self.extremus.setObjectName(u"extremus")
        self.extremus.setGeometry(QRect(390, 170, 341, 221))
        self.foundResult = QPushButton(self.tab)
        self.foundResult.setObjectName(u"foundResult")
        self.foundResult.setGeometry(QRect(110, 200, 251, 81))
        self.foundResult.setFont(font1)
        self.graphButton = QPushButton(self.tab)
        self.graphButton.setObjectName(u"graphButton")
        self.graphButton.setGeometry(QRect(110, 290, 251, 91))
        self.graphButton.setFont(font1)
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(600, 10, 131, 21))
        font2 = QFont()
        font2.setPointSize(11)
        self.label.setFont(font2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.end_3 = QLineEdit(self.tab_2)
        self.end_3.setObjectName(u"end_3")
        self.end_3.setGeometry(QRect(480, 70, 113, 22))
        self.b_3 = QLabel(self.tab_2)
        self.b_3.setObjectName(u"b_3")
        self.b_3.setGeometry(QRect(330, 60, 151, 41))
        self.b_3.setFont(font1)
        self.function_3 = QLabel(self.tab_2)
        self.function_3.setObjectName(u"function_3")
        self.function_3.setGeometry(QRect(230, 10, 361, 41))
        self.function_3.setFont(font)
        self.foundResult_3 = QPushButton(self.tab_2)
        self.foundResult_3.setObjectName(u"foundResult_3")
        self.foundResult_3.setGeometry(QRect(110, 200, 251, 81))
        self.foundResult_3.setFont(font1)
        self.start_3 = QLineEdit(self.tab_2)
        self.start_3.setObjectName(u"start_3")
        self.start_3.setGeometry(QRect(190, 70, 113, 22))
        self.extremus_3 = QTextEdit(self.tab_2)
        self.extremus_3.setObjectName(u"extremus_3")
        self.extremus_3.setGeometry(QRect(390, 170, 341, 221))
        self.epsilonLabel_3 = QLabel(self.tab_2)
        self.epsilonLabel_3.setObjectName(u"epsilonLabel_3")
        self.epsilonLabel_3.setGeometry(QRect(230, 110, 151, 41))
        self.epsilonLabel_3.setFont(font1)
        self.epsilon_3 = QLineEdit(self.tab_2)
        self.epsilon_3.setObjectName(u"epsilon_3")
        self.epsilon_3.setGeometry(QRect(330, 120, 113, 22))
        self.graphButton_3 = QPushButton(self.tab_2)
        self.graphButton_3.setObjectName(u"graphButton_3")
        self.graphButton_3.setGeometry(QRect(110, 290, 251, 91))
        self.graphButton_3.setFont(font1)
        self.a_3 = QLabel(self.tab_2)
        self.a_3.setObjectName(u"a_3")
        self.a_3.setGeometry(QRect(40, 60, 151, 41))
        self.a_3.setFont(font1)
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(640, 10, 91, 21))
        self.label_2.setFont(font2)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Lab03", None))
        self.function.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0443\u043d\u043a\u0446\u0438\u044f f(x) = x^5 * sin(5x)", None))
        self.a.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e \u043e\u0442\u0440\u0435\u0437\u043a\u0430:", None))
        self.b.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0435\u0446 \u043e\u0442\u0440\u0435\u0437\u043a\u0430:", None))
        self.epsilonLabel.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043d\u043e\u0441\u0442\u044c:", None))
        self.foundResult.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 \u044d\u043a\u0441\u0442\u0440\u0435\u043c\u0443\u043c", None))
        self.graphButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a \u0444\u0443\u043d\u043a\u0446\u0438\u0438", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u0414\u0438\u0445\u043e\u0442\u043e\u043c\u0438\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u0414\u0438\u0445\u043e\u0442\u043e\u043c\u0438\u0438", None))
        self.b_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0435\u0446 \u043e\u0442\u0440\u0435\u0437\u043a\u0430:", None))
        self.function_3.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0443\u043d\u043a\u0446\u0438\u044f f(x) = x^5 * sin(5x)", None))
        self.foundResult_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 \u044d\u043a\u0441\u0442\u0440\u0435\u043c\u0443\u043c", None))
        self.epsilonLabel_3.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043d\u043e\u0441\u0442\u044c:", None))
        self.graphButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a \u0444\u0443\u043d\u043a\u0446\u0438\u0438", None))
        self.a_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e \u043e\u0442\u0440\u0435\u0437\u043a\u0430:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u0425\u043e\u0440\u0434", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u0425\u043e\u0440\u0434", None))
    # retranslateUi

