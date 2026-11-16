import streamlit as st
import random

# ==========================================
# 1. KONFIGURASI HALAMAN & STYLE WEB
# ==========================================
st.set_page_config(
    page_title="Simulator Socratic Stepper",
    page_icon="🏛️",
    layout="centered"
)

st.markdown("""
    <style>
    .main-header { text-align: center; color: #1E88E5; font-weight: bold; }
    .sub-header { text-align: center; color: #555555; }
    .card-box { background-color: #F8F9FA; padding: 15px; border-radius: 10px; border: 1px solid #E0E0E0; }
    .success-box { background-color: #E8F5E9; color: #2E7D32; padding: 15px; border-radius: 8px; border-left: 5px solid #4CAF50; margin-top: 10px; }
    .fail-box { background-color: #FFEBEE; color: #C62828; padding: 15px; border-radius: 8px; border-left: 5px solid #F44336; margin-top: 10px; }
    </style>
""", unsafe_allow_html=True)


# ==========================================
# 2. GENERATOR SOAL ACAK & PETUNJUK STEP-BY-STEP
# ==========================================
def generate_semua_soal():
    # --- MODUL ALJABAR (10 LEVEL, MASING-MASING 2 SOAL ACAK) ---
    aljabar = []

    # Level 1: PLSV Dasar
    a1, x1_1 = random.randint(2, 12), random.randint(2, 15)
    b1 = x1_1 + a1
    c1, x1_2 = random.randint(2, 12), random.randint(5, 20)
    d1 = x1_2 - c1
    aljabar.append({
        "level": 1, "kesulitan": "Mudah", "materi": "Persamaan Linear Satu Variabel Dasar",
        "soal_1": {"soal": f"Tentukan nilai x dari: x + {a1} = {b1}", "format": "Ketik format: x=n atau angkanya saja", "jawaban": [str(x1_1), f"x={x1_1}"]},
        "soal_2": {"soal": f"Tentukan nilai x dari: x - {c1} = {d1}", "format": "Ketik format: x=n atau angkanya saja", "jawaban": [str(x1_2), f"x={x1_2}"]},
        "paham_msg": "✅ *BERHASIL PAHAM!* Anda menguasai prinsip dasar kesamaan aljabar dengan menerapkan operasi invers (penjumlahan/pengurangan) pada kedua ruas persamaan.",
        "socratic_hint": """🧭 *TUTOR SOKRATIK (Langkah demi Langkah):*
1. *Identifikasi Target:* Tempatkan variabel $x$ agar berdiri sendirian di ruas kiri.
2. *Periksa Operasi:* Perhatikan angka pengikut $x$ di ruas kiri (apakah ditambah atau dikurang).
3. *Terapkan Invers:* Lakukan operasi matematika yang berlawanan (misal: jika ditambah, kurangkan) ke kedua ruas secara adil."""
    })

    # Level 2: PLSV Perkalian
    a2_1, x2_1 = random.randint(2, 9), random.randint(2, 12)
    a2_2, x2_2 = random.choice([i for i in range(2, 10) if i != a2_1]), random.randint(3, 14)
    aljabar.append({
        "level": 2, "kesulitan": "Mudah", "materi": "Persamaan Linear Satu Variabel (Perkalian)",
        "soal_1": {"soal": f"Tentukan nilai x dari: {a2_1}x = {a2_1 * x2_1}", "format": "Ketik format: x=n atau angkanya saja", "jawaban": [str(x2_1), f"x={x2_1}"]},
        "soal_2": {"soal": f"Tentukan nilai x dari: {a2_2}x = {a2_2 * x2_2}", "format": "Ketik format: x=n atau angkanya saja", "jawaban": [str(x2_2), f"x={x2_2}"]},
        "paham_msg": "✅ *BERHASIL PAHAM!* Anda memahami cara membalikkan operasi perkalian koefisien dengan pembagian pada kedua ruas persamaan.",
        "socratic_hint": """🧭 *TUTOR SOKRATIK (Langkah demi Langkah):*
1. *Analisis Bentuk:* Bentuk $ax = b$ menyatakan koefisien dikali variabel.
2. *Pilih Operasi Invers:* Kebalikan dari perkalian adalah pembagian.
3. *Eksekusi:* Bagilah angka di ruas kanan dengan koefisien yang menempel pada $x$."""
    })

    # Level 3: PLSV Dua Langkah
    a3_1, b3_1, x3_1 = random.randint(2, 6), random.randint(1, 10), random.randint(2, 10)
    a3_2, b3_2, x3_2 = random.randint(3, 7), random.randint(2, 12), random.randint(3, 11)
    aljabar.append({
        "level": 3, "kesulitan": "Mudah", "materi": "Operasi Aljabar Dua Langkah",
        "soal_1": {"soal": f"Tentukan nilai x dari: {a3_1}x + {b3_1} = {a3_1 * x3_1 + b3_1}", "format": "Ketik format: x=n atau angkanya saja", "jawaban": [str(x3_1), f"x={x3_1}"]},
        "soal_2": {"soal": f"Tentukan nilai x dari: {a3_2}x - {b3_2} = {a3_2 * x3_2 - b3_2}", "format": "Ketik format: x=n atau angkanya saja", "jawaban": [str(x3_2), f"x={x3_2}"]},
        "paham_msg": "✅ *BERHASIL PAHAM!* Luar biasa! Anda berhasil mengurutkan langkah: memindahkan konstanta terlebih dahulu baru membagi dengan koefisien variabel.",
        "socratic_hint": """🧭 *TUTOR SOKRATIK (Langkah demi Langkah):*
1. *Tahap 1 (Konstanta):* Singkirkan suku konstanta bebas di ruas kiri terlebih dahulu menggunakan operasi penjumlahan/pengurangan invers.
2. *Tahap 2 (Koefisien):* Setelah menyisakan bentuk $ax = b$, lanjutkan dengan membagi ruas kanan dengan koefisien $a$."""
    })

    # Level 4: Variabel di Kedua Ruas
    c4_1 = random.randint(1, 4)
    a4_1 = c4_1 + random.randint(2, 5)
    x4_1 = random.randint(2, 9)
    b4_1 = random.randint(1, 8)
    d4_1 = (a4_1 - c4_1) * x4_1 - b4_1

    c4_2 = random.randint(2, 5)
    a4_2 = c4_2 + random.randint(2, 4)
    x4_2 = random.randint(3, 10)
    b4_2 = random.randint(1, 9)
    d4_2 = (a4_2 - c4_2) * x4_2 + b4_2
    aljabar.append({
        "level": 4, "kesulitan": "Sedang", "materi": "Persamaan dengan Variabel di Kedua Ruas",
        "soal_1": {"soal": f"Tentukan nilai x dari: {a4_1}x - {b4_1} = {c4_1}x + {d4_1}", "format": "Ketik format: x=n atau angkanya saja", "jawaban": [str(x4_1), f"x={x4_1}"]},
        "soal_2": {"soal": f"Tentukan nilai x dari: {a4_2}x + {b4_2} = {c4_2}x + {d4_2}", "format": "Ketik format: x=n atau angkanya saja", "jawaban": [str(x4_2), f"x={x4_2}"]},
        "paham_msg": "✅ *BERHASIL PAHAM!* Anda memahami prinsip pengelompokan suku-suku sejenis (variabel dengan variabel, konstanta dengan konstanta).",
        "socratic_hint": """🧭 *TUTOR SOKRATIK (Langkah demi Langkah):*
1. *Kelompokkan Variabel:* Pindahkan seluruh suku yang memuat $x$ ke satu sisi (misal: sisi kiri). Ingat ubah tandanya!
2. *Kelompokkan Konstanta:* Pindahkan seluruh angka biasa ke sisi seberangnya.
3. *Sederhanakan:* Lakukan operasi pengurangan/penjumlahan suku sejenis lalu cari nilai $x$."""
    })

    # Level 5: Pecahan Aljabar
    p5_1, a5_1, k5_1 = random.randint(2, 5), random.randint(1, 7), random.randint(2, 8)
    x5_1 = p5_1 * k5_1
    p5_2, a5_2, k5_2 = random.randint(3, 6), random.randint(1, 6), random.randint(2, 7)
    x5_2 = p5_2 * k5_2
    aljabar.append({
        "level": 5, "kesulitan": "Sedang", "materi": "Pecahan Aljabar Sederhana",
        "soal_1": {"soal": f"Tentukan nilai x dari: (x / {p5_1}) + {a5_1} = {k5_1 + a5_1}", "format": "Ketik format: x=n atau angkanya saja", "jawaban": [str(x5_1), f"x={x5_1}"]},
        "soal_2": {"soal": f"Tentukan nilai x dari: (x / {p5_2}) - {a5_2} = {k5_2 - a5_2}", "format": "Ketik format: x=n atau angkanya saja", "jawaban": [str(x5_2), f"x={x5_2}"]},
        "paham_msg": "✅ *BERHASIL PAHAM!* Anda menguasai penanganan persamaan pecahan linear dengan mengisolasi suku pecahan sebelum dikalikan penyebutnya.",
        "socratic_hint": """🧭 *TUTOR SOKRATIK (Langkah demi Langkah):*
1. *Bebaskan Pecahan:* Pindahkan terlebih dahulu konstanta luar yang mengganggu bentuk pecahan.
2. *Hilangkan Penyebut:* Setelah bentuk pecahan berdiri sendiri (misal: $x/p = k$), kalikan kedua ruas dengan nilai penyebut $p$."""
    })

    # Level 6: Pertidaksamaan (Soal 2 koefisien x minus)
    a6_1, b6_1, x6_1 = random.randint(2, 5), random.randint(1, 9), random.randint(2, 8)
    c6_1 = a6_1 * x6_1 - b6_1

    a6_2 = random.randint(2, 5)
    b6_2 = random.randint(2, 10)
    x6_2 = random.randint(1, 7)
    c6_2 = -a6_2 * x6_2 + b6_2
    aljabar.append({
        "level": 6, "kesulitan": "Sedang", "materi": "Pertidaksamaan Linear Satu Variabel",
        "soal_1": {"soal": f"Tentukan batas nilai x untuk: {a6_1}x - {b6_1} > {c6_1}", "format": "Ketik format: x>n", "jawaban": [f"x>{x6_1}"]},
        "soal_2": {"soal": f"Tentukan batas nilai x untuk: -{a6_2}x + {b6_2} <= {c6_2}", "format": "Ketik format pertidaksamaan: x>=n (perhatikan arah tanda saat dibagi negatif!)", "jawaban": [f"x>={x6_2}", f"x=>{x6_2}"]},
        "paham_msg": "✅ *BERHASIL PAHAM!* Anda memahami aturan pertidaksamaan, termasuk prinsip penting membalikkan arah tanda ketidaksamaan saat membagi dengan koefisien negatif.",
        "socratic_hint": """🧭 *TUTOR SOKRATIK (Langkah demi Langkah):*
1. *Perpindahan Suku:* Pindahkan konstanta ke ruas kanan seperti pada persamaan biasa.
2. *Waspada Koefisien Negatif:* Jika pembagi atau koefisien $x$ bernilai negatif, arah tanda ketidaksamaan *wajib dibalik* (misal: $\le$ menjadi $\ge$)."""
    })

    # Level 7: Pemfaktoran Kuadrat (Soal 2 ada minus)
    p7_1, q7_1 = random.sample(range(1, 7), 2)
    b7_1, c7_1 = p7_1 + q7_1, p7_1 * q7_1

    p7_2 = random.randint(2, 7)
    q7_2 = random.choice([i for i in range(1, 7) if i != p7_2])
    b7_2 = p7_2 - q7_2
    c7_2 = -p7_2 * q7_2
    tanda_b7_2 = f"+ {b7_2}x" if b7_2 > 0 else f"- {abs(b7_2)}x"
    aljabar.append({
        "level": 7, "kesulitan": "Sulit", "materi": "Pemfaktoran Bentuk Kuadrat",
        "soal_1": {
            "soal": f"Carilah faktor dari: x² + {b7_1}x + {c7_1} = 0",
            "format": "Ketik format faktor tanpa spasi berlebih: (x+p)(x+q)",
            "jawaban": [f"(x+{p7_1})(x+{q7_1})", f"(x+{q7_1})(x+{p7_1})", f"(x+{p7_1})(x+{q7_1})", f"(x+{q7_1})(x+{p7_1})"]
        },
        "soal_2": {
            "soal": f"Carilah faktor dari: x² {tanda_b7_2} - {abs(c7_2)} = 0",
            "format": "Ketik format faktor campuran tanda: (x+p)(x-q)",
            "jawaban": [f"(x+{p7_2})(x-{q7_2})", f"(x-{q7_2})(x+{p7_2})", f"(x+{p7_2})(x-{q7_2})", f"(x-{q7_2})(x+{p7_2})"]
        },
        "paham_msg": "✅ *BERHASIL PAHAM!* Anda menguasai dekomposisi polinomial kuadrat baik pada konstanta positif maupun negatif dengan menganalisis selisih dan hasil kali faktor.",
        "socratic_hint": """🧭 *TUTOR SOKRATIK (Langkah demi Langkah):*
1. *Analisis Syarat Kali:* Cari dua bilangan yang hasil perkaliannya sama dengan konstanta suku terakhir (perhatikan tanda negatifnya!).
2. *Analisis Syarat Jumlah:* Pastikan kedua bilangan tersebut apabila dijumlahkan menghasilkan koefisien suku tengah ($x$).
3. *Susun Faktor:* Masukkan kedua angka ke dalam format kurung $(x \pm p)(x \pm q)$."""
    })

    # Level 8: Akar Persamaan Kuadrat
    p8_1, q8_1 = sorted(random.sample(range(1, 8), 2))
    p8_2, q8_2 = sorted(random.sample(range(2, 9), 2))
    aljabar.append({
        "level": 8, "kesulitan": "Sulit", "materi": "Akar Persamaan Kuadrat",
        "soal_1": {"soal": f"Tentukan nilai x positif terbesar dari: x² - {p8_1 + q8_1}x + {p8_1 * q8_1} = 0", "format": "Ketik format: x=n atau angkanya saja", "jawaban": [str(q8_1), f"x={q8_1}"]},
        "soal_2": {"soal": f"Tentukan nilai x positif terbesar dari: x² - {p8_2 + q8_2}x + {p8_2 * q8_2} = 0", "format": "Ketik format: x=n atau angkanya saja", "jawaban": [str(q8_2), f"x={q8_2}"]},
        "paham_msg": "✅ *BERHASIL PAHAM!* Anda memahami prinsip pemecahan faktor nol untuk mengekstrak akar-akar persamaan kuadrat dan membandingkannya.",
        "socratic_hint": """🧭 *TUTOR SOKRATIK (Langkah demi Langkah):*
1. *Faktorkan Bentuk Kuadrat:* Ubah bentuk persamaan kuadrat menjadi perkalian dua faktor linear sama dengan nol.
2. *Gunakan Sifat Nol:* Samakan masing-masing faktor kurung dengan angka nol untuk mendapatkan nilai akar-akarnya.
3. *Seleksi Nilai:* Bandingkan nilai akar yang diperoleh dan pilih nilai terbesar sesuai permintaan soal."""
    })

    # Level 9: SPLDV
    x9_1, y9_1, a9_1 = random.randint(2, 8), random.randint(1, 7), random.randint(2, 4)
    x9_2, y9_2, a9_2 = random.randint(3, 9), random.randint(1, 6), random.randint(2, 5)
    aljabar.append({
        "level": 9, "kesulitan": "Sulit", "materi": "Sistem Persamaan Linear Dua Variabel",
        "soal_1": {"soal": f"Selesaikan SPLDV: x + y = {x9_1 + y9_1} dan {a9_1}x - y = {a9_1 * x9_1 - y9_1}. Berapakah x?", "format": "Ketik format: x=n atau angkanya saja", "jawaban": [str(x9_1), f"x={x9_1}"]},
        "soal_2": {"soal": f"Selesaikan SPLDV: x + y = {x9_2 + y9_2} dan {a9_2}x - y = {a9_2 * x9_2 - y9_2}. Berapakah x?", "format": "Ketik format: x=n atau angkanya saja", "jawaban": [str(x9_2), f"x={x9_2}"]},
        "paham_msg": "✅ *BERHASIL PAHAM!* Anda menguasai metode eliminasi untuk mereduksi sistem persamaan linear dua variabel.",
        "socratic_hint": """🧭 *TUTOR SOKRATIK (Langkah demi Langkah):*
1. *Cek Tanda Variabel:* Perhatikan tanda koefisien variabel $y$ pada kedua persamaan (apakah sudah berlawanan tanda?).
2. *Eliminasi:* Jika tandanya berlawanan ($+y$ dan $-y$), jumlahkan kedua persamaan secara langsung agar variabel $y$ tereliminasi.
3. *Selesaikan:* Selesaikan persamaan satu variabel tersisa untuk mencari nilai $x$."""
    })

    # Level 10: Eksponen Aljabar
    b10_1 = random.choice([2, 3])
    k10_1 = random.randint(1, 3)
    x10_1 = random.randint(1, 4)
    m10_1 = x10_1 + k10_1

    b10_2 = random.choice([2, 3, 5])
    k10_2 = random.randint(1, 3)
    x10_2 = random.randint(2, 5)
    m10_2 = x10_2 - k10_2
    aljabar.append({
        "level": 10, "kesulitan": "Sangat Sulit", "materi": "Persamaan Eksponen Aljabar",
        "soal_1": {"soal": f"Tentukan nilai x dari: {b10_1}^(x + {k10_1}) = {b10_1 ** m10_1}", "format": "Ketik format: x=n atau angkanya saja", "jawaban": [str(x10_1), f"x={x10_1}"]},
        "soal_2": {"soal": f"Tentukan nilai x dari: {b10_2}^(x - {k10_2}) = {b10_2 ** m10_2}", "format": "Ketik format: x=n atau angkanya saja", "jawaban": [str(x10_2), f"x={x10_2}"]},
        "paham_msg": "✅ *BERHASIL PAHAM!* Luar biasa! Level puncak Aljabar tercapai. Anda memahami penyetaraan basis eksponen.",
        "socratic_hint": """🧭 *TUTOR SOKRATIK (Langkah demi Langkah):*
1. *Sifat Basis Eksponen:* Ubah angka konstanta di ruas kanan menjadi bentuk bilangan berpangkat yang memiliki basis sama dengan ruas kiri.
2. *Penyetaraan Pangkat:* Jika basis di kiri dan kanan sudah sama ($b^A = b^B$), coret basisnya.
3. *Selesaikan Persamaan:* Turunkan bagian pangkatnya menjadi persamaan linear biasa ($A = B$)."""
    })

    # --- MODUL KALKULUS (10 LEVEL, MASING-MASING 2 SOAL ACAK) ---
    kalkulus = []

    # Level 1: Limit Fungsi
    c1_k1, a1_k1, b1_k1 = random.randint(1, 5), random.randint(2, 6), random.randint(1, 9)
    c1_k2, a1_k2, b1_k2 = random.randint(2, 6), random.randint(2, 5), random.randint(1, 8)
    kalkulus.append({
        "level": 1, "kesulitan": "Mudah", "materi": "Konsep Limit Fungsi Aljabar",
        "soal_1": {"soal": f"Tentukan nilai limit: lim (x->{c1_k1}) ({a1_k1}x + {b1_k1})", "format": "Ketik hasil berupa angka", "jawaban": [str(a1_k1 * c1_k1 + b1_k1)]},
        "soal_2": {"soal": f"Tentukan nilai limit: lim (x->{c1_k2}) ({a1_k2}x - {b1_k2})", "format": "Ketik hasil berupa angka", "jawaban": [str(a1_k2 * c1_k2 - b1_k2)]},
        "paham_msg": "✅ *BERHASIL PAHAM!* Anda menguasai teorema substitusi langsung pada fungsi polinomial yang bersifat kontinu.",
        "socratic_hint": """🧭 *TUTOR SOKRATIK (Langkah demi Langkah):*
1. *Cek Kontinuitas:* Perhatikan apakah fungsi memiliki penyebut yang bernilai nol pada titik limit tersebut.
2. *Substitusi Langsung:* Karena fungsi bersifat kontinu, masukkan nilai pendekatan $x$ secara langsung ke dalam fungsi untuk menghitung nilainya."""
    })

    # Level 2: Turunan Dasar
    a2_k1, n2_k1 = random.randint(2, 6), random.randint(3, 6)
    a2_k2, n2_k2 = random.randint(2, 7), random.randint(3, 7)
    kalkulus.append({
        "level": 2, "kesulitan": "Mudah", "materi": "Turunan Dasar (Aturan Pangkat)",
        "soal_1": {"soal": f"Tentukan turunan f'(x) dari f(x) = {a2_k1}x^{n2_k1}", "format": "Ketik format: ax^n", "jawaban": [f"{a2_k1*n2_k1}x^{n2_k1-1}", f"{a2_k1*n2_k1}x^{n2_k1-1}", f"{a2_k1*n2_k1}x*{n2_k1-1}"]},
        "soal_2": {"soal": f"Tentukan turunan f'(x) dari f(x) = {a2_k2}x^{n2_k2}", "format": "Ketik format: ax^n", "jawaban": [f"{a2_k2*n2_k2}x^{n2_k2-1}", f"{a2_k2*n2_k2}x^{n2_k2-1}", f"{a2_k2*n2_k2}x*{n2_k2-1}"]},
        "paham_msg": "✅ *BERHASIL PAHAM!* Anda memahami Power Rule turunan: pangkat dikalikan ke koefisien depan dan pangkat dikurangi satu.",
        "socratic_hint": """🧭 *TUTOR SOKRATIK (Langkah demi Langkah):*
1. *Turunkan Pangkat:* Pindahkan angka eksponen/pangkat ke depan sebagai pengali koefisien.
2. *Kurangi Pangkat:* Kurangi nilai pangkat variabel semula dengan angka 1."""
    })

    # Level 3: Turunan Penjumlahan
    a3_k1, b3_k1 = random.randint(2, 5), random.randint(2, 6)
    a3_k2, b3_k2 = random.randint(2, 6), random.randint(3, 7)
    kalkulus.append({
        "level": 3, "kesulitan": "Mudah", "materi": "Turunan Penjumlahan Fungsi",
        "soal_1": {"soal": f"Tentukan turunan f'(x) dari f(x) = {a3_k1}x³ + {b3_k1}x²", "format": "Ketik format suku penjumlahan: px^2+qx", "jawaban": [f"{3*a3_k1}x^2+{2*b3_k1}x", f"{3*a3_k1}x^2+{2*b3_k1}*x", f"{3*a3_k1}x*2+{2*b3_k1}x"]},
        "soal_2": {"soal": f"Tentukan turunan f'(x) dari f(x) = {a3_k2}x³ + {b3_k2}x²", "format": "Ketik format suku penjumlahan: px^2+qx", "jawaban": [f"{3*a3_k2}x^2+{2*b3_k2}x", f"{3*a3_k2}x^2+{2*b3_k2}*x", f"{3*a3_k2}x*2+{2*b3_k2}x"]},
        "paham_msg": "✅ *BERHASIL PAHAM!* Anda menguasai sifat linieritas turunan dengan mendeferensiasikan fungsi suku demi suku.",
        "socratic_hint": """🧭 *TUTOR SOKRATIK (Langkah demi Langkah):*
1. *Pecah Suku:* Terapkan aturan turunan pada masing-masing suku secara terpisah.
2. *Gabungkan Kembali:* Jumlahkan hasil turunan setiap suku menggunakan tanda tambah (+) semula."""
    })

    # Level 4: Turunan Trigonometri
    a4_k1 = random.randint(2, 8)
    b4_k2 = random.randint(2, 8)
    kalkulus.append({
        "level": 4, "kesulitan": "Sedang", "materi": "Turunan Fungsi Trigonometri",
        "soal_1": {"soal": f"Tentukan turunan f'(x) dari f(x) = {a4_k1}sin(x)", "format": "Ketik format: a*cos(x) atau acos(x)", "jawaban": [f"{a4_k1}cos(x)", f"{a4_k1}*cos(x)", f"{a4_k1}cosx"]},
        "soal_2": {"soal": f"Tentukan turunan f'(x) dari f(x) = {b4_k2}cos(x)", "format": "Ketik format: -b*sin(x) atau -bsin(x)", "jawaban": [f"-{b4_k2}sin(x)", f"-{b4_k2}*sin(x)", f"-{b4_k2}sinx"]},
        "paham_msg": "✅ *BERHASIL PAHAM!* Anda memahami turunan fungsi trigonometri dasar beserta aturan perkalian konstanta.",
        "socratic_hint": """🧭 *TUTOR SOKRATIK (Langkah demi Langkah):*
1. *Pertahankan Konstanta:* Biarkan angka pengali di depan tetap utuh.
2. *Transformasi Trigonometri:* Ingat kembali tabel turunan baku untuk fungsi sinus dan kosinus."""
    })

    # Level 5: Aturan Rantai
    a5_k1, b5_k1, n5_k1 = random.randint(2, 4), random.randint(1, 5), random.randint(3, 5)
    a5_k2, b5_k2, n5_k2 = random.randint(2, 5), random.randint(1, 6), random.randint(3, 4)
    kalkulus.append({
        "level": 5, "kesulitan": "Sedang", "materi": "Aturan Rantai (Chain Rule)",
        "soal_1": {"soal": f"Tentukan turunan f'(x) dari f(x) = ({a5_k1}x + {b5_k1})^{n5_k1}", "format": "Ketik format: k(ax+b)^m", "jawaban": [f"{n5_k1*a5_k1}({a5_k1}x+{b5_k1})^{n5_k1-1}", f"{n5_k1*a5_k1}({a5_k1}x+{b5_k1})^{n5_k1-1}", f"{n5_k1*a5_k1}({a5_k1}x+{b5_k1})*{n5_k1-1}"]},
        "soal_2": {"soal": f"Tentukan turunan f'(x) dari f(x) = ({a5_k2}x - {b5_k2})^{n5_k2}", "format": "Ketik format: k(ax-b)^m", "jawaban": [f"{n5_k2*a5_k2}({a5_k2}x-{b5_k2})^{n5_k2-1}", f"{n5_k2*a5_k2}({a5_k2}x-{b5_k2})^{n5_k2-1}", f"{n5_k2*a5_k2}({a5_k2}x-{b5_k2})*{n5_k2-1}"]},
        "paham_msg": "✅ *BERHASIL PAHAM!* Anda menguasai Aturan Rantai: menurunkan fungsi pangkat luar lalu mengalikannya dengan turunan fungsi dalam kurung.",
        "socratic_hint": """🧭 *TUTOR SOKRATIK (Langkah demi Langkah):*
1. *Turunan Luar:* Turunkan pangkat fungsi luar terlebih dahulu dengan isi kurung dibiarkan tetap.
2. *Turunan Dalam (Chain):* Kalikan hasil tersebut dengan turunan bagian dalam kurung."""
    })

    # Level 6: Integral Tak Tentu
    n6_k1, c6_k1 = random.randint(3, 5), random.randint(1, 4)
    k6_k1 = n6_k1 * c6_k1
    n6_k2, c6_k2 = random.randint(2, 4), random.randint(2, 5)
    k6_k2 = n6_k2 * c6_k2
    ans6_1 = f"x^{n6_k1}" if c6_k1 == 1 else f"{c6_k1}x^{n6_k1}"
    ans6_2 = f"x^{n6_k2}" if c6_k2 == 1 else f"{c6_k2}x^{n6_k2}"
    kalkulus.append({
        "level": 6, "kesulitan": "Sedang", "materi": "Integral Tak Tentu Dasar",
        "soal_1": {"soal": f"Tentukan hasil integral: ∫ {k6_k1}x^{n6_k1-1} dx (abaikan C)", "format": "Ketik format: ax^n", "jawaban": [ans6_1, ans6_1.replace("x", "x").lstrip(""), ans6_1.replace("^", "**")]},
        "soal_2": {"soal": f"Tentukan hasil integral: ∫ {k6_k2}x^{n6_k2-1} dx (abaikan C)", "format": "Ketik format: ax^n", "jawaban": [ans6_2, ans6_2.replace("x", "x").lstrip(""), ans6_2.replace("^", "**")]},
        "paham_msg": "✅ *BERHASIL PAHAM!* Anda menguasai kebalikan turunan: menaikkan pangkat satu satuan dan membagi koefisien dengan pangkat baru.",
        "socratic_hint": """🧭 *TUTOR SOKRATIK (Langkah demi Langkah):*
1. *Naikkan Pangkat:* Tambahkan nilai eksponen/pangkat variabel dengan angka 1.
2. *Bagi Koefisien:* Bagilah koefisien di depan dengan hasil penjumlahan pangkat yang baru."""
    })

    # Level 7: Integral Tentu
    a7_k1, b7_k1 = random.randint(1, 3), random.randint(1, 3)
    a7_k2, b7_k2 = random.randint(1, 4), random.randint(2, 3)
    kalkulus.append({
        "level": 7, "kesulitan": "Sulit", "materi": "Integral Tentu Batas Sederhana",
        "soal_1": {"soal": f"Hitung integral tentu: ∫ (dari 0 s.d {b7_k1}) {3*a7_k1}x² dx", "format": "Ketik angka hasil akhir", "jawaban": [str(a7_k1 * (b7_k1 ** 3))]},
        "soal_2": {"soal": f"Hitung integral tentu: ∫ (dari 0 s.d {b7_k2}) {3*a7_k2}x² dx", "format": "Ketik angka hasil akhir", "jawaban": [str(a7_k2 * (b7_k2 ** 3))]},
        "paham_msg": "✅ *BERHASIL PAHAM!* Anda menguasai Teorema Dasar Kalkulus dalam mengevaluasi selisih antiturunan pada batas atas dan batas bawah.",
        "socratic_hint": """🧭 *TUTOR SOKRATIK (Langkah demi Langkah):*
1. *Cari Antiturunan:* Selesaikan bentuk integral tak tentu terlebih dahulu.
2. *Evaluasi Batas:* Masukkan batas atas ke fungsi antiturunan, lalu kurangi dengan hasil substitusi batas bawah."""
    })

    # Level 8: Product Rule
    a8_k1 = random.randint(2, 6)
    b8_k2 = random.randint(2, 6)
    kalkulus.append({
        "level": 8, "kesulitan": "Sulit", "materi": "Turunan Aturan Perkalian (Product Rule)",
        "soal_1": {"soal": f"Tentukan turunan f'(x) dari f(x) = {a8_k1}x · sin(x)", "format": "Ketik format: asin(x)+ax*cos(x)", "jawaban": [f"{a8_k1}sin(x)+{a8_k1}x*cos(x)", f"{a8_k1}*sin(x)+{a8_k1}*x*cos(x)", f"{a8_k1}sin(x)+{a8_k1}xcos(x)"]},
        "soal_2": {"soal": f"Tentukan turunan f'(x) dari f(x) = {b8_k2}x · cos(x)", "format": "Ketik format: bcos(x)-bx*sin(x)", "jawaban": [f"{b8_k2}cos(x)-{b8_k2}x*sin(x)", f"{b8_k2}cos(x)+{b8_k2}*x-sin(x)", f"{b8_k2}cos(x)-{b8_k2}xsin(x)"]},
        "paham_msg": "✅ *BERHASIL PAHAM!* Anda menguasai Product Rule: u'v + uv'.",
        "socratic_hint": """🧭 *TUTOR SOKRATIK (Langkah demi Langkah):*
1. *Pemisalan:* Tentukan komponen pertama sebagai $u$ dan komponen kedua sebagai $v$.
2. *Terapkan Rumus:* Gunakan rumus turunan perkalian $u'v + uv'$ secara sistematis."""
    })

    # Level 9: Titik Stasioner
    k9_k1 = random.randint(2, 7)
    k9_k2 = random.choice([i for i in range(2, 9) if i != k9_k1])
    kalkulus.append({
        "level": 9, "kesulitan": "Sulit", "materi": "Titik Stasioner Kurva",
        "soal_1": {"soal": f"Tentukan nilai absis x saat f(x) = x² - {2*k9_k1}x stasioner", "format": "Ketik format: x=n atau angkanya saja", "jawaban": [str(k9_k1), f"x={k9_k1}"]},
        "soal_2": {"soal": f"Tentukan nilai absis x saat f(x) = x² - {2*k9_k2}x stasioner", "format": "Ketik format: x=n atau angkanya saja", "jawaban": [str(k9_k2), f"x={k9_k2}"]},
        "paham_msg": "✅ *BERHASIL PAHAM!* Anda menguasai aplikasi turunan untuk mencari titik stasioner saat gradien bernilai nol.",
        "socratic_hint": """🧭 *TUTOR SOKRATIK (Langkah demi Langkah):*
1. *Cari Turunan Pertama:* Tentukan bentuk $f'(x)$ dari kurva yang diberikan.
2. *Syarat Stasioner:* Tetapkan $f'(x) = 0$ lalu selesaikan persamaan aljabarnya untuk menemukan nilai $x$."""
    })

    # Level 10: Integral Substitusi
    a10_k1, n10_k1 = random.randint(1, 5), random.randint(2, 4)
    a10_k2, n10_k2 = random.randint(2, 6), random.randint(3, 5)
    kalkulus.append({
        "level": 10, "kesulitan": "Sangat Sulit", "materi": "Integral Substitusi Lanjutan",
        "soal_1": {
            "soal": f"Tentukan hasil integral: ∫ 2x(x² + {a10_k1})^{n10_k1} dx (abaikan C)",
            "format": "Ketik format pecahan koefisien dan pangkat: (1/m)(x^2+a)^m",
            "jawaban": [f"(1/{n10_k1+1})(x^2+{a10_k1})^{n10_k1+1}", f"(x^2+{a10_k1})^{n10_k1+1}/{n10_k1+1}", f"(1/{n10_k1+1})*(x^2+{a10_k1})^{n10_k1+1}"]
        },
        "soal_2": {
            "soal": f"Tentukan hasil integral: ∫ 2x(x² - {a10_k2})^{n10_k2} dx (abaikan C)",
            "format": "Ketik format pecahan koefisien dan pangkat: (1/m)(x^2-a)^m",
            "jawaban": [f"(1/{n10_k2+1})(x^2-{a10_k2})^{n10_k2+1}", f"(x^2-{a10_k2})^{n10_k2+1}/{n10_k2+1}", f"(1/{n10_k2+1})*(x^2-{a10_k2})^{n10_k2+1}"]
        },
        "paham_msg": "✅ *BERHASIL PAHAM!* Luar biasa! Level puncak Kalkulus tercapai. Anda menguasai Teknik Integrasi Substitusi.",
        "socratic_hint": """🧭 *TUTOR SOKRATIK (Langkah demi Langkah):*
1. *Pemisalan Variabel ($u$):* Misalkan bagian di dalam kurung sebagai variabel baru $u$.
2. *Diferensial ($du$):* Tentukan turunan $du$ untuk mencocokkan unsur luar.
3. *Integralkan:* Ubah ke bentuk variabel $u$, integralkan pangkatnya, lalu kembalikan ke fungsi asal."""
    })

    return {"Aljabar": aljabar, "Kalkulus": kalkulus}


# ==========================================
# 3. MANAJEMEN STATE GAME (NYAWA HATI = 3, SKOR 10/LEVEL)
# ==========================================
if "database_acak" not in st.session_state:
    st.session_state.database_acak = generate_semua_soal()
if "materi_terpilih" not in st.session_state:
    st.session_state.materi_terpilih = "Aljabar"
if "current_level" not in st.session_state:
    st.session_state.current_level = 0
if "sub_soal" not in st.session_state:
    st.session_state.sub_soal = 1
if "hp" not in st.session_state:
    st.session_state.hp = 3
if "score" not in st.session_state:
    st.session_state.score = 0
if "evaluasi" not in st.session_state:
    st.session_state.evaluasi = None
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "completed" not in st.session_state:
    st.session_state.completed = False


def reset_modul():
    st.session_state.database_acak = generate_semua_soal()
    st.session_state.current_level = 0
    st.session_state.sub_soal = 1
    st.session_state.hp = 3
    st.session_state.score = 0
    st.session_state.evaluasi = None
    st.session_state.game_over = False
    st.session_state.completed = False


# ==========================================
# 4. TAMPILAN UTAMA & SIDEBAR
# ==========================================
st.markdown("<h1 class='main-header'>🏛️ Simulator Socratic Stepper</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Generator Langkah Penyelesaian Aljabar dan Kalkulus Otomatis</p>", unsafe_allow_html=True)
st.divider()

st.sidebar.header("📚 Panel Navigasi Modul")
pilihan_materi = st.sidebar.radio(
    "Pilih Modul Pembelajaran:",
    ["Aljabar", "Kalkulus"],
    format_func=lambda x: f"🧮 {x}" if x == "Aljabar" else f"📈 {x}"
)

if pilihan_materi != st.session_state.materi_terpilih:
    st.session_state.materi_terpilih = pilihan_materi
    reset_modul()

ikon_modul = "🧮" if st.session_state.materi_terpilih == "Aljabar" else "📈"

st.sidebar.divider()
st.sidebar.markdown(f"{ikon_modul} *Modul Aktif:* {st.session_state.materi_terpilih}")
st.sidebar.markdown(f"❤️ *Nyawa (HP):* {'❤️' * st.session_state.hp} ({st.session_state.hp}/3)")
st.sidebar.markdown(f"🎓 *Skor Penguasaan:* {st.session_state.score} / 100")
if st.sidebar.button("🔄 Ulangi & Acak Soal Baru"):
    reset_modul()
    st.rerun()

# ==========================================
# 5. LOGIKA GAME & TAMPILAN (2 SOAL PER LEVEL, SKOR 10 PER LEVEL)
# ==========================================
daftar_soal = st.session_state.database_acak[st.session_state.materi_terpilih]
total_level = len(daftar_soal)

if st.session_state.game_over:
    st.error("💔 *SIMULASI TERHENTI! Nyawa Anda Telah Habis (0/3).*")
    st.info("Metode Sokratik mengajarkan bahwa kesalahan adalah bagian dari proses konstruksi pemahaman. Silakan ulangi modul ini untuk mencoba paket soal baru!")
    if st.button("🔄 Ulangi & Acak Soal Baru", type="primary"):
        reset_modul()
        st.rerun()

elif st.session_state.completed:
    st.balloons()
    st.success(f"🏆 *SELAMAT!* Anda berhasil menuntaskan seluruh 10 Level modul *{st.session_state.materi_terpilih}*!")
    st.metric(label="Total Skor Penguasaan Akhir", value=f"{st.session_state.score} / 100 Poin")
    if st.button("📚 Ulangi dengan Soal Baru"):
        reset_modul()
        st.rerun()

else:
    data_level = daftar_soal[st.session_state.current_level]
    soal_data = data_level[f"soal_{st.session_state.sub_soal}"]

    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown(f"📌 *Modul:* {st.session_state.materi_terpilih}")
    with col_b:
        st.markdown(f"📊 *Kesulitan:* {data_level['kesulitan']}")
    with col_c:
        st.markdown(f"🎯 *Level:* {data_level['level']} / {total_level} (Soal {st.session_state.sub_soal}/2)")

    st.markdown("<div class='card-box'>", unsafe_allow_html=True)
    st.subheader(f"Level {data_level['level']}: {data_level['materi']}")
    st.markdown(f"*Pertanyaan:*\n### {soal_data['soal']}")
    st.markdown(f"📝 {soal_data['format']}")
    st.markdown("</div>", unsafe_allow_html=True)
    st.write("")

    input_user = st.text_input("Ketikkan format jawaban/langkah Anda di sini:", key=f"ans_{st.session_state.materi_terpilih}_lvl{data_level['level']}_s{st.session_state.sub_soal}")

    if st.button("🔍 Periksa Jawaban", type="primary"):
        ans_clean = input_user.strip().replace(" ", "").lower()
        valid_answers = [a.replace(" ", "").lower() for a in soal_data["jawaban"]]

        if ans_clean in valid_answers:
            st.session_state.evaluasi = "paham"
        else:
            st.session_state.evaluasi = "belum_paham"
            st.session_state.hp -= 1
            if st.session_state.hp <= 0:
                st.session_state.game_over = True

    if st.session_state.evaluasi == "paham":
        st.markdown(f"<div class='success-box'>{data_level['paham_msg']}</div>", unsafe_allow_html=True)
        st.write("")

        btn_teks = "➡️ Lanjut ke Soal Berikutnya" if st.session_state.sub_soal == 1 else "➡️ Lanjut ke Level Berikutnya"
        if st.button(btn_teks, type="primary"):
            st.session_state.evaluasi = None
            if st.session_state.sub_soal == 1:
                st.session_state.sub_soal = 2
            else:
                st.session_state.sub_soal = 1
                st.session_state.score += 10
                if st.session_state.current_level + 1 < total_level:
                    st.session_state.current_level += 1
                else:
                    st.session_state.completed = True
            st.rerun()

    elif st.session_state.evaluasi == "belum_paham" and not st.session_state.game_over:
        st.markdown(f"<div class='fail-box'>🧭 *BELUM BERHASIL PAHAM!* Nyawa berkurang 1 (Sisa: {'❤️'*st.session_state.hp} - {st.session_state.hp}/3)</div>", unsafe_allow_html=True)
        st.markdown(data_level['socratic_hint'])

st.divider()
st.caption("Simulator Socratic Stepper - Program Komputer Interaktif Matematika | Universitas Negeri Manado")
