# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Calulator2.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform, QShortcut)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import file_res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 450)
        MainWindow.setMinimumSize(QSize(300, 450))
        MainWindow.setMouseTracking(False)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        icon = QIcon()
        icon.addFile(u":/Icons/Calcul-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"  color: white;\n"
"  background-color: #1d1d1d;\n"
"  font-family: Roboto Mono;\n"
"  font-size: 18pt;\n"
"  font-weight: 400;\n"
"}\n"
"\n"
"QLabel{\n"
"color: #888;\n"
"font-size: 12pt;\n"
"font-weight: 600;\n"
"  border: none;\n"
"}\n"
"QLineEdit{\n"
"  background-color: #1d1d1d;\n"
"  border-radius: 5px;\n"
"  font-size: 30pt;\n"
"  border: none;\n"
"}\n"
"\n"
"QPushButton{\n"
"  background-color: #333235;\n"
"  border: none;\n"
"  background-color: rgba(255, 255, 255, 15);\n"
"  border-radius: 5px;\n"
"  font-size: 14pt;\n"
"  font-weight: 500;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #242425;\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #9184e0;\n"
"}\n"
"\n"
"QToolButton{\n"
"  background-color: #333235;\n"
"  border: none;\n"
"  background-color: rgba(255, 255, 255, 15);\n"
"  border-radius: 5px;\n"
"  font-size: 14pt;\n"
"  font-weight: 500;\n"
"  style=height:24px;width:24px;\n"
"}\n"
"QToolButton:hover{\n"
"  background-color: #242425;\n"
"}\n"
"QToolButton:press"
                        "ed{\n"
"  background-color: #9184e0;\n"
"}\n"
"\n"
"#Bttn_rowno{   \n"
"	background-color: #9184e0;\n"
"	color: black;\n"
"	border: none;\n"
"	font-size: 18pt;\n"
"   font-weight: 500;\n"
"}\n"
"\n"
"#Bttn_rowno:hover{\n"
"    background-color: #7567c9;\n"
"}\n"
"#Bttn_rowno:pressed {\n"
"    background-color:  #333235;\n"
"}\n"
"\n"
"#Bttn_color{   \n"
"	background-color: #9184e0;\n"
"	color: black;\n"
"	border: none;\n"
"	font-size: 18pt;\n"
"   font-weight: 500;\n"
"}\n"
"\n"
"#Bttn_color:hover{\n"
"    background-color: #5a49af;\n"
"}\n"
"#Bttn_color:pressed {\n"
"    background-color:  #333235;\n"
"}")
        MainWindow.setIconSize(QSize(24, 24))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Bttn_right = QPushButton(self.centralwidget)
        self.Bttn_right.setObjectName(u"Bttn_right")
        self.Bttn_right.setMinimumSize(QSize(65, 30))
        self.Bttn_right.setMaximumSize(QSize(65, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Bttn_right.setIcon(icon1)
        self.Bttn_right.setIconSize(QSize(26, 24))

        self.gridLayout_3.addWidget(self.Bttn_right, 0, 4, 1, 1)

        self.Bttn_left = QPushButton(self.centralwidget)
        self.Bttn_left.setObjectName(u"Bttn_left")
        self.Bttn_left.setMinimumSize(QSize(65, 30))
        self.Bttn_left.setMaximumSize(QSize(65, 16777215))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/light.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Bttn_left.setIcon(icon2)
        self.Bttn_left.setIconSize(QSize(26, 26))

        self.gridLayout_3.addWidget(self.Bttn_left, 0, 3, 1, 1)

        self.Bttn_basket = QPushButton(self.centralwidget)
        self.Bttn_basket.setObjectName(u"Bttn_basket")
        self.Bttn_basket.setMinimumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u":/Icons/basket.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Bttn_basket.setIcon(icon3)
        self.Bttn_basket.setIconSize(QSize(26, 26))

        self.gridLayout_3.addWidget(self.Bttn_basket, 0, 2, 1, 1, Qt.AlignRight)

        self.Bttn_color = QPushButton(self.centralwidget)
        self.Bttn_color.setObjectName(u"Bttn_color")
        self.Bttn_color.setMinimumSize(QSize(30, 30))
        icon4 = QIcon()
        icon4.addFile(u":/Icons/cist-Fiol.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Bttn_color.setIcon(icon4)
        self.Bttn_color.setIconSize(QSize(26, 26))

        self.gridLayout_3.addWidget(self.Bttn_color, 0, 0, 1, 1, Qt.AlignLeft)

        self.gridLayout_3.setContentsMargins(10, 2, 10, 0)
        self.verticalLayout_2.addLayout(self.gridLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Story = QLabel(self.centralwidget)
        self.Story.setObjectName(u"Story")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Story.sizePolicy().hasHeightForWidth())
        self.Story.setSizePolicy(sizePolicy)
        self.Story.setMinimumSize(QSize(260, 30))
        self.Story.setMaximumSize(QSize(16777215, 30))
        self.Story.setCursor(QCursor(Qt.ArrowCursor))
        self.Story.setStyleSheet(u"")
        self.Story.setContentsMargins(10, 5, 10, 0)
        self.Story.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.Story)

        self.Operucia = QLineEdit(self.centralwidget)
        self.Operucia.setObjectName(u"Operucia")
        sizePolicy.setHeightForWidth(self.Operucia.sizePolicy().hasHeightForWidth())
        self.Operucia.setSizePolicy(sizePolicy)
        self.Operucia.setMinimumSize(QSize(260, 55))
        self.Operucia.setMaximumSize(QSize(16777215, 55))
        self.Operucia.setCursor(QCursor(Qt.IBeamCursor))
        self.Operucia.setStyleSheet(u"")
        self.Operucia.setContentsMargins(10, 0, 5, 0)
        self.Operucia.setMaxLength(16)
        self.Operucia.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Operucia.setReadOnly(True)

        self.verticalLayout.addWidget(self.Operucia)

        self.Buttons = QFrame(self.centralwidget)
        self.Buttons.setObjectName(u"Buttons")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Buttons.sizePolicy().hasHeightForWidth())
        self.Buttons.setSizePolicy(sizePolicy1)
        self.Buttons.setMinimumSize(QSize(270, 0))
        self.Buttons.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.Buttons)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Bttn_rowno = QPushButton(self.Buttons)
        self.Bttn_rowno.setObjectName(u"Bttn_rowno")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Bttn_rowno.sizePolicy().hasHeightForWidth())
        self.Bttn_rowno.setSizePolicy(sizePolicy2)
        self.Bttn_rowno.setCursor(QCursor(Qt.PointingHandCursor))
        self.Bttn_rowno.setStyleSheet(u"")

        self.gridLayout.addWidget(self.Bttn_rowno, 6, 6, 1, 1)

        self.Bttn_8 = QPushButton(self.Buttons)
        self.Bttn_8.setObjectName(u"Bttn_8")
        sizePolicy2.setHeightForWidth(self.Bttn_8.sizePolicy().hasHeightForWidth())
        self.Bttn_8.setSizePolicy(sizePolicy2)
        self.Bttn_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Bttn_8, 3, 2, 1, 1)

        self.Bttn_1 = QPushButton(self.Buttons)
        self.Bttn_1.setObjectName(u"Bttn_1")
        sizePolicy2.setHeightForWidth(self.Bttn_1.sizePolicy().hasHeightForWidth())
        self.Bttn_1.setSizePolicy(sizePolicy2)
        self.Bttn_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Bttn_1, 5, 1, 1, 1)

        self.Bttn_Clear = QPushButton(self.Buttons)
        self.Bttn_Clear.setObjectName(u"Bttn_Clear")
        sizePolicy2.setHeightForWidth(self.Bttn_Clear.sizePolicy().hasHeightForWidth())
        self.Bttn_Clear.setSizePolicy(sizePolicy2)
        self.Bttn_Clear.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Bttn_Clear, 0, 2, 1, 1)

        self.Bttn_0 = QPushButton(self.Buttons)
        self.Bttn_0.setObjectName(u"Bttn_0")
        sizePolicy2.setHeightForWidth(self.Bttn_0.sizePolicy().hasHeightForWidth())
        self.Bttn_0.setSizePolicy(sizePolicy2)
        self.Bttn_0.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Bttn_0, 6, 2, 1, 1)

        self.Bttn_minus = QPushButton(self.Buttons)
        self.Bttn_minus.setObjectName(u"Bttn_minus")
        sizePolicy2.setHeightForWidth(self.Bttn_minus.sizePolicy().hasHeightForWidth())
        self.Bttn_minus.setSizePolicy(sizePolicy2)
        self.Bttn_minus.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Bttn_minus, 4, 6, 1, 1)

        self.Bttn_7 = QPushButton(self.Buttons)
        self.Bttn_7.setObjectName(u"Bttn_7")
        sizePolicy2.setHeightForWidth(self.Bttn_7.sizePolicy().hasHeightForWidth())
        self.Bttn_7.setSizePolicy(sizePolicy2)
        self.Bttn_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Bttn_7, 3, 1, 1, 1)

        self.Bttn_drob = QPushButton(self.Buttons)
        self.Bttn_drob.setObjectName(u"Bttn_drob")
        sizePolicy2.setHeightForWidth(self.Bttn_drob.sizePolicy().hasHeightForWidth())
        self.Bttn_drob.setSizePolicy(sizePolicy2)
        self.Bttn_drob.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Bttn_drob, 6, 4, 1, 1)

        self.Bttn_Percent = QPushButton(self.Buttons)
        self.Bttn_Percent.setObjectName(u"Bttn_Percent")
        sizePolicy2.setHeightForWidth(self.Bttn_Percent.sizePolicy().hasHeightForWidth())
        self.Bttn_Percent.setSizePolicy(sizePolicy2)
        self.Bttn_Percent.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Bttn_Percent, 0, 1, 1, 1)

        self.Bttn_6 = QPushButton(self.Buttons)
        self.Bttn_6.setObjectName(u"Bttn_6")
        sizePolicy2.setHeightForWidth(self.Bttn_6.sizePolicy().hasHeightForWidth())
        self.Bttn_6.setSizePolicy(sizePolicy2)
        self.Bttn_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Bttn_6, 4, 4, 1, 1)

        self.Bttn_plus = QPushButton(self.Buttons)
        self.Bttn_plus.setObjectName(u"Bttn_plus")
        sizePolicy2.setHeightForWidth(self.Bttn_plus.sizePolicy().hasHeightForWidth())
        self.Bttn_plus.setSizePolicy(sizePolicy2)
        self.Bttn_plus.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Bttn_plus, 5, 6, 1, 1)

        self.Bttn_Degree = QPushButton(self.Buttons)
        self.Bttn_Degree.setObjectName(u"Bttn_Degree")
        sizePolicy2.setHeightForWidth(self.Bttn_Degree.sizePolicy().hasHeightForWidth())
        self.Bttn_Degree.setSizePolicy(sizePolicy2)
        self.Bttn_Degree.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Bttn_Degree, 1, 1, 1, 1)

        self.Bttn_Umnoj = QPushButton(self.Buttons)
        self.Bttn_Umnoj.setObjectName(u"Bttn_Umnoj")
        sizePolicy2.setHeightForWidth(self.Bttn_Umnoj.sizePolicy().hasHeightForWidth())
        self.Bttn_Umnoj.setSizePolicy(sizePolicy2)
        self.Bttn_Umnoj.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Bttn_Umnoj, 3, 6, 1, 1)

        self.Bttn_3 = QPushButton(self.Buttons)
        self.Bttn_3.setObjectName(u"Bttn_3")
        sizePolicy2.setHeightForWidth(self.Bttn_3.sizePolicy().hasHeightForWidth())
        self.Bttn_3.setSizePolicy(sizePolicy2)
        self.Bttn_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Bttn_3, 5, 4, 1, 1)

        self.Bttn_5 = QPushButton(self.Buttons)
        self.Bttn_5.setObjectName(u"Bttn_5")
        sizePolicy2.setHeightForWidth(self.Bttn_5.sizePolicy().hasHeightForWidth())
        self.Bttn_5.setSizePolicy(sizePolicy2)
        self.Bttn_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Bttn_5, 4, 2, 1, 1)

        self.Bttn_Delem = QPushButton(self.Buttons)
        self.Bttn_Delem.setObjectName(u"Bttn_Delem")
        sizePolicy2.setHeightForWidth(self.Bttn_Delem.sizePolicy().hasHeightForWidth())
        self.Bttn_Delem.setSizePolicy(sizePolicy2)
        self.Bttn_Delem.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Bttn_Delem, 1, 6, 1, 1)

        self.Bttn_Fraction = QPushButton(self.Buttons)
        self.Bttn_Fraction.setObjectName(u"Bttn_Fraction")
        sizePolicy2.setHeightForWidth(self.Bttn_Fraction.sizePolicy().hasHeightForWidth())
        self.Bttn_Fraction.setSizePolicy(sizePolicy2)
        self.Bttn_Fraction.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/Icons/1onX.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Bttn_Fraction.setIcon(icon5)
        self.Bttn_Fraction.setIconSize(QSize(26, 26))

        self.gridLayout.addWidget(self.Bttn_Fraction, 1, 2, 1, 1)

        self.Bttn_2 = QPushButton(self.Buttons)
        self.Bttn_2.setObjectName(u"Bttn_2")
        sizePolicy2.setHeightForWidth(self.Bttn_2.sizePolicy().hasHeightForWidth())
        self.Bttn_2.setSizePolicy(sizePolicy2)
        self.Bttn_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Bttn_2, 5, 2, 1, 1)

        self.Bttn_Delete = QPushButton(self.Buttons)
        self.Bttn_Delete.setObjectName(u"Bttn_Delete")
        sizePolicy2.setHeightForWidth(self.Bttn_Delete.sizePolicy().hasHeightForWidth())
        self.Bttn_Delete.setSizePolicy(sizePolicy2)
        self.Bttn_Delete.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/Icons/Bckspc.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Bttn_Delete.setIcon(icon6)
        self.Bttn_Delete.setIconSize(QSize(26, 26))

        self.gridLayout.addWidget(self.Bttn_Delete, 0, 6, 1, 1)

        self.Bttn_CE = QPushButton(self.Buttons)
        self.Bttn_CE.setObjectName(u"Bttn_CE")
        sizePolicy2.setHeightForWidth(self.Bttn_CE.sizePolicy().hasHeightForWidth())
        self.Bttn_CE.setSizePolicy(sizePolicy2)
        self.Bttn_CE.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Bttn_CE, 0, 4, 1, 1)

        self.Bttn_Otricianie = QPushButton(self.Buttons)
        self.Bttn_Otricianie.setObjectName(u"Bttn_Otricianie")
        sizePolicy2.setHeightForWidth(self.Bttn_Otricianie.sizePolicy().hasHeightForWidth())
        self.Bttn_Otricianie.setSizePolicy(sizePolicy2)
        self.Bttn_Otricianie.setCursor(QCursor(Qt.PointingHandCursor))
        self.Bttn_Otricianie.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.Bttn_Otricianie, 6, 1, 1, 1)

        self.Bttn_9 = QPushButton(self.Buttons)
        self.Bttn_9.setObjectName(u"Bttn_9")
        sizePolicy2.setHeightForWidth(self.Bttn_9.sizePolicy().hasHeightForWidth())
        self.Bttn_9.setSizePolicy(sizePolicy2)
        self.Bttn_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Bttn_9, 3, 4, 1, 1)

        self.Bttn_4 = QPushButton(self.Buttons)
        self.Bttn_4.setObjectName(u"Bttn_4")
        sizePolicy2.setHeightForWidth(self.Bttn_4.sizePolicy().hasHeightForWidth())
        self.Bttn_4.setSizePolicy(sizePolicy2)
        self.Bttn_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Bttn_4, 4, 1, 1, 1)

        self.Bttn_Root = QPushButton(self.Buttons)
        self.Bttn_Root.setObjectName(u"Bttn_Root")
        sizePolicy2.setHeightForWidth(self.Bttn_Root.sizePolicy().hasHeightForWidth())
        self.Bttn_Root.setSizePolicy(sizePolicy2)
        self.Bttn_Root.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Bttn_Root, 1, 4, 1, 1)


        self.verticalLayout.addWidget(self.Buttons)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.Bttn_right.setText("")
        self.Bttn_left.setText("")
        self.Bttn_basket.setText("")
        self.Bttn_color.setText("")
        self.Story.setText("")
        self.Operucia.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Bttn_rowno.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        for sc in ('=', 'Enter', 'Return'):
            QShortcut(sc, self.Bttn_rowno).activated.connect(self.Bttn_rowno.animateClick)
#endif // QT_CONFIG(shortcut)
        self.Bttn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.Bttn_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.Bttn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.Bttn_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.Bttn_Clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.Bttn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.Bttn_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.Bttn_minus.setText(QCoreApplication.translate("MainWindow", u"\u2212", None))
#if QT_CONFIG(shortcut)
        self.Bttn_minus.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.Bttn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.Bttn_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.Bttn_drob.setText(QCoreApplication.translate("MainWindow", u",", None))
#if QT_CONFIG(shortcut)
        for sc in (',', '.'):
            QShortcut(sc, self.Bttn_drob).activated.connect(self.Bttn_drob.animateClick)
        #endif // QT_CONFIG(shortcut)
        self.Bttn_Percent.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.Bttn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.Bttn_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.Bttn_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.Bttn_plus.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.Bttn_Degree.setText(QCoreApplication.translate("MainWindow", u"x\u00b2", None))
        self.Bttn_Umnoj.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
#if QT_CONFIG(shortcut)
        self.Bttn_Umnoj.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.Bttn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.Bttn_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.Bttn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.Bttn_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.Bttn_Delem.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.Bttn_Delem.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.Bttn_Fraction.setText("")
        self.Bttn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.Bttn_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.Bttn_Delete.setText("")
#if QT_CONFIG(shortcut)
        self.Bttn_Delete.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.Bttn_CE.setText(QCoreApplication.translate("MainWindow", u"CE", None))
#if QT_CONFIG(shortcut)
        self.Bttn_CE.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.Bttn_Otricianie.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.Bttn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.Bttn_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.Bttn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.Bttn_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.Bttn_Root.setText(QCoreApplication.translate("MainWindow", u"\u221ax", None))
    # retranslateUi

