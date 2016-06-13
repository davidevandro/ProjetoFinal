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
		atualiza a aba Dados da tela
		
		Parâmetros:
		
		nome: String contendo o nome completo do arquivo (nome + caminho)
		
		Retorna:
		
		True: 	se conseguir abrir o dataset em csv
		False: 	caso não consiga abrir o arquivo csv
		'''
				
		self._view.statusbar.showMessage(u"Abrindo dataset...")
		if self._dataset.ler_csv(nome):
			
			self.limpar_tabela_atributos()
			self.carregar_dados_tabela_atributos()
			self.atualizar_grupo_dados(nome)
			self._view.statusbar.showMessage(u"Dataset aberto")			
			
			return True
		else:
			self._view.statusbar.showMessage(u"Nenhum dataset selecionado")
			return False
		
	def limpar_tabela_atributos(self):
		'''Limpa a *tabelaAtributos* da *_view* para poder carregar novos dados'''
		for i in reversed(range(self._view.tabelaAtributos.rowCount())):
				self._view.tabelaAtributos.removeRow(i)
				
	def carregar_dados_tabela_atributos(self):
		'''Carrega os dados de um dataset aberto pelo usuário em *tabelaAtributos*'''
		atributos = self._dataset.get_atributos()
		#carrega o dataset numa tabela mostrada na aba Dados		
		for i in range(self._dataset.get_natributos()):
			currentRowCount = self._view.tabelaAtributos.rowCount()
			self._view.tabelaAtributos.insertRow(currentRowCount)
			item0 = QTableWidgetItem(str(i+1))
			item0.setFlags(Qt.ItemIsEnabled)
			item0.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
			self._view.tabelaAtributos.setItem(currentRowCount, 0, item0)
			item1 = QTableWidgetItem("")
			#para tornar o item da tabela marcável
			item1.setFlags(Qt.ItemIsEnabled| Qt.ItemIsUserCheckable)
			item1.setCheckState(Qt.Unchecked)
			item1.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
			self._view.tabelaAtributos.setItem(currentRowCount,1, item1)
			item2 = QTableWidgetItem(atributos[i])
			item2.setFlags(Qt.ItemIsEnabled)
			item2.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
			self._view.tabelaAtributos.setItem(currentRowCount,2, item2)
	
	def atualizar_grupo_dados(self, nome):
		'''Atualiza o nome do arquivo, o número de instâncias e o número de atributos na tela
		
		Parâmetros:
		
		nome: String contendo o nome completo do arquivo (nome + caminho)
		'''
		#pega somente o nome do arquivo sem o seu endereço
		__, nomeArquivo = os.path.split(nome)
			
		self._view.nomeLabel.setText(nomeArquivo)
		self._view.instanciaLabel.setText(str(self._dataset.get_ninstancias()))
		self._view.atributosLabel.setText(str(self._dataset.get_natributos()))
		
	def atualizar_botao_remover(self, item):
		'''Ativa/desativa o *removerButton* de acordo com a contagem de checkboxes preenchidas
		
		Parâmetros:
		
		item:	QTableWidget item marcado/clicado pelo usuário
		'''		
		#se não há checkbox marcada, desativa botão de remover
		if self.contar_checkboxes_marcadas() == 0:
			self._view.removerButton.setEnabled(False)
		else:
			self._view.removerButton.setEnabled(True)
			
	def contar_checkboxes_marcadas(self):
		'''Conta quantas checkboxes estão marcadas
		
		Retorna:
		
		ativos:	quantidade de checkboxes marcadas'''		
		ativos = 0
		
		#loop percorre as checkboxes para contar quantas estão marcadas
		for i in range(self._view.tabelaAtributos.rowCount()):
			if self._view.tabelaAtributos.item(i,1).checkState() == Qt.Checked:
				ativos += 1
		
		return ativos
	
			