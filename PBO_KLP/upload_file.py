import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QListWidget, QTextEdit, QLabel, QSizePolicy, QFileDialog, QFrame
from PyQt5.QtWebEngineWidgets import QWebEngineView
import magic

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(650, 300, 800, 600)
        self.setWindowTitle("Data Viewer")

        self.init_ui()

    def init_ui(self):
        quit_button = QPushButton("QUIT", self)
        upload_button = QPushButton("UPLOAD", self)
        download_button = QPushButton("DOWNLOAD", self)

        upload_button.clicked.connect(self.upload_file)
        download_button.clicked.connect(self.download_file)

        vbox = QVBoxLayout()
        vbox.addWidget(quit_button)
        vbox.addWidget(upload_button)

        self.file_list_widget = QListWidget(self)
        self.file_list_widget.clicked.connect(self.show_file_content)
        vbox.addWidget(self.file_list_widget)

        vbox.addWidget(download_button)

        self.text_edit = QWebEngineView(self)
        self.text_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        vbox.addWidget(self.text_edit)

        self.setLayout(vbox)

        quit_button.clicked.connect(self.close)

        # Label to show the status of the last operation
        self.status_label = QLabel(self)
        self.status_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        vbox.addWidget(self.status_label)

        # Load existing files from the database
        self.load_files_from_database()

    def load_files_from_database(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pbl"
            )

            cursor = connection.cursor()
            cursor.execute("SELECT id, file, status FROM surat")
            files = cursor.fetchall()

            for file_id, filename, status in files:
                item = f"{file_id}: {filename} - Status: {status}"
                self.file_list_widget.addItem(item)

            connection.close()
        except Exception as e:
            self.status_label.setText(f"Error loading files from the database: {e}")
            
    def update_file_list_widget(self):
        # Bersihkan file_list_widget
        self.file_list_widget.clear()

        # Muat ulang file dari database
        self.load_files_from_database()

    def upload_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', '.', 'PDF Files (*.pdf);;All Files (*)')
        if filename:
            with open(filename, 'rb') as file:
                data = file.read()

            self.save_to_database(filename, data)
            self.status_label.setText("File saved to MySQL database.")

            # Perbarui tampilan file_list_widget
            self.update_file_list_widget()

    def save_to_database(self, filename, data,status='Pending'):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pbl"
            )

            cursor = connection.cursor()
            cursor.execute("INSERT INTO surat (file, content, status) VALUES (%s, %s, %s)", (filename, data, status))
            connection.commit()
            connection.close()
        except Exception as e:
            self.status_label.setText(f"Error: {e}")

    def show_file_content(self):
        selected_item = self.file_list_widget.currentItem()
        if selected_item:
            file_id = selected_item.text().split(":")[0].strip()
            content, status = self.get_file_info_from_database(file_id)
            self.display_file_content(content)
            self.status_label.setText(f"File Status: {status}")

    def get_file_info_from_database(self, file_id):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pbl"
            )

            cursor = connection.cursor()
            cursor.execute("SELECT content, status FROM surat WHERE id = %s", (file_id,))
            result = cursor.fetchone()
            connection.close()

            if result:
                content, status = result
                return content, status
            else:
                return b'', 'Pending'
        except Exception as e:
            self.status_label.setText(f"Error fetching file information from the database: {e}")
            return b'', 'Pending'

    def download_file(self):
        selected_item = self.file_list_widget.currentItem()
        if selected_item:
            file_id = selected_item.text().split(":")[0].strip()
            filename, status = self.get_file_info_from_database(file_id)

            if status == 'Validated':
                content = self.get_file_content_from_database(file_id)

                # Convert filename to string
                try:
                    filename = filename.decode('utf-8')
                except UnicodeDecodeError:
                    filename = filename.hex()

                save_filename, _ = QFileDialog.getSaveFileName(self, 'Save File', filename, 'PDF Files (*.pdf);;All Files (*)')
                if save_filename:
                    with open(save_filename, 'wb') as file:
                        file.write(content)
                    self.status_label.setText(f"File saved to {save_filename} successfully.")
                else:
                    self.status_label.setText("Save operation canceled.")
            else:
                self.status_label.setText("File cannot be downloaded. Status is not Validated.")
        else:
            self.status_label.setText("No file selected.")



    def get_file_content_from_database(self, file_id):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pbl"
            )

            cursor = connection.cursor()
            cursor.execute("SELECT content FROM surat WHERE id = %s", (file_id,))
            result = cursor.fetchone()
            connection.close()

            if result:
                return result[0]
            else:
                return b''
        except Exception as e:
            self.status_label.setText(f"Error fetching file content from the database: {e}")
            return b''


    def display_file_content(self, content):
        mime_type = magic.Magic()
        file_type = mime_type.from_buffer(content)

        if file_type.startswith('text'):
            # Displaying text content
            self.text_edit.setHtml(f"<pre>{content.decode(errors='replace')}</pre>")
        elif file_type.startswith('image'):
            # Displaying images using a label
            self.text_edit.setHtml(f"<img src='data:image/png;base64,{content.decode('utf-8')}'/>")
        elif file_type.startswith('application/pdf'):
            # Display PDF files using QWebEngineView
            self.text_edit.setHtml(f"<embed src='data:application/pdf;base64,{content.decode('utf-8')}' width='100%' height='100%'/>")
        else:
            # Handle other file types as needed
            self.text_edit.setHtml(f"Cannot display content for this file type: {file_type}")

def main():
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
