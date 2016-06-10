# coding: latin1

# Script Name		: datasetmodel.py
# Author			: David Martins
# Created			: 10/06/2016
# Last Modified		: 
# Version			: 1.0.0

# Modifications		: 

# Description		: Contém a classe que encapsula o dataset e permite algumas operações

import pandas as pd
import csv

class DatasetModel():
	'''Classe que encapsula o dataset e permite algumas operações
	
	Atributos:
	
	dados		: dataframe que armazena os dados do dataset
	atributos	: lista de strings que armazena o nome dos atributos
	natributos	: inteiro que especifica quantos atributos o dataset tem
	ninstancias	: inteiro que especifica quantas instâncias o dataset tem
	'''
	
	def __init__(self, dados = []):
		'''Construtor da classe DatasetModel. Garante que dados seja do tipo dataframe e que os demais 
		atributos sejam consistentes com o dataset armazenado
		
		Atributos:
		
		dados	: dataframe ou matriz que armazena o dataset (default = [])
		'''
		self.dados = pd.DataFrame(dados)
		self.atualiza_atributos()
		
	def atualiza_atributos(self):
		'''Atualiza os atributos da classe DatasetModel quando há mudança nos dados'''
		self.atributos = self.dados.columns.tolist()
		self.natributos = self.dados.shape[1]
		self.ninstancias = self.dados.shape[0]
		
	def ler_csv(self, nome):
		'''Lê um arquivo csv e carrega DatasetModel com seus dados
		
		Atributos:
		
		nome	: string contendo o nome do arquivo csv
		'''
		
		self.dados = pd.DataFrame.from_csv(nome)
		self.atualiza_atributos()
	
	def remover_atributo(self, nomeAtributo):
		'''Remove um atributo pelo nome dele e atualiza DatasetModel
		
		Atributos:
		
		nomeAtributo: string contendo o nome do atributo a ser removido
		'''
		
		if nomeAtributo in self.atributos:
			self.dados.pop(nomeAtributo)
			self.atualiza_atributos()
			return True
		else:
			return False
		
		