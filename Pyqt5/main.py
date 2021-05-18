from pytube import YouTube

from ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

import win10toast

n = win10toast.ToastNotifier()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.Browse.pressed.connect(self.browse)
        self.Default_button.pressed.connect(self.default)
        self.Download_button.pressed.connect(self.download)
        self.show()


    def browse(self):
        download_Directory = QFileDialog.getExistingDirectory()
        self.entry_path.setText(download_Directory)

    def default(self):
        self.entry_path.setText("E:\\")

    def download(self):
        global getVideo, Youtube_link, download_Folder
        QMessageBox.information(self.Ui_MainWindow, "info", "The App Will Freeze Till The Download is Done")
        try:
            Youtube_link = self.entry_link.text()
            download_Folder = self.entry_path.text()
        except Exception() as e:
            QMessageBox.critical(self.Ui_MainWindow, "Error", "Fields Empty")
            print(e)
        try:
            getVideo = YouTube(Youtube_link)
        except:
            QMessageBox.critical(self.Ui_MainWindow, "Error", "Check the connection")
        videoStream = getVideo.streams.first()
        videoStream.download(download_Folder)

        n.show_toast("Download", "Download Complete Successfully And Saved At " + download_Folder, duration=5,
                     threaded=True, icon_path="icon.ico")



if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    app.exec_()
