from pytube import YouTube
import os

# Gantilah URL di bawah ini dengan URL video YouTube yang ingin Anda unduh
video_url = input('Masukkan link video:')

# Tentukan direktori tempat Anda ingin menyimpan video
download_dir = "./download"

try:
    yt = YouTube(video_url)
    print('Judul:', yt.title)
    print('views:', yt.views)

    # Pastikan direktori tempat Anda ingin menyimpan video sudah ada
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    yd = yt.streams.get_highest_resolution()

    # Gunakan download() dengan menyertakan jalur direktori
    yd.download(download_dir)
    print(f"Video berhasil disimpan di: {download_dir}")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
