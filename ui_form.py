# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpinBox,
    QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1300, 800)
        icon = QIcon()
        icon.addFile(u"../../interfaz dron/interfaz_1/imagenes/dron.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.fondo = QFrame(self.centralwidget)
        self.fondo.setObjectName(u"fondo")
        self.fondo.setGeometry(QRect(0, 0, 1300, 800))
        self.fondo.setStyleSheet(u"background-color: #141414;\n"
"border: None;")
        self.fondo.setFrameShape(QFrame.Shape.StyledPanel)
        self.fondo.setFrameShadow(QFrame.Shadow.Raised)
        self.menu = QFrame(self.fondo)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(0, 0, 100, 800))
        self.menu.setStyleSheet(u"background-color: #1f2126 ;\n"
"border: None;")
        self.menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.menu.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton = QPushButton(self.menu)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(25, 120, 50, 50))
        self.pushButton.setStyleSheet(u"background-color: #333333  ;\n"
"border: 1px solid #333333;\n"
"border-radius:10px;  /* \ud83d\udd38 Esto redondea los bordes */")
        icon1 = QIcon()
        icon1.addFile(u"imagenes/home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(25, 25))
        self.pushButton_2 = QPushButton(self.menu)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(25, 210, 50, 50))
        self.pushButton_2.setStyleSheet(u"background-color: #333333  ;\n"
"border: 1px solid #333333;\n"
"border-radius:10px;  /* \ud83d\udd38 Esto redondea los bordes */")
        icon2 = QIcon()
        icon2.addFile(u"imagenes/map.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(25, 25))
        self.pushButton_4 = QPushButton(self.menu)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(25, 300, 50, 50))
        self.pushButton_4.setStyleSheet(u"background-color: #333333  ;\n"
"border: 1px solid #333333;\n"
"border-radius:10px;  /* \ud83d\udd38 Esto redondea los bordes */")
        icon3 = QIcon()
        icon3.addFile(u"imagenes/picture.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(25, 25))
        self.pushButton_3 = QPushButton(self.menu)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(25, 450, 50, 50))
        self.pushButton_3.setStyleSheet(u"background-color: #333333  ;\n"
"border: 1px solid #333333;\n"
"border-radius:10px;  /* \ud83d\udd38 Esto redondea los bordes */")
        icon4 = QIcon()
        icon4.addFile(u"imagenes/alert.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setIconSize(QSize(25, 25))
        self.pushButton_6 = QPushButton(self.menu)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(25, 540, 50, 50))
        self.pushButton_6.setStyleSheet(u"background-color: #333333  ;\n"
"border: 1px solid #333333;\n"
"border-radius:10px;  /* \ud83d\udd38 Esto redondea los bordes */")
        icon5 = QIcon()
        icon5.addFile(u"imagenes/config.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QSize(25, 25))
        self.pushButton_5 = QPushButton(self.menu)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(25, 720, 50, 50))
        self.pushButton_5.setStyleSheet(u"background-color: #333333  ;\n"
"border: 1px solid #333333;\n"
"border-radius:10px;  /* \ud83d\udd38 Esto redondea los bordes */")
        icon6 = QIcon()
        icon6.addFile(u"imagenes/start.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon6)
        self.pushButton_5.setIconSize(QSize(25, 25))
        self.video = QFrame(self.fondo)
        self.video.setObjectName(u"video")
        self.video.setGeometry(QRect(120, 20, 768, 432))
        self.video.setStyleSheet(u"background-color: #1f2126 ;\n"
"border: 1px solid #1f2126;\n"
"border-radius: 12px;  /* \ud83d\udd38 Esto redondea los bordes */")
        self.video.setFrameShape(QFrame.Shape.StyledPanel)
        self.video.setFrameShadow(QFrame.Shadow.Raised)
        self.labelvideo = QLabel(self.video)
        self.labelvideo.setObjectName(u"labelvideo")
        self.labelvideo.setGeometry(QRect(0, 0, 768, 432))
        self.labelvideo.setStyleSheet(u"background-color: #1f2126 ;\n"
"border: 1px solid #1f2126;\n"
"border-radius: 12px;  /* \ud83d\udd38 Esto redondea los bordes */")
        self.pushButton_31 = QPushButton(self.video)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setGeometry(QRect(650, 370, 100, 40))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setStyleSheet(u"border: 0px;\n"
"border-radius:1px;\n"
"color: #000000;;\n"
"background-color: #FFFFFF;\n"
"border: 1px solid #FFFFFF;\n"
"border-radius: 5px;  /* \ud83d\udd38 Esto redondea los bordes */")
        icon7 = QIcon()
        icon7.addFile(u"imagenes/rec.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_31.setIcon(icon7)
        self.pushButton_31.setIconSize(QSize(20, 20))
        self.pushButton_32 = QPushButton(self.video)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setGeometry(QRect(590, 370, 40, 40))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.pushButton_32.setFont(font1)
        self.pushButton_32.setStyleSheet(u"border: 0px;\n"
"border-radius:1px;\n"
"color: #000000;;\n"
"background-color: #FFFFFF;\n"
"border: 1px solid #FFFFFF;\n"
"border-radius: 5px;  /* \ud83d\udd38 Esto redondea los bordes */")
        icon8 = QIcon()
        icon8.addFile(u"imagenes/pause.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_32.setIcon(icon8)
        self.pushButton_32.setIconSize(QSize(16, 16))
        self.informacion = QFrame(self.fondo)
        self.informacion.setObjectName(u"informacion")
        self.informacion.setGeometry(QRect(120, 472, 768, 308))
        self.informacion.setStyleSheet(u"background-color: #1f2126 ;\n"
"border: 1px solid #1f2126;\n"
"border-radius: 12px;  /* \ud83d\udd38 Esto redondea los bordes */")
        self.informacion.setFrameShape(QFrame.Shape.StyledPanel)
        self.informacion.setFrameShadow(QFrame.Shadow.Raised)
        self.textBrowser = QTextBrowser(self.informacion)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(414, 20, 81, 31))
        self.textBrowser.setStyleSheet(u"border:None;\n"
"color: #A0A0A0;")
        self.textBrowser_2 = QTextBrowser(self.informacion)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(414, 160, 101, 31))
        self.textBrowser_2.setStyleSheet(u"border:None;\n"
"color: #A0A0A0;")
        self.textBrowser_3 = QTextBrowser(self.informacion)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(414, 90, 81, 31))
        self.textBrowser_3.setStyleSheet(u"border:None;\n"
"color: #A0A0A0;")
        self.textBrowser_4 = QTextBrowser(self.informacion)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(414, 220, 81, 31))
        self.textBrowser_4.setStyleSheet(u"border:None;\n"
"color: #A0A0A0;")
        self.textBrowser_5 = QTextBrowser(self.informacion)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setGeometry(QRect(414, 40, 81, 31))
        self.textBrowser_5.setStyleSheet(u"border:None;\n"
"color: #E0E0E0;")
        self.textBrowser_6 = QTextBrowser(self.informacion)
        self.textBrowser_6.setObjectName(u"textBrowser_6")
        self.textBrowser_6.setGeometry(QRect(414, 110, 81, 31))
        self.textBrowser_6.setStyleSheet(u"border:None;\n"
"color: #E0E0E0;\n"
"background-color: transparent;")
        self.textBrowser_7 = QTextBrowser(self.informacion)
        self.textBrowser_7.setObjectName(u"textBrowser_7")
        self.textBrowser_7.setGeometry(QRect(414, 180, 81, 31))
        self.textBrowser_7.setStyleSheet(u"border:None;\n"
"color: #E0E0E0;")
        self.textBrowser_9 = QTextBrowser(self.informacion)
        self.textBrowser_9.setObjectName(u"textBrowser_9")
        self.textBrowser_9.setGeometry(QRect(280, 180, 81, 31))
        self.textBrowser_9.setStyleSheet(u"border:None;\n"
"color: #E0E0E0;\n"
"background-color: transparent;")
        self.textBrowser_10 = QTextBrowser(self.informacion)
        self.textBrowser_10.setObjectName(u"textBrowser_10")
        self.textBrowser_10.setGeometry(QRect(280, 220, 81, 31))
        self.textBrowser_10.setStyleSheet(u"border:None;\n"
"color: #A0A0A0;\n"
"background-color: transparent;")
        self.textBrowser_11 = QTextBrowser(self.informacion)
        self.textBrowser_11.setObjectName(u"textBrowser_11")
        self.textBrowser_11.setGeometry(QRect(280, 40, 81, 31))
        self.textBrowser_11.setStyleSheet(u"border:None;\n"
"color: #E0E0E0;\n"
"background-color: transparent;")
        self.textBrowser_12 = QTextBrowser(self.informacion)
        self.textBrowser_12.setObjectName(u"textBrowser_12")
        self.textBrowser_12.setGeometry(QRect(280, 20, 81, 31))
        self.textBrowser_12.setStyleSheet(u"border:None;\n"
"color: #A0A0A0;\n"
"background-color: transparent;")
        self.textBrowser_13 = QTextBrowser(self.informacion)
        self.textBrowser_13.setObjectName(u"textBrowser_13")
        self.textBrowser_13.setGeometry(QRect(280, 160, 101, 31))
        self.textBrowser_13.setStyleSheet(u"border:None;\n"
"color: #A0A0A0;\n"
"background-color: transparent;")
        self.textBrowser_14 = QTextBrowser(self.informacion)
        self.textBrowser_14.setObjectName(u"textBrowser_14")
        self.textBrowser_14.setGeometry(QRect(280, 110, 81, 31))
        self.textBrowser_14.setStyleSheet(u"border:None;\n"
"color: #E0E0E0;\n"
"background-color: transparent;")
        self.textBrowser_15 = QTextBrowser(self.informacion)
        self.textBrowser_15.setObjectName(u"textBrowser_15")
        self.textBrowser_15.setGeometry(QRect(280, 90, 81, 31))
        self.textBrowser_15.setStyleSheet(u"border:None;\n"
"color: #A0A0A0;\n"
"background-color: transparent;")
        self.textBrowser_8 = QTextBrowser(self.informacion)
        self.textBrowser_8.setObjectName(u"textBrowser_8")
        self.textBrowser_8.setGeometry(QRect(548, 20, 81, 31))
        self.textBrowser_8.setStyleSheet(u"border:None;\n"
"color: #A0A0A0;")
        self.textBrowser_16 = QTextBrowser(self.informacion)
        self.textBrowser_16.setObjectName(u"textBrowser_16")
        self.textBrowser_16.setGeometry(QRect(548, 120, 121, 31))
        self.textBrowser_16.setStyleSheet(u"border:None;\n"
"color: #A0A0A0;")
        self.textBrowser_17 = QTextBrowser(self.informacion)
        self.textBrowser_17.setObjectName(u"textBrowser_17")
        self.textBrowser_17.setGeometry(QRect(548, 220, 121, 31))
        self.textBrowser_17.setStyleSheet(u"border:None;\n"
"color: #A0A0A0;")
        self.frame = QFrame(self.informacion)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(25, 60, 228, 228))
        self.frame.setStyleSheet(u"background-color: #333333  ;\n"
"border: 1px solid #333333;\n"
"border-radius:10px;  /* \ud83d\udd38 Esto redondea los bordes */")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.mapa = QLabel(self.frame)
        self.mapa.setObjectName(u"mapa")
        self.mapa.setGeometry(QRect(0, 0, 228, 228))
        self.pushButton_26 = QPushButton(self.informacion)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setGeometry(QRect(548, 150, 60, 30))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.pushButton_26.setFont(font2)
        self.pushButton_26.setStyleSheet(u"border: 0px;\n"
"border-radius:1px;\n"
"color: #FFFFFF;;\n"
"background-color: #383838;")
        self.pushButton_26.setIconSize(QSize(20, 20))
        self.pushButton_28 = QPushButton(self.informacion)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setGeometry(QRect(668, 150, 60, 30))
        self.pushButton_28.setFont(font2)
        self.pushButton_28.setStyleSheet(u"border: 0px;\n"
"border-radius:1px;\n"
"color: #FFFFFF;\n"
"background-color: #383838;")
        self.pushButton_28.setIconSize(QSize(20, 20))
        self.pushButton_27 = QPushButton(self.informacion)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setGeometry(QRect(608, 150, 60, 30))
        self.pushButton_27.setFont(font2)
        self.pushButton_27.setStyleSheet(u"border: 0px;\n"
"border-radius:1px;\n"
"color: #FFFFFF;;\n"
"background-color: #4b5563;")
        self.pushButton_27.setIconSize(QSize(20, 20))
        self.frame_2 = QFrame(self.informacion)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(550, 250, 180, 40))
        self.frame_2.setStyleSheet(u"background-color: #383838;\n"
"border: 1px solid #383838;\n"
"border-radius:  5px;  /* \ud83d\udd38 Esto redondea los bordes */")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_30 = QPushButton(self.frame_2)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setGeometry(QRect(5, 5, 85, 30))
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(True)
        self.pushButton_30.setFont(font3)
        self.pushButton_30.setStyleSheet(u"border: 0px;\n"
"border-radius:1px;\n"
"color: #FFFFFF;;\n"
"background-color: #202020;\n"
"border: 1px solid #202020;\n"
"border-radius: 5px;  /* \ud83d\udd38 Esto redondea los bordes */")
        icon9 = QIcon()
        icon9.addFile(u"imagenes/video.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_30.setIcon(icon9)
        self.pushButton_30.setIconSize(QSize(20, 20))
        self.pushButton_29 = QPushButton(self.frame_2)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setGeometry(QRect(90, 5, 85, 30))
        self.pushButton_29.setFont(font3)
        self.pushButton_29.setStyleSheet(u"border: 0px;\n"
"border-radius:1px;\n"
"color: #FFFFFF;;\n"
"background-color: #383838;\n"
"border: 1px solid #383838;\n"
"border-radius: 5px;  /* \ud83d\udd38 Esto redondea los bordes */")
        icon10 = QIcon()
        icon10.addFile(u"imagenes/camera.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_29.setIcon(icon10)
        self.pushButton_29.setIconSize(QSize(20, 20))
        self.spinBox = QSpinBox(self.informacion)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(280, 250, 101, 40))
        self.spinBox.setStyleSheet(u"background-color: #383838;\n"
"color: #ffffff;")
        self.pushButton_7 = QPushButton(self.informacion)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(414, 250, 91, 40))
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setStyleSheet(u"border: 1px solid #22E022;\n"
"border-radius: 2px;")
        icon11 = QIcon()
        icon11.addFile(u"imagenes/zone.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon11)
        self.pushButton_7.setIconSize(QSize(14, 14))
        self.pushButton_37 = QPushButton(self.informacion)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setGeometry(QRect(25, 15, 30, 30))
        self.pushButton_37.setFont(font3)
        self.pushButton_37.setStyleSheet(u"border: 0px;\n"
"border-radius:1px;\n"
"color: #FFFFFF;;\n"
"background-color: #383838;\n"
"border: 1px solid #383838;\n"
"border-radius: 5px;  /* \ud83d\udd38 Esto redondea los bordes */")
        icon12 = QIcon()
        icon12.addFile(u"imagenes/minus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_37.setIcon(icon12)
        self.pushButton_37.setIconSize(QSize(20, 20))
        self.pushButton_38 = QPushButton(self.informacion)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setGeometry(QRect(223, 15, 30, 30))
        self.pushButton_38.setFont(font3)
        self.pushButton_38.setStyleSheet(u"border: 0px;\n"
"border-radius:1px;\n"
"color: #FFFFFF;;\n"
"background-color: #383838;\n"
"border: 1px solid #383838;\n"
"border-radius: 5px;  /* \ud83d\udd38 Esto redondea los bordes */")
        icon13 = QIcon()
        icon13.addFile(u"imagenes/plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_38.setIcon(icon13)
        self.pushButton_38.setIconSize(QSize(20, 20))
        self.pushButton_39 = QPushButton(self.informacion)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setGeometry(QRect(698, 50, 30, 30))
        self.pushButton_39.setFont(font3)
        self.pushButton_39.setStyleSheet(u"border: 0px;\n"
"border-radius:1px;\n"
"color: #FFFFFF;;\n"
"background-color: #383838;\n"
"border: 1px solid #383838;\n"
"border-radius: 5px;  /* \ud83d\udd38 Esto redondea los bordes */")
        self.pushButton_39.setIcon(icon13)
        self.pushButton_39.setIconSize(QSize(20, 20))
        self.pushButton_40 = QPushButton(self.informacion)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setGeometry(QRect(548, 50, 30, 30))
        self.pushButton_40.setFont(font3)
        self.pushButton_40.setStyleSheet(u"border: 0px;\n"
"border-radius:1px;\n"
"color: #FFFFFF;;\n"
"background-color: #383838;\n"
"border: 1px solid #383838;\n"
"border-radius: 5px;  /* \ud83d\udd38 Esto redondea los bordes */")
        self.pushButton_40.setIcon(icon12)
        self.pushButton_40.setIconSize(QSize(20, 20))
        self.pushButton_41 = QPushButton(self.informacion)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setGeometry(QRect(603, 50, 70, 30))
        self.pushButton_41.setFont(font2)
        self.pushButton_41.setStyleSheet(u"border: 0px;\n"
"border-radius:5px;\n"
"color: #E0E0E0;;\n"
"background-color: #383838;")
        self.pushButton_41.setIconSize(QSize(20, 20))
        self.tareas = QFrame(self.fondo)
        self.tareas.setObjectName(u"tareas")
        self.tareas.setEnabled(True)
        self.tareas.setGeometry(QRect(908, 20, 372, 432))
        self.tareas.setStyleSheet(u"background-color: #1f2126 ;\n"
"border: 1px solid #1f2126;\n"
"border-radius: 12px;  /* \ud83d\udd38 Esto redondea los bordes */")
        self.tareas.setFrameShape(QFrame.Shape.StyledPanel)
        self.tareas.setFrameShadow(QFrame.Shadow.Raised)
        self.tarea_1 = QFrame(self.tareas)
        self.tarea_1.setObjectName(u"tarea_1")
        self.tarea_1.setGeometry(QRect(0, 0, 372, 57))
        self.tarea_1.setStyleSheet(u"background-color: #282828;")
        self.tarea_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.tarea_1.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_33 = QPushButton(self.tarea_1)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setGeometry(QRect(20, 10, 160, 37))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.pushButton_33.setFont(font4)
        self.pushButton_33.setStyleSheet(u"border: 0px;\n"
"border-radius:1px;\n"
"color: #FFFFFF;;\n"
"background-color: #1F402C  ;\n"
"border: 1px solid #1F402C  ;\n"
"border-radius: 5px;  /* \ud83d\udd38 Esto redondea los bordes */")
        self.pushButton_33.setIconSize(QSize(20, 20))
        self.pushButton_34 = QPushButton(self.tarea_1)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setGeometry(QRect(180, 10, 180, 37))
        self.pushButton_34.setFont(font1)
        self.pushButton_34.setStyleSheet(u"border: 0px;\n"
"border-radius:1px;\n"
"color: #FFFFFF;;\n"
"background-color: #282828  ;\n"
"border: 1px solid #282828  ;\n"
"border-radius: 5px;  /* \ud83d\udd38 Esto redondea los bordes */")
        icon14 = QIcon()
        icon14.addFile(u"imagenes/battery.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_34.setIcon(icon14)
        self.pushButton_34.setIconSize(QSize(20, 20))
        self.tarea_2 = QFrame(self.tareas)
        self.tarea_2.setObjectName(u"tarea_2")
        self.tarea_2.setGeometry(QRect(0, 57, 372, 75))
        self.tarea_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.tarea_2.setFrameShadow(QFrame.Shadow.Raised)
        self.textBrowser_18 = QTextBrowser(self.tarea_2)
        self.textBrowser_18.setObjectName(u"textBrowser_18")
        self.textBrowser_18.setGeometry(QRect(40, 3, 181, 40))
        self.textBrowser_18.setStyleSheet(u"border:None;\n"
"color: #E0E0E0;\n"
"background-color: transparent;")
        self.textBrowser_19 = QTextBrowser(self.tarea_2)
        self.textBrowser_19.setObjectName(u"textBrowser_19")
        self.textBrowser_19.setGeometry(QRect(40, 35, 141, 30))
        self.textBrowser_19.setStyleSheet(u"border:None;\n"
"color: #E0E0E0;\n"
"background-color: transparent;")
        self.tarea_3 = QFrame(self.tareas)
        self.tarea_3.setObjectName(u"tarea_3")
        self.tarea_3.setGeometry(QRect(0, 132, 372, 75))
        self.tarea_3.setStyleSheet(u" border-top: 2px solid #888888;\n"
"border-radius: None;")
        self.tarea_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.tarea_3.setFrameShadow(QFrame.Shadow.Raised)
        self.textBrowser_20 = QTextBrowser(self.tarea_3)
        self.textBrowser_20.setObjectName(u"textBrowser_20")
        self.textBrowser_20.setGeometry(QRect(40, 35, 141, 30))
        self.textBrowser_20.setStyleSheet(u"border:None;\n"
"color: #E0E0E0;\n"
"background-color: transparent;")
        self.textBrowser_21 = QTextBrowser(self.tarea_3)
        self.textBrowser_21.setObjectName(u"textBrowser_21")
        self.textBrowser_21.setGeometry(QRect(40, 3, 181, 40))
        self.textBrowser_21.setStyleSheet(u"border:None;\n"
"color: #E0E0E0;\n"
"background-color: transparent;")
        self.textBrowser_28 = QTextBrowser(self.tarea_3)
        self.textBrowser_28.setObjectName(u"textBrowser_28")
        self.textBrowser_28.setGeometry(QRect(260, 22, 81, 30))
        self.textBrowser_28.setStyleSheet(u"background-color: #383838;\n"
"border:None;\n"
"border-radius: 10px;\n"
"color: #E0E0E0;")
        self.tarea_4 = QFrame(self.tareas)
        self.tarea_4.setObjectName(u"tarea_4")
        self.tarea_4.setGeometry(QRect(0, 207, 372, 75))
        self.tarea_4.setStyleSheet(u" border-top: 2px solid #888888;\n"
"border-radius: None;")
        self.tarea_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.tarea_4.setFrameShadow(QFrame.Shadow.Raised)
        self.textBrowser_22 = QTextBrowser(self.tarea_4)
        self.textBrowser_22.setObjectName(u"textBrowser_22")
        self.textBrowser_22.setGeometry(QRect(40, 35, 141, 30))
        self.textBrowser_22.setStyleSheet(u"border:None;\n"
"color: #E0E0E0;\n"
"background-color: transparent;")
        self.textBrowser_23 = QTextBrowser(self.tarea_4)
        self.textBrowser_23.setObjectName(u"textBrowser_23")
        self.textBrowser_23.setGeometry(QRect(40, 3, 181, 40))
        self.textBrowser_23.setStyleSheet(u"border:None;\n"
"color: #E0E0E0;\n"
"background-color: transparent;")
        self.tarea_5 = QFrame(self.tareas)
        self.tarea_5.setObjectName(u"tarea_5")
        self.tarea_5.setGeometry(QRect(0, 282, 372, 75))
        self.tarea_5.setStyleSheet(u" border-top: 2px solid #888888;\n"
"border-radius: None;")
        self.tarea_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.tarea_5.setFrameShadow(QFrame.Shadow.Raised)
        self.textBrowser_24 = QTextBrowser(self.tarea_5)
        self.textBrowser_24.setObjectName(u"textBrowser_24")
        self.textBrowser_24.setGeometry(QRect(40, 35, 141, 30))
        self.textBrowser_24.setStyleSheet(u"border:None;\n"
"color: #E0E0E0;\n"
"background-color: transparent;")
        self.textBrowser_25 = QTextBrowser(self.tarea_5)
        self.textBrowser_25.setObjectName(u"textBrowser_25")
        self.textBrowser_25.setGeometry(QRect(40, 3, 181, 40))
        self.textBrowser_25.setStyleSheet(u"border:None;\n"
"color: #E0E0E0;\n"
"background-color: transparent;")
        self.tarea_6 = QFrame(self.tareas)
        self.tarea_6.setObjectName(u"tarea_6")
        self.tarea_6.setGeometry(QRect(0, 357, 372, 75))
        self.tarea_6.setStyleSheet(u"border-top: 2px solid #888888;\n"
"border-top-left: None;\n"
"border-top-right: None;\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 12px solid #1f2126;\n"
"border-bottom-right-radius: 12px solid #1f2126;")
        self.tarea_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.tarea_6.setFrameShadow(QFrame.Shadow.Raised)
        self.textBrowser_26 = QTextBrowser(self.tarea_6)
        self.textBrowser_26.setObjectName(u"textBrowser_26")
        self.textBrowser_26.setGeometry(QRect(40, 35, 141, 30))
        self.textBrowser_26.setStyleSheet(u"border:None;\n"
"color: #E0E0E0;\n"
"background-color: transparent;")
        self.textBrowser_27 = QTextBrowser(self.tarea_6)
        self.textBrowser_27.setObjectName(u"textBrowser_27")
        self.textBrowser_27.setGeometry(QRect(40, 3, 181, 40))
        self.textBrowser_27.setStyleSheet(u"border:None;\n"
"color: #E0E0E0;\n"
"background-color: transparent;")
        self.control = QFrame(self.fondo)
        self.control.setObjectName(u"control")
        self.control.setGeometry(QRect(908, 472, 372, 308))
        self.control.setStyleSheet(u"background-color: #1f2126 ;\n"
"border: 1px solid #1f2126;\n"
"border-radius: 12px; ")
        self.control.setFrameShape(QFrame.Shape.StyledPanel)
        self.control.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_35 = QPushButton(self.control)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setGeometry(QRect(40, 40, 120, 80))
        self.pushButton_35.setFont(font1)
        self.pushButton_35.setStyleSheet(u"border: 0px;\n"
"border-radius:1px;\n"
"color: #FFFFFF;;\n"
"background-color: #383838;\n"
"border: 1px solid #383838;\n"
"border-radius: 5px;  /* \ud83d\udd38 Esto redondea los bordes */")
        self.pushButton_35.setIconSize(QSize(20, 20))
        self.pushButton_36 = QPushButton(self.control)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setGeometry(QRect(212, 40, 120, 80))
        self.pushButton_36.setFont(font1)
        self.pushButton_36.setStyleSheet(u"border: 0px;\n"
"border-radius:1px;\n"
"color: #FFFFFF;;\n"
"background-color: #383838;\n"
"border: 1px solid #383838;\n"
"border-radius: 5px;  /* \ud83d\udd38 Esto redondea los bordes */")
        self.pushButton_36.setIconSize(QSize(20, 20))
        self.frame_3 = QFrame(self.control)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(86, 74, 200, 200))
        self.frame_3.setStyleSheet(u"border: 5px solid #1f2126;\n"
"background-color: #383838;\n"
"border-radius: 100px;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_12 = QPushButton(self.frame_3)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setStyleSheet(u"border: none;\n"
"border-radius: 20px;")
        icon15 = QIcon()
        icon15.addFile(u"imagenes/up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_12.setIcon(icon15)

        self.gridLayout.addWidget(self.pushButton_12, 0, 1, 1, 1)

        self.pushButton_13 = QPushButton(self.frame_3)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setStyleSheet(u"border: none;\n"
"border-radius: 20px;")
        icon16 = QIcon()
        icon16.addFile(u"imagenes/down.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_13.setIcon(icon16)

        self.gridLayout.addWidget(self.pushButton_13, 2, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.frame_3)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setStyleSheet(u"border: none;\n"
"border-radius: 20px;")
        icon17 = QIcon()
        icon17.addFile(u"imagenes/left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_9.setIcon(icon17)

        self.gridLayout.addWidget(self.pushButton_9, 1, 0, 1, 1)

        self.pushButton_15 = QPushButton(self.frame_3)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setStyleSheet(u"border: none;\n"
"border-radius: 20px;")
        icon18 = QIcon()
        icon18.addFile(u"imagenes/right.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_15.setIcon(icon18)

        self.gridLayout.addWidget(self.pushButton_15, 1, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.frame_3)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setStyleSheet(u"background-color: transparent;\n"
"border: None;")

        self.gridLayout.addWidget(self.pushButton_8, 2, 0, 1, 1)

        self.pushButton_16 = QPushButton(self.frame_3)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setStyleSheet(u"background-color: transparent;\n"
"border: None;")

        self.gridLayout.addWidget(self.pushButton_16, 2, 2, 1, 1)

        self.pushButton_14 = QPushButton(self.frame_3)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setStyleSheet(u"background-color: transparent;\n"
"border: None;")

        self.gridLayout.addWidget(self.pushButton_14, 0, 2, 1, 1)

        self.pushButton_10 = QPushButton(self.frame_3)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setStyleSheet(u"background-color: transparent;\n"
"border: None;")

        self.gridLayout.addWidget(self.pushButton_10, 0, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.frame_3)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setStyleSheet(u"background-color: #1f2126 ;\n"
"border: none;\n"
"border-radius: 25px;")

        self.gridLayout.addWidget(self.pushButton_11, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Control de UAV", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_4.setText("")
        self.pushButton_3.setText("")
        self.pushButton_6.setText("")
        self.pushButton_5.setText("")
        self.labelvideo.setText("")
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"3:30", None))
        self.pushButton_32.setText("")
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">ISO</span></p></body></html>", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">SHUTTER</span></p></body></html>", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">DISTANCE</span></p></body></html>", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">ZONE</span></p></body></html>", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">550</span></p></body></html>", None))
        self.textBrowser_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">180.0</span></p></body></html>", None))
        self.textBrowser_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">147 km</span></p></body></html>", None))
        self.textBrowser_9.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">06:58</span></p></body></html>", None))
        self.textBrowser_10.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">FRAME</span></p></body></html>", None))
        self.textBrowser_11.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">20 km/h</span></p></body></html>", None))
        self.textBrowser_12.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">SPEED</span></p></body></html>", None))
        self.textBrowser_13.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">FLIGHT TIME</span></p></body></html>", None))
        self.textBrowser_14.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">90 m</span></p></body></html>", None))
        self.textBrowser_15.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">HEIGHT</span></p></body></html>", None))
        self.textBrowser_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">ALTITUDE</span></p></body></html>", None))
        self.textBrowser_16.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">PICTURE MODE</span></p></body></html>", None))
        self.textBrowser_17.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">CAMERA</span></p></body></html>", None))
        self.mapa.setText("")
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"ISO", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"DVR", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"HDR", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"Photo", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u" Green", None))
        self.pushButton_37.setText("")
        self.pushButton_38.setText("")
        self.pushButton_39.setText("")
        self.pushButton_40.setText("")
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"200 ML", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"Ongoing task - 8", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"   12:56 PM", None))
        self.textBrowser_18.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700;\">Task Name Here</span></p></body></html>", None))
        self.textBrowser_19.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">In progress</span></p></body></html>", None))
        self.textBrowser_20.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">In progress</span></p></body></html>", None))
        self.textBrowser_21.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700;\">Task Name Here</span></p></body></html>", None))
        self.textBrowser_28.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">89 %</span></p></body></html>", None))
        self.textBrowser_22.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">In progress</span></p></body></html>", None))
        self.textBrowser_23.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700;\">Task Name Here</span></p></body></html>", None))
        self.textBrowser_24.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">In progress</span></p></body></html>", None))
        self.textBrowser_25.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700;\">Task Name Here</span></p></body></html>", None))
        self.textBrowser_26.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">In progress</span></p></body></html>", None))
        self.textBrowser_27.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700;\">Task Name Here</span></p></body></html>", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"AWB            ", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"            DISP", None))
        self.pushButton_12.setText("")
        self.pushButton_13.setText("")
        self.pushButton_9.setText("")
        self.pushButton_15.setText("")
        self.pushButton_8.setText("")
        self.pushButton_16.setText("")
        self.pushButton_14.setText("")
        self.pushButton_10.setText("")
        self.pushButton_11.setText("")
    # retranslateUi

