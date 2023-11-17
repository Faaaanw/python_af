import os
import tkinter as tk
from tkinter import Entry, Label, Button, StringVar, ttk
from pytube import YouTube
from plyer import notification
import threading
from PIL import Image, ImageTk

def show_notification(message, title='YouTube Downloader'):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=10,
    )

def download_video():
    def download():
        nonlocal video_url, download_dir
        try:
            yt = YouTube(video_url)
            title_label.config(text='Judul: ' + yt.title)
            views_label.config(text='Views: ' + str(yt.views))

            if not os.path.exists(download_dir):
                os.makedirs(download_dir)

            yd = yt.streams.get_highest_resolution()
            yd.download(download_dir)
            result_label.config(text=f"Video berhasil disimpan di: {download_dir}")

            # Menampilkan notifikasi setelah video diunduh
            show_notification(f"Video '{yt.title}' berhasil diunduh!")

        except Exception as e:
            result_label.config(text=f"Terjadi kesalahan: {e}")

    video_url = url_entry.get()
    download_dir = "./Downloads"

    # Membuat jendela progres
    progress_window = tk.Toplevel(window)
    progress_window.title("Progress")

    # Menambahkan logo YouTube ke dalam jendela progres
    image_path = os.path.join(os.getcwd(), "youtube_logo.png")
    youtube_logo = Image.open(image_path)
    youtube_logo = youtube_logo.resize((200, 200), )
    youtube_logo = ImageTk.PhotoImage(youtube_logo)
    

    logo_label = tk.Label(progress_window, image=youtube_logo)
    logo_label.image = youtube_logo
    logo_label.pack(pady=10)

    progress_label = Label(progress_window, text="Sedang mengunduh...")
    progress_label.pack(pady=10)

    progress_bar = ttk.Progressbar(progress_window, length=300, mode='indeterminate')
    progress_bar.pack(pady=10)
    progress_bar.start()

    # Menjalankan proses pengunduhan pada thread terpisah
    download_thread = threading.Thread(target=download)
    download_thread.start()

    # Memanggil fungsi untuk menutup jendela progres setelah selesai diunduh
    window.after(100, check_download_complete, download_thread, progress_window)

def check_download_complete(download_thread, progress_window):
    # Menutup jendela progres jika proses pengunduhan telah selesai
    if not download_thread.is_alive():
        progress_window.destroy()

# Membuat instance dari kelas Tk (jendela utama)
window = tk.Tk()
window.title("YouTube Downloader")

# Menambahkan logo YouTube di atas kata "YouTube Downloader"
image_path = os.path.join(os.getcwd(), "youtube_logo.png")
youtube_logo = Image.open(image_path)
youtube_logo = youtube_logo.resize((100,100), resample=Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
youtube_logo = ImageTk.PhotoImage(youtube_logo)


logo_label = tk.Label(window, image=youtube_logo, text="YouTube Downloader", compound="top", font=("Helvetica", 20))
logo_label.image = youtube_logo
logo_label.pack(pady=20)

# Membuat label, entry, dan button
url_label = Label(window, text="Masukkan link video:")
url_label.pack(pady=10)

url_entry = Entry(window, width=50)
url_entry.pack(pady=10)

download_button = Button(window, text="Download", command=download_video)
download_button.pack(pady=10)

title_label = Label(window, text="")
title_label.pack(pady=5)

views_label = Label(window, text="")
views_label.pack(pady=5)

result_label = Label(window, text="")
result_label.pack(pady=10)

# Menetapkan ukuran awal layar
window.geometry("700x700")

# Memulai loop utama
window.mainloop()
