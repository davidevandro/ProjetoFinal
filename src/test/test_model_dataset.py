# coding: latin1

# Script Name		: test_model_dataset.py
# Author			: David Martins
# Created			: 09/06/2016
# Last Modified		: 
# Version			: 1.0.0

# Modifications		: 

# Description		: Contém a classe de testes para a classe DatasetModel

import unittest2 as ut
import pandas as pd
import numpy as np
from model  import datasetmodel as dm
import csv
import os
import pandas.util.testing as pdt

class DatasetModelTest(ut.TestCase):
	'''Classe de testes unitários da classe DatasetModel'''
	
	def test_dados_eh_dataframe(self):
		'''Verifica se o atributo *dados* é do tipo pandas.DataFrame'''
		ds = dm.DatasetModel()
		self.assertIsInstance(ds.dados, pd.DataFrame)
		
	def test_atributos_eh_consistente_ds_vazio(self):
		'''Verifica se o atributo *atributos* de DatasetModel eh consistente 
		quando *dados* é vazio'''
		ds = dm.DatasetModel()
		self.assertEquals(ds.atributos, [])
	
	def test_atributos_eh_consistente_ds_cheio(self):
		'''Verifica se o atributo *atributos* de DatasetModel eh consistente 
		quando *dados* é não vazio'''
		dados = np.zeros(shape = (500, 400))
		ds = dm.DatasetModel(dados)
		#o vetor de colunas é convertido para lista para ser possível a comparação
		self.assertEquals(ds.atributos, pd.DataFrame(dados).columns.tolist())
		
	def test_natributos_eh_consistente_ds_vazio(self):
		'''Verifica se o atributo *natributos* de DatasetModel eh consistente 
		quando *dados* é vazio'''
		ds = dm.DatasetModel()
		self.assertEquals(ds.natributos,0)
		
	def test_natributos_eh_consistente_ds_cheio(self):
		'''Verifica se o atributo *natributos* de DatasetModel eh consistente 
		quando *dados* é não vazio'''
		dados = np.zeros(shape = (500, 400))
		ds = dm.DatasetModel(dados)
		self.assertEquals(ds.natributos, 400)
		
	def test_ninstancias_eh_consistente_ds_vazio(self):
		'''Verifica se o atributo *ninstancias* de DatasetModel eh consistente 
		quando *dados* é vazio'''
		ds = dm.DatasetModel()
		self.assertEquals(ds.ninstancias,0)
		
	def test_ninstancias_eh_consistentes_ds_cheio(self):
		'''Verifica se o atributo *ninstancias* de DatasetModel eh consistente 
		quando *dados* é não vazio'''
		dados = np.zeros(shape = (500, 400))
		ds = dm.DatasetModel(dados)
		self.assertEquals(ds.ninstancias, 500)
	
	def test_atualiza_atributos(self):
		'''Verifica se o método atualiza_atributos atualiza os atributos *atributos*,
		*natributos* e *ninstancias* quando dados é modificado'''
		ds = dm.DatasetModel()
		dados = np.zeros(shape = (500, 400))
		ds.dados = pd.DataFrame(dados)
		ds.atualiza_atributos()
		#o vetor de colunas é convertido para lista para ser possível a comparação
		self.assertEquals(ds.atributos, pd.DataFrame(dados).columns.tolist())
		self.assertEquals(ds.natributos, 400)
		self.assertEquals(ds.ninstancias, 500)
		
	
	def test_ler_csv_carrega_dataset(self):
		'''Verifica se o método ler_csv le um arquivo csv existente e carrega 
		o atributo *dados* corretamente'''
		dados = np.zeros(shape = (500,400))
		df = pd.DataFrame(dados)
		df.columns = [str(i) for i in df.columns] #os nomes dos atributos tem que ser strings
		nomeArquivo = "teste.csv"
		df.to_csv(nomeArquivo)
		ds = dm.DatasetModel()
		ds.ler_csv(nomeArquivo)
		pdt.assert_frame_equal(ds.dados,df) #verifica se os dois dataframes são iguais
		os.remove(nomeArquivo)
		
	def test_remover_atributo_existente(self):
		'''Verifica se o método remover_atributo remove um atributo existente'''
		dados = np.zeros(shape = (500,400))
		ds = dm.DatasetModel(dados)
		ds.remover_atributo(1)
		self.assertFalse(1 in ds.atributos)
		
	def test_remover_atributo_inexistente(self):
		'''Verifica se o método remover_atributo avisa sobre um atributo inexistente'''
		dados = np.zeros(shape = (500,400))
		ds = dm.DatasetModel(dados)
		self.assertFalse(ds.remover_atributo(800))
		
		
				
		
	
		
if __name__ == "__main__":
	ut.main()