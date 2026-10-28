# Pertemuan 13 - Debugging dan Testing

Nama: Aulia Rahma Ramadhani  
NIM: 2225250001  
Kelas: 3A

## Kasus

Pertemuan ini membahas debugging, tracing, testing, dan test case pada program Python. Terdapat beberapa kasus yang dipelajari, yaitu bug batas kelulusan, kesalahan perhitungan rata-rata, pencarian nilai tertinggi, serta penanganan file nilai.

## Test Case

| ID | Target | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|---|
| T1 | Rata-rata | `[80, 60, 90, 70]` | 75.0 | Belum dicatat | Belum diuji |
| T2 | Rata-rata | `[100, 80]` | 90.0 | Belum dicatat | Belum diuji |
| T3 | Status kelulusan | 60 | Lulus | Belum dicatat | Belum diuji |
| T4 | Status kelulusan | 59 | Tidak lulus | Belum dicatat | Belum diuji |
| T5 | Nilai tertinggi | `[80, 60, 90, 70]` | 90 | Belum dicatat | Belum diuji |

## Bug Report

### B01 - Kesalahan Perhitungan Rata-rata
- **Gejala:** Hasil rata-rata tidak sesuai dengan jumlah data.
- **Test case:** T1 dan T2.
- **Lokasi:** Fungsi `hitung_rata_rata()`.
- **Akar penyebab:** Pembagi selalu menggunakan angka 5.
- **Perbaikan:** Menggunakan `len(nilai)` sebagai pembagi dan menangani list kosong.
- **Retest:** Hasil untuk data `[80, 60, 90, 70]` sudah menunjukkan rata-rata 75.0. T2 perlu diuji secara terpisah.

### B02 - Kesalahan Status Kelulusan
- **Gejala:** Nilai 60 dapat dinyatakan tidak lulus.
- **Test case:** T3.
- **Lokasi:** Fungsi `status()`.
- **Akar penyebab:** Operator pembanding menggunakan `>`.
- **Perbaikan:** Mengganti operator menjadi `>=`.
- **Retest:** Nilai 60 menghasilkan status Lulus.

### B03 - Kesalahan Nilai Tertinggi
- **Gejala:** Nilai tertinggi dapat menghasilkan nilai yang salah.
- **Test case:** T5.
- **Lokasi:** Fungsi `nilai_tertinggi()`.
- **Akar penyebab:** Kondisi perbandingan menggunakan `<` dan nilai awal ditetapkan 0.
- **Perbaikan:** Menggunakan `>` dan menginisialisasi nilai tertinggi dari data pertama.
- **Retest:** Data `[80, 60, 90, 70]` menghasilkan nilai tertinggi 90.

## Retest

Setelah perbaikan, program `praktik/praktik_4_debugging.py` menghasilkan output:

```text
Rata-rata: 75.0
Status 60: Lulus
Tertinggi: 90
```

Hasil tersebut sesuai dengan expected untuk T1, T3, dan T5. T2 dan T4 perlu dijalankan secara terpisah untuk memastikan seluruh test case berhasil.

## Cara Menjalankan

Jalankan program praktik menggunakan perintah:

```bash
python praktik/praktik_4_debugging.py
```

Untuk menjalankan kasus penanganan file nilai tambahan:

```bash
python kasus/kasus_03_file_nilai.py
```

## Refleksi

Saya mempelajari bahwa debugging harus dilakukan secara sistematis dengan mengamati output, menelusuri nilai variabel, menemukan akar penyebab bug, dan melakukan pengujian ulang. Test case membantu memastikan program menghasilkan output sesuai harapan setelah diperbaiki. Penggunaan breakpoint dan tracing juga membantu memahami alur program serta perubahan nilai variabel.