# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowvRKVCD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtWidgets import QAction, QWidget, QTextEdit, QCheckBox, QGroupBox, QMenu, QPushButton, QRadioButton, QLabel, QSpinBox, QMenuBar,QStatusBar, QDoubleSpinBox
from PyQt5.QtCore import Qt, QRect, QCoreApplication, QMetaObject
from PyQt5.QtGui import QPixmap, QFont

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1005, 605)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(830, 0, 171, 251))
        self.cbPokemon = QCheckBox(self.groupBox)
        self.cbPokemon.setObjectName(u"cbPokemon")
        self.cbPokemon.setGeometry(QRect(10, 20, 121, 17))
        self.cbTrainers = QCheckBox(self.groupBox)
        self.cbTrainers.setObjectName(u"cbTrainers")
        self.cbTrainers.setGeometry(QRect(10, 100, 121, 17))
        self.cbSafari = QCheckBox(self.groupBox)
        self.cbSafari.setObjectName(u"cbSafari")
        self.cbSafari.setGeometry(QRect(10, 40, 121, 17))
        self.cbUnderground = QCheckBox(self.groupBox)
        self.cbUnderground.setObjectName(u"cbUnderground")
        self.cbUnderground.setGeometry(QRect(10, 60, 141, 17))
        self.cbEvolutions = QCheckBox(self.groupBox)
        self.cbEvolutions.setObjectName(u"cbEvolutions")
        self.cbEvolutions.setGeometry(QRect(10, 80, 141, 17))
        self.cbLevels = QCheckBox(self.groupBox)
        self.cbLevels.setObjectName(u"cbLevels")
        self.cbLevels.setEnabled(False)
        self.cbLevels.setGeometry(QRect(10, 220, 121, 17))
        font = QFont()
        font.setStrikeOut(True)
        self.cbLevels.setFont(font)
        self.cbShops = QCheckBox(self.groupBox)
        self.cbShops.setObjectName(u"cbShops")
        self.cbShops.setGeometry(QRect(10, 120, 121, 17))
        self.cbTM = QCheckBox(self.groupBox)
        self.cbTM.setObjectName(u"cbTM")
        self.cbTM.setGeometry(QRect(10, 140, 121, 17))
        self.cbFieldItems = QCheckBox(self.groupBox)
        self.cbFieldItems.setObjectName(u"cbFieldItems")
        self.cbFieldItems.setEnabled(False)
        self.cbFieldItems.setGeometry(QRect(10, 200, 121, 17))
        self.cbFieldItems.setFont(font)
        self.cbFieldItems_2 = QCheckBox(self.groupBox)
        self.cbFieldItems_2.setObjectName(u"cbFieldItems_2")
        self.cbFieldItems_2.setEnabled(False)
        self.cbFieldItems_2.setGeometry(QRect(10, 180, 121, 17))
        self.cbFieldItems_2.setFont(font)
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(False)
        self.label_5.setGeometry(QRect(10, 160, 71, 16))
        self.tbLog = QTextEdit(self.centralwidget)
        self.tbLog.setObjectName(u"tbLog")
        self.tbLog.setGeometry(QRect(10, 270, 671, 291))
        self.tbLog.setReadOnly(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 0, 571, 251))
        self.label.setPixmap(QPixmap(u"BDSP.png"))
        self.label.setScaledContents(True)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QRect(690, 0, 131, 111))
        self.cbGen1 = QCheckBox(self.groupBox_2)
        self.cbGen1.setObjectName(u"cbGen1")
        self.cbGen1.setGeometry(QRect(10, 30, 51, 17))
        self.cbGen1.setChecked(True)
        self.cbGen2 = QCheckBox(self.groupBox_2)
        self.cbGen2.setObjectName(u"cbGen2")
        self.cbGen2.setGeometry(QRect(70, 30, 51, 17))
        self.cbGen2.setChecked(True)
        self.cbGen3 = QCheckBox(self.groupBox_2)
        self.cbGen3.setObjectName(u"cbGen3")
        self.cbGen3.setGeometry(QRect(10, 60, 51, 17))
        self.cbGen3.setChecked(True)
        self.cbGen4 = QCheckBox(self.groupBox_2)
        self.cbGen4.setObjectName(u"cbGen4")
        self.cbGen4.setGeometry(QRect(70, 60, 51, 17))
        self.cbGen4.setChecked(True)
        self.cbLegends = QCheckBox(self.groupBox_2)
        self.cbLegends.setObjectName(u"cbLegends")
        self.cbLegends.setGeometry(QRect(10, 85, 111, 20))
        self.cbLegends.setChecked(True)
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setGeometry(QRect(690, 110, 131, 141))
        self.rbFlat = QRadioButton(self.groupBox_3)
        self.rbFlat.setObjectName(u"rbFlat")
        self.rbFlat.setGeometry(QRect(10, 20, 111, 17))
        self.rbFlat.setChecked(True)
        self.rbPercent = QRadioButton(self.groupBox_3)
        self.rbPercent.setObjectName(u"rbPercent")
        self.rbPercent.setGeometry(QRect(10, 40, 111, 17))
        self.sbMin = QSpinBox(self.groupBox_3)
        self.sbMin.setObjectName(u"sbMin")
        self.sbMin.setGeometry(QRect(80, 80, 42, 22))
        self.sbMin.setMinimum(1)
        self.sbMax = QSpinBox(self.groupBox_3)
        self.sbMax.setObjectName(u"sbMax")
        self.sbMax.setGeometry(QRect(80, 110, 42, 22))
        self.sbMax.setMinimum(1)
        self.sbMax.setValue(99)
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 80, 47, 13))
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 110, 47, 13))
        self.btnRandomize = QPushButton(self.centralwidget)
        self.btnRandomize.setObjectName(u"btnRandomize")
        self.btnRandomize.setGeometry(QRect(690, 460, 301, 101))
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(830, 250, 171, 191))
        self.cb60FPS = QCheckBox(self.groupBox_4)
        self.cb60FPS.setObjectName(u"cb60FPS")
        self.cb60FPS.setGeometry(QRect(10, 20, 121, 17))
        self.cbTimeSkip = QCheckBox(self.groupBox_4)
        self.cbTimeSkip.setObjectName(u"cbTimeSkip")
        self.cbTimeSkip.setGeometry(QRect(10, 40, 121, 17))
        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setEnabled(True)
        self.groupBox_5.setGeometry(QRect(690, 250, 131, 51))
        self.label_4 = QLabel(self.groupBox_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 20, 47, 13))
        self.sbTimeStep = QDoubleSpinBox(self.groupBox_5)
        self.sbTimeStep.setObjectName(u"sbTimeStep")
        self.sbTimeStep.setGeometry(QRect(60, 21, 62, 21))
        self.sbTimeStep.setSingleStep(0.100000000000000)
        self.sbTimeStep.setValue(1.000000000000000)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1005, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Randomizers", None))
        self.cbPokemon.setText(QCoreApplication.translate("MainWindow", u"Randomize Pokemon", None))
        self.cbTrainers.setText(QCoreApplication.translate("MainWindow", u"Randomize Trainers", None))
        self.cbSafari.setText(QCoreApplication.translate("MainWindow", u"Randomize Safari", None))
        self.cbUnderground.setText(QCoreApplication.translate("MainWindow", u"Randomize Underground", None))
        self.cbEvolutions.setText(QCoreApplication.translate("MainWindow", u"Randomize Evolutions", None))
        self.cbLevels.setText(QCoreApplication.translate("MainWindow", u"Randomize Levels", None))
        self.cbShops.setText(QCoreApplication.translate("MainWindow", u"Randomize Shops", None))
        self.cbTM.setText(QCoreApplication.translate("MainWindow", u"Randomize TMs", None))
        self.cbFieldItems.setText(QCoreApplication.translate("MainWindow", u"Randomize Field Items", None))
        self.cbFieldItems_2.setText(QCoreApplication.translate("MainWindow", u"Randomize Abilities", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Coming Soon", None))
        self.tbLog.setPlaceholderText("")
        self.label.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Pokemon Options", None))
        self.cbGen1.setText(QCoreApplication.translate("MainWindow", u"Gen 1", None))
        self.cbGen2.setText(QCoreApplication.translate("MainWindow", u"Gen 2", None))
        self.cbGen3.setText(QCoreApplication.translate("MainWindow", u"Gen 3", None))
        self.cbGen4.setText(QCoreApplication.translate("MainWindow", u"Gen 4", None))
        self.cbLegends.setText(QCoreApplication.translate("MainWindow", u"Keep Legendarys", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Level Options", None))
        self.rbFlat.setText(QCoreApplication.translate("MainWindow", u"Flat Random", None))
        self.rbPercent.setText(QCoreApplication.translate("MainWindow", u"% Random", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Min Lvl", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Max Lvl", None))
        self.btnRandomize.setText(QCoreApplication.translate("MainWindow", u"Lets go!!!", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Utilities", None))
        self.cb60FPS.setText(QCoreApplication.translate("MainWindow", u"60FPS Mod", None))
        self.cbTimeSkip.setText(QCoreApplication.translate("MainWindow", u"Timestep Multipler", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Timestep", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Timestep", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

