# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pdManager_v2_UI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

# from PyQt4 import QtCore, QtGui
from PySide import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_pdManager_MainWindow(object):
    def setupUi(self, pdManager_MainWindow):
        pdManager_MainWindow.setObjectName(_fromUtf8("pdManager_MainWindow"))
        pdManager_MainWindow.resize(975, 861)
        pdManager_MainWindow.setToolTip(_fromUtf8(""))
        pdManager_MainWindow.setStatusTip(_fromUtf8(""))
        pdManager_MainWindow.setWhatsThis(_fromUtf8(""))
        pdManager_MainWindow.setAccessibleName(_fromUtf8(""))
        pdManager_MainWindow.setAccessibleDescription(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(pdManager_MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.setProject_pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.setProject_pushButton_3.setMinimumSize(QtCore.QSize(150, 45))
        self.setProject_pushButton_3.setMaximumSize(QtCore.QSize(150, 45))
        self.setProject_pushButton_3.setToolTip(_fromUtf8(""))
        self.setProject_pushButton_3.setStatusTip(_fromUtf8(""))
        self.setProject_pushButton_3.setWhatsThis(_fromUtf8(""))
        self.setProject_pushButton_3.setAccessibleName(_fromUtf8(""))
        self.setProject_pushButton_3.setAccessibleDescription(_fromUtf8(""))
        self.setProject_pushButton_3.setText(_fromUtf8("Save As Version"))
        self.setProject_pushButton_3.setObjectName(_fromUtf8("setProject_pushButton_3"))
        self.horizontalLayout.addWidget(self.setProject_pushButton_3)
        self.setProject_pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.setProject_pushButton_2.setMinimumSize(QtCore.QSize(150, 45))
        self.setProject_pushButton_2.setMaximumSize(QtCore.QSize(150, 45))
        self.setProject_pushButton_2.setToolTip(_fromUtf8(""))
        self.setProject_pushButton_2.setStatusTip(_fromUtf8(""))
        self.setProject_pushButton_2.setWhatsThis(_fromUtf8(""))
        self.setProject_pushButton_2.setAccessibleName(_fromUtf8(""))
        self.setProject_pushButton_2.setAccessibleDescription(_fromUtf8(""))
        self.setProject_pushButton_2.setText(_fromUtf8("Save Base Scene"))
        self.setProject_pushButton_2.setObjectName(_fromUtf8("setProject_pushButton_2"))
        self.horizontalLayout.addWidget(self.setProject_pushButton_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.setProject_pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.setProject_pushButton_4.setMinimumSize(QtCore.QSize(150, 45))
        self.setProject_pushButton_4.setMaximumSize(QtCore.QSize(150, 45))
        self.setProject_pushButton_4.setToolTip(_fromUtf8(""))
        self.setProject_pushButton_4.setStatusTip(_fromUtf8(""))
        self.setProject_pushButton_4.setWhatsThis(_fromUtf8(""))
        self.setProject_pushButton_4.setAccessibleName(_fromUtf8(""))
        self.setProject_pushButton_4.setAccessibleDescription(_fromUtf8(""))
        self.setProject_pushButton_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setProject_pushButton_4.setText(_fromUtf8("Load Scene"))
        self.setProject_pushButton_4.setObjectName(_fromUtf8("setProject_pushButton_4"))
        self.horizontalLayout.addWidget(self.setProject_pushButton_4)
        self.horizontalLayout.setStretch(0, 1)
        self.gridLayout_3.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.load_radioButton = QtGui.QRadioButton(self.centralwidget)
        self.load_radioButton.setToolTip(_fromUtf8(""))
        self.load_radioButton.setStatusTip(_fromUtf8(""))
        self.load_radioButton.setWhatsThis(_fromUtf8(""))
        self.load_radioButton.setAccessibleName(_fromUtf8(""))
        self.load_radioButton.setAccessibleDescription(_fromUtf8(""))
        self.load_radioButton.setText(_fromUtf8("Load Mode"))
        self.load_radioButton.setChecked(False)
        self.load_radioButton.setObjectName(_fromUtf8("load_radioButton"))
        self.gridLayout_2.addWidget(self.load_radioButton, 0, 0, 1, 1)
        self.subProject_label = QtGui.QLabel(self.centralwidget)
        self.subProject_label.setToolTip(_fromUtf8(""))
        self.subProject_label.setStatusTip(_fromUtf8(""))
        self.subProject_label.setWhatsThis(_fromUtf8(""))
        self.subProject_label.setAccessibleName(_fromUtf8(""))
        self.subProject_label.setAccessibleDescription(_fromUtf8(""))
        self.subProject_label.setText(_fromUtf8("Sub-Project:"))
        self.subProject_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.subProject_label.setObjectName(_fromUtf8("subProject_label"))
        self.gridLayout_2.addWidget(self.subProject_label, 0, 2, 1, 1)
        self.subProject_comboBox = QtGui.QComboBox(self.centralwidget)
        self.subProject_comboBox.setMinimumSize(QtCore.QSize(150, 30))
        self.subProject_comboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.subProject_comboBox.setToolTip(_fromUtf8(""))
        self.subProject_comboBox.setStatusTip(_fromUtf8(""))
        self.subProject_comboBox.setWhatsThis(_fromUtf8(""))
        self.subProject_comboBox.setAccessibleName(_fromUtf8(""))
        self.subProject_comboBox.setAccessibleDescription(_fromUtf8(""))
        self.subProject_comboBox.setObjectName(_fromUtf8("subProject_comboBox"))
        self.gridLayout_2.addWidget(self.subProject_comboBox, 0, 3, 1, 1)
        self.reference_radioButton = QtGui.QRadioButton(self.centralwidget)
        self.reference_radioButton.setToolTip(_fromUtf8(""))
        self.reference_radioButton.setStatusTip(_fromUtf8(""))
        self.reference_radioButton.setWhatsThis(_fromUtf8(""))
        self.reference_radioButton.setAccessibleName(_fromUtf8(""))
        self.reference_radioButton.setAccessibleDescription(_fromUtf8(""))
        self.reference_radioButton.setText(_fromUtf8("Reference Mode"))
        self.reference_radioButton.setChecked(True)
        self.reference_radioButton.setObjectName(_fromUtf8("reference_radioButton"))
        self.gridLayout_2.addWidget(self.reference_radioButton, 0, 1, 1, 1)
        self.addSubProject_pushButton = QtGui.QPushButton(self.centralwidget)
        self.addSubProject_pushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.addSubProject_pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.addSubProject_pushButton.setToolTip(_fromUtf8(""))
        self.addSubProject_pushButton.setStatusTip(_fromUtf8(""))
        self.addSubProject_pushButton.setWhatsThis(_fromUtf8(""))
        self.addSubProject_pushButton.setAccessibleName(_fromUtf8(""))
        self.addSubProject_pushButton.setAccessibleDescription(_fromUtf8(""))
        self.addSubProject_pushButton.setText(_fromUtf8("+"))
        self.addSubProject_pushButton.setObjectName(_fromUtf8("addSubProject_pushButton"))
        self.gridLayout_2.addWidget(self.addSubProject_pushButton, 0, 4, 1, 1)
        self.user_label = QtGui.QLabel(self.centralwidget)
        self.user_label.setToolTip(_fromUtf8(""))
        self.user_label.setStatusTip(_fromUtf8(""))
        self.user_label.setWhatsThis(_fromUtf8(""))
        self.user_label.setAccessibleName(_fromUtf8(""))
        self.user_label.setAccessibleDescription(_fromUtf8(""))
        self.user_label.setText(_fromUtf8("User:"))
        self.user_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.user_label.setObjectName(_fromUtf8("user_label"))
        self.gridLayout_2.addWidget(self.user_label, 0, 5, 1, 1)
        self.user_comboBox = QtGui.QComboBox(self.centralwidget)
        self.user_comboBox.setMinimumSize(QtCore.QSize(130, 30))
        self.user_comboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.user_comboBox.setToolTip(_fromUtf8(""))
        self.user_comboBox.setStatusTip(_fromUtf8(""))
        self.user_comboBox.setWhatsThis(_fromUtf8(""))
        self.user_comboBox.setAccessibleName(_fromUtf8(""))
        self.user_comboBox.setAccessibleDescription(_fromUtf8(""))
        self.user_comboBox.setObjectName(_fromUtf8("user_comboBox"))
        self.gridLayout_2.addWidget(self.user_comboBox, 0, 6, 1, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.baseScene_label = QtGui.QLabel(self.centralwidget)
        self.baseScene_label.setToolTip(_fromUtf8(""))
        self.baseScene_label.setStatusTip(_fromUtf8(""))
        self.baseScene_label.setWhatsThis(_fromUtf8(""))
        self.baseScene_label.setAccessibleName(_fromUtf8(""))
        self.baseScene_label.setAccessibleDescription(_fromUtf8(""))
        self.baseScene_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.baseScene_label.setText(_fromUtf8("Base Scene:"))
        self.baseScene_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.baseScene_label.setObjectName(_fromUtf8("baseScene_label"))
        self.gridLayout.addWidget(self.baseScene_label, 0, 0, 1, 1)
        self.baseScene_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.baseScene_lineEdit.setToolTip(_fromUtf8(""))
        self.baseScene_lineEdit.setStatusTip(_fromUtf8(""))
        self.baseScene_lineEdit.setWhatsThis(_fromUtf8(""))
        self.baseScene_lineEdit.setAccessibleName(_fromUtf8(""))
        self.baseScene_lineEdit.setAccessibleDescription(_fromUtf8(""))
        self.baseScene_lineEdit.setInputMask(_fromUtf8(""))
        self.baseScene_lineEdit.setText(_fromUtf8(""))
        self.baseScene_lineEdit.setPlaceholderText(_fromUtf8(""))
        self.baseScene_lineEdit.setObjectName(_fromUtf8("baseScene_lineEdit"))
        self.gridLayout.addWidget(self.baseScene_lineEdit, 0, 1, 1, 1)
        self.project_label = QtGui.QLabel(self.centralwidget)
        self.project_label.setToolTip(_fromUtf8(""))
        self.project_label.setStatusTip(_fromUtf8(""))
        self.project_label.setWhatsThis(_fromUtf8(""))
        self.project_label.setAccessibleName(_fromUtf8(""))
        self.project_label.setAccessibleDescription(_fromUtf8(""))
        self.project_label.setText(_fromUtf8("Project:"))
        self.project_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.project_label.setObjectName(_fromUtf8("project_label"))
        self.gridLayout.addWidget(self.project_label, 1, 0, 1, 1)
        self.project_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.project_lineEdit.setToolTip(_fromUtf8(""))
        self.project_lineEdit.setStatusTip(_fromUtf8(""))
        self.project_lineEdit.setWhatsThis(_fromUtf8(""))
        self.project_lineEdit.setAccessibleName(_fromUtf8(""))
        self.project_lineEdit.setAccessibleDescription(_fromUtf8(""))
        self.project_lineEdit.setInputMask(_fromUtf8(""))
        self.project_lineEdit.setText(_fromUtf8(""))
        self.project_lineEdit.setPlaceholderText(_fromUtf8(""))
        self.project_lineEdit.setObjectName(_fromUtf8("project_lineEdit"))
        self.gridLayout.addWidget(self.project_lineEdit, 1, 1, 1, 1)
        self.setProject_pushButton = QtGui.QPushButton(self.centralwidget)
        self.setProject_pushButton.setToolTip(_fromUtf8(""))
        self.setProject_pushButton.setStatusTip(_fromUtf8(""))
        self.setProject_pushButton.setWhatsThis(_fromUtf8(""))
        self.setProject_pushButton.setAccessibleName(_fromUtf8(""))
        self.setProject_pushButton.setAccessibleDescription(_fromUtf8(""))
        self.setProject_pushButton.setText(_fromUtf8("SET"))
        self.setProject_pushButton.setObjectName(_fromUtf8("setProject_pushButton"))
        self.gridLayout.addWidget(self.setProject_pushButton, 1, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 22))
        self.tabWidget.setToolTip(_fromUtf8(""))
        self.tabWidget.setStatusTip(_fromUtf8(""))
        self.tabWidget.setWhatsThis(_fromUtf8(""))
        self.tabWidget.setAccessibleName(_fromUtf8(""))
        self.tabWidget.setAccessibleDescription(_fromUtf8(""))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab)
        self.gridLayout_4.setContentsMargins(9, -1, -1, -1)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget, 2, 0, 1, 1)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setToolTip(_fromUtf8(""))
        self.splitter.setStatusTip(_fromUtf8(""))
        self.splitter.setWhatsThis(_fromUtf8(""))
        self.splitter.setAccessibleName(_fromUtf8(""))
        self.splitter.setAccessibleDescription(_fromUtf8(""))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.listWidget = QtGui.QListWidget(self.splitter)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.frame = QtGui.QFrame(self.splitter)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_6 = QtGui.QGridLayout(self.frame)
        self.gridLayout_6.setContentsMargins(-1, -1, 0, 0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.version_label_2 = QtGui.QLabel(self.frame)
        self.version_label_2.setToolTip(_fromUtf8(""))
        self.version_label_2.setStatusTip(_fromUtf8(""))
        self.version_label_2.setWhatsThis(_fromUtf8(""))
        self.version_label_2.setAccessibleName(_fromUtf8(""))
        self.version_label_2.setAccessibleDescription(_fromUtf8(""))
        self.version_label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.version_label_2.setText(_fromUtf8("Version Notes:"))
        self.version_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.version_label_2.setObjectName(_fromUtf8("version_label_2"))
        self.verticalLayout.addWidget(self.version_label_2)
        self.textEdit = QtGui.QTextEdit(self.frame)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.label = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(221, 124))
        self.label.setMaximumSize(QtCore.QSize(884, 496))
        self.label.setSizeIncrement(QtCore.QSize(1, 1))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        self.label.setToolTip(_fromUtf8(""))
        self.label.setStatusTip(_fromUtf8(""))
        self.label.setWhatsThis(_fromUtf8(""))
        self.label.setAccessibleName(_fromUtf8(""))
        self.label.setAccessibleDescription(_fromUtf8(""))
        self.label.setFrameShape(QtGui.QFrame.Box)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.gridLayout_6.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setContentsMargins(-1, -1, 10, 10)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.setProject_pushButton_5 = QtGui.QPushButton(self.frame)
        self.setProject_pushButton_5.setMinimumSize(QtCore.QSize(100, 30))
        self.setProject_pushButton_5.setMaximumSize(QtCore.QSize(150, 30))
        self.setProject_pushButton_5.setToolTip(_fromUtf8(""))
        self.setProject_pushButton_5.setStatusTip(_fromUtf8(""))
        self.setProject_pushButton_5.setWhatsThis(_fromUtf8(""))
        self.setProject_pushButton_5.setAccessibleName(_fromUtf8(""))
        self.setProject_pushButton_5.setAccessibleDescription(_fromUtf8(""))
        self.setProject_pushButton_5.setText(_fromUtf8("Show Preview"))
        self.setProject_pushButton_5.setObjectName(_fromUtf8("setProject_pushButton_5"))
        self.gridLayout_7.addWidget(self.setProject_pushButton_5, 0, 3, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.version_label = QtGui.QLabel(self.frame)
        self.version_label.setMinimumSize(QtCore.QSize(60, 30))
        self.version_label.setMaximumSize(QtCore.QSize(60, 30))
        self.version_label.setToolTip(_fromUtf8(""))
        self.version_label.setStatusTip(_fromUtf8(""))
        self.version_label.setWhatsThis(_fromUtf8(""))
        self.version_label.setAccessibleName(_fromUtf8(""))
        self.version_label.setAccessibleDescription(_fromUtf8(""))
        self.version_label.setFrameShape(QtGui.QFrame.Box)
        self.version_label.setText(_fromUtf8("Version:"))
        self.version_label.setAlignment(QtCore.Qt.AlignCenter)
        self.version_label.setObjectName(_fromUtf8("version_label"))
        self.horizontalLayout_4.addWidget(self.version_label)
        self.version_comboBox = QtGui.QComboBox(self.frame)
        self.version_comboBox.setMinimumSize(QtCore.QSize(60, 30))
        self.version_comboBox.setMaximumSize(QtCore.QSize(100, 30))
        self.version_comboBox.setToolTip(_fromUtf8(""))
        self.version_comboBox.setStatusTip(_fromUtf8(""))
        self.version_comboBox.setWhatsThis(_fromUtf8(""))
        self.version_comboBox.setAccessibleName(_fromUtf8(""))
        self.version_comboBox.setAccessibleDescription(_fromUtf8(""))
        self.version_comboBox.setObjectName(_fromUtf8("version_comboBox"))
        self.horizontalLayout_4.addWidget(self.version_comboBox)
        self.gridLayout_7.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.setProject_pushButton_6 = QtGui.QPushButton(self.frame)
        self.setProject_pushButton_6.setMinimumSize(QtCore.QSize(100, 30))
        self.setProject_pushButton_6.setMaximumSize(QtCore.QSize(300, 30))
        self.setProject_pushButton_6.setToolTip(_fromUtf8(""))
        self.setProject_pushButton_6.setStatusTip(_fromUtf8(""))
        self.setProject_pushButton_6.setWhatsThis(_fromUtf8(""))
        self.setProject_pushButton_6.setAccessibleName(_fromUtf8(""))
        self.setProject_pushButton_6.setAccessibleDescription(_fromUtf8(""))
        self.setProject_pushButton_6.setText(_fromUtf8("Make Reference"))
        self.setProject_pushButton_6.setObjectName(_fromUtf8("setProject_pushButton_6"))
        self.gridLayout_7.addWidget(self.setProject_pushButton_6, 1, 0, 1, 1)
        self.setProject_pushButton_7 = QtGui.QPushButton(self.frame)
        self.setProject_pushButton_7.setMinimumSize(QtCore.QSize(100, 30))
        self.setProject_pushButton_7.setMaximumSize(QtCore.QSize(150, 30))
        self.setProject_pushButton_7.setToolTip(_fromUtf8(""))
        self.setProject_pushButton_7.setStatusTip(_fromUtf8(""))
        self.setProject_pushButton_7.setWhatsThis(_fromUtf8(""))
        self.setProject_pushButton_7.setAccessibleName(_fromUtf8(""))
        self.setProject_pushButton_7.setAccessibleDescription(_fromUtf8(""))
        self.setProject_pushButton_7.setText(_fromUtf8("Add Note"))
        self.setProject_pushButton_7.setObjectName(_fromUtf8("setProject_pushButton_7"))
        self.gridLayout_7.addWidget(self.setProject_pushButton_7, 1, 3, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.splitter, 3, 0, 1, 1)
        pdManager_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(pdManager_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 975, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        pdManager_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(pdManager_MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        pdManager_MainWindow.setStatusBar(self.statusbar)
        self.actionCreate_Project = QtGui.QAction(pdManager_MainWindow)
        self.actionCreate_Project.setObjectName(_fromUtf8("actionCreate_Project"))
        self.actionSave_Version = QtGui.QAction(pdManager_MainWindow)
        self.actionSave_Version.setObjectName(_fromUtf8("actionSave_Version"))
        self.actionSave_Base_Scene = QtGui.QAction(pdManager_MainWindow)
        self.actionSave_Base_Scene.setObjectName(_fromUtf8("actionSave_Base_Scene"))
        self.actionLoad_Reference_Scene = QtGui.QAction(pdManager_MainWindow)
        self.actionLoad_Reference_Scene.setObjectName(_fromUtf8("actionLoad_Reference_Scene"))
        self.actionAdd_Remove_Users = QtGui.QAction(pdManager_MainWindow)
        self.actionAdd_Remove_Users.setObjectName(_fromUtf8("actionAdd_Remove_Users"))
        self.actionPreview_Settings = QtGui.QAction(pdManager_MainWindow)
        self.actionPreview_Settings.setObjectName(_fromUtf8("actionPreview_Settings"))
        self.actionDelete_Selected_Base_Scene = QtGui.QAction(pdManager_MainWindow)
        self.actionDelete_Selected_Base_Scene.setObjectName(_fromUtf8("actionDelete_Selected_Base_Scene"))
        self.actionDelete_Reference_of_Selected_Scene = QtGui.QAction(pdManager_MainWindow)
        self.actionDelete_Reference_of_Selected_Scene.setObjectName(_fromUtf8("actionDelete_Reference_of_Selected_Scene"))
        self.actionProject_Report = QtGui.QAction(pdManager_MainWindow)
        self.actionProject_Report.setObjectName(_fromUtf8("actionProject_Report"))
        self.actionCheck_References = QtGui.QAction(pdManager_MainWindow)
        self.actionCheck_References.setObjectName(_fromUtf8("actionCheck_References"))
        self.actionImage_Manager = QtGui.QAction(pdManager_MainWindow)
        self.actionImage_Manager.setObjectName(_fromUtf8("actionImage_Manager"))
        self.actionSequence_Viewer = QtGui.QAction(pdManager_MainWindow)
        self.actionSequence_Viewer.setObjectName(_fromUtf8("actionSequence_Viewer"))
        self.menuFile.addAction(self.actionCreate_Project)
        self.menuFile.addAction(self.actionSave_Version)
        self.menuFile.addAction(self.actionSave_Base_Scene)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLoad_Reference_Scene)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionAdd_Remove_Users)
        self.menuFile.addAction(self.actionPreview_Settings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionDelete_Selected_Base_Scene)
        self.menuFile.addAction(self.actionDelete_Reference_of_Selected_Scene)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionProject_Report)
        self.menuFile.addAction(self.actionCheck_References)
        self.menuTools.addAction(self.actionImage_Manager)
        self.menuTools.addAction(self.actionSequence_Viewer)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(pdManager_MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(pdManager_MainWindow)

    def retranslateUi(self, pdManager_MainWindow):
        pdManager_MainWindow.setWindowTitle(_translate("pdManager_MainWindow", "Scene Manager", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("pdManager_MainWindow", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("pdManager_MainWindow", "Tab 2", None))
        self.label.setText(_translate("pdManager_MainWindow", "TextLabel", None))
        self.menuFile.setTitle(_translate("pdManager_MainWindow", "File", None))
        self.menuTools.setTitle(_translate("pdManager_MainWindow", "Tools", None))
        self.actionCreate_Project.setText(_translate("pdManager_MainWindow", "Create Project", None))
        self.actionSave_Version.setText(_translate("pdManager_MainWindow", "Save Version", None))
        self.actionSave_Base_Scene.setText(_translate("pdManager_MainWindow", "Save Base Scene", None))
        self.actionLoad_Reference_Scene.setText(_translate("pdManager_MainWindow", "Load/Reference Scene", None))
        self.actionAdd_Remove_Users.setText(_translate("pdManager_MainWindow", "Add/Remove Users", None))
        self.actionPreview_Settings.setText(_translate("pdManager_MainWindow", "Preview Settings", None))
        self.actionDelete_Selected_Base_Scene.setText(_translate("pdManager_MainWindow", "Delete Selected Base Scene", None))
        self.actionDelete_Reference_of_Selected_Scene.setText(_translate("pdManager_MainWindow", "Delete Reference of Selected Scene", None))
        self.actionProject_Report.setText(_translate("pdManager_MainWindow", "Project Report", None))
        self.actionCheck_References.setText(_translate("pdManager_MainWindow", "Check References", None))
        self.actionImage_Manager.setText(_translate("pdManager_MainWindow", "Image Manager", None))
        self.actionSequence_Viewer.setText(_translate("pdManager_MainWindow", "Sequence Viewer", None))

r = Ui_pdManager_MainWindow()
print r