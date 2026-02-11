import time
import datetime
import os
from playsound import playsound
#========== LIBARY ADD ====== (SUTA)


# ================== FUNGSI KELOMPOK HARIAN ================== (AZMI)
def tentukan_kelompok(hari):
    if hari == 0:
        return 1
    elif hari == 1:
        return 2
    elif hari == 2:
        return 3
    elif hari == 3:
        return 4
    elif hari == 4:
        return 1
    elif hari == 5:
        return 2
    else:
        return 3


# ================== CEK APAKAH PIKET AKBAR ================== (AQIL)
def cek_piket_akbar():
    tanggal_mulai = datetime.date(2025, 1, 6)  # bebas, patokan awal
    hari_ini = datetime.date.today()
    selisih_hari = (hari_ini - tanggal_mulai).days

    if selisih_hari % 14 == 0:
        return True
    else:
        return False


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("=== SISTEM BEL PIKET AKTIF ===")

sudah_bunyi_pagi = False
sudah_bunyi_sore = False
tanggal_terakhir = ""

while True:
    sekarang = datetime.datetime.now()
    jam = sekarang.strftime("%H:%M")
    hari = sekarang.weekday()
    tanggal = sekarang.strftime("%Y-%m-%d")

    if tanggal != tanggal_terakhir:
        sudah_bunyi_pagi = False
        sudah_bunyi_sore = False
        tanggal_terakhir = tanggal

    kelompok = tentukan_kelompok(hari)

    # ================== BEL PAGI ================== (SUTA)
    if jam == "06:10" and sudah_bunyi_pagi == False:
        print("BEL PAGI BERBUNYI")
        print("Kelompok piket pagi: Kelompok", kelompok)

        playsound(os.path.join(BASE_DIR, "musik", "alarm_piket_pagi.mp3"))
        playsound(os.path.join(BASE_DIR, "kelompok_piket_pagi", f"kelompok_piket_pagi{kelompok}.mp3"))

        if cek_piket_akbar() == True: # jika pekan kedua atau ke empat hari minggu untuk bersih akbar
            print("HARI INI PIKET AKBAR")
            playsound(os.path.join(BASE_DIR, "musik", "alarm_piket_akbar.mp3"))

        sudah_bunyi_pagi = True
        time.sleep(60)

    # ================== BEL SORE ================== (AZMI)
    elif jam == "18:30" and sudah_bunyi_sore == False:
        print("BEL SORE BERBUNYI")
        print("Kelompok piket sore: Kelompok", kelompok)

        playsound(os.path.join(BASE_DIR, "musik", "alarm_piket_sore.mp3"))
        playsound(os.path.join(BASE_DIR, "kelompok_piket_sore", f"kelompok_piket_sore{kelompok}.mp3"))


        sudah_bunyi_sore = True
        time.sleep(60)

    time.sleep(1)
