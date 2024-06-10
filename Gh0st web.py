import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5 import QtCore

class MainWindow(QMainWindow):

    def go_home(self):
        self.browser.setUrl(QUrl('https://google.com.br'))

    def go_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, url):
        self.url_bar.setText(url.toString())

    def __init__(self, *args, **kwargs):
        super(MainWindow, self). __init__(*args, **kwargs)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com.br'))
        self.setCentralWidget(self.browser)
        self.setWindowIcon(QtGui.QIcon("pngegg.png"))
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction ('◀', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        refresh_btn = QAction('🔄', self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)

        forward_btn = QAction ('►', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.go_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)


        home_btn = QAction('🏠︎', self)
        home_btn.triggered.connect(self.go_home)
        navbar.addAction(home_btn)

app = QApplication(sys.argv)
QApplication.setApplicationName('Gh0st')
windows = MainWindow()

app.exec()