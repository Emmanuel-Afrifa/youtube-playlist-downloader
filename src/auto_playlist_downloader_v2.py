# importing the necessary libraries
import os
from pytube import Playlist
import queue
import sys
import threading
import tkinter as tk
from tkinter import ttk


def image_path(image_relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, image_relative_path)

class YPD:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Youtube Playlist Downloader')
        self.root.configure(bg='#A9A9A9')
        self.root.geometry('600x480')
        self.img_path = image_path('youtube_logo.png')
        self.icon_pic = tk.PhotoImage(file=self.img_path)
        self.root.iconphoto(False, self.icon_pic)

        self.root.resizable(height=False, width=False)

        self.widgets_list = []

        # NEW DIRECTORY INFO
        self.label_new_path = tk.Label(self.root, text='Enter the name of the new folder for the playlist', bd=8, font=('calibre', 12, 'bold'), height=1, bg='#A9A9A9', foreground='white')
        self.label_new_path.pack(pady=19)
        self.widgets_list.append(self.label_new_path)

        self.new_path_str = tk.StringVar()
        self.entry_new_path= tk.Entry(self.root, textvariable=self.new_path_str, selectbackground='blue', selectforeground='white', width=90)
        self.entry_new_path.pack(padx=15)
        self.widgets_list.append(self.entry_new_path)


        # URL INFO
        self.label_url = tk.Label(self.root, text='Enter the URL of the playlist', bd=8, font=('calibre', 12, 'bold'), height=1, bg='#A9A9A9', foreground='white')
        self.label_url.pack(pady=19)
        self.widgets_list.append(self.label_url)

        self.url_str = tk.StringVar()
        self.entry_url = tk.Entry(self.root, textvariable=self.url_str, selectbackground='blue', selectforeground='white', width=90)
        self.entry_url.pack(padx=15)
        self.widgets_list.append(self.entry_url)

        self.download_log = tk.Label(self.root, text='Number of files downloaded: \n\n0', width=75, highlightthickness=5, highlightbackground='red', height=5)
        self.download_log.pack(pady=18)
        self.widgets_list.append(self.download_log)

        self.message_queue = queue.Queue()
        self.stop_download = tk.BooleanVar(value=False)

        self.download_button = tk.Button(self.root, text='Download Playlist', bg='#A9A9A9', foreground='white', activebackground='white', \
                        activeforeground='#A9A9A9', relief=tk.RAISED, width=28, height=1, font=('calibre', 12, 'bold'), cursor='arrow',
                        command=self.get_playlist)
        self.download_button.pack(pady=12)
        self.widgets_list.append(self.download_button)

        self.root.mainloop()

    def destroy_widgets_after_download(self):
        if len(self.widgets_list) > 0:
            download_index = self.widgets_list.index(self.download_button)
            for widget in self.widgets_list[download_index+1:]:
                widget.destroy()


    def download_videos(self, playlist, stop_button):
        global stop_download
        for i in range(len(playlist.videos)):
            if self.stop_download.get():
                break
            
            message = f"Number of files downloaded: \n\n{i + 1}"
            self.message_queue.put(message)
            self.root.after(0, self.label_updater)
            playlist.videos[i].streams.get_highest_resolution().download()
        self.root.after(0, lambda: self.download_button.config(state='normal'))
        self.root.after(0, lambda: stop_button.pack_forget())
        self.stop_download.set(False)

            
            
    def stop_downloading(self, stop_button):
        self.stop_download.set(True)
        stop_button.pack_forget()
        

    def label_updater(self):
        try:
            while not self.message_queue.empty():
                new_message = self.message_queue.get_nowait()
                self.download_log.config(text=new_message)
        except queue.Empty:
            pass
        self.root.after(10, self.label_updater)

    def get_playlist(self):
        self.download_button.config(state='disabled')
        url = self.url_str.get()

        self.destroy_widgets_after_download()

        try:
            url = self.url_str.get()
            if Playlist(url):
                playlist = Playlist(url)
            else:
                print('boooo')

                warning_label = tk.Label(self.root, text='Kindly fill the necessary fields with the correct details!', height=5, anchor=tk.CENTER, \
                                    font=('calibre', 16, 'bold'), fg='red', bg='#A9A9A9')
                warning_label.pack(pady=10)
                self.widgets_list.append(warning_label)
                return

            # global stop_button
            stop_button = tk.Button(self.root, text='STOP', bg='red', foreground='white', activebackground='white', \
                            activeforeground='red', relief=tk.RAISED, width=20, height=1, font=('calibre', 12, 'bold'), cursor='arrow', \
                                command=lambda: self.stop_downloading(stop_button))
            stop_button.pack()
            self.widgets_list.append(stop_button)


            current_path = os.getcwd()
            new_path = current_path + '\\' + self.new_path_str.get()
            try:
                os.makedirs(new_path)
            except:
                raise TypeError('The directory name is all existent')
            
            # changing the directory to the new new path
            os.chdir(new_path)

            # downloading the videos in the playlist
            download_thread = threading.Thread(target=self.download_videos, args=(playlist,stop_button))
            download_thread.start()
            self.label_updater()

        except:
            warning_label = tk.Label(self.root, text='Kindly fill the necessary fields with the correct details!', height=5, anchor=tk.CENTER, \
                                    font=('calibre', 16, 'bold'), fg='red', bg='#A9A9A9')
            warning_label.pack(pady=10)
            self.widgets_list.append(warning_label)
            self.download_button.config(state='active')

        self.root.after(10, self.label_updater)
