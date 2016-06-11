# coding: latin1

# Script Name		: test_model_dataset.py
# Author			: David Martins
# Created			: 09/06/2016
# Last Modified		: 11/06/2016
# Version			: 1.0.2
# Modifications		: 1.0.2 - Inclusão de novo teste para aumentar cobertura de código

# Description		: Contém a classe de testes para a classe DatasetModel

import unittest2 as ut
import pandas as pd
import numpy as np
from model  import datasetmodel as dm
import os
import pandas.util.testing as pdt

class DatasetModelTest(ut.TestCase):
	'''Classe de testes unitários da classe DatasetModel'''
	
	def test_dados_eh_dataframe(self):
		'''Verifica se o atributo *_dados* é do tipo pandas.DataFrame'''
		ds = dm.DatasetModel()
		self.assertIsInstance(ds.get_dados(), pd.DataFrame)
		
	def test_atributos_eh_consistente_ds_vazio(self):
		'''Verifica se o atributo *_atributos* de DatasetModel eh consistente 
		quando *_dados* é vazio'''
		ds = dm.DatasetModel()
		self.assertEquals([], ds.get_atributos())
	
	def test_atributos_eh_consistente_ds_cheio(self):
		'''Verifica se o atributo *_atributos* de DatasetModel eh consistente 
		quando *_dados* é não vazio'''
		dados = np.zeros(shape = (5, 4))
		ds = dm.DatasetModel(dados)
		#o vetor de colunas é convertido para lista para ser possível a comparação
		self.assertEquals(pd.DataFrame(dados).columns.tolist(), ds.get_atributos())
		
	def test_natributos_eh_consistente_ds_vazio(self):
		'''Verifica se o atributo *_natributos* de DatasetModel eh consistente 
		quando *_dados* é vazio'''
		ds = dm.DatasetModel()
		self.assertEquals(0, ds.get_natributos())
		
	def test_natributos_eh_consistente_ds_cheio(self):
		'''Verifica se o atributo *_natributos* de DatasetModel eh consistente 
		quando *_dados* é não vazio'''
		dados = np.zeros(shape = (5, 4))
		ds = dm.DatasetModel(dados)
		self.assertEquals(4, ds.get_natributos())
		
	def test_ninstancias_eh_consistente_ds_vazio(self):
		'''Verifica se o atributo *_ninstancias* de DatasetModel eh consistente 
		quando *_dados* é vazio'''
		ds = dm.DatasetModel()
		self.assertEquals(0, ds.get_ninstancias())
		
	def test_ninstancias_eh_consistentes_ds_cheio(self):
		'''Verifica se o atributo *_ninstancias* de DatasetModel eh consistente 
		quando *_dados* é não vazio'''
		dados = np.zeros(shape = (5, 4))
		ds = dm.DatasetModel(dados)
		self.assertEquals(5, ds.get_ninstancias())
	
	def test_atualiza_atributos(self):
		'''Verifica se o método atualiza_atributos atualiza os _atributos *_atributos*,
		*_natributos* e *_ninstancias* quando *_dados* é modificado'''
		ds = dm.DatasetModel()
		dados = np.zeros(shape = (5, 4))
		ds.set_dados(dados)
		ds.atualiza_atributos()
		#o vetor de colunas é convertido para lista para ser possível a comparação
		self.assertEquals(pd.DataFrame(dados).columns.tolist(), ds.get_atributos())
		self.assertEquals(4, ds.get_natributos())
		self.assertEquals(5, ds.get_ninstancias())
		
	
	def test_ler_csv_nao_existente(self):
		'''Verifica se o método ler_csv retorna Falso quando o recebe o 
		nome de um arquivo csv inexiste'''
		ds = dm.DatasetModel()
		self.assertFalse(ds.ler_csv("blah.csv"))
	
	def test_ler_csv_existente_carrega_dataset(self):
		'''Verifica se o método ler_csv le um arquivo csv existente e carrega 
		o atributo *_dados* corretamente'''
		dados = np.zeros(shape = (5,4))
		df = pd.DataFrame(dados)
		df.columns = [str(i) for i in df.columns] #os nomes dos _atributos tem que ser strings
		nomeArquivo = "teste.csv"
		df.to_csv(nomeArquivo)
		ds = dm.DatasetModel()
		ds.ler_csv(nomeArquivo)
		pdt.assert_frame_equal(df, ds.get_dados()) #verifica se os dois dataframes são iguais
		os.remove(nomeArquivo)
		
	def test_remover_atributo_existente(self):
		'''Verifica se o método remover_atributo remove um atributo existente'''
		dados = np.zeros(shape = (5,4))
		ds = dm.DatasetModel(dados)
		ds.remover_atributos([1])
		self.assertFalse(1 in ds.get_atributos())
		
	def test_remover_atributo_inexistente(self):
		'''Verifica se o método remover_atributo avisa sobre um atributo inexistente'''
		dados = np.zeros(shape = (5,4))
		ds = dm.DatasetModel(dados)
		self.assertFalse(ds.remover_atributos([8]))	
		
if __name__ == "__main__":
	ut.main()