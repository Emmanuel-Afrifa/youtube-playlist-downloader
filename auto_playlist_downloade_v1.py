import tkinter as tk
import auto_playlist_downloade_v1 as apd1 

root = tk.Tk()
root.title('Youtube Playlist Downloader')
root.configure(bg='#A9A9A9')
root.geometry('600x480')
icon_pic = tk.PhotoImage(file="youtube_logo.png")
root.iconphoto(False, icon_pic)

root.resizable(height=False, width=False)

# NEW DIRECTORY INFO
label_new_path = tk.Label(root, text='Enter the name of the new folder to for th eplaylist', bd=8, font=('calibre', 12, 'bold'), height=1, bg='#A9A9A9', foreground='white')
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

download_button = tk.Button(root, text='Download Playlist', bg='#A9A9A9', foreground='white', activebackground='white', \
                    activeforeground='#A9A9A9', relief=tk.RAISED, width=28, height=1, font=('calibre', 12, 'bold'), cursor='arrow')

download_button.pack(pady=12)





root.mainloop()