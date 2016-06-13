# coding: latin1

# Script Name        : model_estatistica_numerica.py
# Author            : David Martins
# Created            : 09/06/2016
# Last Modified        : 
# Version            : 1.0.0

# Modifications        : 

# Description        : Contém a classe EstatisticaNominalModel que serve de modelo para a tabela 
#                      de estatisticas de um atributo nominal

from PySide.QtCore import QAbstractTableModel, Qt


class EstatisticaNominalModel(QAbstractTableModel):
    '''Classe que serve de modelo para a view de tabela de estatisticas de um atributo
    nominal do dataset
    
    Atributos:
    
    _dados    : lista das instancias do atributo
    _estatistica: lista de estatistica dos dados
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
        '''Retorna o total de linhas na tabela de estatisticas. No caso, deve ser igual ao 
         numero de labels'''
        return len(self._dados.unique())
    
    def columnCount(self, parent):
        '''Retorna o total de colunas na tabela de dados. No caso, deve ser igual a
        2 (uma para as labels e outra para as contagens)'''
        return 2
    
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
            column = index.column()
            if column == 0:
                return self._dados.unique()[row]
            elif column == 1:
                return str(sum(self._dados == self._dados.unique()[row]))
                      
    def headerData(self, section, orientation, role):
        '''Retorna os cabeçalhos e como eles devem ser dispostos dependendo do tipo de 
        atividade sendo executada pelo usuário (role)
        
        Parâmetros:
        
        section:      Indice da coluna ou da linha
        orientation:  Horizontal ou vertical
        role:         Contexto da atividade (exibição, alinhamento, checagem do status, edição,...)
        
        '''
        headers = ["Labels", "Contagem"]
        if role ==  Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return headers[section]
            if orientation == Qt.Vertical:
                return section + 1
    