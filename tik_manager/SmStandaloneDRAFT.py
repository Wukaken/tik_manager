"""Creates a tree structure for image sequences

Image sequences can be listed recursively if the checkbox is checked.
Meaning all the sequence under the selected folder will be listed
recursively.
Double clicking on the seguence will execute the file on the defined application
"""

from PyQt4 import QtCore, QtGui, Qt

import sys, os

windowName = "test"

class MainUI(QtGui.QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        # self.projectPath = os.path.normpath("M:\Projects\Bambi_Yatak_shortcut_171130\images")

        self.setObjectName(windowName)
        self.resize(670, 624)
        self.setWindowTitle(windowName)
        self.centralwidget = QtGui.QWidget(self)

        self.setupUi(self)

        self.setCentralWidget(self.centralwidget)

    def setupUi(self, sceneManager_MainWindow):
        sceneManager_MainWindow.setObjectName(("sceneManager_MainWindow"))
        sceneManager_MainWindow.resize(975, 861)
        sceneManager_MainWindow.setToolTip((""))
        sceneManager_MainWindow.setStatusTip((""))
        sceneManager_MainWindow.setWhatsThis((""))
        sceneManager_MainWindow.setAccessibleName((""))
        sceneManager_MainWindow.setAccessibleDescription((""))
        self.centralwidget = QtGui.QWidget(sceneManager_MainWindow)
        self.centralwidget.setObjectName(("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(("gridLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(("horizontalLayout"))
        self.setProject_pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.setProject_pushButton_3.setMinimumSize(QtCore.QSize(150, 45))
        self.setProject_pushButton_3.setMaximumSize(QtCore.QSize(150, 45))
        self.setProject_pushButton_3.setToolTip((""))
        self.setProject_pushButton_3.setStatusTip((""))
        self.setProject_pushButton_3.setWhatsThis((""))
        self.setProject_pushButton_3.setAccessibleName((""))
        self.setProject_pushButton_3.setAccessibleDescription((""))
        self.setProject_pushButton_3.setText(("Save As Version"))
        self.setProject_pushButton_3.setObjectName(("setProject_pushButton_3"))
        self.horizontalLayout.addWidget(self.setProject_pushButton_3)
        self.setProject_pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.setProject_pushButton_2.setMinimumSize(QtCore.QSize(150, 45))
        self.setProject_pushButton_2.setMaximumSize(QtCore.QSize(150, 45))
        self.setProject_pushButton_2.setToolTip((""))
        self.setProject_pushButton_2.setStatusTip((""))
        self.setProject_pushButton_2.setWhatsThis((""))
        self.setProject_pushButton_2.setAccessibleName((""))
        self.setProject_pushButton_2.setAccessibleDescription((""))
        self.setProject_pushButton_2.setText(("Save Base Scene"))
        self.setProject_pushButton_2.setObjectName(("setProject_pushButton_2"))
        self.horizontalLayout.addWidget(self.setProject_pushButton_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.setProject_pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.setProject_pushButton_4.setMinimumSize(QtCore.QSize(150, 45))
        self.setProject_pushButton_4.setMaximumSize(QtCore.QSize(150, 45))
        self.setProject_pushButton_4.setToolTip((""))
        self.setProject_pushButton_4.setStatusTip((""))
        self.setProject_pushButton_4.setWhatsThis((""))
        self.setProject_pushButton_4.setAccessibleName((""))
        self.setProject_pushButton_4.setAccessibleDescription((""))
        self.setProject_pushButton_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setProject_pushButton_4.setText(("Load Scene"))
        self.setProject_pushButton_4.setObjectName(("setProject_pushButton_4"))
        self.horizontalLayout.addWidget(self.setProject_pushButton_4)
        self.horizontalLayout.setStretch(0, 1)
        self.gridLayout_3.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(("gridLayout_2"))
        self.load_radioButton = QtGui.QRadioButton(self.centralwidget)
        self.load_radioButton.setToolTip((""))
        self.load_radioButton.setStatusTip((""))
        self.load_radioButton.setWhatsThis((""))
        self.load_radioButton.setAccessibleName((""))
        self.load_radioButton.setAccessibleDescription((""))
        self.load_radioButton.setText(("Load Mode"))
        self.load_radioButton.setChecked(False)
        self.load_radioButton.setObjectName(("load_radioButton"))
        self.gridLayout_2.addWidget(self.load_radioButton, 0, 0, 1, 1)
        self.subProject_label = QtGui.QLabel(self.centralwidget)
        self.subProject_label.setToolTip((""))
        self.subProject_label.setStatusTip((""))
        self.subProject_label.setWhatsThis((""))
        self.subProject_label.setAccessibleName((""))
        self.subProject_label.setAccessibleDescription((""))
        self.subProject_label.setText(("Sub-Project:"))
        self.subProject_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.subProject_label.setObjectName(("subProject_label"))
        self.gridLayout_2.addWidget(self.subProject_label, 0, 2, 1, 1)
        self.subProject_comboBox = QtGui.QComboBox(self.centralwidget)
        self.subProject_comboBox.setMinimumSize(QtCore.QSize(150, 30))
        self.subProject_comboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.subProject_comboBox.setToolTip((""))
        self.subProject_comboBox.setStatusTip((""))
        self.subProject_comboBox.setWhatsThis((""))
        self.subProject_comboBox.setAccessibleName((""))
        self.subProject_comboBox.setAccessibleDescription((""))
        self.subProject_comboBox.setObjectName(("subProject_comboBox"))
        self.gridLayout_2.addWidget(self.subProject_comboBox, 0, 3, 1, 1)
        self.reference_radioButton = QtGui.QRadioButton(self.centralwidget)
        self.reference_radioButton.setToolTip((""))
        self.reference_radioButton.setStatusTip((""))
        self.reference_radioButton.setWhatsThis((""))
        self.reference_radioButton.setAccessibleName((""))
        self.reference_radioButton.setAccessibleDescription((""))
        self.reference_radioButton.setText(("Reference Mode"))
        self.reference_radioButton.setChecked(True)
        self.reference_radioButton.setObjectName(("reference_radioButton"))
        self.gridLayout_2.addWidget(self.reference_radioButton, 0, 1, 1, 1)
        self.addSubProject_pushButton = QtGui.QPushButton(self.centralwidget)
        self.addSubProject_pushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.addSubProject_pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.addSubProject_pushButton.setToolTip((""))
        self.addSubProject_pushButton.setStatusTip((""))
        self.addSubProject_pushButton.setWhatsThis((""))
        self.addSubProject_pushButton.setAccessibleName((""))
        self.addSubProject_pushButton.setAccessibleDescription((""))
        self.addSubProject_pushButton.setText(("+"))
        self.addSubProject_pushButton.setObjectName(("addSubProject_pushButton"))
        self.gridLayout_2.addWidget(self.addSubProject_pushButton, 0, 4, 1, 1)
        self.user_label = QtGui.QLabel(self.centralwidget)
        self.user_label.setToolTip((""))
        self.user_label.setStatusTip((""))
        self.user_label.setWhatsThis((""))
        self.user_label.setAccessibleName((""))
        self.user_label.setAccessibleDescription((""))
        self.user_label.setText(("User:"))
        self.user_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.user_label.setObjectName(("user_label"))
        self.gridLayout_2.addWidget(self.user_label, 0, 5, 1, 1)
        self.user_comboBox = QtGui.QComboBox(self.centralwidget)
        self.user_comboBox.setMinimumSize(QtCore.QSize(130, 30))
        self.user_comboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.user_comboBox.setToolTip((""))
        self.user_comboBox.setStatusTip((""))
        self.user_comboBox.setWhatsThis((""))
        self.user_comboBox.setAccessibleName((""))
        self.user_comboBox.setAccessibleDescription((""))
        self.user_comboBox.setObjectName(("user_comboBox"))
        self.gridLayout_2.addWidget(self.user_comboBox, 0, 6, 1, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(("gridLayout"))
        self.baseScene_label = QtGui.QLabel(self.centralwidget)
        self.baseScene_label.setToolTip((""))
        self.baseScene_label.setStatusTip((""))
        self.baseScene_label.setWhatsThis((""))
        self.baseScene_label.setAccessibleName((""))
        self.baseScene_label.setAccessibleDescription((""))
        self.baseScene_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.baseScene_label.setText(("Base Scene:"))
        self.baseScene_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.baseScene_label.setObjectName(("baseScene_label"))
        self.gridLayout.addWidget(self.baseScene_label, 0, 0, 1, 1)
        self.baseScene_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.baseScene_lineEdit.setToolTip((""))
        self.baseScene_lineEdit.setStatusTip((""))
        self.baseScene_lineEdit.setWhatsThis((""))
        self.baseScene_lineEdit.setAccessibleName((""))
        self.baseScene_lineEdit.setAccessibleDescription((""))
        self.baseScene_lineEdit.setInputMask((""))
        self.baseScene_lineEdit.setText((""))
        self.baseScene_lineEdit.setPlaceholderText((""))
        self.baseScene_lineEdit.setObjectName(("baseScene_lineEdit"))
        self.gridLayout.addWidget(self.baseScene_lineEdit, 0, 1, 1, 1)
        self.project_label = QtGui.QLabel(self.centralwidget)
        self.project_label.setToolTip((""))
        self.project_label.setStatusTip((""))
        self.project_label.setWhatsThis((""))
        self.project_label.setAccessibleName((""))
        self.project_label.setAccessibleDescription((""))
        self.project_label.setText(("Project:"))
        self.project_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.project_label.setObjectName(("project_label"))
        self.gridLayout.addWidget(self.project_label, 1, 0, 1, 1)
        self.project_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.project_lineEdit.setToolTip((""))
        self.project_lineEdit.setStatusTip((""))
        self.project_lineEdit.setWhatsThis((""))
        self.project_lineEdit.setAccessibleName((""))
        self.project_lineEdit.setAccessibleDescription((""))
        self.project_lineEdit.setInputMask((""))
        self.project_lineEdit.setText((""))
        self.project_lineEdit.setPlaceholderText((""))
        self.project_lineEdit.setObjectName(("project_lineEdit"))
        self.gridLayout.addWidget(self.project_lineEdit, 1, 1, 1, 1)
        self.setProject_pushButton = QtGui.QPushButton(self.centralwidget)
        self.setProject_pushButton.setToolTip((""))
        self.setProject_pushButton.setStatusTip((""))
        self.setProject_pushButton.setWhatsThis((""))
        self.setProject_pushButton.setAccessibleName((""))
        self.setProject_pushButton.setAccessibleDescription((""))
        self.setProject_pushButton.setText(("SET"))
        self.setProject_pushButton.setObjectName(("setProject_pushButton"))
        self.gridLayout.addWidget(self.setProject_pushButton, 1, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 22))
        self.tabWidget.setToolTip((""))
        self.tabWidget.setStatusTip((""))
        self.tabWidget.setWhatsThis((""))
        self.tabWidget.setAccessibleName((""))
        self.tabWidget.setAccessibleDescription((""))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setObjectName(("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(("tab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab)
        self.gridLayout_4.setContentsMargins(9, -1, -1, -1)
        self.gridLayout_4.setObjectName(("gridLayout_4"))
        self.tabWidget.addTab(self.tab, (""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(("tab_2"))
        self.tabWidget.addTab(self.tab_2, (""))
        self.gridLayout_3.addWidget(self.tabWidget, 2, 0, 1, 1)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setToolTip((""))
        self.splitter.setStatusTip((""))
        self.splitter.setWhatsThis((""))
        self.splitter.setAccessibleName((""))
        self.splitter.setAccessibleDescription((""))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(("splitter"))
        self.listWidget = QtGui.QListWidget(self.splitter)
        self.listWidget.setObjectName(("listWidget"))
        self.frame = QtGui.QFrame(self.splitter)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(("frame"))
        self.gridLayout_6 = QtGui.QGridLayout(self.frame)
        self.gridLayout_6.setContentsMargins(-1, -1, 0, 0)
        self.gridLayout_6.setObjectName(("gridLayout_6"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(("verticalLayout"))
        self.version_label_2 = QtGui.QLabel(self.frame)
        self.version_label_2.setToolTip((""))
        self.version_label_2.setStatusTip((""))
        self.version_label_2.setWhatsThis((""))
        self.version_label_2.setAccessibleName((""))
        self.version_label_2.setAccessibleDescription((""))
        self.version_label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.version_label_2.setText(("Version Notes:"))
        self.version_label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.version_label_2.setObjectName(("version_label_2"))
        self.verticalLayout.addWidget(self.version_label_2)
        self.textEdit = QtGui.QTextEdit(self.frame)
        self.textEdit.setObjectName(("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)

        # testFile = os.path.normpath("D:\\PROJECT_AND_ARGE\\testo_testo_testo_180715\\DSC_2179.JPG")
        # self.tPixmap = QtGui.QPixmap((testFile))

        self.label = ImageWidget(self.frame)
        # self.label = QtGui.QLabel(self.frame)
        # self.label.setPixmap(self.tPixmap.scaledToHeight(300))
        # sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        # sizePolicy.setHeightForWidth(True)
        # self.label.setSizePolicy(sizePolicy)

        self.label.setMinimumSize(QtCore.QSize(221, 124))
        # self.label.setMaximumSize(QtCore.QSize(884, 496))
        # self.label.setSizeIncrement(QtCore.QSize(1, 1))
        # self.label.setBaseSize(QtCore.QSize(0, 0))
        self.label.setText(("test"))
        self.label.setFrameShape(QtGui.QFrame.Box)
        # self.label.setScaledContents(False)
        # self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(("label"))
        self.verticalLayout.addWidget(self.label)
        self.gridLayout_6.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setContentsMargins(-1, -1, 10, 10)
        self.gridLayout_7.setObjectName(("gridLayout_7"))
        self.setProject_pushButton_5 = QtGui.QPushButton(self.frame)
        self.setProject_pushButton_5.setMinimumSize(QtCore.QSize(100, 30))
        self.setProject_pushButton_5.setMaximumSize(QtCore.QSize(150, 30))
        self.setProject_pushButton_5.setToolTip((""))
        self.setProject_pushButton_5.setStatusTip((""))
        self.setProject_pushButton_5.setWhatsThis((""))
        self.setProject_pushButton_5.setAccessibleName((""))
        self.setProject_pushButton_5.setAccessibleDescription((""))
        self.setProject_pushButton_5.setText(("Show Preview"))
        self.setProject_pushButton_5.setObjectName(("setProject_pushButton_5"))
        self.gridLayout_7.addWidget(self.setProject_pushButton_5, 0, 3, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(("horizontalLayout_4"))
        self.version_label = QtGui.QLabel(self.frame)
        self.version_label.setMinimumSize(QtCore.QSize(60, 30))
        self.version_label.setMaximumSize(QtCore.QSize(60, 30))
        self.version_label.setToolTip((""))
        self.version_label.setStatusTip((""))
        self.version_label.setWhatsThis((""))
        self.version_label.setAccessibleName((""))
        self.version_label.setAccessibleDescription((""))
        self.version_label.setFrameShape(QtGui.QFrame.Box)
        self.version_label.setText(("Version:"))
        self.version_label.setAlignment(QtCore.Qt.AlignCenter)
        self.version_label.setObjectName(("version_label"))
        self.horizontalLayout_4.addWidget(self.version_label)
        self.version_comboBox = QtGui.QComboBox(self.frame)
        self.version_comboBox.setMinimumSize(QtCore.QSize(60, 30))
        self.version_comboBox.setMaximumSize(QtCore.QSize(100, 30))
        self.version_comboBox.setToolTip((""))
        self.version_comboBox.setStatusTip((""))
        self.version_comboBox.setWhatsThis((""))
        self.version_comboBox.setAccessibleName((""))
        self.version_comboBox.setAccessibleDescription((""))
        self.version_comboBox.setObjectName(("version_comboBox"))
        self.horizontalLayout_4.addWidget(self.version_comboBox)
        self.gridLayout_7.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.setProject_pushButton_6 = QtGui.QPushButton(self.frame)
        self.setProject_pushButton_6.setMinimumSize(QtCore.QSize(100, 30))
        self.setProject_pushButton_6.setMaximumSize(QtCore.QSize(300, 30))
        self.setProject_pushButton_6.setToolTip((""))
        self.setProject_pushButton_6.setStatusTip((""))
        self.setProject_pushButton_6.setWhatsThis((""))
        self.setProject_pushButton_6.setAccessibleName((""))
        self.setProject_pushButton_6.setAccessibleDescription((""))
        self.setProject_pushButton_6.setText(("Make Reference"))
        self.setProject_pushButton_6.setObjectName(("setProject_pushButton_6"))
        self.gridLayout_7.addWidget(self.setProject_pushButton_6, 1, 0, 1, 1)
        self.setProject_pushButton_7 = QtGui.QPushButton(self.frame)
        self.setProject_pushButton_7.setMinimumSize(QtCore.QSize(100, 30))
        self.setProject_pushButton_7.setMaximumSize(QtCore.QSize(150, 30))
        self.setProject_pushButton_7.setToolTip((""))
        self.setProject_pushButton_7.setStatusTip((""))
        self.setProject_pushButton_7.setWhatsThis((""))
        self.setProject_pushButton_7.setAccessibleName((""))
        self.setProject_pushButton_7.setAccessibleDescription((""))
        self.setProject_pushButton_7.setText(("Add Note"))
        self.setProject_pushButton_7.setObjectName(("setProject_pushButton_7"))
        self.gridLayout_7.addWidget(self.setProject_pushButton_7, 1, 3, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.splitter, 3, 0, 1, 1)
        sceneManager_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(sceneManager_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 975, 21))
        self.menubar.setObjectName(("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(("menuFile"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(("menuTools"))
        sceneManager_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(sceneManager_MainWindow)
        self.statusbar.setObjectName(("statusbar"))
        sceneManager_MainWindow.setStatusBar(self.statusbar)
        self.actionCreate_Project = QtGui.QAction(sceneManager_MainWindow)
        self.actionCreate_Project.setObjectName(("actionCreate_Project"))
        self.actionSave_Version = QtGui.QAction(sceneManager_MainWindow)
        self.actionSave_Version.setObjectName(("actionSave_Version"))
        self.actionSave_Base_Scene = QtGui.QAction(sceneManager_MainWindow)
        self.actionSave_Base_Scene.setObjectName(("actionSave_Base_Scene"))
        self.actionLoad_Reference_Scene = QtGui.QAction(sceneManager_MainWindow)
        self.actionLoad_Reference_Scene.setObjectName(("actionLoad_Reference_Scene"))
        self.actionAdd_Remove_Users = QtGui.QAction(sceneManager_MainWindow)
        self.actionAdd_Remove_Users.setObjectName(("actionAdd_Remove_Users"))
        self.actionPreview_Settings = QtGui.QAction(sceneManager_MainWindow)
        self.actionPreview_Settings.setObjectName(("actionPreview_Settings"))
        self.actionDelete_Selected_Base_Scene = QtGui.QAction(sceneManager_MainWindow)
        self.actionDelete_Selected_Base_Scene.setObjectName(("actionDelete_Selected_Base_Scene"))
        self.actionDelete_Reference_of_Selected_Scene = QtGui.QAction(sceneManager_MainWindow)
        self.actionDelete_Reference_of_Selected_Scene.setObjectName(("actionDelete_Reference_of_Selected_Scene"))
        self.actionProject_Report = QtGui.QAction(sceneManager_MainWindow)
        self.actionProject_Report.setObjectName(("actionProject_Report"))
        self.actionCheck_References = QtGui.QAction(sceneManager_MainWindow)
        self.actionCheck_References.setObjectName(("actionCheck_References"))
        self.actionImage_Manager = QtGui.QAction(sceneManager_MainWindow)
        self.actionImage_Manager.setObjectName(("actionImage_Manager"))
        self.actionSequence_Viewer = QtGui.QAction(sceneManager_MainWindow)
        self.actionSequence_Viewer.setObjectName(("actionSequence_Viewer"))
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

        # self.retranslateUi(sceneManager_MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(sceneManager_MainWindow)


# class ScaledLabel(QtGui.QLabel):
#     def __init__(self, *args, **kwargs):
#         QtGui.QLabel.__init__(self)
#         self.tPixmap = QtGui.QPixmap((""))
#         # self.thumbnail_label.setPixmap(self.tPixmap)
#         self._pixmap = QtGui.QPixmap(self.tPixmap)
#
#     def resizeEvent(self, event):
#         self.setPixmap(self._pixmap.scaled(
#             self.width(), self.height(),
#             QtCore.Qt.KeepAspectRatio))

class ImageWidget(QtGui.QLabel):
    def __init__(self, parent=None):
        super(ImageWidget, self).__init__()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)

    def resizeEvent(self, r):
        # print r
        w = self.width()
        # print w
        self.setMinimumHeight(w*0.5)
        self.setMaximumHeight(w*0.5)


    def heightForWidth(self, width):
        return width * 1.5
    #
    # def hasHeightForWidth(self):
    #     return self.pixmap() is not None
    #
    #
    #
    # def heightForWidth(self, w):
    #     # return w * 5
    #     if self.pixmap():
    #         return int(w * (self.pixmap().height() / self.pixmap().width()))

    # def retranslateUi(self, sceneManager_MainWindow):
    #     sceneManager_MainWindow.setWindowTitle(_translate("sceneManager_MainWindow", "Scene Manager", None))
    #     self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("sceneManager_MainWindow", "Tab 1", None))
    #     self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("sceneManager_MainWindow", "Tab 2", None))
    #     self.label.setText(_translate("sceneManager_MainWindow", "TextLabel", None))
    #     self.menuFile.setTitle(_translate("sceneManager_MainWindow", "File", None))
    #     self.menuTools.setTitle(_translate("sceneManager_MainWindow", "Tools", None))
    #     self.actionCreate_Project.setText(_translate("sceneManager_MainWindow", "Create Project", None))
    #     self.actionSave_Version.setText(_translate("sceneManager_MainWindow", "Save Version", None))
    #     self.actionSave_Base_Scene.setText(_translate("sceneManager_MainWindow", "Save Base Scene", None))
    #     self.actionLoad_Reference_Scene.setText(_translate("sceneManager_MainWindow", "Load/Reference Scene", None))
    #     self.actionAdd_Remove_Users.setText(_translate("sceneManager_MainWindow", "Add/Remove Users", None))
    #     self.actionPreview_Settings.setText(_translate("sceneManager_MainWindow", "Preview Settings", None))
    #     self.actionDelete_Selected_Base_Scene.setText(_translate("sceneManager_MainWindow", "Delete Selected Base Scene", None))
    #     self.actionDelete_Reference_of_Selected_Scene.setText(_translate("sceneManager_MainWindow", "Delete Reference of Selected Scene", None))
    #     self.actionProject_Report.setText(_translate("sceneManager_MainWindow", "Project Report", None))
    #     self.actionCheck_References.setText(_translate("sceneManager_MainWindow", "Check References", None))
    #     self.actionImage_Manager.setText(_translate("sceneManager_MainWindow", "Image Manager", None))
    #     self.actionSequence_Viewer.setText(_translate("sceneManager_MainWindow", "Sequence Viewer", None))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainUI()
    window.show()
    sys.exit(app.exec_())
