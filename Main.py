import tkinter
import customtkinter
from pytube import YouTube

def download():
    try:
        YouTubeLink = link.get()
        YouTubeObject = YouTube(YouTubeLink)
        Video = YouTubeObject.streams.get_highest_resolution()
        Video.download()
    except:
        print("Invalid Link")
    print("Done!")

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-,blue green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("720x480")
app.title("YouTube Downloader")

title = customtkinter.CTkLabel(app, text="Insert a YouTube Link")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

download = customtkinter.CTkButton(app, text="Download", command=download)
download.pack(padx=20, pady=20)

app.mainloop()