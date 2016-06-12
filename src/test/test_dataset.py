# coding: latin1

# Script Name		: test_model_dataset.py
# Author			: David Martins
# Created			: 09/06/2016
# Last Modified		: 11/06/2016
# Version			: 1.0.2
# Modifications		: 1.0.2 - Inclus�o de novo teste para aumentar cobertura de c�digo

# Description		: Cont�m a classe de testes para a classe Dataset

import unittest2 as ut
import pandas as pd
import numpy as np
from data import dataset as dm
import os
import pandas.util.testing as pdt

class DatasetTest(ut.TestCase):
	'''Classe de testes unit�rios da classe Dataset'''
	
	def test_dados_eh_dataframe(self):
		'''Verifica se o atributo *_dados* � do tipo pandas.DataFrame'''
		ds = dm.Dataset()
		self.assertIsInstance(ds.get_dados(), pd.DataFrame)
		
	def test_atributos_eh_consistente_ds_vazio(self):
		'''Verifica se o atributo *_atributos* de Dataset eh consistente 
		quando *_dados* � vazio'''
		ds = dm.Dataset()
		self.assertEquals([], ds.get_atributos())
	
	def test_atributos_eh_consistente_ds_cheio(self):
		'''Verifica se o atributo *_atributos* de Dataset eh consistente 
		quando *_dados* � n�o vazio'''
		dados = np.zeros(shape = (5, 4))
		ds = dm.Dataset(dados)
		#o vetor de colunas � convertido para lista para ser poss�vel a compara��o
		self.assertEquals(pd.DataFrame(dados).columns.tolist(), ds.get_atributos())
		
	def test_natributos_eh_consistente_ds_vazio(self):
		'''Verifica se o atributo *_natributos* de Dataset eh consistente 
		quando *_dados* � vazio'''
		ds = dm.Dataset()
		self.assertEquals(0, ds.get_natributos())
		
	def test_natributos_eh_consistente_ds_cheio(self):
		'''Verifica se o atributo *_natributos* de Dataset eh consistente 
		quando *_dados* � n�o vazio'''
		dados = np.zeros(shape = (5, 4))
		ds = dm.Dataset(dados)
		self.assertEquals(4, ds.get_natributos())
		
	def test_ninstancias_eh_consistente_ds_vazio(self):
		'''Verifica se o atributo *_ninstancias* de Dataset eh consistente 
		quando *_dados* � vazio'''
		ds = dm.Dataset()
		self.assertEquals(0, ds.get_ninstancias())
		
	def test_ninstancias_eh_consistentes_ds_cheio(self):
		'''Verifica se o atributo *_ninstancias* de Dataset eh consistente 
		quando *_dados* � n�o vazio'''
		dados = np.zeros(shape = (5, 4))
		ds = dm.Dataset(dados)
		self.assertEquals(5, ds.get_ninstancias())
	
	def test_atualiza_atributos(self):
		'''Verifica se o m�todo atualiza_atributos atualiza os _atributos *_atributos*,
		*_natributos* e *_ninstancias* quando *_dados* � modificado'''
		ds = dm.Dataset()
		dados = np.zeros(shape = (5, 4))
		ds.set_dados(dados)
		ds.atualiza_atributos()
		#o vetor de colunas � convertido para lista para ser poss�vel a compara��o
		self.assertEquals(pd.DataFrame(dados).columns.tolist(), ds.get_atributos())
		self.assertEquals(4, ds.get_natributos())
		self.assertEquals(5, ds.get_ninstancias())
		
	
	def test_ler_csv_nao_existente(self):
		'''Verifica se o m�todo ler_csv retorna Falso quando o recebe o 
		nome de um arquivo csv inexiste'''
		ds = dm.Dataset()
		self.assertFalse(ds.ler_csv("blah.csv"))
	
	def test_ler_csv_existente_carrega_dataset(self):
		'''Verifica se o m�todo ler_csv le um arquivo csv existente e carrega 
		o atributo *_dados* corretamente'''
		dados = np.zeros(shape = (5,4))
		df = pd.DataFrame(dados)
		df.columns = [str(i) for i in df.columns] #os nomes dos _atributos tem que ser strings
		nomeArquivo = "teste.csv"
		df.to_csv(nomeArquivo)
		ds = dm.Dataset()
		ds.ler_csv(nomeArquivo)
		pdt.assert_frame_equal(df, ds.get_dados()) #verifica se os dois dataframes s�o iguais
		os.remove(nomeArquivo)
		
	def test_remover_atributo_existente(self):
		'''Verifica se o m�todo remover_atributo remove um atributo existente'''
		dados = np.zeros(shape = (5,4))
		ds = dm.Dataset(dados)
		ds.remover_atributos([1])
		self.assertFalse(1 in ds.get_atributos())
		
	def test_remover_atributo_inexistente(self):
		'''Verifica se o m�todo remover_atributo avisa sobre um atributo inexistente'''
		dados = np.zeros(shape = (5,4))
		ds = dm.Dataset(dados)
		self.assertFalse(ds.remover_atributos([8]))	
		
if __name__ == "__main__":
	ut.main()