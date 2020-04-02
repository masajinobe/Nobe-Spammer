import smtplib
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_Form

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

#NobeSpammer
server = smtplib.SMTP("smtp.gmail.com", 587)

def login():
	sender = ui.lineEdit.text()
	passw = ui.lineEdit_2.text()
	try:
		server.starttls()
		server.login(sender,passw)
		print("Login!")
	except:
		print("Login error...")

def mail():
	sender = ui.lineEdit.text()
	to = ui.lineEdit_3.text()
	msg = ui.lineEdit_4.text()
	while True:
		try:
			server.sendmail(sender,to,msg)
			print("Sent successfully!")
		except:
			print("Sending error...")

ui.pushButton.clicked.connect(mail)
ui.pushButton_2.clicked.connect(login)


sys.exit(app.exec_())