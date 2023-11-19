import tkinter as tk
import customtkinter
from pytube import YouTube
from PIL import Image, ImageTk
from tkinter import filedialog


def download():
    try:
        YouTubeLink = link.get()
        YouTubeObject = YouTube(YouTubeLink, on_progress_callback=on_progress)

        # Get the highest resolution stream
        Video = YouTubeObject.streams.get_highest_resolution()

        # Ask the user to select a folder
        folder_path = filedialog.askdirectory()
        if folder_path:
            # Set the download path to the selected folder
            download_path = folder_path

            # Download the video to the selected folder
            title.configure(text=YouTubeObject.title)
            Video.download(download_path)
            Finished.configure(text="Download Complete!")
    except:
        Finished.configure(text="Download Failed!")
    Finished.configure(text="Download Complete!")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    NumPercentage.configure(text=per + "%")
    NumPercentage.update()
    progressBar.set(float(percentage_of_completion))


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: blue (default), dark-,blue green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("720x480")
app.title("YouTube Downloader")

# Open an image file
image = Image.open("Image Assets/Youtube_logo.png")

# Resize the image
resized_image = image.resize((200, 150))

# Convert the image to a PhotoImage object
tk_image = ImageTk.PhotoImage(resized_image)

# Create a canvas to display the image
canvas = tk.Canvas(app, width=200, height=150)
canvas.pack()

# Display the image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

title = customtkinter.CTkLabel(app, text="Insert a YouTube Link")
title.pack(padx=10, pady=10)

url_var = tk.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

Finished = customtkinter.CTkLabel(app, text="")
Finished.pack()

NumPercentage = customtkinter.CTkLabel(app, text="0%")
NumPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

download = customtkinter.CTkButton(app, text="Download", command=download)
download.pack(padx=20, pady=20)

app.mainloop()
