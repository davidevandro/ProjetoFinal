# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainWindow.ui'
#
# Created: Mon Jun 13 00:52:18 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 572)
        MainWindow.setMinimumSize(QtCore.QSize(796, 572))
        MainWindow.setMaximumSize(QtCore.QSize(796, 572))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 80))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.dadosButton = QtGui.QToolButton(self.frame)
        self.dadosButton.setGeometry(QtCore.QRect(10, 0, 190, 80))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        self.dadosButton.setFont(font)
        self.dadosButton.setAutoExclusive(True)
        self.dadosButton.setObjectName("dadosButton")
        self.classificacaoButton = QtGui.QToolButton(self.frame)
        self.classificacaoButton.setGeometry(QtCore.QRect(206, 0, 190, 80))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        self.classificacaoButton.setFont(font)
        self.classificacaoButton.setAutoExclusive(True)
        self.classificacaoButton.setObjectName("classificacaoButton")
        self.entrada2Button = QtGui.QToolButton(self.frame)
        self.entrada2Button.setGeometry(QtCore.QRect(403, 0, 190, 80))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        self.entrada2Button.setFont(font)
        self.entrada2Button.setAutoExclusive(True)
        self.entrada2Button.setObjectName("entrada2Button")
        self.resultado2Button = QtGui.QToolButton(self.frame)
        self.resultado2Button.setGeometry(QtCore.QRect(600, 0, 190, 80))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        self.resultado2Button.setFont(font)
        self.resultado2Button.setAutoExclusive(True)
        self.resultado2Button.setObjectName("resultado2Button")
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 90, 801, 491))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName("page_4")
        self.abrirButton = QtGui.QPushButton(self.page_4)
        self.abrirButton.setGeometry(QtCore.QRect(30, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        self.abrirButton.setFont(font)
        self.abrirButton.setObjectName("abrirButton")
        self.groupBox_2 = QtGui.QGroupBox(self.page_4)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 170, 381, 291))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.removerButton = QtGui.QPushButton(self.groupBox_2)
        self.removerButton.setEnabled(False)
        self.removerButton.setGeometry(QtCore.QRect(120, 245, 131, 40))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.removerButton.setFont(font)
        self.removerButton.setObjectName("removerButton")
        self.tabelaAtributos = QtGui.QTableView(self.groupBox_2)
        self.tabelaAtributos.setGeometry(QtCore.QRect(10, 30, 361, 211))
        self.tabelaAtributos.setObjectName("tabelaAtributos")
        self.tabelaAtributos.horizontalHeader().setCascadingSectionResizes(True)
        self.tabelaAtributos.horizontalHeader().setDefaultSectionSize(20)
        self.tabelaAtributos.horizontalHeader().setMinimumSectionSize(31)
        self.tabelaAtributos.horizontalHeader().setStretchLastSection(True)
        self.groupBox = QtGui.QGroupBox(self.page_4)
        self.groupBox.setGeometry(QtCore.QRect(30, 70, 379, 91))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 29, 354, 56))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setItalic(False)
        font.setUnderline(False)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setItalic(False)
        font.setUnderline(False)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setItalic(False)
        font.setUnderline(False)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.instanciaLabel = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.instanciaLabel.setFont(font)
        self.instanciaLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.instanciaLabel.setObjectName("instanciaLabel")
        self.gridLayout.addWidget(self.instanciaLabel, 1, 1, 1, 1)
        self.atributosLabel = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.atributosLabel.setFont(font)
        self.atributosLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.atributosLabel.setObjectName("atributosLabel")
        self.gridLayout.addWidget(self.atributosLabel, 0, 3, 1, 1)
        self.nomeLabel = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.nomeLabel.setFont(font)
        self.nomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nomeLabel.setObjectName("nomeLabel")
        self.gridLayout.addWidget(self.nomeLabel, 0, 1, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.page_4)
        self.groupBox_3.setGeometry(QtCore.QRect(410, 70, 371, 391))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayoutWidget_2 = QtGui.QWidget(self.groupBox_3)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(9, 29, 354, 56))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setItalic(False)
        font.setUnderline(False)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setItalic(False)
        font.setUnderline(False)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setItalic(False)
        font.setUnderline(False)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.ausentesLabel = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.ausentesLabel.setFont(font)
        self.ausentesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ausentesLabel.setObjectName("ausentesLabel")
        self.gridLayout_2.addWidget(self.ausentesLabel, 1, 1, 1, 1)
        self.tipoLabel = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.tipoLabel.setFont(font)
        self.tipoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tipoLabel.setObjectName("tipoLabel")
        self.gridLayout_2.addWidget(self.tipoLabel, 0, 3, 1, 1)
        self.nomeAtributoLabel = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.nomeAtributoLabel.setFont(font)
        self.nomeAtributoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nomeAtributoLabel.setObjectName("nomeAtributoLabel")
        self.gridLayout_2.addWidget(self.nomeAtributoLabel, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setItalic(False)
        font.setUnderline(False)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 2, 1, 1)
        self.distintosLabel = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.distintosLabel.setFont(font)
        self.distintosLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.distintosLabel.setObjectName("distintosLabel")
        self.gridLayout_2.addWidget(self.distintosLabel, 1, 3, 1, 1)
        self.tabelaEstatistica = QtGui.QTableView(self.groupBox_3)
        self.tabelaEstatistica.setGeometry(QtCore.QRect(10, 130, 349, 211))
        self.tabelaEstatistica.setObjectName("tabelaEstatistica")
        self.tabelaEstatistica.horizontalHeader().setCascadingSectionResizes(True)
        self.tabelaEstatistica.horizontalHeader().setDefaultSectionSize(40)
        self.tabelaEstatistica.horizontalHeader().setMinimumSectionSize(31)
        self.tabelaEstatistica.horizontalHeader().setStretchLastSection(True)
        self.stackedWidget.addWidget(self.page_4)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.dadosButton.setText(QtGui.QApplication.translate("MainWindow", "Dados", None, QtGui.QApplication.UnicodeUTF8))
        self.classificacaoButton.setText(QtGui.QApplication.translate("MainWindow", "Classificação", None, QtGui.QApplication.UnicodeUTF8))
        self.entrada2Button.setText(QtGui.QApplication.translate("MainWindow", "Entrada 2", None, QtGui.QApplication.UnicodeUTF8))
        self.resultado2Button.setText(QtGui.QApplication.translate("MainWindow", "Resultado 2", None, QtGui.QApplication.UnicodeUTF8))
        self.abrirButton.setText(QtGui.QApplication.translate("MainWindow", "Abrir dataset...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Atributos", None, QtGui.QApplication.UnicodeUTF8))
        self.removerButton.setText(QtGui.QApplication.translate("MainWindow", "Remover", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Dataset", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Instâncias:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Atributos:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Nome:", None, QtGui.QApplication.UnicodeUTF8))
        self.instanciaLabel.setText(QtGui.QApplication.translate("MainWindow", "Nenhum", None, QtGui.QApplication.UnicodeUTF8))
        self.atributosLabel.setText(QtGui.QApplication.translate("MainWindow", "Nenhum", None, QtGui.QApplication.UnicodeUTF8))
        self.nomeLabel.setText(QtGui.QApplication.translate("MainWindow", "Nenhum", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Atributo Selecionado", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Ausentes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Tipo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Nome:", None, QtGui.QApplication.UnicodeUTF8))
        self.ausentesLabel.setText(QtGui.QApplication.translate("MainWindow", "Nenhum", None, QtGui.QApplication.UnicodeUTF8))
        self.tipoLabel.setText(QtGui.QApplication.translate("MainWindow", "Nenhum", None, QtGui.QApplication.UnicodeUTF8))
        self.nomeAtributoLabel.setText(QtGui.QApplication.translate("MainWindow", "Nenhum", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Distintos:", None, QtGui.QApplication.UnicodeUTF8))
        self.distintosLabel.setText(QtGui.QApplication.translate("MainWindow", "Nenhum", None, QtGui.QApplication.UnicodeUTF8))

