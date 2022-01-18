import sys
from aulaPyQT5.aula03.design import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class RedimensionarImagem(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnEscolherArquivo.clicked.connect(self.abrir_imagem)
        self.btnRedimensionar.clicked.connect(self.redimensionar)
        self.btnSalvar.clicked.connect(self.salvar)

    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,  # QUem é pai da caixa de Diálogo
            'Abrir Imagem',  # título da caixa de Diálogo
            'C:\\Users\\desen\\Pictures\\',  # caminho que ela vai inciar
            # options=QFileDialog.DontUseNativeDialog Se não quisar usar a caixa nativa do sistema
        )
        self.edtAbrirArquivo.setText(imagem)
        self.orignal_img = QPixmap(imagem)
        self.lblImg.setPixmap(self.orignal_img)
        self.edtLargura.setText(str(self.orignal_img.width()))
        self.edtAltura.setText(str(self.orignal_img.height()))

    def redimensionar(self):
        largura = int(self.edtLargura.text())
        self.nova_imagem = self.orignal_img.scaledToWidth(largura)  # calcula altomatimente com base na largura passada
        self.lblImg.setPixmap(self.nova_imagem)
        self.edtLargura.setText(str(self.nova_imagem.width()))
        self.edtAltura.setText(str(self.nova_imagem.height()))

    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,  # QUem é pai da caixa de Diálogo
            'Salvar Imagem',  # título da caixa de Diálogo
            'C:\\Users\\desen\\Pictures\\',  # caminho que ela vai inciar
            # options=QFileDialog.DontUseNativeDialog Se não quisar usar a caixa nativa do sistema
        )
        self.nova_imagem.save(imagem, 'PNG')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    ri = RedimensionarImagem()
    ri.show()
    qt.exec_()
