import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Konstanta
LEBAR, TINGGI = 800, 600
WARNA_LATAR = (0, 0, 0)
WARNA_PADDLE = (255, 255, 255)
WARNA_BOLA = (255, 255, 255)
PADDLE_LEBAR = 10
PADDLE_TINGGI = 100
BOLA_UKURAN = 15
KECEPATAN_PADDLE = 1
KECEPATAN_BOLA = 0.3

# Membuat layar
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Pong")

# Atribut paddle
paddle_1_x = 50
paddle_1_y = TINGGI // 2 - PADDLE_TINGGI // 2
paddle_2_x = LEBAR - 50 - PADDLE_LEBAR
paddle_2_y = TINGGI // 2 - PADDLE_TINGGI // 2
paddle_1_kecepatan = 0
paddle_2_kecepatan = 0

# Atribut bola
bola_x = LEBAR // 2 - BOLA_UKURAN // 2
bola_y = TINGGI // 2 - BOLA_UKURAN // 2
bola_kecepatan_x = KECEPATAN_BOLA
bola_kecepatan_y = KECEPATAN_BOLA

# Game variables
skor_1 = 0
skor_2 = 0
font = pygame.font.Font(None, 36)

# Main game loop
berjalan = True
while berjalan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            berjalan = False

    # Deteksi input pemain
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_1_kecepatan = -KECEPATAN_PADDLE
    elif keys[pygame.K_s]:
        paddle_1_kecepatan = KECEPATAN_PADDLE
    else:
        paddle_1_kecepatan = 0

    if keys[pygame.K_UP]:
        paddle_2_kecepatan = -KECEPATAN_PADDLE
    elif keys[pygame.K_DOWN]:
        paddle_2_kecepatan = KECEPATAN_PADDLE
    else:
        paddle_2_kecepatan = 0

    # Menggerakkan paddle
    paddle_1_y += paddle_1_kecepatan
    paddle_2_y += paddle_2_kecepatan

    # Batasan gerakan paddle
    if paddle_1_y < 0:
        paddle_1_y = 0
    if paddle_1_y > TINGGI - PADDLE_TINGGI:
        paddle_1_y = TINGGI - PADDLE_TINGGI
    if paddle_2_y < 0:
        paddle_2_y = 0
    if paddle_2_y > TINGGI - PADDLE_TINGGI:
        paddle_2_y = TINGGI - PADDLE_TINGGI

    # Menggerakkan bola
    bola_x += bola_kecepatan_x
    bola_y += bola_kecepatan_y

    # Deteksi tabrakan dengan paddle
    if (
        bola_x <= paddle_1_x + PADDLE_LEBAR
        and paddle_1_y <= bola_y + BOLA_UKURAN <= paddle_1_y + PADDLE_TINGGI
    ):
        bola_kecepatan_x = KECEPATAN_BOLA
    if (
        bola_x + BOLA_UKURAN >= paddle_2_x
        and paddle_2_y <= bola_y + BOLA_UKURAN <= paddle_2_y + PADDLE_TINGGI
    ):
        bola_kecepatan_x = -KECEPATAN_BOLA

    # Deteksi bola keluar dari layar
    if bola_x < 0:
        skor_2 += 1
        bola_x = LEBAR // 2 - BOLA_UKURAN // 2
        bola_y = TINGGI // 2 - BOLA_UKURAN // 2
        bola_kecepatan_x = KECEPATAN_BOLA
        bola_kecepatan_y = KECEPATAN_BOLA
    if bola_x > LEBAR:
        skor_1 += 1
        bola_x = LEBAR // 2 - BOLA_UKURAN // 2
        bola_y = TINGGI // 2 - BOLA_UKURAN // 2
        bola_kecepatan_x = -KECEPATAN_BOLA
        bola_kecepatan_y = KECEPATAN_BOLA

    # Deteksi bola keluar dari atas atau bawah layar
    if bola_y < 0 or bola_y + BOLA_UKURAN > TINGGI:
        bola_kecepatan_y = -bola_kecepatan_y

    # Membersihkan layar
    layar.fill(WARNA_LATAR)

    # Menggambar paddle
    pygame.draw.rect(layar, WARNA_PADDLE, (paddle_1_x, paddle_1_y, PADDLE_LEBAR, PADDLE_TINGGI))
    pygame.draw.rect(layar, WARNA_PADDLE, (paddle_2_x, paddle_2_y, PADDLE_LEBAR, PADDLE_TINGGI))

    # Menggambar bola
    pygame.draw.rect(layar, WARNA_BOLA, (bola_x, bola_y, BOLA_UKURAN, BOLA_UKURAN))

    # Menampilkan skor
    skor_teks = font.render(f"{skor_1} - {skor_2}", True, WARNA_PADDLE)
    layar.blit(skor_teks, (LEBAR // 2 - 20, 10))

    pygame.display.flip()

# Menunggu beberapa detik sebelum menutup game
pygame.time.delay(3000)

pygame.quit()
sys.exit()
