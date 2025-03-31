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
    QPlainTextEdit, QPushButton, QSizePolicy, QTabWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(575, 565)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(-10, 0, 591, 571))
        self.linear = QWidget()
        self.linear.setObjectName(u"linear")
        self.linear_method = QLabel(self.linear)
        self.linear_method.setObjectName(u"linear_method")
        self.linear_method.setGeometry(QRect(110, 20, 281, 41))
        font = QFont()
        font.setPointSize(14)
        self.linear_method.setFont(font)
        self.inpit_x = QLabel(self.linear)
        self.inpit_x.setObjectName(u"inpit_x")
        self.inpit_x.setGeometry(QRect(80, 80, 131, 41))
        font1 = QFont()
        font1.setPointSize(18)
        self.inpit_x.setFont(font1)
        self.input_count = QLabel(self.linear)
        self.input_count.setObjectName(u"input_count")
        self.input_count.setGeometry(QRect(300, 80, 251, 41))
        self.input_count.setFont(font1)
        self.generated_linear = QPlainTextEdit(self.linear)
        self.generated_linear.setObjectName(u"generated_linear")
        self.generated_linear.setGeometry(QRect(50, 220, 331, 181))
        self.generated = QLabel(self.linear)
        self.generated.setObjectName(u"generated")
        self.generated.setGeometry(QRect(80, 180, 221, 41))
        self.generated.setFont(font)
        self.generate_linear = QPushButton(self.linear)
        self.generate_linear.setObjectName(u"generate_linear")
        self.generate_linear.setGeometry(QRect(50, 430, 171, 61))
        self.generate_linear.setFont(font)
        self.diagram_linear = QPushButton(self.linear)
        self.diagram_linear.setObjectName(u"diagram_linear")
        self.diagram_linear.setGeometry(QRect(290, 430, 171, 61))
        self.diagram_linear.setFont(font)
        self.x = QLineEdit(self.linear)
        self.x.setObjectName(u"x")
        self.x.setGeometry(QRect(60, 140, 171, 41))
        self.count_linear = QLineEdit(self.linear)
        self.count_linear.setObjectName(u"count_linear")
        self.count_linear.setGeometry(QRect(340, 140, 171, 41))
        self.tabWidget.addTab(self.linear, "")
        self.beta_random = QWidget()
        self.beta_random.setObjectName(u"beta_random")
        self.generated_beta_label = QLabel(self.beta_random)
        self.generated_beta_label.setObjectName(u"generated_beta_label")
        self.generated_beta_label.setGeometry(QRect(180, 150, 221, 41))
        self.generated_beta_label.setFont(font)
        self.generated_beta = QPlainTextEdit(self.beta_random)
        self.generated_beta.setObjectName(u"generated_beta")
        self.generated_beta.setGeometry(QRect(130, 200, 331, 181))
        self.generate_beta = QPushButton(self.beta_random)
        self.generate_beta.setObjectName(u"generate_beta")
        self.generate_beta.setGeometry(QRect(90, 410, 171, 61))
        self.generate_beta.setFont(font)
        self.diagram_beta = QPushButton(self.beta_random)
        self.diagram_beta.setObjectName(u"diagram_beta")
        self.diagram_beta.setGeometry(QRect(330, 410, 171, 61))
        self.diagram_beta.setFont(font)
        self.input_count_beta = QLabel(self.beta_random)
        self.input_count_beta.setObjectName(u"input_count_beta")
        self.input_count_beta.setGeometry(QRect(170, 50, 251, 41))
        self.input_count_beta.setFont(font1)
        self.count_beta = QLineEdit(self.beta_random)
        self.count_beta.setObjectName(u"count_beta")
        self.count_beta.setGeometry(QRect(190, 110, 211, 31))
        self.tabWidget.addTab(self.beta_random, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.linear_method.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u043d\u0435\u0439\u043d\u044b\u0439 \u043a\u043e\u043d\u0433\u0440\u0443\u044d\u043d\u0442\u043d\u044b\u0439 \u043c\u0435\u0442\u043e\u0434", None))
        self.inpit_x.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 Xi:", None))
        self.input_count.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043b-\u0432\u043e \u0447\u0438\u0441\u0435\u043b", None))
        self.generated.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u0447\u0438\u0441\u043b\u0430", None))
        self.generate_linear.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.diagram_linear.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.linear), QCoreApplication.translate("MainWindow", u"\u041b\u0438\u043d\u0435\u0439\u043d\u044b\u0439 \u043a\u043e\u043d\u0433\u0440\u0443\u044d\u043d\u0442\u043d\u044b\u0439 \u043c\u0435\u0442\u043e\u0434", None))
        self.generated_beta_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u0447\u0438\u0441\u043b\u0430", None))
        self.generate_beta.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.diagram_beta.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u0430", None))
        self.input_count_beta.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043b-\u0432\u043e \u0447\u0438\u0441\u0435\u043b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.beta_random), QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0442\u0430-\u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
    # retranslateUi

