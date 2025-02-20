import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Carrega o arquivo .ui criado no Qt Designer
        uic.loadUi("template.ui", self)

        # Acessando widgets do template
        self.pushButton.clicked.connect(self.on_button_click)

    def on_button_click(self):
        # Lógica para o botão
        QMessageBox.information(self, "Mensagem", "Você clicou no botão!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Instancia a janela principal
    window = MainWindow()
    window.show()

    # Executa o loop da aplicação
    sys.exit(app.exec())