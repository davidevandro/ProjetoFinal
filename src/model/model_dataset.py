# coding: latin1

# Script Name        : model_dataset.py
# Author            : David Martins
# Created            : 09/06/2016
# Last Modified        : 
# Version            : 1.0.0

# Modifications        : 

# Description        : Contém a classe DatasetModel que serve de modelo para a tabela de atributos do dataset

from PySide.QtCore import QAbstractTableModel, Qt

from data.dataset import Dataset


class DatasetModel(QAbstractTableModel):
    '''Classe que serve de modelo para a view de tabela de atributos do dataset
    
    Atributos:
    
    _dataset    : objeto Dataset que contém os dados
    '''
    
    def __init__(self, dataset = Dataset(), parent = None):
        '''Construtor de DatasetModel. 
        
        Parâmetros:
        
        dataset    : objeto Dataset para ser atribuído a *_dataset*
        '''
        QAbstractTableModel.__init__(self, parent)
        self._dataset = dataset
    
    def get_dataset(self):
        '''Obtem o atributo _dataset'''
        return self._dataset
    
    def rowCount(self, parent):
        '''Retorna o total de linhas na tabela de dados. No caso, deve ser igual ao 
        total de atributos do Dataset'''
        return self._dataset.get_natributos()
    
    def columnCount(self, parent):
        '''Retorna o total de colunas na tabela de dados. No caso, deve ser igual a
        2 (uma coluna para a checkbox e outra para o nome do atributo)'''
        return 2
    
    def flags(self, index):
        '''Indica quais flags estão ativos para cada item
        
        Parâmetros:
        
        index:    QIndexModel contendo linha e coluna de um item'''
        if index.column() == 0:
            #itens da primeira coluna devem ser marcáveis, selecionáveis e não editáveis
            return Qt.ItemIsUserCheckable | Qt.ItemIsEnabled |Qt.ItemIsSelectable
        else:
            #itens da segunda coluna devem ser selecionáveis não editáveis
            return Qt.ItemIsEnabled |Qt.ItemIsSelectable
        
    
    def data(self, index, role):
        '''Retorna os dados e como eles devem ser dispostos dependendo do tipo de contexto (role)
        
        Parâmetros:
        
        index:    QIndexModel contendo linha e coluna de um item
        role:     Contexto da atividade (exibição, alinhamento, checagem do status, edição,...)
        '''
        
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        
        if role ==  Qt.CheckStateRole:
            row = index.row()
            column = index.column()
            if column == 0:
                return self._dataset.get_marcados()[row]        
        
        if role ==  Qt.DisplayRole:
            row = index.row()
            column = index.column()
            if column == 0:
                return ""
            elif column == 1:
                return self._dataset.get_atributos()[row]
            elif column == 2:
                return self._dataset.get_nomearquivo()
            elif column == 3:
                return str(self._dataset.get_natributos())
            elif column == 4:    
                return str(self._dataset.get_ninstancias())
            
    def setData(self, index, value, role):
        '''Permite modificar os dados na view
        
        Parâmetros:
        
        index:    QIndexModel contendo linha e coluna de um item
        value:    Novo valor do item indexado por index
        role:     Contexto da atividade (exibição, alinhamento, checagem do status, edição,...)
        '''
        if role == Qt.CheckStateRole:
            row = index.row()
            column = index.column()
            #somente permite mudar o status da checkbox
            if column == 0:
                self._dataset.set_marcados(row, value)
                self.dataChanged.emit(index, index)
                return True
        return False
            
    def headerData(self, section, orientation, role):
        '''Retorna os cabeçalhos e como eles devem ser dispostos dependendo do tipo de 
        atividade sendo executada pelo usuário (role)
        
        Parâmetros:
        
        section:      Indice da coluna ou da linha
        orientation:  Horizontal ou vertical
        role:         Contexto da atividade (exibição, alinhamento, checagem do status, edição,...)
        
        '''
        headers = ["","Atributo"]
        if role ==  Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return headers[section]
            if orientation == Qt.Vertical:
                return section+1
    