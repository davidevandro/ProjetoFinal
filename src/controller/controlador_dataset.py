# coding: latin1

# Script Name		: controlador.py
# Author			: David Martins
# Created			: 12/06/2016
# Last Modified		: 
# Version			: 1.0.0

# Modifications		: 

# Description		: Contém a classe que controla a atualização das telas e adquire os dados dos modelos

from PySide.QtCore import Qt
from PySide.QtGui import QMainWindow, QFileDialog, QTableView

from data.dataset import Dataset
from model.model_dataset import DatasetModel
from model.model_estatistica_nominal import EstatisticaNominalModel
from model.model_estatistica_numerica import EstatisticaNumericaModel
from view.mainGui import Ui_MainWindow


class ControladorDataset(QMainWindow):
	'''Classe que controla e atualiza as telas com base nos dados adquiridos das classes de modelo
	
	Atributos:
	
	_view			: MainGui que o controlador está controlando
	_dataset		: DatasetModel com os dados carregados através da tela
	'''
	
	def __init__(self, view, parent = None):
		'''Construtor da classe Controlador. Inicia seus atributos e conecta os sinais dos botões da tela
		a métodos
		
		Parâmetros:
		
		view:	: MainGui que o controlador está controlando
		'''
		super(ControladorDataset, self).__init__(parent)
		
		#conecta o controlador a view
		self._view = view
		self._view.setupUi(self)
		
		self._dataset = Dataset()	
		
		#conecta controlador ao modelo dos dados a ser usado
		#pelos elementos da view
		self._datasetmodel = DatasetModel(self._dataset)
		
		#conecta os sinais dos botões e das ações do usuário na tela a funções
		self._view.abrirButton.clicked.connect(self.abrir_janela_para_escolher_arquivo)
		self._view.tabelaAtributos.entered.connect(self.atualizar_atributo_selecionado)
		self._view.tabelaAtributos.clicked.connect(self.atualizar_atributo_selecionado)
		self._view.removerButton.clicked.connect(self.remover_atributos)
		
		#modifica parâmetros da view
		self._view.tabelaAtributos.setSelectionBehavior(QTableView.SelectRows)
		self._view.tabelaAtributos.setSelectionMode(QTableView.SingleSelection)
		self._view.tabelaEstatistica.setFocusPolicy(Qt.NoFocus)
		
		#atribui os modelos aos elementos da tela 
		self._view.tabelaAtributos.setModel(self._datasetmodel)
	
		
	def abrir_janela_para_escolher_arquivo(self):
		'''Abre uma janela para o usuário escolher um arquivo e chama o método abrir'''
	
		#o endereço do arquivo + nome estão no primeiro campo de nome
		nome = QFileDialog.getOpenFileName(self, "Abrir", "", "Arquivos de Texto (*.csv)")[0]
		self.abrir(nome)	
		
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
		#avisa que o modelo vai mudar
		
		if self._dataset.ler_csv(nome):

			self._datasetmodel.beginResetModel()
			self.atualizar_grupo_dados()
			self._view.statusbar.showMessage(u"Dataset aberto")		
			#avisa que o modelo encerrou a mudança
			self._datasetmodel.endResetModel()
			return True
		else:
			self._view.statusbar.showMessage(u"Nenhum dataset selecionado")
			return False
		
	def atualizar_grupo_dados(self):
		'''Atualiza os dados na tela sobre o dataset (nome, instancias e atributos)'''
		
		self._view.nomeLabel.setText(self._dataset.get_nomearquivo())
		self._view.atributosLabel.setText(str(self._dataset.get_natributos()))
		self._view.instanciaLabel.setText(str(self._dataset.get_ninstancias()))
	
	def atualizar_botao_remover(self):
		'''Ativa/desativa o *removerButton* de acordo com a contagem de checkboxes preenchidas'''	
			
		#se não há checkbox marcada, desativa botão de remover
		if sum(self._dataset.get_marcados()) == 0:
			self._view.removerButton.setEnabled(False)
		else:
			self._view.removerButton.setEnabled(True)
			
	def atualizar_atributo_selecionado(self, indiceClicado = None):	
		'''Atualiza os dados do atributo na tela (nome, ausentes, distintos, tipo, estatisticas)
		e chama atualiza_botão_remover caso uma checkbox seja marcada ou desmarcada
		
		Parâmetros:
		
		indiceCLicado: QModelIndex contendo a posição do item clicado
		'''
		
		#o método foi acionado a partir de remover dados
		#nesse caso, deve mostrar os dados do atributo na primeira linha
		if indiceClicado is None:
			row = 0
			column = 1
		else:
			row = indiceClicado.row()
			column = indiceClicado.row()
		
		#se o usuario marcar uma checkbox
		if column == 0:
			self.atualizar_botao_remover()
		
		#encontra o nome do atributo selecionado
		atributo = self._dataset.get_atributos()[row]
		#encontra a coluna do dataframe relativa ao atributo
		dados_atributo = self._dataset.get_dados()[atributo]
		#calcula estatisticas sobre a coluna
		estatisticas = dados_atributo.describe()
		#calcula o número de dados ausentes
		ausentes = int(len(dados_atributo) - estatisticas['count'])
		pct_ausentes = int(100 * ausentes / len(dados_atributo))
		#coluna contém strings
		if 'unique' in estatisticas:
			distintos = estatisticas['unique']
			tipo = "Nominal"
			self._view.tabelaEstatistica.setModel(EstatisticaNominalModel(dados_atributo))
		#coluna contém números
		else:		
			distintos = len(dados_atributo.unique())
			tipo = "Numérico"
			self._view.tabelaEstatistica.setModel(EstatisticaNumericaModel(dados_atributo))
		
		#atualiza os dados do atributo na tela
		self._view.nomeAtributoLabel.setText(atributo)	
		self._view.ausentesLabel.setText("%d (%d%%)" % (ausentes, pct_ausentes))
		self._view.tipoLabel.setText(tipo)
		self._view.distintosLabel.setText(str(distintos))
		
	def remover_atributos(self):
		'''Remove os atributos com as checkboxes selecionadas'''
		self._datasetmodel.beginResetModel()
		self._dataset.remover_atributos()
		self._datasetmodel.endResetModel()
		self.atualizar_grupo_dados()
		self.atualizar_atributo_selecionado()