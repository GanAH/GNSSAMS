# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inversionGravityFieldWight.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from database.database import Database
from window.geodeticSurvey import actionInversionGravityFieldThread
from window.tipDig import ActionWarnException


class Ui_Form(QtCore.QObject):
    infoEmit = QtCore.pyqtSignal(str, str)
    filePath = None
    lineLenght = 0
    nowN = 0
    thread_status = 0

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1167, 768)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./source/icon/bance.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setMaximumSize(QtCore.QSize(300, 450))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setMinimum(2)
        self.spinBox.setMaximum(5000)
        self.spinBox.setProperty("value", 180)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_5.addWidget(self.spinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.radioButton_local = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_local.setObjectName("radioButton_local")
        self.verticalLayout_2.addWidget(self.radioButton_local)
        self.radioButton_world = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_world.setObjectName("radioButton_world")
        self.verticalLayout_2.addWidget(self.radioButton_world)
        self.radioButton_satelliteOrbit = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_satelliteOrbit.setCheckable(True)
        self.radioButton_satelliteOrbit.setChecked(False)
        self.radioButton_satelliteOrbit.setObjectName("radioButton_satelliteOrbit")
        self.verticalLayout_2.addWidget(self.radioButton_satelliteOrbit)
        self.radioButton_lowerOrbitSatellite = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_lowerOrbitSatellite.setObjectName("radioButton_lowerOrbitSatellite")
        self.verticalLayout_2.addWidget(self.radioButton_lowerOrbitSatellite)
        self.radioButton_other = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_other.setObjectName("radioButton_other")
        self.verticalLayout_2.addWidget(self.radioButton_other)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_inversion = QtWidgets.QPushButton(self.groupBox)
        self.button_inversion.setObjectName("button_inversion")
        self.horizontalLayout.addWidget(self.button_inversion)
        self.button_stop = QtWidgets.QPushButton(self.groupBox)
        self.button_stop.setObjectName("button_stop")
        self.horizontalLayout.addWidget(self.button_stop)
        self.button_clear = QtWidgets.QPushButton(self.groupBox)
        self.button_clear.setObjectName("button_clear")
        self.horizontalLayout.addWidget(self.button_clear)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./source/icon/earth.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_m = QtWidgets.QLabel(self.groupBox_2)
        self.label_m.setAlignment(QtCore.Qt.AlignCenter)
        self.label_m.setObjectName("label_m")
        self.verticalLayout.addWidget(self.label_m)
        self.progressBar_m = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar_m.setProperty("value", 20)
        self.progressBar_m.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_m.setObjectName("progressBar_m")
        self.verticalLayout.addWidget(self.progressBar_m)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_n = QtWidgets.QLabel(self.groupBox_2)
        self.label_n.setAlignment(QtCore.Qt.AlignCenter)
        self.label_n.setObjectName("label_n")
        self.verticalLayout_3.addWidget(self.label_n)
        self.progressBar_n = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar_n.setProperty("value", 0)
        self.progressBar_n.setTextVisible(True)
        self.progressBar_n.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_n.setInvertedAppearance(False)
        self.progressBar_n.setObjectName("progressBar_n")
        self.verticalLayout_3.addWidget(self.progressBar_n)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addWidget(self.groupBox_2)

        self.retranslateUi(Form)
        # setDefault
        self.radioButton_world.setChecked(True)
        self.checkBox.setChecked(True)
        self.radioButton_local.clicked.connect(self.actionRadioButton)
        self.radioButton_world.clicked.connect(self.actionRadioButton)
        self.radioButton_satelliteOrbit.clicked.connect(self.actionRadioButton)
        self.radioButton_lowerOrbitSatellite.clicked.connect(self.actionRadioButton)
        self.radioButton_other.clicked.connect(self.actionRadioButton)

        self.button_inversion.clicked.connect(self.startInversionGravityFiled)
        self.button_clear.clicked.connect(self.textEdit.clear)
        self.button_stop.clicked.connect(self.violenceStop)

        self.cacuThread = actionInversionGravityFieldThread.ActionInversionGravityField()
        self.cacuThread.infoEmit.connect(self.sendTopInfo)
        self.cacuThread.overEmit.connect(self.killCacuThread)
        self.cacuThread.processEmit.connect(self.setProcess)
        self.cacuThread.stopEmit.connect(self.cacuThread.setStop)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "操作"))
        self.label_2.setText(_translate("Form", "反演最大阶："))
        self.checkBox.setText(_translate("Form", "保存模型到工作空间"))
        self.radioButton_local.setText(_translate("Form", "区域重力异常数据反演"))
        self.radioButton_world.setText(_translate("Form", "全球重力异常数据反演"))
        self.radioButton_satelliteOrbit.setText(_translate("Form", "重力卫星轨道和梯度数据反演"))
        self.radioButton_lowerOrbitSatellite.setText(_translate("Form", "GRACE卫星等低轨卫星跟踪数据反演"))
        self.radioButton_other.setText(_translate("Form", "其他反演手段"))
        self.button_inversion.setText(_translate("Form", "反演重力场"))
        self.button_stop.setText(_translate("Form", "强制终止"))
        self.button_clear.setText(_translate("Form", "清空"))
        self.groupBox_2.setTitle(_translate("Form", "信息"))
        self.label_m.setText(_translate("Form", "0"))
        self.label_4.setText(_translate("Form", "m"))
        self.label_n.setText(_translate("Form", "0"))
        self.label_3.setText(_translate("Form", "n"))

    def actionRadioButton(self):
        if self.radioButton_world.isChecked():
            pass
        else:
            self.sendTopInfo("T", "当前功能尚未开发！")

    def sendTopInfo(self, type, strInfo):
        if type == "G":
            self.textEdit.append(strInfo)
            if self.lineLenght > 100:
                self.textEdit.clear()
        else:
            self.infoEmit.emit(type, strInfo)

    def setProcess(self, m, n):
        # 打开窗口
        self.progressBar_m.setMaximum(n)
        self.progressBar_m.setValue(m)
        self.label_m.setText("{}/{}".format(m, n))
        if self.nowN != n:
            self.label_m.setText("{}/{}".format(n, int(self.spinBox.text())))
            self.progressBar_n.setValue(n)
            self.nowN = n

    def startInversionGravityFiled(self):

        # 从数据库获取文件路径
        if Database.inversionGroupFilePath is None:
            self.sendTopInfo("T", "未选择反演方法并导入数据")
        else:
            # 判断选择的方法
            if self.radioButton_local.isChecked():
                controlCode = 100
            elif self.radioButton_world.isChecked():
                controlCode = 101
            elif self.radioButton_satelliteOrbit.isChecked():
                controlCode = 102
            elif self.radioButton_lowerOrbitSatellite.isChecked():
                controlCode = 103
            else:
                controlCode = 104
            # 设置线程参数
            paraDict = {"code": controlCode,
                        "filePath": Database.inversionGroupFilePath,
                        "autoSave": self.checkBox.isChecked(),
                        "N": int(self.spinBox.text())}
            self.cacuThread.setPara(paraDict)
            self.progressBar_n.setMaximum(paraDict["N"])
            self.label_n.setText("{}/{}".format(0, paraDict["N"]))
            # 开启线程
            self.cacuThread.start()
            self.thread_status = 1
            self.sendTopInfo("I", "子线程已启动，准备进行重力场模型反演...")

    def violenceStop(self):
        if self.thread_status == 1:
            reply = ActionWarnException(self.parent()).actionWarnException("R", "执行该操作将终止当前反演进程！是否继续？")
            if reply:
                self.cacuThread.stopEmit.emit()

    def killCacuThread(self):
        self.cacuThread.killThread()
        self.thread_status = 0
        self.sendTopInfo("I", "已关闭重力场模型反演线程")