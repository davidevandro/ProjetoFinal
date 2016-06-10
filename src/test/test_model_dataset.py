# coding: latin1

# Script Name		: test_model_dataset.py
# Author			: David Martins
# Created			: 09/06/2016
# Last Modified		: 
# Version			: 1.0.0

# Modifications		: 

# Description		: Cont�m a classe de testes para a classe DatasetModel

import unittest2 as ut
import pandas as pd
import numpy as np
from model  import datasetmodel as dm
import csv
import os
import pandas.util.testing as pdt

class DatasetModelTest(ut.TestCase):
	'''Classe de testes unit�rios da classe DatasetModel'''
	
	def test_dados_eh_dataframe(self):
		'''Verifica se o atributo *dados* � do tipo pandas.DataFrame'''
		ds = dm.DatasetModel()
		self.assertIsInstance(ds.dados, pd.DataFrame)
		
	def test_atributos_eh_consistente_ds_vazio(self):
		'''Verifica se o atributo *atributos* de DatasetModel eh consistente 
		quando *dados* � vazio'''
		ds = dm.DatasetModel()
		self.assertEquals(ds.atributos, [])
	
	def test_atributos_eh_consistente_ds_cheio(self):
		'''Verifica se o atributo *atributos* de DatasetModel eh consistente 
		quando *dados* � n�o vazio'''
		dados = np.zeros(shape = (500, 400))
		ds = dm.DatasetModel(dados)
		#o vetor de colunas � convertido para lista para ser poss�vel a compara��o
		self.assertEquals(ds.atributos, pd.DataFrame(dados).columns.tolist())
		
	def test_natributos_eh_consistente_ds_vazio(self):
		'''Verifica se o atributo *natributos* de DatasetModel eh consistente 
		quando *dados* � vazio'''
		ds = dm.DatasetModel()
		self.assertEquals(ds.natributos,0)
		
	def test_natributos_eh_consistente_ds_cheio(self):
		'''Verifica se o atributo *natributos* de DatasetModel eh consistente 
		quando *dados* � n�o vazio'''
		dados = np.zeros(shape = (500, 400))
		ds = dm.DatasetModel(dados)
		self.assertEquals(ds.natributos, 400)
		
	def test_ninstancias_eh_consistente_ds_vazio(self):
		'''Verifica se o atributo *ninstancias* de DatasetModel eh consistente 
		quando *dados* � vazio'''
		ds = dm.DatasetModel()
		self.assertEquals(ds.ninstancias,0)
		
	def test_ninstancias_eh_consistentes_ds_cheio(self):
		'''Verifica se o atributo *ninstancias* de DatasetModel eh consistente 
		quando *dados* � n�o vazio'''
		dados = np.zeros(shape = (500, 400))
		ds = dm.DatasetModel(dados)
		self.assertEquals(ds.ninstancias, 500)
	
	def test_atualiza_atributos(self):
		'''Verifica se o m�todo atualiza_atributos atualiza os atributos *atributos*,
		*natributos* e *ninstancias* quando dados � modificado'''
		ds = dm.DatasetModel()
		dados = np.zeros(shape = (500, 400))
		ds.dados = pd.DataFrame(dados)
		ds.atualiza_atributos()
		#o vetor de colunas � convertido para lista para ser poss�vel a compara��o
		self.assertEquals(ds.atributos, pd.DataFrame(dados).columns.tolist())
		self.assertEquals(ds.natributos, 400)
		self.assertEquals(ds.ninstancias, 500)
		
	
	def test_ler_csv_carrega_dataset(self):
		'''Verifica se o m�todo ler_csv le um arquivo csv existente e carrega 
		o atributo *dados* corretamente'''
		dados = np.zeros(shape = (500,400))
		df = pd.DataFrame(dados)
		df.columns = [str(i) for i in df.columns] #os nomes dos atributos tem que ser strings
		nomeArquivo = "teste.csv"
		df.to_csv(nomeArquivo)
		ds = dm.DatasetModel()
		ds.ler_csv(nomeArquivo)
		pdt.assert_frame_equal(ds.dados,df) #verifica se os dois dataframes s�o iguais
		os.remove(nomeArquivo)
		
	def test_remover_atributo_existente(self):
		'''Verifica se o m�todo remover_atributo remove um atributo existente'''
		dados = np.zeros(shape = (500,400))
		ds = dm.DatasetModel(dados)
		ds.remover_atributo(1)
		self.assertFalse(1 in ds.atributos)
		
	def test_remover_atributo_inexistente(self):
		'''Verifica se o m�todo remover_atributo avisa sobre um atributo inexistente'''
		dados = np.zeros(shape = (500,400))
		ds = dm.DatasetModel(dados)
		self.assertFalse(ds.remover_atributo(800))
		
		
				
		
	
		
if __name__ == "__main__":
	ut.main()