# coding: latin1

# Script Name		: dataset.py
# Author			: David Martins
# Created			: 10/06/2016
# Last Modified		: 11/06/2016
# Version			: 1.0.2

# Modifications		: 1.0.1 - Atributos tornados privados e implementados getters e setters
#					  1.0.2 - Adaptação do método remover_atributo para remover_atributos

# Description		: Contém a classe que encapsula o dataset e permite algumas operações

import pandas as pd

class Dataset(object):
	'''Classe que encapsula o dataset e permite algumas operações
	
	Atributos:
	
	_dados		: dataframe que armazena os dados do dataset
	_atributos	: lista de strings que armazena o nome dos _atributos
	_natributos	: inteiro que especifica quantos _atributos o dataset tem
	_ninstancias	: inteiro que especifica quantas instâncias o dataset tem
	'''
	
	def __init__(self, dados = [], parent = None):
		'''Construtor da classe DatasetModel. Garante que dados seja do tipo dataframe e que os demais 
		_atributos sejam consistentes com o dataset armazenado
		
		Parâmetros:
		
		dados	: dataframe ou matriz que armazena o dataset (default = [])
		'''
		self.set_dados(dados)
		self.atualiza_atributos()
		
	def atualiza_atributos(self):
		'''Atualiza os _atributos da classe DatasetModel quando há mudança nos dados'''
		self._atributos = self._dados.columns.tolist()
		self._natributos = self._dados.shape[1]
		self._ninstancias = self._dados.shape[0]
		
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
			self.atualiza_atributos()
			return True
		except:
			return False
	
	def remover_atributos(self, atributos):
		'''Remove atributos pelos nomes deles e atualiza DatasetModel
		
		Parâmetros:
		
		atributos: lista de strings contendo os nomes do atributos a serem removido
		
		Retorna:
		
		True:	se conseguir remover todos os atributos
		False:	se algum atributo não for válido
		'''
		for elemento in atributos:
			if elemento not in self._atributos:
				return False
			
		for elemento in atributos:
			self._dados.pop(elemento)
					
		self.atualiza_atributos()
		return True
		
	def get_dados(self):
		'''Retorna o atributo *_dados*'''
		return self._dados
	
	def set_dados(self,dados):
		'''Atribui o valor *dados* ao atributo *_dados*'''
		self._dados = pd.DataFrame(dados)
	
	def get_atributos(self):
		'''Retorna o atributo *_atributos*'''
		return self._atributos
		
	def get_ninstancias(self):
		'''Retorna o atributo *_ninstancias*'''
		return self._ninstancias
	
	def get_natributos(self):
		'''Retorna o atributo *_natributos*'''
		return self._natributos