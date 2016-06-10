# coding: latin1

# Script Name		: main.py
# Author			: David Martins
# Created			: 10/06/2016
# Last Modified		: 
# Version			: 1.0.0

# Modifications		: 

# Description		: Executa o controlador e exibe a tela do software

from controller.controlador import Controlador
import sys

from PySide.QtCore import *
from PySide.QtGui import *


if __name__ == "__main__":
	app = QApplication(sys.argv)
	c = Controlador()
	c.show()
	sys.exit(app.exec_())