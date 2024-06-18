def playlist_downloader(new_directory_name, playlist_url):
    """
    Returns a new directory containing the downloaded Youtube playlist

        Parameters:
            new_directory_name (str): name of the new directory where you wish to download the playlist
            playlist_url (str): url of the playlist
        
        Returns:
            None
    """
    import os
    from pytube import Playlist

    # getting the path of the current working directory
    current_path = os.getcwd()

    # path for new directory
    new_path = current_path + '\\' + new_directory_name
    try:
        os.makedirs(new_path)
    except:
        raise TypeError('The directory name is all existent')
    
    # changing the directory to the new new path
    os.chdir(new_path)

    # downloading the videos in the playlist
    url = playlist_url
    playlist = Playlist(url)
    counter = 0
    for video in playlist.videos:
        counter += 1
        video.streams.get_highest_resolution().download()
        if counter <= 1:
            print(f"{counter} file downloaded")
        else: 
            print(f"{counter} files downloaded")


if __name__ == "__main__":
    url = 'https://www.youtube.com/watch?v=Ri7-vnrJD3k&list=PLgdrWpDs7VaEpI5KfP47WOF9VjAl0ilSY'
    playlist_downloader('fav rep', url)