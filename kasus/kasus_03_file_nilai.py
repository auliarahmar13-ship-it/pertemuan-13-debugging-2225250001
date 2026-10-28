
def baca_nilai(nama_file):
    try:
        with open(nama_file, "r") as file:
            nilai = []
            for baris in file:
                nilai.append(float(baris.strip()))
            return nilai
    except FileNotFoundError:
        print("File tidak ditemukan")
        return []
    except ValueError:
        print("Data nilai tidak valid")
        return []


print(baca_nilai("nilai.txt"))