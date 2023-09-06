#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
import os
import vlc
import glob
import fnmatch

# Initialize the VLC media player.
vlc_instance = vlc.Instance()
player = vlc_instance.media_player_new()

#Define the path to the music
my_music = r"C:\\Users\hp\OneDrive\Desktop\project music\\"
#To much all the files inside the folder, we have to create a pattern
pattern = "*.mp3"

window = tk.Tk()
window.geometry("350x300")
window.resizable(False, False)
window.title("MusicMuse")
window.config(bg= 'Grey')

#in order to include images, it has to be initialized first (image declaration)
prev_img = tk.PhotoImage(file = "Back.png")
next_img = tk.PhotoImage(file = "Forward.png")
play_img = tk.PhotoImage(file = "Play.png")
pause_img = tk.PhotoImage(file = "Pause.png")
stop_img = tk.PhotoImage(file = "Stop.png")

#assigning funtions to what the buttons do
def select():
    selected_song = listBox.get("anchor")
    label.config(text=selected_song)
    song_path = os.path.join(my_music, selected_song)
    media = vlc_instance.media_new(song_path)
    player.set_media(media)
    player.play()

def stop():
    player.stop()
    listBox.select_clear('active') #This line deselects the active song playing

def play_next():
  selected_index = listBox.curselection()
  if selected_index:
    next_index = int(selected_index[0]) + 1
    if next_index < listBox.size():
      next_song_name = listBox.get(next_index)
      label.config(text=next_song_name)
      song_path = os.path.join(my_music, next_song_name)
      media = vlc_instance.media_new(song_path)
      player.set_media(media)
      player.play()
      
      # This moves the hover from the current song to the next song
      listBox.select_clear(0, 'end')
      listBox.activate(next_index)
      listBox.select_set(next_index)

def play_prev():
  selected_index = listBox.curselection()
  if selected_index:
    next_index = int(selected_index[0]) - 1
    if next_index < listBox.size():
      next_song_name = listBox.get(next_index)
      label.config(text=next_song_name)
      song_path = os.path.join(my_music, next_song_name)
      media = vlc_instance.media_new(song_path)
      player.set_media(media)
      player.play()
      
      # This moves the hover from the current song to the next song
      listBox.select_clear(0, 'end')
      listBox.activate(next_index)
      listBox.select_set(next_index)

def pause():
   if pause_button["text"] == "Pause":
      player.pause()
      pause_button["text"] == "Play"
   else:
      player.unpause()
      pause_button["text"] == "Pause"

#to insert items into a list box, use listBox.insert(0, "Coding"). the number shows the arrangement order
#Creating a listbox to display the songs
listBox = tk.Listbox(window, fg = "cyan", bg = "black", width = "100", font = ('ds-digital', 10))

#To pack the listbox with parameters
listBox.pack(padx = 15, pady = 15) #padx specifies horizontal padding and pady specifies vert

# Creating a label to display the current song
label = tk.Label(window, text = '', bg = 'black', fg = 'blue', font = ('ds-digital', 18))
label.pack(pady = 15)

# Create a frame for the music player controls
controls_frame = ttk.Frame(window)
controls_frame.pack(fill="both", expand=True)

# Create a button to pause the music
pause_button = ttk.Button(controls_frame, text="Pause", image=pause_img, command = pause)
pause_button.pack(side="left", padx=5, pady=5)

# Create a button to skip to the previous song
previous_button = ttk.Button(controls_frame, text="Previous", image=prev_img, command = play_prev)
previous_button.pack(side="left", padx=5, pady=5)

# Create a button to play the music
play_button = ttk.Button(controls_frame, text="Play", image=play_img, command = select )
play_button.pack(side="left", padx=5, pady=5)

# Create a button to skip to the next song
next_button = ttk.Button(controls_frame, text="Next", image=next_img, command = play_next)
next_button.pack(side="left", padx=5, pady=5)

# Create a button to stop the music
stop_button = ttk.Button(controls_frame, text="Pause", image=stop_img, command = stop)
stop_button.pack(side="left", padx=5, pady=5)

#Searching for the inventory files within the path (my_music).
for root, dir, files in os.walk(my_music):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)


window.mainloop()
