# coding: latin1

# Script Name		: controlador.py
# Author			: David Martins
# Created			: 10/06/2016
# Last Modified		: 
# Version			: 1.0.0

# Modifications		: 

# Description		: Cont�m a classe que controla a atualiza��o das telas e adquire os dados dos modelos

from PySide.QtCore import *
from PySide.QtGui import *

from model import datasetmodel as dm
from view import mainGui as gui
import os

class Controlador(QMainWindow):
	'''Classe que controla e atualiza as telas com base nos dados adquiridos das classes de modelo
	
	Atributos:
	
	view		: QMainWindow montada no Qt Designer
	dataset		: DatasetModel com os dados carregados atrav�s da tela
	'''
	
	def __init__(self, parent = None):
		'''Construtor da classe Controlador. Inicia seus atributos e conecta os sinais dos bot�es da tela
		a m�todos'''
		
		super(Controlador, self).__init__(parent)
		self.view = gui.Ui_MainWindow()
		self.view.setupUi(self)
	
		self.dataset = dm.DatasetModel()
		
		self.view.abrirButton.clicked.connect(self.abrir_janela_para_escolher_arquivo)
		
	def abrir_janela_para_escolher_arquivo(self):
		'''Abre uma janela para o usu�rio escolher um arquivo e chama o m�todo abrir'''
	
		#o endere�o do arquivo + nome est�o no primeiro campo de nome
		nome = QFileDialog.getOpenFileName(self, "Abrir", "", "Arquivos de Texto (*.csv)")[0]
		self.abrir(nome)
		
	def abrir(self, nome):
		'''Abre o arquivo com nome *nome*  e carrega esse arquivo em DatasetModel e 
		atualiza a aba Dados da tela'''
				
		self.view.statusbar.showMessage(u"Abrindo dataset...")
		if self.dataset.ler_csv(nome):
			self.view.statusbar.showMessage(u"Dataset aberto")
			
			#carrega o dataset numa tabela mostrada na aba Dados
			for i in range(self.dataset.natributos):
				currentRowCount = self.view.tabelaAtributos.rowCount()
				self.view.tabelaAtributos.insertRow(currentRowCount)
				item = QTableWidgetItem(str(i+1))
				item.setFlags(Qt.ItemIsEnabled)
				item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
				self.view.tabelaAtributos.setItem(currentRowCount, 0, item)
				item = QTableWidgetItem("")
				#para tornar o item da tabela marc�vel
				item.setFlags(Qt.ItemIsEnabled| Qt.ItemIsUserCheckable)
				item.setCheckState(Qt.Unchecked)
				item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
				self.view.tabelaAtributos.setItem(currentRowCount,1, item)
				item = QTableWidgetItem(self.dataset.atributos[i])
				item.setFlags(Qt.ItemIsEnabled)
				item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
				self.view.tabelaAtributos.setItem(currentRowCount,2, item)
				
			self.view.tabelaAtributos.itemClicked.connect(self.ativar_botao_remover)
			
			#pega somente o nome do arquivo sem o seu endere�o
			head, tail = os.path.split(nome)
			
			self.view.nomeLabel.setText(tail)
			self.view.instanciaLabel.setText(str(self.dataset.ninstancias))
			self.view.atributosLabel.setText(str(self.dataset.natributos))
			
			return True
		else:
			self.view.statusbar.showMessage(u"Nenhum dataset selecionado")
			return False
		
	def ativar_botao_remover(self, item):
		
		ativos = 0
		
		for i in range(self.view.tabelaAtributos.rowCount()):
			if self.view.tabelaAtributos.cellWidget(i,1).findChild(type(QCheckBox())).isChecked():
				ativos += 1
			else: 
				ativos -= 1
		
		if ativos == 0:
			self.view.removerButton.setEnabled(False)
		else:
			self.view.removerButton.setEnabled(True)