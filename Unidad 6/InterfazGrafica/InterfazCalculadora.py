import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora y Conversión")
        self.setGeometry(100, 100, 350, 250)

        self.initUI()

    def initUI(self):
        # Sección de conversión
        self.label_conversion = QLabel("Numero float:", self)
        self.text_input = QLineEdit(self)
        self.convert_button = QPushButton("Convertir", self)
        self.result_conversion = QLabel("", self)

        self.convert_button.clicked.connect(self.convert_to_float)

        # Sección de cálculo
        self.label_num1 = QLabel("Número 1:", self)
        self.input_num1 = QLineEdit(self)

        self.label_num2 = QLabel("Número 2:", self)
        self.input_num2 = QLineEdit(self)

        self.label_result = QLabel("Resultado:", self)
        self.result_label = QLabel("", self)

        self.sum_button = QPushButton("Suma", self)
        self.sub_button = QPushButton("Resta", self)
        self.mul_button = QPushButton("Multiplicación", self)
        self.div_button = QPushButton("División", self)

        self.sum_button.clicked.connect(lambda: self.calculate_operation(self.suma))
        self.sub_button.clicked.connect(lambda: self.calculate_operation(self.resta))
        self.mul_button.clicked.connect(lambda: self.calculate_operation(self.multiplicacion))
        self.div_button.clicked.connect(lambda: self.calculate_operation(self.division))

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(self.label_conversion)
        layout.addWidget(self.text_input)
        layout.addWidget(self.convert_button)
        layout.addWidget(self.result_conversion)

        layout.addWidget(self.label_num1)
        layout.addWidget(self.input_num1)
        layout.addWidget(self.label_num2)
        layout.addWidget(self.input_num2)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.sum_button)
        button_layout.addWidget(self.sub_button)
        button_layout.addWidget(self.mul_button)
        button_layout.addWidget(self.div_button)
        
        layout.addLayout(button_layout)
        layout.addWidget(self.label_result)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def convert_to_float(self):
        texto = self.text_input.text()
        try:
            numero = float(texto)
            self.result_conversion.setText(f"Número convertido: {numero}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor ingresa un número válido.")

    def calculate_operation(self, operation):
        try:
            num1 = float(self.input_num1.text())
            num2 = float(self.input_num2.text())
            resultado = operation(num1, num2)
            self.result_label.setText(f"Resultado: {resultado}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor ingresa números válidos.")

    @staticmethod
    def suma(a, b):
        return a + b

    @staticmethod
    def resta(a, b):
        return a - b

    @staticmethod
    def multiplicacion(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        return a / b if b != 0 else "Error: División por cero"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = CalculatorApp()
    ventana.show()
    sys.exit(app.exec_())
