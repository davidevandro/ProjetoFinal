from PySide.QtCore import QAbstractTableModel, Qt


class DatasetModel(QAbstractTableModel):
    def rowCount(self, parent):
        '''Override de m�todo de QAbstractTableModel. Em cada linha deve-se
        dispor um atributo'''
        return self._natributos
    
    def columnCount(self, parent):
        '''Override de m�todo de QAbstractTableModel. S�o apenas duas colunas,
        uma marc�vel e outra com o nome do atributo.'''
        return 2
    
    def flags(self, index):
        '''Override de m�todo de QAbstractTableModel. Indica quais flags est�o ativos
        para cada item'''
        if index.column() == 0:
            #itens da primeira coluna devem ser marc�veis e n�o edit�veis
            return Qt.ItemIsUserCheckable | Qt.ItemIsEnabled
        else:
            #itens da segunda coluna devem ser n�o edit�veis
            return Qt.ItemIsEnabled
        
    
    def data(self, index, role):
        '''Override de m�todo de QAbstractTableModel. Retorna os dados e como eles devem ser
        dispostos dependendo do tipo de atividade sendo executada pelo usu�rio (role)'''
        
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        
        if role ==  Qt.CheckStateRole:
            row = index.row()
            column = index.column()
            if column == 0:
                return self._marcados[row]        
        
        if role ==  Qt.DisplayRole:
            row = index.row()
            column = index.column()
            if column == 0:
                return ""
            else:
                return self._atributos[row]    
            
    def setData(self, index, value, role):
        '''Override de m�todo de QAbstractTableModel. Permite modificar o status da checkbox'''
        if role == Qt.CheckStateRole:
            row = index.row()
            column = index.column()
            if column == 0:
                self._marcados[row] = value
                self.dataChanged.emit(index, index)
                return True
        return False
            
    def headerData(self, section, orientation, role):
        '''Override de m�todo de QAbstractTableModel. Retorna os cabe�alhos e como eles devem ser
        dispostos dependendo do tipo de atividade sendo executada pelo usu�rio (role)'''
        headers = ["","Atributo"]
        if role ==  Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return headers[section]