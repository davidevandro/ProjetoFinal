# coding: latin1

# Script Name		: test_model_database.py
# Author			: David Martins
# Created			: 09/06/2016
# Last Modified		: 
# Version			: 1.0.0

# Modifications		: 

# Description		: Contém a classe de testes para a classe DatasetModel

import unittest2 as ut
import pandas as pd

class DatasetModelTest(ut.TestCase):
	'''Classe de testes unitários da classe DatasetModel'''
	
	def test_dados_eh_dataframe(self):
		'Verifica se o atributo dados é do tipo pandas.DataFrame'
		df = DataframeModel()
		self.assertIsInstance(df.dados, pd.DataFrame)
		
if __name__ == "__main__":
	ut.main()