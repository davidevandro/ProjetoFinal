from PySide.QtCore import QAbstractTableModel, Qt


class DatasetModel(QAbstractTableModel):
    def rowCount(self, parent):
        '''Override de método de QAbstractTableModel. Em cada linha deve-se
        dispor um atributo'''
        return self._natributos
    
    def columnCount(self, parent):
        '''Override de método de QAbstractTableModel. São apenas duas colunas,
        uma marcável e outra com o nome do atributo.'''
        return 2
    
    def flags(self, index):
        '''Override de método de QAbstractTableModel. Indica quais flags estão ativos
        para cada item'''
        if index.column() == 0:
            #itens da primeira coluna devem ser marcáveis e não editáveis
            return Qt.ItemIsUserCheckable | Qt.ItemIsEnabled
        else:
            #itens da segunda coluna devem ser não editáveis
            return Qt.ItemIsEnabled
        
    
    def data(self, index, role):
        '''Override de método de QAbstractTableModel. Retorna os dados e como eles devem ser
        dispostos dependendo do tipo de atividade sendo executada pelo usuário (role)'''
        
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
        '''Override de método de QAbstractTableModel. Permite modificar o status da checkbox'''
        if role == Qt.CheckStateRole:
            row = index.row()
            column = index.column()
            if column == 0:
                self._marcados[row] = value
                self.dataChanged.emit(index, index)
                return True
        return False
            
    def headerData(self, section, orientation, role):
        '''Override de método de QAbstractTableModel. Retorna os cabeçalhos e como eles devem ser
        dispostos dependendo do tipo de atividade sendo executada pelo usuário (role)'''
        headers = ["","Atributo"]
        if role ==  Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return headers[section]