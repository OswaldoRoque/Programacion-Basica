import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class TypecastingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conversión de Texto a Float")
        self.setGeometry(100, 100, 300, 150)
        
        self.initUI()

    def initUI(self):
        # Crear widgets
        self.label = QLabel("Ingresa un número:", self)
        self.text_input = QLineEdit(self)
        self.button = QPushButton("Convertir a float", self)
        self.result_label = QLabel("", self)

        # Conectar el botón al método
        self.button.clicked.connect(self.convert_to_float)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.text_input)
        layout.addWidget(self.button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def convert_to_float(self):
        texto = self.text_input.text()
        try:
            numero = float(texto)
            self.result_label.setText(f"Resultado: {numero}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor ingresa un número válido.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = TypecastingApp()
    ventana.show()
    sys.exit(app.exec_())