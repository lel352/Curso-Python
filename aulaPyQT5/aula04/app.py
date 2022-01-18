import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from aulaPyQT5.aula04.telaapp import Ui_MainWindow
from aulaPyQT5.aula04.validadorcpf import valida_cpf
from aulaPyQT5.aula04.geradorcpf import gerador_cpf



class GeraValidaCPF(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnGerarCPF.clicked.connect(self.gerar_cpf)
        self.btnValidarCpf.clicked.connect(self.valida_cpf)


    def gerar_cpf(self):
        self.edtRetorno.setText(gerador_cpf())

    def valida_cpf(self):
        cpf = self.edtValidarCPF.text()
        if valida_cpf(cpf):
            self.edtRetorno.setText('CPF Válido !!!')
        else:
            self.edtRetorno.setText('CPF inválido !!!')




if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera_valida_cpf = GeraValidaCPF()
    gera_valida_cpf.show()
    qt.exec_()