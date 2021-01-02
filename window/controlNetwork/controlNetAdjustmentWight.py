# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controlNetAdjustmentWight.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from database.database import Database
from window.controlNetwork.actionControlNet import ActionTwoDissControlNet


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(774, 551)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("./source/icon/designer-tools.png"))
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout_6.addWidget(self.tableWidget)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(400, 0))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_4.addWidget(self.textEdit)
        self.verticalLayout_7.addWidget(self.groupBox_3)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.retranslateUi(Form)

        self.actionTwoDissControlNet = ActionTwoDissControlNet()
        self.pushButton.clicked.connect(self.controlNetAdjustment)
        self.actionTwoDissControlNet.infoEmit.connect(self.textEdit.append)
        self.actionTwoDissControlNet.overEmit.connect(self.actionTwoDissControlNet.killThead)

        self.pushButton_2.clicked.connect(self.textEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "操作"))
        self.comboBox.setItemText(0, _translate("Form", "单位权"))
        self.comboBox.setItemText(1, _translate("Form", "按距离定权"))
        self.comboBox.setItemText(2, _translate("Form", "自定义(表格定义)"))
        self.pushButton.setText(_translate("Form", "网平差解算"))
        self.pushButton_2.setText(_translate("Form", "清空"))
        self.pushButton_4.setText(_translate("Form", "平面网视图"))
        self.groupBox_2.setTitle(_translate("Form", "定权"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "A"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "B"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "B"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "D"))
        self.groupBox_3.setTitle(_translate("Form", "解算过程"))

    def controlNetAdjustment(self):
        self.actionTwoDissControlNet.setParaEmit.emit(1)
        # print("开始了")
        self.actionTwoDissControlNet.start()

    def setSourceData(self):
        self.textEdit.append(Database.COSAControlNetMersureData)

    def getTextEditText(self):
        return self.textEdit.toPlainText()
