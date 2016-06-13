# coding: latin1

# Script Name        : model_estatistica_numerica.py
# Author            : David Martins
# Created            : 09/06/2016
# Last Modified        : 
# Version            : 1.0.0

# Modifications        : 

# Description        : Contém a classe EstatisticaNominalModel que serve de modelo para a tabela 
#                      de estatisticas de um atributo numerico

from PySide.QtCore import QAbstractTableModel, Qt


class EstatisticaNumericaModel(QAbstractTableModel):
    '''Classe que serve de modelo para a view de tabela de estatisticas de um atributo
    numerico do dataset
    
    Atributos:
    
    _dados    : lista das instancias do atributo
    _estatistica: list de estatisticas dos dados
    '''
    
    def __init__(self, dados = [], parent = None):
        '''Construtor de DatasetModel. 
        
        Parâmetros:
        
        dados   : objeto Dataset para ser atribuído a *_dataset*
        '''
        QAbstractTableModel.__init__(self, parent)
        self._dados = dados
        self._estatistica = dados.describe()
    
    def get_dataset(self):
        '''Obtem o atributo _dados'''
        return self._dados
    
    def rowCount(self, parent):
        '''Retorna o total de linhas na tabela de estatisticas. No caso, deve ser igual a 
        4 (mínimo, máximo, média e desvio padrão)'''
        return 4
    
    def columnCount(self, parent):
        '''Retorna o total de colunas na tabela de dados. No caso, deve ser igual a
        1 (para os valores das estatisticas)'''
        return 1
    
    def flags(self, index):
        '''Indica quais flags estão ativos para cada item
         
        Parâmetros:
         
        index:    QIndexModel contendo linha e coluna de um item'''
        return Qt.NoItemFlags
        
    
    def data(self, index, role):
        '''Retorna os dados e como eles devem ser dispostos dependendo do tipo de contexto (role)
        
        Parâmetros:
        
        index:    QIndexModel contendo linha e coluna de um item
        role:     Contexto da atividade (exibição, alinhamento, checagem do status, edição,...)
        '''
        
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter 
        
        if role ==  Qt.DisplayRole:
            row = index.row()
            if row == 0:
                return "%.2f" % self._estatistica['min']
            elif row == 1:
                return "%.2f" % self._estatistica['max']
            elif row == 2:
                return "%.2f" % self._estatistica['mean']
            elif row == 3:
                return "%.2f" % self._estatistica['std']
                      
    def headerData(self, section, orientation, role):
        '''Retorna os cabeçalhos e como eles devem ser dispostos dependendo do tipo de 
        atividade sendo executada pelo usuário (role)
        
        Parâmetros:
        
        section:      Indice da coluna ou da linha
        orientation:  Horizontal ou vertical
        role:         Contexto da atividade (exibição, alinhamento, checagem do status, edição,...)
        
        '''
        headers = ["Valor"]
        labels = ["Mínimo", "Máximo", "Média", "Desvio Padrão"]
        if role ==  Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return headers[section]
            if orientation == Qt.Vertical:
                return labels[section]
    