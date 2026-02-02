import json
import time
import datetime
import os
from playsound import playsound
import pyttsx3

# =============================
# KONFIGURASI
# =============================
KELOMPOK_SIZE = 4
JAM_BEL = ["14:41", "14:57"]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
AUDIO_BEL = os.path.join(BASE_DIR, "musik", "alarm jawa.mp3")

# =============================
# TEXT TO SPEECH
# =============================
engine = pyttsx3.init()
engine.setProperty("rate", 140)


voices = engine.getProperty('voices')  # ⬅️ INI YANG KURANG

# tampilkan dulu biar kelihatan
print("=== DAFTAR VOICE ===")
for i, v in enumerate(voices):
    print(i, v.name)

engine.setProperty('voice', voices[2].id)  # bisa ganti index

def sebut_nama(nama_list):
    kalimat = "Petugas piket dapur hari ini adalah... "
    kalimat += ", ".join(nama_list)
    engine.say(kalimat)
    engine.runAndWait()

# =============================
# LOAD DATA
# =============================
with open(os.path.join(DATA_DIR, "anggota.json")) as f:
    anggota = json.load(f)["dapur"]

with open(os.path.join(DATA_DIR, "state.json")) as f:
    state = json.load(f)

# =============================
# BENTUK KELOMPOK
# =============================
kelompok = [
    anggota[i:i + KELOMPOK_SIZE]
    for i in range(0, len(anggota), KELOMPOK_SIZE)
]

print("=== SISTEM BEL PIKET DAPUR AKTIF ===")

# =============================
# LOOP UTAMA
# =============================
while True:
    now = datetime.datetime.now()
    hari_ini = now.date().isoformat()
    jam = now.strftime("%H:%M")

    # === SWITCHING HARIAN ===
    if state["last_date"] != hari_ini:
        state["group_index"] = (state["group_index"] + 1) % len(kelompok)
        state["last_date"] = hari_ini

        with open(os.path.join(DATA_DIR, "state.json"), "w") as f:
            json.dump(state, f, indent=4)

    # === BEL & SUARA ===
    if jam in JAM_BEL:
        petugas = kelompok[state["group_index"]]

        print("\n=== BEL PIKET DAPUR ===")
        print("Tanggal :", hari_ini)
        print("Jam     :", jam)
        print("Petugas :")
        for p in petugas:
            print("-", p)

        playsound(AUDIO_BEL)     # 🔔 bel mp3
        sebut_nama(petugas)      # 🗣️ sebut nama

        time.sleep(60)

    time.sleep(1)