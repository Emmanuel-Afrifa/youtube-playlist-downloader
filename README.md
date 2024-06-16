# Youtube Playlist Downloader (YPD v1)

This repository contains the source code for a python program that automates the downloading of a Youtube playlist

In order to use this code;
1. clone this repository
1. install the Pytube module using the command below
    - ```pip install pytube```
1. call the ```playlist_downloader``` function by passing in the arguments for;
    - Direcetory in which the playlist will be downloaded
    - url of the playlist

The version two file contains the source code for the GUI implementation of the Youtube Playlist Downloader
- In order to use the GUI version, you can download the .exe file and install it on your Windows PCs
- For MACOS and Linux users,
    - clone the repository
    - use pyinstaller to build the executable file by running the following command;
        ```pip install pyinstaller``` - (to install pyinstaller)
        ```pyinstaller auto_playlist_downloader_v2.py``` - (to build the executable)

## Tools Used
-  This application was built using the Python programming language (version 3.10.8). The modules used are
    - tkinter
    - os
    - queue
    - threading
    - pytube
    

## References
- [Doenloading a Youtube playlist with Python](https://x.com/clcoding/status/1801801848304640129)
- [OS Module in Python](https://www.geeksforgeeks.org/os-module-python-examples/)
- [Building Modern GUIs with tkinter and Python by Saurabh Chandrakar nd Dr Nilesh Bhaskarrao Bahadure](https://www.bing.com/ck/a?!&&p=d61167f3e6f2360cJmltdHM9MTcxODQ5NjAwMCZpZ3VpZD0zODg3OGRmNC0zZTU3LTZiNTUtM2U1MC05ZTA3M2ZlYzZhNjAmaW5zaWQ9NTE4Mw&ptn=3&ver=2&hsh=3&fclid=38878df4-3e57-6b55-3e50-9e073fec6a60&psq=building+modern+guis+with+tkinter+and+python+saurabh+chandrakar&u=a1aHR0cHM6Ly9hcmNoaXZlLm9yZy9kZXRhaWxzL2J1aWxkaW5nLW1vZGVybi1ndWlzLXdpdGgtdGtpbnRlci1hbmQtcHl0aG9uLTIwMjM&ntb=1)


## Author
- Emmanuel Afrifa
- [emmaquame9@gmail.com](mailto:emmaquame9@gmail.com)
- [Frontend-Mentor](https://www.frontendmentor.io/profile/Emmanuel-Afrifa)
- [Twitter](https://twitter.com/Emma33712365)
- [Linkedin](https://www.linkedin.com/in/emmanuel-afrifa-840674214/)