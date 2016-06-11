# coding: latin1

# Script Name		: main.py
# Author			: David Martins
# Created			: 10/06/2016
# Last Modified		: 
# Version			: 1.0.0

# Modifications		: 

# Description		: Executa o MainGui e exibe a tela do software

from view.mainGui import MainGui
import sys

from PySide.QtCore import *
from PySide.QtGui import *


if __name__ == "__main__":
	app = QApplication(sys.argv)
	tela = MainGui()
	tela.show()
	sys.exit(app.exec_())