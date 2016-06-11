# coding: latin1

# Script Name        : mainGui.py
# Author             : David Martins
# Created            : 11/06/2016
# Last Modified      : 
# Version            : 1.0.0
# Modifications      : 

# Description        : Cont�m a classe MainGui que representa toda a view do software

from PySide.QtCore import *
from PySide.QtGui import *
from customWindow import Ui_MainWindow
from controller.controlador import Controlador

class MainGui(QMainWindow, Ui_MainWindow):
    '''Classe que executa a view do software e que conecta a l�gica da view com
    o controlador, permitindo a execu��o do MVC
    '''

    def __init__(self, parent = None):
        '''Construtor da classe MainGui. Inicia seus atributos e conecta os sinais dos bot�es da tela
        a m�todos da classe Controlador'''
        super(MainGui, self).__init__(parent)
        self.setupUi(self)
        
        #conecta tela ao controlador
        self._controlador = Controlador(self)
        
        self.abrirButton.clicked.connect(self.abrir_janela_para_escolher_arquivo)
        self.tabelaAtributos.itemClicked.connect(self._controlador.atualizar_botao_remover)
    
    def abrir_janela_para_escolher_arquivo(self):
        '''Abre uma janela para o usu�rio escolher um arquivo e chama o m�todo abrir'''
    
        #o endere�o do arquivo + nome est�o no primeiro campo de nome
        nome = QFileDialog.getOpenFileName(self, "Abrir", "", "Arquivos de Texto (*.csv)")[0]
        self._controlador.abrir(nome)
        
        