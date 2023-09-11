
"""
Created on Sun Aug 20 00:17:00 2023

@author: vc
"""

'''Task 8 : Music Player
Create a simple music player that can play
MP3 files and allows the user to create and
manage playlists.'''

import pygame

pygame.init()
pygame.mixer.init()
# name of file present in present folder

playlists = []
playlist_name = []
# making a playlist

# select file

def select_file():
    file_name = input("Enter File name")
    pygame.mixer.music.load(file_name)

def make_playlist():
    name_of_playlist = input("Enter name of Playlist: ")
    if name_of_playlist:
        playlists.append(name_of_playlist)
        print("Playlist created successfully")    
    

# save to playlist
def save_to_playlist():
    song = input("Enter song name: ")
    print("Your Created list of Playlists are: ",playlists )
    p = input("Enter name of playlist in which you want to save: ")
    if p in playlists:
        playlist_name.append(p)
        playlist_name.append(song)
        print(playlist_name)
        print("song added")

    else:
        print("No such playlist")    

# remove from playlist
def remove_from_playlist():
    print("Select playlist: ", playlists)
    select = input("select_playlist")
    if select:
        print("select song: ", select)
        select_song = input("Enter song name")
        if select_song:
            select.pop(select_song)
            print("Song removed Successfully")

# load playlist
# def load_playlist():
#     pass

while True:
    print("Select One Option:")
    print("1. select file to play")
    print("2. play")
    print("3. stop")
    print("4. exit")
    print("5. make playlist")
    print("6. save to playlist")
    print("7. remove from playlist")
    # print("4. load playlist")
    option = int(input("Enter Your Choice: "))

    if option == 1:
        select_file() 

    elif option == 2:
        pygame.mixer.music.play()

    elif option == 3:
        pygame.mixer.music.stop()

    elif option == 4:
        pygame.mixer.music.stop()
        pygame.quit()
        break
    elif option == 5:
        make_playlist()

    elif option == 6:
        save_to_playlist()

    elif option == 7:
        remove_from_playlist()   

    else: 
        print("Enter valid Option: ")   



