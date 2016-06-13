# coding: latin1

# Script Name        : model_dataset.py
# Author            : David Martins
# Created            : 09/06/2016
# Last Modified        : 
# Version            : 1.0.0

# Modifications        : 

# Description        : Cont�m a classe DatasetModel que serve de modelo para a tabela de atributos do dataset

from PySide.QtCore import QAbstractTableModel, Qt

from data.dataset import Dataset


class DatasetModel(QAbstractTableModel):
    '''Classe que serve de modelo para a view de tabela de atributos do dataset
    
    Atributos:
    
    _dataset    : objeto Dataset que cont�m os dados
    '''
    
    def __init__(self, dataset = Dataset(), parent = None):
        '''Construtor de DatasetModel. 
        
        Par�metros:
        
        dataset    : objeto Dataset para ser atribu�do a *_dataset*
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
        '''Indica quais flags est�o ativos para cada item
        
        Par�metros:
        
        index:    QIndexModel contendo linha e coluna de um item'''
        if index.column() == 0:
            #itens da primeira coluna devem ser marc�veis, selecion�veis e n�o edit�veis
            return Qt.ItemIsUserCheckable | Qt.ItemIsEnabled |Qt.ItemIsSelectable
        else:
            #itens da segunda coluna devem ser selecion�veis n�o edit�veis
            return Qt.ItemIsEnabled |Qt.ItemIsSelectable
        
    
    def data(self, index, role):
        '''Retorna os dados e como eles devem ser dispostos dependendo do tipo de contexto (role)
        
        Par�metros:
        
        index:    QIndexModel contendo linha e coluna de um item
        role:     Contexto da atividade (exibi��o, alinhamento, checagem do status, edi��o,...)
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
        
        Par�metros:
        
        index:    QIndexModel contendo linha e coluna de um item
        value:    Novo valor do item indexado por index
        role:     Contexto da atividade (exibi��o, alinhamento, checagem do status, edi��o,...)
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
        '''Retorna os cabe�alhos e como eles devem ser dispostos dependendo do tipo de 
        atividade sendo executada pelo usu�rio (role)
        
        Par�metros:
        
        section:      Indice da coluna ou da linha
        orientation:  Horizontal ou vertical
        role:         Contexto da atividade (exibi��o, alinhamento, checagem do status, edi��o,...)
        
        '''
        headers = ["","Atributo"]
        if role ==  Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return headers[section]
            if orientation == Qt.Vertical:
                return section+1
    