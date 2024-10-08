import sys
import os 
from PyQt6.QtWidgets import QApplication, QWidget, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt6.QtCore import Qt
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('LoginForm')
        self.setGeometry(100,100,300,150)

        layout = QVBoxLayout()

        self.label_username= QLabel("Username")
        layout.addWidget(self.label_username)

        self.input_username = QLineEdit()
        layout.addWidget(self.input_username)

        self.label_password = QLabel("Password")
        layout.addWidget(self.label_password)

        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.input_password)

        self.button_login= QPushButton('Login')
        self.button_login.setObjectName("login_button")
        layout.addWidget(self.button_login)

        self.button_login.clicked.connect(self.check_login)
        self.setLayout(layout)
     
        self.load_styles()

    def load_styles(self):
        style_file_path = os.path.join("PyQT_Project\Homeworks\main.css")
        try:
            with open(style_file_path, "r") as file:
                style = file.read()
                self.setStyleSheet(style)
        except Exception as e:
            print(f"Грешка при зареждане на стиловете: {e}")




    def check_login(self):
        username=self.input_username.text()
        password=self.input_password.text()
        
        print(f"Username: {username}, Password: {password}")


        file_path = os.path.join("F:\\Python_2024\\Projects\\PyQT_Project\\Homeworks\\44. HW", "login_data.txt")
        print(f"Запис във файл на път: {file_path}")

        try:
            with open(file_path, "a", encoding='utf-8') as file:
                file.write(f"Въведено птребителско име: {username}\n")
                file.write(f"Въведена парола: {password}\n")
                print("Данните бяха записани успешно.")
        except Exception as e:
            print(f"Грешка при запис в файл: {e}")

        if username == 'admin'and password == '1234':
            QMessageBox.information(self, 'Login Success', 'Welcome')
        else:
            QMessageBox.critical(self, 'Login Failed', "Invalid username or password")
            
            self.show_try_again_message()

    def show_try_again_message(self): 
        dialog = QDialog(self)
        dialog.setWindowTitle("Try Again!")
        dialog.setFixedSize(200,100)

        layout = QVBoxLayout(dialog)
        message_label = QLabel("<div style='text-align: center; font-size: 20px;'>Please Try Again!</div>")
        message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(message_label)

        ok_button = QPushButton("OK")
        ok_button.setObjectName("btn")
        layout.addWidget(ok_button)

        ok_button.clicked.connect(dialog.accept)

        dialog.setLayout(layout)
        dialog.exec()
        



    def read_login_data(self):
        file_path = os.path.join("F:\\Python_2024\\Projects\\PyQT_Project\\Homeworks\\44. HW", "login_data.txt")
        try:
            with open(file_path, "r") as file:
                data = file.read()
                print("Съдържание на login_data.txt:")
                print(data)

        except Exception as e:
            print(f"Грешка при четене на файл: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_form = LoginForm()
    login_form.show()

    sys.exit(app.exec())
