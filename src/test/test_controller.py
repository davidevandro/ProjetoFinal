# coding: latin1

# Script Name		: test_controller.py
# Author			: David Martins
# Created			: 09/06/2016
# Last Modified		: 
# Version			: 1.0.0

# Modifications		: 

# Description		: Contém a classe de testes para a classe Controlador

import unittest2 as ut
import sys

from controller import controlador as ctl
from PySide.QtCore import *
from PySide.QtGui import *

class ControladorTest(ut.TestCase):
	'''Classe de testes unitários da classe DatasetModel'''
	
	def setUp(self):
		'''Cria uma instancia da classe Controlador e exibe uma tela para testes'''
		#verifica se já existe uma instancia de QApplication
		self.app = QApplication.instance()
		if not self.app:
			self.app = QApplication(sys.argv)
		self.c = ctl.Controlador()
		self.c.show()
		
	def tearDown(self):	
		'''Encerra a aplicação depois dos testes'''
		del self.app

	
	def test_dataset_nao_existe_statusbar(self):
		'''Testa o método abrir quando nenhum dataset é passado e verifica se a status
		bar da tela indica que nenhum dataset foi selecionado '''
		self.assertFalse(self.c.abrir(""))
		self.assertEquals(self.c.view.statusbar.currentMessage(), u"Nenhum dataset selecionado")
	
	def test_dataset_existe_statusbar(self):
		'''Testa o método abrir quando um dataset existente é passado e verifica se a status
		bar da tela indica que dataset foi aberto '''
		self.assertTrue(self.c.abrir("test\dados_teste.csv"))
		self.assertEquals(self.c.view.statusbar.currentMessage(), u"Dataset aberto")
	
	def test_dataset_existe_dadosgroup(self):
		'''Testa o método abrir quando um dataset existente é passado e verifica se o nome do 
		arquivo, o numero de instancias e o numero de atributos foram preenchidos corretamente
		na tela'''
		self.assertTrue(self.c.abrir("test\dados_teste.csv"))
		self.assertEquals(self.c.view.nomeLabel.text(), "dados_teste.csv")
		self.assertEquals(self.c.view.atributosLabel.text(), str(4))
		self.assertEquals(self.c.view.instanciaLabel.text(), str(5))
	
