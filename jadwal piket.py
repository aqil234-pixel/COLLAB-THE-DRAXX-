import json
import time
import datetime
import winsound  # WINDOWS ONLY

KELOMPOK_SIZE = 4
JAM_BEL = ["05:00", "17:00"]  # pagi & sore

# =============================
# LOAD DATA
# =============================
with open("data/anggota.json") as f:
    anggota = json.load(f)["dapur"]

with open("data/state.json") as f:
    state = json.load(f)

# =============================
# BENTUK KELOMPOK
# =============================
kelompok = [
    anggota[i:i+KELOMPOK_SIZE]
    for i in range(0, len(anggota), KELOMPOK_SIZE)
]

# =============================
# FUNGSI BEL
# =============================
def bunyi_bel():
    for _ in range(3):
        winsound.Beep(1000, 500)
        time.sleep(0.3)

print("SISTEM BEL PIKET DAPUR AKTIF")

# =============================
# LOOP UTAMA
# =============================
while True:
    now = datetime.datetime.now()
    hari_ini = now.date().isoformat()
    jam_sekarang = now.strftime("%H:%M")

    # === SWITCHING HARIAN ===
    if state["last_date"] != hari_ini:
        state["group_index"] = (state["group_index"] + 1) % len(kelompok)
        state["last_date"] = hari_ini

        with open("data/state.json", "w") as f:
            json.dump(state, f, indent=4)

    # === BEL & TAMPILAN ===
    if jam_sekarang in JAM_BEL:
        petugas = kelompok[state["group_index"]]

        print("\n=== BEL PIKET DAPUR ===")
        print("Tanggal :", hari_ini)
        print("Jam     :", jam_sekarang)
        print("Petugas :")
        for p in petugas:
            print("-", p)

        bunyi_bel()
        time.sleep(60)  # cegah bunyi berulang

    time.sleep(1)
