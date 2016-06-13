# coding: latin1

# Script Name		: dataset.py
# Author			: David Martins
# Created			: 10/06/2016
# Last Modified		: 11/06/2016
# Version			: 1.0.2

# Modifications		: 1.0.1 - Atributos tornados privados e implementados getters e setters
#					  1.0.2 - Adaptação do método remover_atributo para remover_atributos

# Description		: Contém a classe que encapsula o dataset e permite algumas operações

import os

import pandas as pd


class Dataset(object):
	'''Classe que encapsula o dataset e permite algumas operações
	
	Atributos:
	
	_dados		: dataframe que armazena os dados do dataset
	_atributos	: lista de strings que armazena o nome dos _atributos
	_natributos	: inteiro que especifica quantos _atributos o dataset tem
	_ninstancias: inteiro que especifica quantas instâncias o dataset tem
	_marcados   : lista de booleanos que armazena se um atributo está selecionado
	_nomearquivo: nome do arquivo carregado com ler_csv
	'''
	
	def __init__(self, dados = [], parent = None):
		'''Construtor da classe DatasetModel. Garante que dados seja do tipo dataframe e que os demais 
		_atributos sejam consistentes com o dataset armazenado
		
		Parâmetros:
		
		dados	: dataframe ou matriz que armazena o dataset (default = [])
		'''
		self._nomearquivo = ""
		self.set_dados(dados)
		self.atualiza_atributos()
		
	def atualiza_atributos(self):
		'''Atualiza os _atributos da classe DatasetModel quando há mudança nos dados'''
		self._atributos = self._dados.columns.tolist()
		self._natributos = self._dados.shape[1]
		self._ninstancias = self._dados.shape[0]
		self._marcados = [False] * self._natributos
		
	def ler_csv(self, nome):
		'''Lê um arquivo csv e carrega DatasetModel com seus dados
		
		Parâmetros:
		
		nome	: string contendo o nome do arquivo csv
		
		Retorna:
		
		True	: se conseguir carregar o csv no DatasetModel
		False	: caso não consiga carregar o csv no DatasetModel
		'''
		try:
			self._dados = pd.DataFrame.from_csv(nome)
			
			#pega somente o nome do arquivo sem o seu endereço
			__, nomeArquivo = os.path.split(nome)
			self._nomearquivo = nomeArquivo
			
			self.atualiza_atributos()
			return True
		except:
			return False
	
	def remover_atributos(self):
		'''Remove atributos pelos nomes deles e atualiza DatasetModel'''
		indices_a_manter = [not i for i in self._marcados]
		self._dados = self._dados.loc[:,indices_a_manter]
		self.atualiza_atributos()
		
	def get_dados(self):
		'''Retorna o atributo *_dados*'''
		return self._dados
	
	def set_dados(self,dados):
		'''Atribui o valor *dados* ao atributo *_dados*'''
		self._dados = pd.DataFrame(dados)
		self.atualiza_atributos()
	
	def get_atributos(self):
		'''Retorna o atributo *_atributos*'''
		return self._atributos
		
	def get_ninstancias(self):
		'''Retorna o atributo *_ninstancias*'''
		return self._ninstancias
	
	def get_natributos(self):
		'''Retorna o atributo *_natributos*'''
		return self._natributos
	
	def get_nomearquivo(self):
		'''Retorna o atributo *_nomearquivo*'''
		return self._nomearquivo
	
	def get_marcados(self):
		'''Retorna o atributo *_marcados*'''
		return self._marcados
	
	def set_marcados(self, index, value):
		'''Atribui o valor *value* para *_marcados[index]*'''
		self._marcados[index] = value