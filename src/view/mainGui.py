# coding: latin1

# Script Name        : mainGui.py
# Author             : David Martins
# Created            : 11/06/2016
# Last Modified      : 
# Version            : 1.0.0
# Modifications      : 

# Description        : Contém a classe MainGui que representa toda a view do software

from PySide.QtCore import *
from PySide.QtGui import *
from customWindow import Ui_MainWindow
from controller.controlador import Controlador

class MainGui(QMainWindow, Ui_MainWindow):
    '''Classe que executa a view do software e que conecta a lógica da view com
    o controlador, permitindo a execução do MVC
    '''

    def __init__(self, parent = None):
        '''Construtor da classe MainGui. Inicia seus atributos e conecta os sinais dos botões da tela
        a métodos da classe Controlador'''
        super(MainGui, self).__init__(parent)
        self.setupUi(self)
        
        #conecta tela ao controlador
        self._controlador = Controlador(self)
        
        self.abrirButton.clicked.connect(self.abrir_janela_para_escolher_arquivo)
        self.tabelaAtributos.itemClicked.connect(self._controlador.atualizar_botao_remover)
    
    def abrir_janela_para_escolher_arquivo(self):
        '''Abre uma janela para o usuário escolher um arquivo e chama o método abrir'''
    
        #o endereço do arquivo + nome estão no primeiro campo de nome
        nome = QFileDialog.getOpenFileName(self, "Abrir", "", "Arquivos de Texto (*.csv)")[0]
        self._controlador.abrir(nome)
        
        