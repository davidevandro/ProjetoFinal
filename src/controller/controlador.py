# coding: latin1

# Script Name		: controlador.py
# Author			: David Martins
# Created			: 10/06/2016
# Last Modified		: 
# Version			: 1.0.0

# Modifications		: 

# Description		: Contém a classe que controla a atualização das telas e adquire os dados dos modelos



from model import datasetmodel as dm
import os

from PySide.QtCore import *
from PySide.QtGui import *

class Controlador():
	'''Classe que controla e atualiza as telas com base nos dados adquiridos das classes de modelo
	
	Atributos:
	
	_view			: MainGui que o controlador está controlando
	_dataset		: DatasetModel com os dados carregados através da tela
	'''
	
	def __init__(self, view):
		'''Construtor da classe Controlador. Inicia seus atributos e conecta os sinais dos botões da tela
		a métodos
		
		Atributos:
		
		view		: MainGui que o controlador está controlando
		'''
		
		#conecta controlador a tela
		self._view = view
		#conecta controlador ao modelo de Dataset
		self._dataset = dm.DatasetModel()
				
	def abrir(self, nome):
		'''Abre o arquivo com nome *nome*  e carrega esse arquivo em DatasetModel e 
		atualiza a aba Dados da tela'''
				
		self._view.statusbar.showMessage(u"Abrindo dataset...")
		if self._dataset.ler_csv(nome):
			self._view.statusbar.showMessage(u"Dataset aberto")
			
			atributos = self._dataset.get_atributos()
			#carrega o dataset numa tabela mostrada na aba Dados		
			for i in range(self._dataset.get_natributos()):
				currentRowCount = self._view.tabelaAtributos.rowCount()
				self._view.tabelaAtributos.insertRow(currentRowCount)
				item = QTableWidgetItem(str(i+1))
				item.setFlags(Qt.ItemIsEnabled)
				item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
				self._view.tabelaAtributos.setItem(currentRowCount, 0, item)
				item = QTableWidgetItem("")
				#para tornar o item da tabela marcável
				item.setFlags(Qt.ItemIsEnabled| Qt.ItemIsUserCheckable)
				item.setCheckState(Qt.Unchecked)
				item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
				self._view.tabelaAtributos.setItem(currentRowCount,1, item)
				item = QTableWidgetItem(atributos[i])
				item.setFlags(Qt.ItemIsEnabled)
				item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
				self._view.tabelaAtributos.setItem(currentRowCount,2, item)
				
			self._view.tabelaAtributos.itemClicked.connect(self.ativar_botao_remover)
			
			#pega somente o nome do arquivo sem o seu endereço
			__, tail = os.path.split(nome)
			
			self._view.nomeLabel.setText(tail)
			self._view.instanciaLabel.setText(str(self._dataset.get_ninstancias()))
			self._view.atributosLabel.setText(str(self._dataset.get_natributos()))
			
			return True
		else:
			self.view.statusbar.showMessage(u"Nenhum dataset selecionado")
			return False
		
	'''def ativar_botao_remover(self, item):
		
		ativos = 0
		
		for i in range(self.view.tabelaAtributos.rowCount()):
			if self.view.tabela-Atributos.cellWidget(i,1).findChild(type(QCheckBox())).isChecked():
				ativos += 1
			else: 
				ativos -= 1
		
		if ativos == 0:
			self.view.removerButton.setEnabled(False)
		else:
			self.view.removerButton.setEnabled(True)'''