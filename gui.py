import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel, QTextEdit, QPushButton
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QColor, QFont, QPalette
import serial
import serial.tools.list_ports


class ArduinoMonitor(QMainWindow):
    def __init__(self):
        super(ArduinoMonitor, self).__init__()

        self.init_ui()
        self.init_serial()

    def init_ui(self):
        self.setWindowTitle('Arduino Monitor')
        self.setGeometry(100, 100, 800, 600)

        # تنظیم پالت برنامه به حالت تاریک
        dark_palette = self.palette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Base, QColor(35, 35, 35))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Text, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
        self.setPalette(dark_palette)

        # تنظیم فونت برنامه
        font = self.font()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.setFont(font)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)

        data_label = QLabel('Received Data:')
        data_label.setFont(QFont('Segoe UI', 18, QFont.Bold))
        data_label.setStyleSheet("color: #3498db;")
        grid_layout.addWidget(data_label, 0, 0, 1, 2)

        self.data_text_edit = QTextEdit()
        self.data_text_edit.setReadOnly(True)
        self.data_text_edit.setStyleSheet("background-color: #ecf0f1; color: #2c3e50; font-size: 14px;")
        grid_layout.addWidget(self.data_text_edit, 1, 0, 4, 2)

        refresh_button = QPushButton('Refresh Serial Ports')
        refresh_button.setFont(QFont('Segoe UI', 12))
        refresh_button.setStyleSheet("background-color: #2ecc71; color: white;")
        refresh_button.clicked.connect(self.refresh_serial_ports)
        grid_layout.addWidget(refresh_button, 5, 0)

        connect_button = QPushButton('Connect')
        connect_button.setFont(QFont('Segoe UI', 12))
        connect_button.setStyleSheet("background-color: #e74c3c; color: white;")
        connect_button.clicked.connect(self.connect_to_arduino)
        grid_layout.addWidget(connect_button, 5, 1)

        self.show()

    def init_serial(self):
        self.serial_port = None
        self.serial_thread = None

    def refresh_serial_ports(self):
        ports = [port.device for port in serial.tools.list_ports.comports()]
        print("Available Serial Ports:", ports)

    def connect_to_arduino(self):
        port_name = 'COM2'  # Replace with the actual port name
        baud_rate = 9600

        try:
            self.serial_port = serial.Serial(port_name, baud_rate)
            print("Connected to Arduino on", port_name)

            self.serial_thread = SerialThread(self.serial_port, self)
            self.serial_thread.data_received.connect(self.process_data)
            self.serial_thread.start()

        except serial.SerialException as e:
            print("Error connecting to Arduino:", str(e))

    def process_data(self, data):
        received_data = data.decode('utf-8').strip()
        low_bits = received_data[-3:]  # Extract the last 3 characters as low bits
        low_bits_sum = sum(int(char, 16) for char in low_bits)
        result_text = f'Low Bits: {low_bits}\nSum of Low Bits: {low_bits_sum}\n\n'
        self.data_text_edit.append(received_data + '\n')  # این خط اضافه شده است
        self.data_text_edit.append(result_text)



    def closeEvent(self, event):
        if self.serial_thread:
            self.serial_thread.stop_thread()
            self.serial_thread.wait()


class SerialThread(QThread):
    data_received = pyqtSignal(bytes)

    def __init__(self, serial_port, parent=None):
        super(SerialThread, self).__init__(parent)
        self.serial_port = serial_port
        self.running = True

    def run(self):
        while self.running:
            if self.serial_port.in_waiting > 0:
                data = self.serial_port.readline()
                self.data_received.emit(data)

    def stop_thread(self):
        self.running = False


def main():
    app = QApplication(sys.argv)
    window = ArduinoMonitor()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
