import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pygame


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        self.playlist = []
        self.current_track = 0
        self.paused = False

        pygame.init()

        self.create_widgets()

    def create_widgets(self):
        self.playlistbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.playlistbox.pack(fill=tk.BOTH, expand=True)

        open_button = ttk.Button(self.root, text="Open Music", command=self.open_music)
        play_button = ttk.Button(self.root, text="Play", command=self.play_music)
        pause_button = ttk.Button(self.root, text="Pause", command=self.pause_music)
        next_button = ttk.Button(self.root, text="Next", command=self.next_track)

        open_button.pack()
        play_button.pack()
        pause_button.pack()
        next_button.pack()

    def open_music(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("Audio files", "*.mp3")])
        if file_paths:
            for path in file_paths:
                self.playlist.append(path)
                self.playlistbox.insert(tk.END, os.path.basename(path))

    def play_music(self):
        if not self.playlist:
            return

        if pygame.mixer.music.get_busy():
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            pygame.mixer.music.load(self.playlist[self.current_track])
            pygame.mixer.music.play()

    def pause_music(self):
        if pygame.mixer.music.get_busy() and not self.paused:
            pygame.mixer.music.pause()
            self.paused = True

    def next_track(self):
        if self.current_track < len(self.playlist) - 1:
            self.current_track += 1
            self.play_music()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    player = MusicPlayer(root)
    player.run()
