from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import urllib.request

class DownloadManager(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QGridLayout()
        url_label = QLabel("Enter URL")
        self.url = QLineEdit()
        location_label= QLabel("Enter Location")
        self.location = QLineEdit()
        progress_label = QLabel()
        self.progress = QProgressBar()
        download = QPushButton("Download")
        browse = QPushButton("Browse")

        self.url.setPlaceholderText("Web URL")
        self.location.setPlaceholderText("Enter location")

        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)


        layout.addWidget(url_label,0,0)
        layout.addWidget(self.url,0,1)
        layout.addWidget(location_label,1,0)
        layout.addWidget(self.location,1,1)
        layout.addWidget(browse,1,2)
        layout.addWidget(progress_label,2,0)
        layout.addWidget(self.progress,2,1)
        layout.addWidget(download,3,1)

        download.clicked.connect(self.download)
        browse.clicked.connect(self.browse_file)
        self.setLayout(layout)
        self.setFocus()

    def download(self):
        url = self.url.text()
        location = self.location.text()

        try:
            urllib.request.urlretrieve(url,location,self.report)
        except:
            QMessageBox.warning(self,"Warning", "Downloading Failed")
            return

        QMessageBox.information(self,"Information", "The download is complete")
        self.progress.setValue(0)
        self.url.setText("")
        self.location.setText("")


    def report(self, blocknum, blocksize, totalsize):
        readsofar = blocknum*blocksize;
        if totalsize>0:
            percent = readsofar/totalsize*100
            self.progress.setValue(int(percent))

    def browse_file(self):
        save_file = QFileDialog.getSaveFileName(self,caption = "Save File As", directory = "~", filter = "All Files (*.*)")
        self.location.setText(QDir.toNativeSeparators(save_file))

app = QApplication(sys.argv)
dl = DownloadManager()
dl.show()
app.exec_()
__author__ = 'Shikhar K Gupta'