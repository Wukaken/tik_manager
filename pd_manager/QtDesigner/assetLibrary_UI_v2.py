# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assetLibrary_UI_v2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        pdManager_MainWindow.resize(735, 622)
        pdManager_MainWindow.setToolTip(_fromUtf8(""))
        pdManager_MainWindow.setStatusTip(_fromUtf8(""))
        pdManager_MainWindow.setWhatsThis(_fromUtf8(""))
        pdManager_MainWindow.setAccessibleName(_fromUtf8(""))
        pdManager_MainWindow.setAccessibleDescription(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(pdManager_MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 167777))
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
        self.bottom_horizontalLayout = QtGui.QHBoxLayout()
        self.bottom_horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.bottom_horizontalLayout.setSpacing(6)
        self.bottom_horizontalLayout.setObjectName(_fromUtf8("bottom_horizontalLayout"))
        self.createNewAsset_pushButton = QtGui.QPushButton(self.tab)
        self.createNewAsset_pushButton.setMinimumSize(QtCore.QSize(150, 45))
        self.createNewAsset_pushButton.setMaximumSize(QtCore.QSize(15000, 45))
        self.createNewAsset_pushButton.setToolTip(_fromUtf8(""))
        self.createNewAsset_pushButton.setStatusTip(_fromUtf8(""))
        self.createNewAsset_pushButton.setWhatsThis(_fromUtf8(""))
        self.createNewAsset_pushButton.setAccessibleName(_fromUtf8(""))
        self.createNewAsset_pushButton.setAccessibleDescription(_fromUtf8(""))
        self.createNewAsset_pushButton.setText(_fromUtf8("Create New Asset"))
        self.createNewAsset_pushButton.setObjectName(_fromUtf8("createNewAsset_pushButton"))
        self.bottom_horizontalLayout.addWidget(self.createNewAsset_pushButton)
        self.gridLayout_4.addLayout(self.bottom_horizontalLayout, 1, 0, 1, 1)
        self.splitter = QtGui.QSplitter(self.tab)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.frame_5 = QtGui.QFrame(self.splitter)
        self.frame_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_5.setLineWidth(0)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.gridLayout_10 = QtGui.QGridLayout(self.frame_5)
        self.gridLayout_10.setMargin(0)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.rightBelow_verticalLayout_5 = QtGui.QVBoxLayout()
        self.rightBelow_verticalLayout_5.setSpacing(0)
        self.rightBelow_verticalLayout_5.setObjectName(_fromUtf8("rightBelow_verticalLayout_5"))
        self.assets_listWidget_4 = QtGui.QListWidget(self.frame_5)
        self.assets_listWidget_4.setToolTip(_fromUtf8(""))
        self.assets_listWidget_4.setStatusTip(_fromUtf8(""))
        self.assets_listWidget_4.setWhatsThis(_fromUtf8(""))
        self.assets_listWidget_4.setAccessibleName(_fromUtf8(""))
        self.assets_listWidget_4.setAccessibleDescription(_fromUtf8(""))
        self.assets_listWidget_4.setObjectName(_fromUtf8("assets_listWidget_4"))
        self.rightBelow_verticalLayout_5.addWidget(self.assets_listWidget_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 6, -1, -1)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.filter_label_2 = QtGui.QLabel(self.frame_5)
        self.filter_label_2.setObjectName(_fromUtf8("filter_label_2"))
        self.horizontalLayout_3.addWidget(self.filter_label_2)
        self.filter_lineEdit_2 = QtGui.QLineEdit(self.frame_5)
        self.filter_lineEdit_2.setObjectName(_fromUtf8("filter_lineEdit_2"))
        self.horizontalLayout_3.addWidget(self.filter_lineEdit_2)
        self.rightBelow_verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.gridLayout_10.addLayout(self.rightBelow_verticalLayout_5, 2, 0, 1, 1)
        self.frame_6 = QtGui.QFrame(self.splitter)
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.gridLayout_11 = QtGui.QGridLayout(self.frame_6)
        self.gridLayout_11.setContentsMargins(-1, -1, 0, 0)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.rightBelow_verticalLayout_6 = QtGui.QVBoxLayout()
        self.rightBelow_verticalLayout_6.setObjectName(_fromUtf8("rightBelow_verticalLayout_6"))
        self.assetNotes_label_4 = QtGui.QLabel(self.frame_6)
        self.assetNotes_label_4.setToolTip(_fromUtf8(""))
        self.assetNotes_label_4.setStatusTip(_fromUtf8(""))
        self.assetNotes_label_4.setWhatsThis(_fromUtf8(""))
        self.assetNotes_label_4.setAccessibleName(_fromUtf8(""))
        self.assetNotes_label_4.setAccessibleDescription(_fromUtf8(""))
        self.assetNotes_label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.assetNotes_label_4.setText(_fromUtf8("Asset Notes"))
        self.assetNotes_label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.assetNotes_label_4.setObjectName(_fromUtf8("assetNotes_label_4"))
        self.rightBelow_verticalLayout_6.addWidget(self.assetNotes_label_4)
        self.notes_textEdit_4 = QtGui.QTextEdit(self.frame_6)
        self.notes_textEdit_4.setObjectName(_fromUtf8("notes_textEdit_4"))
        self.rightBelow_verticalLayout_6.addWidget(self.notes_textEdit_4)
        self.thumb_label_4 = QtGui.QLabel(self.frame_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thumb_label_4.sizePolicy().hasHeightForWidth())
        self.thumb_label_4.setSizePolicy(sizePolicy)
        self.thumb_label_4.setMinimumSize(QtCore.QSize(221, 124))
        self.thumb_label_4.setMaximumSize(QtCore.QSize(884, 496))
        self.thumb_label_4.setSizeIncrement(QtCore.QSize(1, 1))
        self.thumb_label_4.setBaseSize(QtCore.QSize(0, 0))
        self.thumb_label_4.setToolTip(_fromUtf8(""))
        self.thumb_label_4.setStatusTip(_fromUtf8(""))
        self.thumb_label_4.setWhatsThis(_fromUtf8(""))
        self.thumb_label_4.setAccessibleName(_fromUtf8(""))
        self.thumb_label_4.setAccessibleDescription(_fromUtf8(""))
        self.thumb_label_4.setFrameShape(QtGui.QFrame.Box)
        self.thumb_label_4.setScaledContents(False)
        self.thumb_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.thumb_label_4.setObjectName(_fromUtf8("thumb_label_4"))
        self.rightBelow_verticalLayout_6.addWidget(self.thumb_label_4)
        self.gridLayout_11.addLayout(self.rightBelow_verticalLayout_6, 3, 0, 1, 1)
        self.rightUp_gridLayout_4 = QtGui.QGridLayout()
        self.rightUp_gridLayout_4.setContentsMargins(-1, -1, 10, 10)
        self.rightUp_gridLayout_4.setObjectName(_fromUtf8("rightUp_gridLayout_4"))
        self.importOnly_pushButton_4 = QtGui.QPushButton(self.frame_6)
        self.importOnly_pushButton_4.setMinimumSize(QtCore.QSize(100, 30))
        self.importOnly_pushButton_4.setMaximumSize(QtCore.QSize(150, 30))
        self.importOnly_pushButton_4.setToolTip(_fromUtf8(""))
        self.importOnly_pushButton_4.setStatusTip(_fromUtf8(""))
        self.importOnly_pushButton_4.setWhatsThis(_fromUtf8(""))
        self.importOnly_pushButton_4.setAccessibleName(_fromUtf8(""))
        self.importOnly_pushButton_4.setAccessibleDescription(_fromUtf8(""))
        self.importOnly_pushButton_4.setText(_fromUtf8("Import Only"))
        self.importOnly_pushButton_4.setObjectName(_fromUtf8("importOnly_pushButton_4"))
        self.rightUp_gridLayout_4.addWidget(self.importOnly_pushButton_4, 1, 0, 1, 1)
        self.load_pushButton_4 = QtGui.QPushButton(self.frame_6)
        self.load_pushButton_4.setMinimumSize(QtCore.QSize(100, 30))
        self.load_pushButton_4.setMaximumSize(QtCore.QSize(150, 30))
        self.load_pushButton_4.setToolTip(_fromUtf8(""))
        self.load_pushButton_4.setStatusTip(_fromUtf8(""))
        self.load_pushButton_4.setWhatsThis(_fromUtf8(""))
        self.load_pushButton_4.setAccessibleName(_fromUtf8(""))
        self.load_pushButton_4.setAccessibleDescription(_fromUtf8(""))
        self.load_pushButton_4.setText(_fromUtf8("Load"))
        self.load_pushButton_4.setObjectName(_fromUtf8("load_pushButton_4"))
        self.rightUp_gridLayout_4.addWidget(self.load_pushButton_4, 0, 3, 1, 1)
        self.importObj_pushButton_4 = QtGui.QPushButton(self.frame_6)
        self.importObj_pushButton_4.setMinimumSize(QtCore.QSize(100, 30))
        self.importObj_pushButton_4.setMaximumSize(QtCore.QSize(150, 30))
        self.importObj_pushButton_4.setToolTip(_fromUtf8(""))
        self.importObj_pushButton_4.setStatusTip(_fromUtf8(""))
        self.importObj_pushButton_4.setWhatsThis(_fromUtf8(""))
        self.importObj_pushButton_4.setAccessibleName(_fromUtf8(""))
        self.importObj_pushButton_4.setAccessibleDescription(_fromUtf8(""))
        self.importObj_pushButton_4.setText(_fromUtf8("Import .obj"))
        self.importObj_pushButton_4.setObjectName(_fromUtf8("importObj_pushButton_4"))
        self.rightUp_gridLayout_4.addWidget(self.importObj_pushButton_4, 1, 3, 1, 1)
        self.importAndCopy_pushButton_4 = QtGui.QPushButton(self.frame_6)
        self.importAndCopy_pushButton_4.setMinimumSize(QtCore.QSize(100, 30))
        self.importAndCopy_pushButton_4.setMaximumSize(QtCore.QSize(150, 30))
        self.importAndCopy_pushButton_4.setToolTip(_fromUtf8(""))
        self.importAndCopy_pushButton_4.setStatusTip(_fromUtf8(""))
        self.importAndCopy_pushButton_4.setWhatsThis(_fromUtf8(""))
        self.importAndCopy_pushButton_4.setAccessibleName(_fromUtf8(""))
        self.importAndCopy_pushButton_4.setAccessibleDescription(_fromUtf8(""))
        self.importAndCopy_pushButton_4.setText(_fromUtf8("Import/Copy Textures"))
        self.importAndCopy_pushButton_4.setObjectName(_fromUtf8("importAndCopy_pushButton_4"))
        self.rightUp_gridLayout_4.addWidget(self.importAndCopy_pushButton_4, 0, 0, 1, 1)
        self.gridLayout_11.addLayout(self.rightUp_gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.splitter.raise_()
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget, 1, 0, 1, 1)
        pdManager_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(pdManager_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 735, 21))
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
        self.actionImport_Selected_Item = QtGui.QAction(pdManager_MainWindow)
        self.actionImport_Selected_Item.setObjectName(_fromUtf8("actionImport_Selected_Item"))
        self.actionImport_Only = QtGui.QAction(pdManager_MainWindow)
        self.actionImport_Only.setObjectName(_fromUtf8("actionImport_Only"))
        self.actionAdd_New_Library = QtGui.QAction(pdManager_MainWindow)
        self.actionAdd_New_Library.setObjectName(_fromUtf8("actionAdd_New_Library"))
        self.actionRemove_Library = QtGui.QAction(pdManager_MainWindow)
        self.actionRemove_Library.setObjectName(_fromUtf8("actionRemove_Library"))
        self.menuFile.addAction(self.actionAdd_New_Library)
        self.menuFile.addAction(self.actionCreate_Project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLoad_Reference_Scene)
        self.menuFile.addAction(self.actionImport_Selected_Item)
        self.menuFile.addAction(self.actionImport_Only)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionAdd_Remove_Users)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionRemove_Library)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(pdManager_MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(pdManager_MainWindow)

    def retranslateUi(self, pdManager_MainWindow):
        pdManager_MainWindow.setWindowTitle(_translate("pdManager_MainWindow", "Pd Manager", None))
        self.filter_label_2.setText(_translate("pdManager_MainWindow", "Filter", None))
        self.thumb_label_4.setText(_translate("pdManager_MainWindow", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("pdManager_MainWindow", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("pdManager_MainWindow", "Tab 2", None))
        self.menuFile.setTitle(_translate("pdManager_MainWindow", "File", None))
        self.menuTools.setTitle(_translate("pdManager_MainWindow", "Tools", None))
        self.actionCreate_Project.setText(_translate("pdManager_MainWindow", "Create New Asset", None))
        self.actionSave_Version.setText(_translate("pdManager_MainWindow", "Save Version", None))
        self.actionSave_Base_Scene.setText(_translate("pdManager_MainWindow", "Save Base Scene", None))
        self.actionLoad_Reference_Scene.setText(_translate("pdManager_MainWindow", "Load Selected Asset", None))
        self.actionAdd_Remove_Users.setText(_translate("pdManager_MainWindow", "Delete Selected Asset", None))
        self.actionPreview_Settings.setText(_translate("pdManager_MainWindow", "Preview Settings", None))
        self.actionDelete_Selected_Base_Scene.setText(_translate("pdManager_MainWindow", "Delete Selected Base Scene", None))
        self.actionDelete_Reference_of_Selected_Scene.setText(_translate("pdManager_MainWindow", "Delete Reference of Selected Scene", None))
        self.actionProject_Report.setText(_translate("pdManager_MainWindow", "Project Report", None))
        self.actionCheck_References.setText(_translate("pdManager_MainWindow", "Check References", None))
        self.actionImage_Manager.setText(_translate("pdManager_MainWindow", "Image Manager", None))
        self.actionSequence_Viewer.setText(_translate("pdManager_MainWindow", "Sequence Viewer", None))
        self.actionImport_Selected_Item.setText(_translate("pdManager_MainWindow", "Import and Copy Textures", None))
        self.actionImport_Only.setText(_translate("pdManager_MainWindow", "Import Only", None))
        self.actionAdd_New_Library.setText(_translate("pdManager_MainWindow", "Add New Library", None))
        self.actionRemove_Library.setText(_translate("pdManager_MainWindow", "Remove Library", None))

