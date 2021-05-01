from pytube import YouTube 
from win10toast import ToastNotifier
from PyQt5 import QtWidgets
n = ToastNotifier()

def Browse(entry_path): 
    download_Directory=QtWidgets.QFileDialog.getExistingDirectory()
    entry_path.setText(download_Directory)

def Default(entry_path):
    entry_path.setText("E:\\")


def Download(entry_path,entry_link , mainwindow):
    QtWidgets.QMessageBox.information(mainwindow, "info", "The App Will Freeze Till The Download is Done")
    try:
        Youtube_link = entry_link.text()
        download_Folder = entry_path.text()
    except Exception() as e:
        QtWidgets.QMessageBox.critical(mainwindow, "Error", "Fields Empty")
    try:
        getVideo = YouTube(Youtube_link)
    except:
        QtWidgets.QMessageBox.critical(mainwindow, "Error", "Check the connection")
    videoStream = getVideo.streams.first()
    videoStream.download(download_Folder) 
    n.show_toast("Download","Download Complete Successfully And Saved At " + download_Folder,duration=5,threaded=True,icon_path="icon.ico")
