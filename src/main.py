# coding: latin1

# Script Name		: main.py
# Author			: David Martins
# Created			: 10/06/2016
# Last Modified		: 
# Version			: 1.0.0

# Modifications		: 

# Description		: Executa o controlador e exibe a tela do software




import sys
from PySide.QtGui import QApplication
from controller.controlador_dataset import ControladorDataset
from view.mainGui import Ui_MainWindow



if __name__ == "__main__":
	app = QApplication(sys.argv)
	tela = Ui_MainWindow()
	c = ControladorDataset(tela)
	c.show()
	sys.exit(app.exec_())