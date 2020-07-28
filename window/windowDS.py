# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowDS.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os
import webbrowser

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl, QFileInfo
from PyQt5.QtWebEngineWidgets import QWebEngineView

from engineerMesure.leicaGsiFormat import LeicaGSIFormat
from database.database import Database
from window import welcomeWight
from window.geodeticSurvey import inversionGravityFieldWight
from window.measureTool import coorTranWight, coorTranOpenFileDiaog, stablePointGroupWight
from window.controlNetwork import stablePointGroupFileDialog, controlNetAdjustmentWight
from window.engineeringSurvey import leicaDataFormatWight
from window.windowEvent.actionReport import Report
from window.file.fileMsg import FileMsg
from window.tipDig import ActionWarnException
from window.GNSS import SPPWight, PPPWight


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.NonModal)
        mainWindow.resize(1241, 725)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./source/icon/EMACS-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet("")
        mainWindow.setDocumentMode(False)
        mainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        mainWindow.setDockNestingEnabled(False)
        mainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_operate = QtWidgets.QWidget()
        self.tab_operate.setObjectName("tab_operate")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_operate)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget = QtWidgets.QWidget(self.tab_operate)
        self.widget.setObjectName("widget")
        self.verticalLayout_4.addWidget(self.widget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./source/icon/zaogao.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_operate, icon1, "")
        self.tab_position = QtWidgets.QWidget()
        self.tab_position.setObjectName("tab_position")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_position)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.tab_position)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2.addWidget(self.widget_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./source/icon/sd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_position, icon2, "")
        self.tab_monitor = QtWidgets.QWidget()
        self.tab_monitor.setObjectName("tab_monitor")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_monitor)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_3 = QtWidgets.QWidget(self.tab_monitor)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.textEdit_monitor = QtWidgets.QTextEdit(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEdit_monitor.setFont(font)
        self.textEdit_monitor.setObjectName("textEdit_monitor")
        self.verticalLayout_7.addWidget(self.textEdit_monitor)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tableWidget_monitor = QtWidgets.QTableWidget(self.widget_3)
        self.tableWidget_monitor.setObjectName("tableWidget_monitor")
        self.tableWidget_monitor.setColumnCount(2)
        self.tableWidget_monitor.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_monitor.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_monitor.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_monitor.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_monitor.setHorizontalHeaderItem(1, item)
        self.verticalLayout_8.addWidget(self.tableWidget_monitor)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_5.addWidget(self.widget_3)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./source/icon/document.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_monitor, icon3, "")
        self.tab_more = QtWidgets.QWidget()
        self.tab_more.setObjectName("tab_more")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_more)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mdiArea = QtWidgets.QMdiArea(self.tab_more)
        self.mdiArea.setStyleSheet("")
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.Dense7Pattern)
        self.mdiArea.setBackground(brush)
        self.mdiArea.setViewMode(QtWidgets.QMdiArea.TabbedView)
        self.mdiArea.setDocumentMode(False)
        self.mdiArea.setTabsClosable(True)
        self.mdiArea.setTabsMovable(True)
        self.mdiArea.setObjectName("mdiArea")
        self.verticalLayout_3.addWidget(self.mdiArea)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./source/icon/more.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_more, icon4, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1241, 26))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menu_C = QtWidgets.QMenu(self.menubar)
        self.menu_C.setObjectName("menu_C")
        self.menu_C_2 = QtWidgets.QMenu(self.menu_C)
        self.menu_C_2.setObjectName("menu_C_2")
        self.menu_G = QtWidgets.QMenu(self.menu_C)
        self.menu_G.setObjectName("menu_G")
        self.menu_T = QtWidgets.QMenu(self.menu_C)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_T.sizePolicy().hasHeightForWidth())
        self.menu_T.setSizePolicy(sizePolicy)
        self.menu_T.setObjectName("menu_T")
        self.menu_S = QtWidgets.QMenu(self.menubar)
        self.menu_S.setObjectName("menu_S")
        self.menu_V = QtWidgets.QMenu(self.menubar)
        self.menu_V.setObjectName("menu_V")
        self.menu_H = QtWidgets.QMenu(self.menubar)
        self.menu_H.setObjectName("menu_H")
        self.menuGNSS_2 = QtWidgets.QMenu(self.menubar)
        self.menuGNSS_2.setObjectName("menuGNSS_2")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.dockWidget_File = QtWidgets.QDockWidget(mainWindow)
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.dockWidget_File.setFont(font)
        self.dockWidget_File.setToolTip("")
        self.dockWidget_File.setStyleSheet("")
        self.dockWidget_File.setFloating(False)
        self.dockWidget_File.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget_File.setObjectName("dockWidget_File")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeView = QtWidgets.QTreeView(self.dockWidgetContents_2)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)
        self.dockWidget_File.setWidget(self.dockWidgetContents_2)
        mainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_File)
        self.toolBar = QtWidgets.QToolBar(mainWindow)
        self.toolBar.setObjectName("toolBar")
        mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidget_status = QtWidgets.QDockWidget(mainWindow)
        self.dockWidget_status.setTabletTracking(False)
        self.dockWidget_status.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dockWidget_status.setAutoFillBackground(False)
        self.dockWidget_status.setStyleSheet("")
        self.dockWidget_status.setFloating(False)
        self.dockWidget_status.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockWidget_status.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget_status.setObjectName("dockWidget_status")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.textEdit_status = QtWidgets.QTextEdit(self.dockWidgetContents_4)
        self.textEdit_status.setObjectName("textEdit_status")
        self.verticalLayout_6.addWidget(self.textEdit_status)
        self.dockWidget_status.setWidget(self.dockWidgetContents_4)
        mainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_status)
        self.toolBar_2 = QtWidgets.QToolBar(mainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.menuItem_new = QtWidgets.QAction(mainWindow)
        self.menuItem_new.setCheckable(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./source/icon/baogao.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuItem_new.setIcon(icon5)
        self.menuItem_new.setObjectName("menuItem_new")
        self.menuItem_openFile = QtWidgets.QAction(mainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./source/icon/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuItem_openFile.setIcon(icon6)
        self.menuItem_openFile.setObjectName("menuItem_openFile")
        self.menuItem_saveFile = QtWidgets.QAction(mainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("./source/icon/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuItem_saveFile.setIcon(icon7)
        self.menuItem_saveFile.setObjectName("menuItem_saveFile")
        self.menuItem_quitSystem = QtWidgets.QAction(mainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("./source/icon/decentralized-02.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuItem_quitSystem.setIcon(icon8)
        self.menuItem_quitSystem.setObjectName("menuItem_quitSystem")
        self.munuItem_markbook = QtWidgets.QAction(mainWindow)
        self.munuItem_markbook.setObjectName("munuItem_markbook")
        self.munuItem_controlNet = QtWidgets.QAction(mainWindow)
        self.munuItem_controlNet.setObjectName("munuItem_controlNet")
        self.munuItem_railwayCurve = QtWidgets.QAction(mainWindow)
        self.munuItem_railwayCurve.setEnabled(True)
        self.munuItem_railwayCurve.setObjectName("munuItem_railwayCurve")
        self.munuItem_CPIII = QtWidgets.QAction(mainWindow)
        self.munuItem_CPIII.setEnabled(False)
        self.munuItem_CPIII.setObjectName("munuItem_CPIII")
        self.munuItem_GNSSNet = QtWidgets.QAction(mainWindow)
        self.munuItem_GNSSNet.setObjectName("munuItem_GNSSNet")
        self.munuItem_cacuPara = QtWidgets.QAction(mainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("./source/icon/designer-tools.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.munuItem_cacuPara.setIcon(icon9)
        self.munuItem_cacuPara.setObjectName("munuItem_cacuPara")
        self.munuItem_systemPara = QtWidgets.QAction(mainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("./source/icon/set.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.munuItem_systemPara.setIcon(icon10)
        self.munuItem_systemPara.setObjectName("munuItem_systemPara")
        self.munuItem_windowSet = QtWidgets.QAction(mainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("./source/icon/calender.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.munuItem_windowSet.setIcon(icon11)
        self.munuItem_windowSet.setObjectName("munuItem_windowSet")
        self.munuItem_onlineHelp = QtWidgets.QAction(mainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("./source/icon/lineOneline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.munuItem_onlineHelp.setIcon(icon12)
        self.munuItem_onlineHelp.setObjectName("munuItem_onlineHelp")
        self.munuItem_localHelp = QtWidgets.QAction(mainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("./source/icon/line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.munuItem_localHelp.setIcon(icon13)
        self.munuItem_localHelp.setObjectName("munuItem_localHelp")
        self.menuItem_resultReport = QtWidgets.QAction(mainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("./source/icon/outPut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuItem_resultReport.setIcon(icon14)
        self.menuItem_resultReport.setObjectName("menuItem_resultReport")
        self.munuItem_version = QtWidgets.QAction(mainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("../source/icon/note.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.munuItem_version.setIcon(icon15)
        self.munuItem_version.setObjectName("munuItem_version")
        self.menuItem_backWelcome = QtWidgets.QAction(mainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("./source/icon/resu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuItem_backWelcome.setIcon(icon16)
        self.menuItem_backWelcome.setObjectName("menuItem_backWelcome")
        self.munuItem_statusBar = QtWidgets.QAction(mainWindow)
        self.munuItem_statusBar.setCheckable(True)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("./source/icon/mes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.munuItem_statusBar.setIcon(icon17)
        self.munuItem_statusBar.setObjectName("munuItem_statusBar")
        self.munuItem_fileStatusBar = QtWidgets.QAction(mainWindow)
        self.munuItem_fileStatusBar.setCheckable(True)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("./source/icon/tree.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.munuItem_fileStatusBar.setIcon(icon18)
        self.munuItem_fileStatusBar.setObjectName("munuItem_fileStatusBar")
        self.munuItem_license = QtWidgets.QAction(mainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("./source/icon/icon_any.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.munuItem_license.setIcon(icon19)
        self.munuItem_license.setObjectName("munuItem_license")
        self.munuItem_stablePointGround = QtWidgets.QAction(mainWindow)
        self.munuItem_stablePointGround.setObjectName("munuItem_stablePointGround")
        self.munuItem_satellite = QtWidgets.QAction(mainWindow)
        self.munuItem_satellite.setObjectName("munuItem_satellite")
        self.munuItem_coorSystemTran = QtWidgets.QAction(mainWindow)
        self.munuItem_coorSystemTran.setObjectName("munuItem_coorSystemTran")
        self.munuItem_coorTran = QtWidgets.QAction(mainWindow)
        self.munuItem_coorTran.setObjectName("munuItem_coorTran")
        self.munuItem_GussianTran = QtWidgets.QAction(mainWindow)
        self.munuItem_GussianTran.setObjectName("munuItem_GussianTran")
        self.munuItem_contact = QtWidgets.QAction(mainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("./source/icon/conme.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.munuItem_contact.setIcon(icon20)
        self.munuItem_contact.setObjectName("munuItem_contact")
        self.menuItem_SPP = QtWidgets.QAction(mainWindow)
        self.menuItem_SPP.setObjectName("menuItem_SPP")
        self.actionPPP_P = QtWidgets.QAction(mainWindow)
        self.actionPPP_P.setObjectName("actionPPP_P")
        self.action_G = QtWidgets.QAction(mainWindow)
        self.action_G.setObjectName("action_G")
        self.actionGNSS_L = QtWidgets.QAction(mainWindow)
        self.actionGNSS_L.setObjectName("actionGNSS_L")
        self.menu_F.addAction(self.menuItem_new)
        self.menu_F.addSeparator()
        self.menu_F.addAction(self.menuItem_openFile)
        self.menu_F.addSeparator()
        self.menu_F.addAction(self.menuItem_saveFile)
        self.menu_F.addSeparator()
        self.menu_F.addAction(self.menuItem_resultReport)
        self.menu_F.addSeparator()
        self.menu_F.addAction(self.menuItem_quitSystem)
        self.menu_C_2.addAction(self.munuItem_stablePointGround)
        self.menu_G.addAction(self.munuItem_railwayCurve)
        self.menu_G.addAction(self.munuItem_CPIII)
        self.menu_T.addAction(self.munuItem_coorSystemTran)
        self.menu_T.addAction(self.munuItem_coorTran)
        self.menu_T.addAction(self.munuItem_GussianTran)
        self.menu_C.addAction(self.menu_T.menuAction())
        self.menu_C.addSeparator()
        self.menu_C.addAction(self.munuItem_markbook)
        self.menu_C.addSeparator()
        self.menu_C.addAction(self.munuItem_controlNet)
        self.menu_C.addSeparator()
        self.menu_C.addAction(self.menu_G.menuAction())
        self.menu_C.addSeparator()
        self.menu_C.addAction(self.menu_C_2.menuAction())
        self.menu_C.addSeparator()
        self.menu_S.addAction(self.munuItem_windowSet)
        self.menu_S.addSeparator()
        self.menu_S.addAction(self.menuItem_backWelcome)
        self.menu_S.addSeparator()
        self.menu_S.addAction(self.munuItem_cacuPara)
        self.menu_S.addAction(self.munuItem_systemPara)
        self.menu_S.addSeparator()
        self.menu_S.addAction(self.munuItem_statusBar)
        self.menu_S.addAction(self.munuItem_fileStatusBar)
        self.menu_V.addAction(self.munuItem_version)
        self.menu_V.addAction(self.munuItem_license)
        self.menu_V.addAction(self.munuItem_contact)
        self.menu_H.addAction(self.munuItem_onlineHelp)
        self.menu_H.addAction(self.munuItem_localHelp)
        self.menuGNSS_2.addAction(self.munuItem_satellite)
        self.menuGNSS_2.addSeparator()
        self.menuGNSS_2.addAction(self.munuItem_GNSSNet)
        self.menuGNSS_2.addSeparator()
        self.menuGNSS_2.addAction(self.menuItem_SPP)
        self.menuGNSS_2.addSeparator()
        self.menuGNSS_2.addAction(self.actionPPP_P)
        self.menuGNSS_2.addSeparator()
        self.menuGNSS_2.addAction(self.action_G)
        self.menuGNSS_2.addSeparator()
        self.menuGNSS_2.addAction(self.actionGNSS_L)
        self.menuGNSS_2.addSeparator()
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menuGNSS_2.menuAction())
        self.menubar.addAction(self.menu_C.menuAction())
        self.menubar.addAction(self.menu_S.menuAction())
        self.menubar.addAction(self.menu_H.menuAction())
        self.menubar.addAction(self.menu_V.menuAction())
        self.toolBar.addAction(self.menuItem_new)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.menuItem_openFile)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.menuItem_saveFile)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.munuItem_windowSet)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.menuItem_resultReport)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.munuItem_contact)
        self.toolBar_2.addAction(self.munuItem_systemPara)
        self.toolBar_2.addAction(self.munuItem_statusBar)
        self.toolBar_2.addAction(self.munuItem_fileStatusBar)
        self.toolBar_2.addAction(self.munuItem_localHelp)
        self.toolBar_2.addAction(self.munuItem_onlineHelp)
        self.toolBar_2.addSeparator()

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)

        # 初始化页面
        self.welcomeWight_ui = welcomeWight.Ui_Form()
        self.welcomeWight_ui.setupUi(self.widget)
        self.welcomeWight()

        self.coorTranWight_ui = coorTranWight.Ui_Form()
        self.coorTranWight_ui.infoEmit.connect(self.displayInfo)

        # self.leicaDataFormat_ui = leicaDataFormatWight.Ui_Form()

        self.controlNetAdjustment_ui = controlNetAdjustmentWight.Ui_Form()

        self.dialogUi = coorTranOpenFileDiaog.Ui_Dialog()
        self.dialogUi.fileReadEmit.connect(self.setOpenFileInfo)
        self.dialogUi.infoEmit.connect(self.displayInfo)
        # 稳定点组
        self.stablePointGroupDialog = QtWidgets.QDialog()
        self.stablePointGroupFileDialog_ui = stablePointGroupFileDialog.Ui_Dialog()
        self.stablePointGroupFileDialog_ui.fileReadEmit.connect(self.setOpenFileInfo_stable)
        self.stablePointGroupFileDialog_ui.infoEmit.connect(self.displayInfo)
        self.stablePointGroupFileDialog_ui.closeEventEmit.connect(self.stableDotGroupTable)

        # GNSS菜单
        self.menuItem_SPP.triggered.connect(self.sppWight)
        self.actionPPP_P.triggered.connect(self.pppWight)
        self.action_G.triggered.connect(self.gravityFieldWight)

        self.munuItem_coorTran.triggered.connect(self.coorTranQwight)
        self.munuItem_markbook.triggered.connect(self.leicaFormatWight)
        self.munuItem_controlNet.triggered.connect(self.horizontalControlNetworkWight)
        self.munuItem_stablePointGround.triggered.connect(self.stablePointGroupWight)
        self.menuItem_openFile.triggered.connect(self.coorTranOpenFileDialog)
        self.menuItem_backWelcome.triggered.connect(self.welcomeWight)
        self.munuItem_statusBar.triggered.connect(self.dockWidget_status.show)
        self.munuItem_fileStatusBar.triggered.connect(self.dockWidget_File.show)
        self.menuItem_resultReport.triggered.connect(self.saveReport)

        # self.menuItem_new.triggered.connect(self.actionMoreWindow)
        self.munuItem_fileStatusBar.triggered.connect(self.actionMenuItem_fileStatusBar)
        self.munuItem_statusBar.triggered.connect(self.actionMenuItem_statusBar)
        self.dockWidget_File.visibilityChanged['bool'].connect(self.dockWight_fileStatusCloseEvent)
        self.dockWidget_status.visibilityChanged['bool'].connect(self.dockWight_statusCloseEvent)
        self.munuItem_onlineHelp.triggered.connect(self.onlineHelp)

        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "EMACS 2020"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_operate), _translate("mainWindow", "操作"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_position), _translate("mainWindow", "可视化"))
        item = self.tableWidget_monitor.verticalHeaderItem(0)
        item.setText(_translate("mainWindow", "1"))
        item = self.tableWidget_monitor.verticalHeaderItem(1)
        item.setText(_translate("mainWindow", "2"))
        item = self.tableWidget_monitor.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "A"))
        item = self.tableWidget_monitor.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "B "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_monitor), _translate("mainWindow", "阅览"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_more), _translate("mainWindow", "更多"))
        self.menu_F.setTitle(_translate("mainWindow", "文件(&F)"))
        self.menu_C.setTitle(_translate("mainWindow", "更多功能(&C)"))
        self.menu_C_2.setTitle(_translate("mainWindow", "形变监测(&C)"))
        self.menu_G.setTitle(_translate("mainWindow", "工程测量(&G)"))
        self.menu_T.setTitle(_translate("mainWindow", "坐标变换(&T)"))
        self.menu_S.setTitle(_translate("mainWindow", "设置(&S)"))
        self.menu_V.setTitle(_translate("mainWindow", "版本(&V)"))
        self.menu_H.setTitle(_translate("mainWindow", "帮助(&H)"))
        self.menuGNSS_2.setTitle(_translate("mainWindow", "GNSS(&G)"))
        self.dockWidget_File.setWindowTitle(_translate("mainWindow", "文件列表"))
        self.toolBar.setWindowTitle(_translate("mainWindow", "toolBar"))
        self.dockWidget_status.setWindowTitle(_translate("mainWindow", "状态信息"))
        self.toolBar_2.setWindowTitle(_translate("mainWindow", "toolBar_2"))
        self.menuItem_new.setText(_translate("mainWindow", "新建(&N)"))
        self.menuItem_openFile.setText(_translate("mainWindow", "打开文件(&O)"))
        self.menuItem_saveFile.setText(_translate("mainWindow", "保存文件(&S)"))
        self.menuItem_quitSystem.setText(_translate("mainWindow", "退出系统(&Q)"))
        self.munuItem_markbook.setText(_translate("mainWindow", "电子手簿(&P)"))
        self.munuItem_markbook.setIconText(_translate("mainWindow", "徕卡GSI格式解析与水准电子手簿(P)"))
        self.munuItem_controlNet.setText(_translate("mainWindow", "地面控制网平差(&D)"))
        self.munuItem_railwayCurve.setText(_translate("mainWindow", "铁路曲线计算(&T)"))
        self.munuItem_CPIII.setText(_translate("mainWindow", "CPIII控制网平差(&C)"))
        self.munuItem_GNSSNet.setText(_translate("mainWindow", "静态GNSS网平差(&A)"))
        self.munuItem_cacuPara.setText(_translate("mainWindow", "计算参数(&P)"))
        self.munuItem_systemPara.setText(_translate("mainWindow", "系统参数(&S)"))
        self.munuItem_windowSet.setText(_translate("mainWindow", "界面设置(&W)"))
        self.munuItem_onlineHelp.setText(_translate("mainWindow", "在线帮助(&I)"))
        self.munuItem_localHelp.setText(_translate("mainWindow", "本地文档(&I)"))
        self.menuItem_resultReport.setText(_translate("mainWindow", "导出报告(&O)"))
        self.munuItem_version.setText(_translate("mainWindow", "版本信息(&V)"))
        self.menuItem_backWelcome.setText(_translate("mainWindow", "返回欢迎界面(&B)"))
        self.munuItem_statusBar.setText(_translate("mainWindow", "状态信息栏(&S) "))
        self.munuItem_fileStatusBar.setText(_translate("mainWindow", "文件列表栏(&F)"))
        self.munuItem_license.setText(_translate("mainWindow", "授权注册(&L)"))
        self.munuItem_stablePointGround.setText(_translate("mainWindow", "稳定点组分析(&X)"))
        self.munuItem_satellite.setText(_translate("mainWindow", "卫星轨道解算与预测(&S)"))
        self.munuItem_coorSystemTran.setText(_translate("mainWindow", "坐标系统转换(&S)"))
        self.munuItem_coorTran.setText(_translate("mainWindow", "坐标(系)转换"))
        self.munuItem_GussianTran.setText(_translate("mainWindow", "高斯坐标正反算(&S)"))
        self.munuItem_contact.setText(_translate("mainWindow", "联系方式(&L)"))
        self.menuItem_SPP.setText(_translate("mainWindow", "标准单点定位SPP(&S)"))
        self.actionPPP_P.setText(_translate("mainWindow", "PPP精密单点定位(&P)"))
        self.action_G.setText(_translate("mainWindow", "GNSS重力场反演(&G)"))
        self.actionGNSS_L.setText(_translate("mainWindow", "GNSS与重力场应用(&L)"))

    def displayInfo(self, type, strInfo):

        if type == "I":
            self.textEdit_status.append(strInfo)
        elif type == "M":
            self.actionShowStationPositonInMap(strInfo)
        else:
            ActionWarnException(self.centralwidget).actionWarnException(type, strInfo)

    def showPan(self, fileRoot):
        """
        文件列表树
        :param: 文件所在相对目录，不能包含文件名
        :return:None
        """
        model = QtWidgets.QFileSystemModel()
        model.setRootPath(fileRoot)
        self.treeView.setModel(model)
        self.treeView.setRootIndex(model.index(fileRoot))

    """
    # 切换功能面板构造
    """

    def actionMoreWindow(self):
        pass

    def actionShowStationPositonInMap(self, title):
        """
        多文档界面
        :return:
        """
        _translate = QtCore.QCoreApplication.translate
        # 加载完成后跳转
        self.tabWidget.setCurrentIndex(3)
        # 实例化多文档界面对象
        self.sub = QtWidgets.QMdiSubWindow()
        # 设置新建子窗口的标题
        self.sub.setWindowTitle(title)
        # self.verticalLayout_more.addWidget(self.sub,wight)
        self.brower = QWebEngineView(self.sub)
        # 设置网页在窗口中显示的位置和大小
        self.brower.setGeometry(0, 0, self.sub.width() + 1000, self.sub.height() + 500)
        # 在QWebEngineView中加载网址
        # print("nima","file:///"+QFileInfo("./source/template/baiduMap.html").absoluteFilePath())
        localHtmlPath = "file:///" + QFileInfo(Database.baiduMapLinkPath).absoluteFilePath()
        self.brower.load(QUrl(localHtmlPath))
        # 将子窗口添加到Mdi区域
        self.mdiArea.addSubWindow(self.sub)
        self.brower.show()
        # 子窗口显示
        self.sub.show()

    def coorTranQwight(self):
        """
        坐标转换功能面板
        :return: None
        """
        self.tabWidget.setCurrentIndex(0)
        _translate = QtCore.QCoreApplication.translate
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_operate), _translate("mainWindow", "坐标转换"))
        # 界面重构存储区域
        self.widget.deleteLater()
        self.widget = QtWidgets.QWidget(self.tab_operate)
        self.widget.setObjectName("widget")
        self.verticalLayout_4.addWidget(self.widget)
        self.coorTranWight_ui.setupUi(self.widget)

    def leicaFormatWight(self):
        self.tabWidget.setCurrentIndex(0)
        _translate = QtCore.QCoreApplication.translate
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_operate), _translate("mainWindow", "电子手簿"))
        # 界面重构存储区域
        self.widget.deleteLater()
        self.widget = QtWidgets.QWidget(self.tab_operate)
        self.widget.setObjectName("widget")
        self.verticalLayout_4.addWidget(self.widget)
        self.leicaDataFormat_ui = leicaDataFormatWight.Ui_Form()
        self.leicaDataFormat_ui.setupUi(self.widget)

    def horizontalControlNetworkWight(self):
        self.tabWidget.setCurrentIndex(0)
        _translate = QtCore.QCoreApplication.translate
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_operate), _translate("mainWindow", "控制网"))
        # 界面重构存储区域
        self.widget.deleteLater()
        self.widget = QtWidgets.QWidget(self.tab_operate)
        self.widget.setObjectName("widget")
        self.verticalLayout_4.addWidget(self.widget)

        self.controlNetAdjustment_ui.setupUi(self.widget)

    def stablePointGroupWight(self):
        """
        相对稳定点组
        :return:
        """
        self.tabWidget.setCurrentIndex(0)
        _translate = QtCore.QCoreApplication.translate
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_operate), _translate("mainWindow", "稳定点组"))
        # 界面重构存储区域
        self.widget.deleteLater()
        self.widget = QtWidgets.QWidget(self.tab_operate)
        self.widget.setObjectName("widget")
        self.stablePointGroupWight_ui = stablePointGroupWight.Ui_Form()
        self.stablePointGroupWight_ui.setupUi(self.widget)
        self.verticalLayout_4.addWidget(self.widget)
        self.stablePointGroupWight_ui.infoEmit.connect(self.displayInfo)

    def sppWight(self):
        """GNSS单点定位界面"""
        self.tabWidget.setCurrentIndex(0)
        _translate = QtCore.QCoreApplication.translate
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_operate), _translate("mainWindow", "单点定位(SPP)"))
        # 界面重构存储区域
        self.widget.deleteLater()
        self.widget = QtWidgets.QWidget(self.tab_operate)
        self.widget.setObjectName("widget")
        # GNSS单点定位
        self.sppWight_ui = SPPWight.Ui_Form()
        self.sppWight_ui.setupUi(self.widget)
        self.verticalLayout_4.addWidget(self.widget)
        self.sppWight_ui.infoEmit.connect(self.displayInfo)

    def pppWight(self):
        """GNSS单点定位界面"""
        self.tabWidget.setCurrentIndex(0)
        _translate = QtCore.QCoreApplication.translate
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_operate), _translate("mainWindow", "单点定位(PPP)"))
        # 界面重构存储区域
        self.widget.deleteLater()
        self.widget = QtWidgets.QWidget(self.tab_operate)
        self.widget.setObjectName("widget")
        # GNSS单点定位
        self.pppWight_ui = PPPWight.Ui_Form()
        self.pppWight_ui.setupUi(self.widget)
        self.verticalLayout_4.addWidget(self.widget)
        self.pppWight_ui.infoEmit.connect(self.displayInfo)

    def gravityFieldWight(self):
        """重力场反演界面"""
        self.tabWidget.setCurrentIndex(0)
        _translate = QtCore.QCoreApplication.translate
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_operate), _translate("mainWindow", "重力场反演"))
        # 界面重构存储区域
        self.widget.deleteLater()
        self.widget = QtWidgets.QWidget(self.tab_operate)
        self.widget.setObjectName("widget")
        # GNSS单点定位
        self.gravityFieldWight_ui = inversionGravityFieldWight.Ui_Form()
        self.gravityFieldWight_ui.setupUi(self.widget)
        self.verticalLayout_4.addWidget(self.widget)
        self.gravityFieldWight_ui.infoEmit.connect(self.displayInfo)

    def welcomeWight(self):
        """
        欢迎页面
        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_operate), _translate("mainWindow", "欢迎"))
        self.widget.deleteLater()
        self.widget = QtWidgets.QWidget(self.tab_operate)
        self.widget.setObjectName("widget")
        self.verticalLayout_4.addWidget(self.widget)
        self.welcomeWight_ui.setupUi(self.widget)

    def coorTranOpenFileDialog(self):
        """
        坐标文件打开对话框
        :return: None
        """
        try:
            # 获取当前功能模块
            tabIndex = self.tabWidget.currentIndex()
            tabLable = self.tabWidget.tabText(tabIndex)
            _translate = QtCore.QCoreApplication.translate
            if tabLable == "坐标转换":
                # 界面重构存储区域
                self.dialog = QtWidgets.QDialog()
                self.dialogUi.setupUi(self.dialog)
                self.dialog.setWindowModality(QtCore.Qt.ApplicationModal)
                self.dialog.show()

            elif tabLable == "电子手簿":
                # 界面wight区域重构
                gsiDataList, filePath = FileMsg(self.centralwidget).openFile()
                Database.leicaSourceGsiData = gsiDataList
                # 显示文件区域
                self.showPan(os.path.dirname(os.path.realpath(filePath)))

                # 直接执行解析
                # ActionLeicaGSIThread().start()
                # 从数据库获取数据
                self.textEdit_status.append("---读取GSI数据文件....")
                self.displayInfo('I', "打开窗口并读取GSI数据文件")
                sourceStrData = Database.leicaSourceGsiData
                # 格式解析
                leicaGSIAnalysisDict = LeicaGSIFormat(sourceStrData).getAnalysisDict()
                self.textEdit_status.append("---完成GSI数据文件解析....")
                self.displayInfo('I', "完成GSI数据文件解析")
                # 解析显示
                self.textEdit_status.append("\n~\n")  # 分化
                self.textEdit_status.append("----【 GSI 文件解析结果 】-----")
                self.textEdit_status.append(" 一.测量模式\n" + str(leicaGSIAnalysisDict.get("model")))
                self.textEdit_status.append("\n 二.控制点或重要点ID（非普通）及地面高/mm\n * 指点名一段测段两端记录的点,点名记录值规定三位\n")
                self.textEditFormatAdd(leicaGSIAnalysisDict.get("ID"))
                self.textEdit_status.append(
                    "\n 四.BFFB 数据\n * 六位的数据前两位为标识符，非有效数据 \n 照准点ID 距离Distance/mm  后视|前视距/mm 复测次数  单次测量标准偏差/mm \n")
                self.textEditFormatAdd(leicaGSIAnalysisDict.get("data"))
                self.textEdit_status.append("\n 五.解算数据\n 当前归算点 站间差/mm 累积站差/mm   距离平衡/mm  测线总距离/mm  地面高（起点高或测量高）/mm \n")
                self.textEditFormatAdd(leicaGSIAnalysisDict.get("calculator"))
                # 解析结果，存入数据库
                Database.leicaAnalysisDict = leicaGSIAnalysisDict
                # 发送表格开始显示信号
                self.leicaDataFormat_ui.showTableEmit.emit()
                self.displayInfo('A', "\n解析数据文件完成\n# 注意：在退出请选择是否保存报告或数据")

            elif tabLable == "控制网":
                measureNetData, filePath = FileMsg(self.centralwidget).openFile()
                # 显示文件信息
                self.showPan(os.path.dirname(os.path.realpath(filePath)))
                # 显示到监控区域
                self.textEdit_status.append("--【CASA in2 测量数据】--\n")
                self.textEdit_status.append(" 1.文件路径：" + filePath + "\n")
                self.textEdit_status.append(" 2.数据：\n")
                self.textEditFormatAdd(measureNetData)
                # 存入数据库
                Database.COSAControlNetMersureData = measureNetData
            elif tabLable == "稳定点组":
                # 界面重构存储区域
                self.stablePointGroupFileDialog_ui.setupUi(self.stablePointGroupDialog)
                self.stablePointGroupDialog.setWindowModality(QtCore.Qt.ApplicationModal)
                self.stablePointGroupDialog.show()
            elif tabLable == "单点定位(SPP)":
                # 界面重构存储区域
                fileNameList, filter = QtWidgets.QFileDialog.getOpenFileNames(self.centralwidget, "导入观测文件与导航电文",
                                                                              Database.default_workspace,
                                                                              "All Files(*)")
                # self.displayInfo("I",str(fileNameList))
                # 存入数据库
                if len(fileNameList) > 0:
                    dir, fileName = os.path.split(fileNameList[0])
                    self.showPan(dir)
                    Database().setSppFilePath(fileNameList)
                    self.displayInfo("I", "文件过滤筛选：" + str(Database().getSppFilePath("sp3")) + str(
                        Database().getSppFilePath("n")))
                    # 数据显示
                    self.sppWight_ui.setFileInfo()
            elif tabLable == "单点定位(PPP)":
                # 界面重构存储区域
                fileNameList, filter = QtWidgets.QFileDialog.getOpenFileNames(self.centralwidget, "导入观测文件与SP3文件",
                                                                              Database.default_workspace,
                                                                              "All Files(*)")
                # self.displayInfo("I",str(fileNameList))
                # 存入数据库
                if len(fileNameList) > 0:
                    dir, fileName = os.path.split(fileNameList[0])
                    self.showPan(dir)
                    Database().setPppFilePath(fileNameList)
                    self.displayInfo("I", "文件过滤筛选：" + str(Database.oFilePathList) + str(
                        Database.sp3FilePathList))
                    # 数据显示
                    self.pppWight_ui.setFileInfo()
            else:
                ActionWarnException(self.centralwidget).actionWarnException("W", "请先选择相应的功能！")
        except Exception as e:
            self.displayInfo("E", e.__str__())

    def setOpenFileInfo(self, typeInt, dirPath):
        """
        导入坐标文件信息监控
        :param typeInt: 文件类型
        :return:None
        """
        self.textEdit_status.append("导入文件....")
        self.textEdit_status.append("数据如下：")
        if typeInt == 0:
            self.textEdit_status.append("---【原始坐标文件】---")
            self.textEdit_status.append(str(Database.coorTranSourceData))
            self.showPan(dirPath)
        else:
            self.textEdit_status.append("---【目标坐标文件】---")
            self.textEdit_status.append(str(Database.coorTranTargetData))

    def setOpenFileInfo_stable(self, typeInt, dirPath):
        """
        导入坐标文件信息监控
        :param typeInt: 文件类型
        :return:None
        """
        self.textEdit_status.append("导入文件....")
        self.textEdit_status.append("数据如下：")
        if typeInt == 0:
            self.textEdit_status.append("---【一期观测坐标文件】---")
            self.textEdit_status.append(str(Database.stableDotGroupMeasure_I))
            self.showPan(dirPath)
        else:
            self.textEdit_status.append("---【二期观测坐标文件】---")
            self.textEdit_status.append(str(Database.stableDotGroupMeasure_I))

    def stableDotGroupTable(self):
        """
        稳定点组文件导入窗口关闭事件
        :return:
        """
        print("已收到信号")
        # 关闭窗体
        self.stablePointGroupDialog.close()
        # 设定表格数据
        self.stablePointGroupWight_ui.setTableData()

    def saveReport(self):
        # 从选择判断当前执行的操作
        tabIndex = self.tabWidget.currentIndex()
        tabLabel = self.tabWidget.tabText(tabIndex)
        # 第一标签页
        try:
            if tabIndex == 0:
                if tabLabel == "坐标转换":
                    self.textEdit_status.append("坐标转换报告导出中....")
                    # 从数据库获取结果
                    resultDict = Database.coorTranResultDict
                    resultFormatList = Database.coorTranResultFormatListData

                    # 获取保存的文件路径/文件名
                    filePath = FileMsg(self.centralwidget).getWriteFilePath("txt")
                    self.report = Report("C", filePath, resultDict, resultFormatList)
                    self.report.start()
                elif tabLabel == "电子手簿":
                    """
                    # 徕卡数据
                    """
                    measureINFO, stationId, stationRemark, dataItemCell = self.leicaDataFormat_ui.saveTable()
                    # 获取状态栏的输出的文本
                    statusText = self.textEdit_status.toPlainText()
                    index = 0
                    for i in range(len(statusText)):
                        if statusText[i].strip() == "~":
                            index = i
                            break
                    statusText = statusText[index + 1:]

                    filePath = FileMsg(self.centralwidget).getWriteFilePath("docx")

                    if filePath != "":
                        self.report = Report("L", filePath, measureINFO, stationId, stationRemark, dataItemCell,
                                             statusText)
                        self.report.start()
                        # 结束弹窗
                        ActionWarnException(self.centralwidget).actionWarnException("A",
                                                                                    "【" + tabLabel + "】" + "报告导出中，文件转码时间\n较长，请耐心等待！")
                        self.textEdit_status.append("【" + tabLabel + "】" + "报告导出中，文件转码时间较长，请耐心等待！完成后将在指定目录生成")
                    else:
                        ActionWarnException(self.centralwidget).actionWarnException("A", "已取消导出操作。")
                elif tabLabel == "控制网":  # 平面控制网
                    text = self.controlNetAdjustment_ui.getTextEditText()
                    FileMsg(self.centralwidget).writeFile("txt", text)
                    ActionWarnException(self.centralwidget).actionWarnException("A", "已导出计算数据。")
                elif tabLabel == "稳定点组":
                    text = self.stablePointGroupWight_ui.getTextEdit()
                    FileMsg(self.centralwidget).writeFile("txt", text)
                    ActionWarnException(self.centralwidget).actionWarnException("I", "已导出稳定点组解算报告。")
                elif tabLabel == "单点定位(SPP)" or tabLabel == "单点定位(PPP)":
                    # 用户打开文件保存界面
                    filePath, ok = QtWidgets.QFileDialog.getSaveFileName(self.centralwidget, "导出报告", Database.workspace,
                                                                         "Text Files (*.txt)")
                    if filePath != "":
                        # 从数据库获取数据
                        dataFrame = Database.stationPositionDataFrame
                        textReport = Database.stationPositionReport

                        dir, fileName = os.path.split(filePath)
                        self.showPan(dir)
                        # 获取文件名
                        [name, type] = fileName.split(".")
                        # 写入Txt报告
                        with open(filePath, "w", encoding="utf-8") as txtFile:
                            txtFile.flush()  # 缓冲区
                            for line in textReport:
                                txtFile.write(line)
                            os.fsync(txtFile)
                            txtFile.close()
                        dataFrame.to_html(dir + "/" + name + ".html")
                        self.displayInfo("T", "已导出{}的解算报告.保存路径为：{}/.html".format(tabLabel, filePath))
                # 写入内存
                else:
                    self.displayInfo("A", "当前所进行的操作无需本功能的支持。")


        except Exception as e:
            self.displayInfo("W", "错误！可能原因：\n 1.没有任何需要导出的数据；\n2. " + e.__str__())

    def onlineHelp(self):
        self.tabWidget.setCurrentIndex(3)
        self.helpSub = QtWidgets.QMdiSubWindow()
        # 实例化多文档界面对象
        # 设置新建子窗口的标题
        self.helpSub.setWindowTitle('在线帮助')
        # self.verticalLayout_more.addWidget(self.sub,wight)
        self.qwebengine = QWebEngineView(self.helpSub)
        # 设置网页在窗口中显示的位置和大小
        self.qwebengine.setGeometry(0, 0, self.helpSub.width() + 1000, self.helpSub.height() + 500)
        # 在QWebEngineView中加载网址
        self.qwebengine.load(QUrl("https://www.ganahe.top/"))
        # 将子窗口添加到Mdi区域
        self.mdiArea.addSubWindow(self.helpSub)
        self.qwebengine.show()
        self.helpSub.show()

    def textEditFormatAdd(self, twoDissList):
        listLen = len(twoDissList)
        if listLen == 0:
            return False
        else:
            for i in range(len(twoDissList)):
                self.textEdit_status.append(str(twoDissList[i]))

    def actionMenuItem_fileStatusBar(self):
        stat = self.munuItem_fileStatusBar.isChecked()
        if stat:  # 选中状态
            self.dockWidget_File.show()
        else:  # 取消选择状态
            self.dockWidget_File.setVisible(False)

    def actionMenuItem_statusBar(self):
        stat = self.munuItem_statusBar.isChecked()
        if stat:  # 选中状态
            self.dockWidget_status.show()
        else:  # 取消选择状态
            self.dockWidget_status.setVisible(False)

    def dockWight_fileStatusCloseEvent(self):
        self.munuItem_fileStatusBar.setChecked(False)

    def dockWight_statusCloseEvent(self):
        self.munuItem_statusBar.setChecked(False)
