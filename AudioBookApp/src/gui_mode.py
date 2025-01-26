import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QLabel, QFileDialog, QMessageBox
import pdf_man

class PDFToAudioConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.add_pdfs_button = QPushButton('Add PDFs', self)
        self.add_pdfs_button.clicked.connect(self.add_pdfs)
        layout.addWidget(self.add_pdfs_button)

        self.pdf_list = QListWidget(self)
        layout.addWidget(self.pdf_list)

        self.output_path_button = QPushButton('Output Path', self)
        self.output_path_button.clicked.connect(self.select_output_path)
        layout.addWidget(self.output_path_button)

        self.output_path_input = QLineEdit(self)
        layout.addWidget(self.output_path_input)

        self.audio_file_label = QLabel('Audio File Name (without .mp3):', self)
        layout.addWidget(self.audio_file_label)

        self.audio_file_input = QLineEdit(self)
        layout.addWidget(self.audio_file_input)

        self.convert_button = QPushButton('Convert', self)
        self.convert_button.clicked.connect(self.convert)
        layout.addWidget(self.convert_button)

        self.setLayout(layout)
        self.setWindowTitle('PDF to Audio Converter')
        self.show()

    def add_pdfs(self):
        files, _ = QFileDialog.getOpenFileNames(self, 'Open PDF Files', '.', 'PDF Files (*.pdf)')
        if files:
            for file in files:
                self.pdf_list.addItem(file)

    def select_output_path(self):
        path = QFileDialog.getExistingDirectory(self, 'Select Output Directory')
        if path:
            self.output_path_input.setText(path)

    def convert(self):
        pdf_files = [self.pdf_list.item(i).text() for i in range(self.pdf_list.count())]
        output_path = self.output_path_input.text()
        audio_filename = self.audio_file_input.text() + ".mp3"

        if not pdf_files:
            QMessageBox.critical(self, 'Error', 'Please add at least one PDF file.')
            return
        if not output_path:
            QMessageBox.critical(self, 'Error', 'Please select an output path.')
            return
        if not audio_filename:
            QMessageBox.critical(self, 'Error', 'Please enter a name for the audio file.')
            return

        pdf_man.merge_pdf_files(pdf_files, "merged.pdf")
        pdf_man.pdf_to_audio("merged.pdf", f"{output_path}/{audio_filename}")
        QMessageBox.information(self, 'Success', f'Audio file saved at {output_path}/{audio_filename}')

def main():
    app = QApplication(sys.argv)
    ex = PDFToAudioConverter()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
