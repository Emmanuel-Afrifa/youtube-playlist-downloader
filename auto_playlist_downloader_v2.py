# importing the necessary libraries
import os
from pytube import Playlist
import queue
import threading
import tkinter as tk
from tkinter import ttk


def YPD():
    """
    Returns the GUI version of the YPD application
    """
    root = tk.Tk()
    root.title('Youtube Playlist Downloader')
    root.configure(bg='#A9A9A9')
    root.geometry('600x480')
    icon_pic = tk.PhotoImage(file="youtube_logo.png")
    root.iconphoto(False, icon_pic)

    root.resizable(height=False, width=False)

    widgets_list = []

    # NEW DIRECTORY INFO
    label_new_path = tk.Label(root, text='Enter the name of the new folder for the playlist', bd=8, font=('calibre', 12, 'bold'), height=1, bg='#A9A9A9', foreground='white')
    label_new_path.pack(pady=19)
    widgets_list.append(label_new_path)

    new_path_str = tk.StringVar()
    entry_new_path= tk.Entry(root, textvariable=new_path_str, selectbackground='blue', selectforeground='white', width=90)
    entry_new_path.pack(padx=15)
    widgets_list.append(entry_new_path)


    # URL INFO
    label_url = tk.Label(root, text='Enter the URL of the playlist', bd=8, font=('calibre', 12, 'bold'), height=1, bg='#A9A9A9', foreground='white')
    label_url.pack(pady=19)
    widgets_list.append(label_url)

    url_str = tk.StringVar()
    entry_url = tk.Entry(root, textvariable=url_str, selectbackground='blue', selectforeground='white', width=90)
    entry_url.pack(padx=15)
    widgets_list.append(entry_url)

    def destroy_widgets_after_download():
        if len(widgets_list) > 0:
            download_index = widgets_list.index(download_button)
            for widget in widgets_list[download_index+1:]:
                widget.destroy()

    download_log = tk.Label(root, text='Number of files downloaded: \n\n0', width=75, highlightthickness=5, highlightbackground='red', height=5)
    download_log.pack(pady=18)
    widgets_list.append(download_log)

    message_queue = queue.Queue()
    stop_download = tk.BooleanVar(value=False)

    def download_videos(playlist, stop_button):
        global stop_download
        for i in range(len(playlist.videos)):
            if stop_download.get():
                break
            
            message = f"Number of files downloaded: \n\n{i + 1}"
            message_queue.put(message)
            root.after(0, label_updater)
            playlist.videos[i].streams.get_highest_resolution().download()
        root.after(0, lambda: download_button.config(state='normal'))
        root.after(0, lambda: stop_button.pack_forget())
        stop_download.set(False)

            
            
    def stop_downloading(stop_button):
        stop_download.set(True)
        stop_button.pack_forget()
        

    def label_updater():
        try:
            while not message_queue.empty():
                new_message = message_queue.get_nowait()
                download_log.config(text=new_message)
        except queue.Empty:
            pass
        root.after(10, label_updater)

    def get_playlist():
        download_button.config(state='disabled')
        url = url_str.get()

        destroy_widgets_after_download()

        try:
            url = url_str.get()
            if Playlist(url):
                playlist = Playlist(url)
            else:
                print('boooo')

                warning_label = tk.Label(root, text='Kindly fill the necessary fields with the correct details!', height=5, anchor=tk.CENTER, \
                                    font=('calibre', 16, 'bold'), fg='red', bg='#A9A9A9')
                warning_label.pack(pady=10)
                widgets_list.append(warning_label)
                return

            # global stop_button
            stop_button = tk.Button(root, text='STOP', bg='red', foreground='white', activebackground='white', \
                            activeforeground='red', relief=tk.RAISED, width=20, height=1, font=('calibre', 12, 'bold'), cursor='arrow', \
                                command=lambda: stop_downloading(stop_button))
            stop_button.pack()
            widgets_list.append(stop_button)


            current_path = os.getcwd()
            new_path = current_path + '\\' + new_path_str.get()
            try:
                os.makedirs(new_path)
            except:
                raise TypeError('The directory name is all existent')
            
            # changing the directory to the new new path
            os.chdir(new_path)

            # downloading the videos in the playlist
            download_thread = threading.Thread(target=download_videos, args=(playlist,stop_button))
            download_thread.start()
            label_updater()

        except:
            warning_label = tk.Label(root, text='Kindly fill the necessary fields with the correct details!', height=5, anchor=tk.CENTER, \
                                    font=('calibre', 16, 'bold'), fg='red', bg='#A9A9A9')
            warning_label.pack(pady=10)
            widgets_list.append(warning_label)
            download_button.config(state='active')

    root.after(10, label_updater)

    download_button = tk.Button(root, text='Download Playlist', bg='#A9A9A9', foreground='white', activebackground='white', \
                        activeforeground='#A9A9A9', relief=tk.RAISED, width=28, height=1, font=('calibre', 12, 'bold'), cursor='arrow',
                        command=get_playlist)
    download_button.pack(pady=12)
    widgets_list.append(download_button)
    root.mainloop()


