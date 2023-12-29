import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QListWidget, QTextEdit, QLabel, QSizePolicy, QFileDialog, QFrame, QDialog, QListWidgetItem
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QListWidget

class AllFilesDialog(QDialog):
    def __init__(self, files):
        super().__init__()

        self.setWindowTitle("All Files")
        self.setGeometry(650, 300, 400, 300)

        vbox = QVBoxLayout(self)

        self.file_list_widget = QListWidget(self)
        vbox.addWidget(self.file_list_widget)

        for file_id, filename, status in files:
            item = f"{file_id}: {filename} - Status: {status}"
            self.file_list_widget.addItem(item)

        self.setLayout(vbox)

class ValidationDialog(QDialog):
    def __init__(self, file_id):
        super().__init__()

        self.setWindowTitle("Validation")
        self.setGeometry(650, 300, 300, 100)

        vbox = QVBoxLayout(self)

        validate_button = QPushButton("Validate", self)
        validate_button.clicked.connect(self.validate_file)
        vbox.addWidget(validate_button)

        self.file_id = file_id

        self.setLayout(vbox)

    def validate_file(self):
        selected_item = self.file_list_widget.currentItem()
        if selected_item:
            file_id = selected_item.text().split(":")[0].strip()

            # Tampilkan dialog validasi
            validation_dialog = ValidationDialog(file_id)
            if validation_dialog.exec_() == QDialog.Accepted:
                # Perbarui tampilan file_list_widget setelah validasi
                self.update_file_list_widget()

class DownloadDialog(QDialog):
    def __init__(self, filename, content):
        super().__init__()

        self.setWindowTitle("Download")
        self.setGeometry(650, 300, 300, 100)

        vbox = QVBoxLayout(self)

        download_button = QPushButton("Download", self)
        download_button.clicked.connect(self.download_file)
        vbox.addWidget(download_button)

        self.filename = filename
        self.content = content

        self.setLayout(vbox)


    def download_file(self):
        selected_item = self.file_list_widget.currentItem()
        if selected_item:
            file_id = selected_item.text().split(":")[0].strip()
            filename, content = self.get_file_info_from_database(file_id)

            # Tampilkan dialog unduhan
            download_dialog = DownloadDialog(filename, content)
            if download_dialog.exec_() == QDialog.Accepted:
                self.status_label.setText("File downloaded successfully.")

class DeleteDialog(QDialog):
    def __init__(self, file_id):
        super().__init__()

        self.setWindowTitle("Delete")
        self.setGeometry(650, 300, 300, 100)

        vbox = QVBoxLayout(self)

        delete_button = QPushButton("Delete", self)
        delete_button.clicked.connect(self.delete_file)
        vbox.addWidget(delete_button)

        self.file_id = file_id

        self.setLayout(vbox)

    def delete_file(self):
        selected_item = self.file_list_widget.currentItem()
        if selected_item:
            file_id = selected_item.text().split(":")[0].strip()

            # Tampilkan dialog penghapusan
            delete_dialog = DeleteDialog(file_id)
            if delete_dialog.exec_() == QDialog.Accepted:
                # Perbarui tampilan file_list_widget setelah penghapusan
                self.update_file_list_widget()
                
                
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
        validate_button = QPushButton("VALIDATE", self)
        delete_button = QPushButton("DELETE", self)

        upload_button.clicked.connect(self.upload_file)
        download_button.clicked.connect(self.download_file)
        validate_button.clicked.connect(self.validate_file)
        delete_button.clicked.connect(self.delete_file)

        vbox = QVBoxLayout()
        vbox.addWidget(quit_button)
        vbox.addWidget(upload_button)

        self.file_list_widget = QListWidget(self)
        self.file_list_widget.clicked.connect(self.show_file_content)
        vbox.addWidget(self.file_list_widget)

        vbox.addWidget(download_button)
        vbox.addWidget(validate_button)
        vbox.addWidget(delete_button)

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

    def upload_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', '.', 'PDF Files (*.pdf);;All Files (*)')
        if filename:
            with open(filename, 'rb') as file:
                data = file.read()

            self.save_to_database(filename, data)
            self.status_label.setText("File saved to MySQL database.")

            # Clear the content of file_list_widget
            self.file_list_widget.clear()

            # Show all files in a new dialog
            self.show_all_files_dialog()

    def show_all_files_dialog(self):
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

            connection.close()

            dialog = AllFilesDialog(files)
            dialog.exec_()  # Show the dialog
        except Exception as e:
            self.status_label.setText(f"Error loading files from the database: {e}")

    def save_to_database(self, filename, data, status='Pending'):
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
        # Implementasi sesuai dengan kebutuhan
        pass

    def validate_file(self):
        selected_item = self.file_list_widget.currentItem()
        if selected_item:
            file_id = selected_item.text().split(":")[0].strip()

            # Tampilkan dialog validasi
            validation_dialog = ValidationDialog(file_id)
            if validation_dialog.exec_() == QDialog.Accepted:
                # Perbarui tampilan file_list_widget setelah validasi
                self.update_file_list_widget()

    def update_file_list_widget(self):
        # Implementasi pembaruan file_list_widget
        # Misalnya, dapat memanggil metode load_files_from_database untuk memuat ulang data dari database
        self.load_files_from_database()

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

    def delete_file(self):
        selected_item = self.file_list_widget.currentItem()
        if selected_item:
            file_id = selected_item.text().split(":")[0].strip()

            # Tampilkan dialog penghapusan
            delete_dialog = DeleteDialog(file_id)
            if delete_dialog.exec_() == QDialog.Accepted:
                # Perbarui tampilan file_list_widget setelah penghapusan
                self.update_file_list_widget()

def main():
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
