import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox as mg
from tkinter import filedialog
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
from win10toast import ToastNotifier

n = ToastNotifier()
root = tk.Tk()
style = ThemedStyle(root)

style.set_theme("ubuntu")
root.geometry("500x120")
root.resizable(False, False)
root.title("YouTube Video Downloader")
root.config(bg="white")
root.iconbitmap("youtube.ico")


def Widgets():
    tk.Label(root, text="YouTube link :",background="white").grid(row=1, column=0, pady=5, padx=5)
    ttk.Entry(root, width=55, textvariable=video_Link).grid(row=1, column=1, pady=5, padx=5, columnspan=2)
    tk.Label(root, text="Destination :",background="white").grid(row=2, column=0, pady=5, padx=5)
    ttk.Entry(root, width=40, textvariable=download_Path).grid(row=2, column=1, pady=5, padx=5)
    ttk.Button(root, text="Browse", command=Browse).grid(row=2, column=2, pady=1, padx=1)
    ttk.Button(root, text="Download", command=Download ).grid(row=3, column=1, pady=3, padx=3)


def Browse():
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
    download_Path.set(download_Directory)


def Download():
    mg.showinfo("Freeze", "The App Will Freeze Till The Download is Done")
    Youtube_link = video_Link.get()
    download_Folder = download_Path.get()
    try:
        getVideo = YouTube(Youtube_link)
    except:
        mg.showerror("Internet", "Check the connection")
    videoStream = getVideo.streams.first()
    videoStream.download(download_Folder)
    n.show_toast("Download", "Download Complete Successfully", duration=5, threaded=True, icon_path="youtube.ico")
    mg.showinfo("SUCCESSFULLY", "DOWNLOADED AND SAVED IN\n" + download_Folder)


video_Link = StringVar()
download_Path = StringVar()
Widgets()
root.mainloop()
