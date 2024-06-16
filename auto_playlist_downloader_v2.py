import tkinter as tk
from tkinter import ttk
import os
from pytube import Playlist
import time

# import auto_playlist_downloader_v1 as apd1 

root = tk.Tk()
root.title('Youtube Playlist Downloader')
root.configure(bg='#A9A9A9')
root.geometry('600x520')
icon_pic = tk.PhotoImage(file="youtube_logo.png")
root.iconphoto(False, icon_pic)

root.resizable(height=False, width=False)

# NEW DIRECTORY INFO
label_new_path = tk.Label(root, text='Enter the name of the new folder for the playlist', bd=8, font=('calibre', 12, 'bold'), height=1, bg='#A9A9A9', foreground='white')
label_new_path.pack(pady=19)

new_path_str = tk.StringVar()
entry_new_path= tk.Entry(root, textvariable=new_path_str, selectbackground='blue', selectforeground='white', width=95)
entry_new_path.pack()


# URL INFO
label_url = tk.Label(root, text='Enter the URL of the playlist', bd=8, font=('calibre', 12, 'bold'), height=1, bg='#A9A9A9', foreground='white')
label_url.pack(pady=19)

url_str = tk.StringVar()
entry_url = tk.Entry(root, textvariable=url_str, selectbackground='blue', selectforeground='white', width=95)
entry_url.pack()



# defining a function to download the playlists
def showwe():
    url = url_str.get()
    try:
        url = url_str.get()
        playlist = Playlist(url)
        counter = 0

        stop_button = tk.Button(root, text='STOP', bg='red', foreground='white', activebackground='white', \
                        activeforeground='red', relief=tk.RAISED, width=20, height=1, font=('calibre', 12, 'bold'), cursor='arrow')
        stop_button.pack()

        label_frame = tk.Frame(width=90, height=8)
        label_frame.pack(pady=10)
        scroll = tk.Scrollbar(label_frame)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        listbox = tk.Listbox(label_frame, width=90, justify='center')

        current_path = os.getcwd()
        new_path = current_path + '\\' + new_path_str.get()
        try:
            os.makedirs(new_path)
        except:
            raise TypeError('The directory name is all existent')
        
        # changing the directory to the new new path
        os.chdir(new_path)

        # downloading the videos in the playlist
        
        for i in range(len(playlist.videos)):
            # playlist.videos[i].streams.get_highest_resolution().download()
            if i+1 <= 1:
                message = f"{i+1} file downloaded"
            else: 
                message = f"{i+1} files downloaded"
            
            listbox.insert(tk.END, message)
            listbox.pack()
            listbox.config(yscrollcommand=scroll.set) 
            scroll.config(command=listbox.yview)
        
    except:
        warning_label = tk.Label(root, text='Kindly fill the necessary fields with the correct details!', height=5, anchor=tk.CENTER, \
                                 font=('calibre', 16, 'bold'), fg='red', bg='#A9A9A9')
        warning_label.pack(pady=10)
        # warning_label.destroy()





download_button = tk.Button(root, text='Download Playlist', bg='#A9A9A9', foreground='white', activebackground='white', \
                    activeforeground='#A9A9A9', relief=tk.RAISED, width=28, height=1, font=('calibre', 12, 'bold'), cursor='arrow',
                    command=showwe)
download_button.pack(pady=12)
# command=lambda: apd1.playlist_downloader(new_path_str.get(), label_url.get())
# print(new_path_str.get(), url_str.get())
root.mainloop()


newww = "https://www.youtube.com/watch?v=RXkAq9p24FQ&list=PLVErkmXVj2RMV8DdXwPVz1bS5vzbGjUN5"