import time
import pygame
import threading
import tkinter as tk

pygame.mixer.init()

audio_file = 'party-on-u.wav'  
pygame.mixer.music.load(audio_file)

lyrics_timeline = [
    (0, "Watch me, watch me party on you, yeah", 0.05),
    (2, "You could watch me pull up on your body", 0.045),
    (3.9, "like it's summer, take my clothes off in the water", 0.04),
    (6.2, "Splash around and get you blessed like holy water", 0.04),
    (8.4, "I don't know what you were waiting for", 0.04),
    (10.4, "You know that I've been waiting for you", 0.05),
    (11.9, "(I only threw this party for you)", 0.07),
    (14, "Yeah, if you saw my tears, would you touch me?", 0.04),
]

root = tk.Tk()
root.title("Party On U Lyrics")
root.geometry("800x400")
root.configure(bg="black")

lyric_label = tk.Label(root, text="", font=("Courier New", 28), fg="hotpink", bg="black")
lyric_label.pack(expand=True)

def typing_effect(text, speed=0.05):
    lyric_label.config(text="") 
    def inner_typing():
        displayed = ""
        for char in text:
            displayed += char
            lyric_label.config(text=displayed)
            time.sleep(speed)
    typing_thread = threading.Thread(target=inner_typing)
    typing_thread.start()

def play_music():
    pygame.mixer.music.play()

def show_lyrics():
    start_time = time.time()
    for timestamp, line, speed in lyrics_timeline:
        current_time = time.time()
        sleep_duration = timestamp - (current_time - start_time)
        if sleep_duration > 0:
            time.sleep(sleep_duration)
        typing_effect(line, speed)

def start_show():
    threading.Thread(target=play_music).start()
    threading.Thread(target=show_lyrics).start()

start_button = tk.Button(root, text="Start Party 🎶", command=start_show, font=("Courier New", 18), bg="pink", fg="black")
start_button.pack(pady=20)

root.mainloop()
