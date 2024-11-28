data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

# # Menampilkan data panen
# for lokasi, data in data_panen.items():
#     print(f"Lokasi: {data['nama_lokasi']}")
#     print("Hasil Panen:")
#     for komoditas, jumlah in data['hasil_panen'].items():
#         print(f"  {komoditas.capitalize()}: {jumlah}")
#     print()

# # Mengakses hasil panen jagung dari lokasi2
# hasil_jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
# print(f"Jumlah hasil panen jagung dari lokasi2: {hasil_jagung_lokasi2}")

# # Mengakses nama lokasi dari lokasi3
# nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
# print(f"Nama lokasi dari lokasi3: {nama_lokasi3}")

# # Membuat variabel untuk menyimpan jumlah hasil panen padi
# padi_lokasi1 = data_panen['lokasi1']['hasil_panen']['padi']
# padi_lokasi2 = data_panen['lokasi2']['hasil_panen']['padi']
# padi_lokasi3 = data_panen['lokasi3']['hasil_panen']['padi']
# padi_lokasi4 = data_panen['lokasi4']['hasil_panen']['padi']
# padi_lokasi5 = data_panen['lokasi5']['hasil_panen']['padi']

# # Membuat variabel untuk menyimpan jumlah hasil panen kedelai
# kedelai_lokasi1 = data_panen['lokasi1']['hasil_panen']['kedelai']
# kedelai_lokasi2 = data_panen['lokasi2']['hasil_panen']['kedelai']
# kedelai_lokasi3 = data_panen['lokasi3']['hasil_panen']['kedelai']
# kedelai_lokasi4 = data_panen['lokasi4']['hasil_panen']['kedelai']
# kedelai_lokasi5 = data_panen['lokasi5']['hasil_panen']['kedelai']

# # Menampilkan hasil
# print(f"Hasil Panen Padi:")
# print(f"  Lokasi 1: {padi_lokasi1}")
# print(f"  Lokasi 2: {padi_lokasi2}")
# print(f"  Lokasi 3: {padi_lokasi3}")
# print(f"  Lokasi 4: {padi_lokasi4}")
# print(f"  Lokasi 5: {padi_lokasi5}")

# print("\nHasil Panen Kedelai:")
# print(f"  Lokasi 1: {kedelai_lokasi1}")
# print(f"  Lokasi 2: {kedelai_lokasi2}")
# print(f"  Lokasi 3: {kedelai_lokasi3}")
# print(f"  Lokasi 4: {kedelai_lokasi4}")
# print(f"  Lokasi 5: {kedelai_lokasi5}")

# # Memeriksa kondisi setiap lokasi
# for lokasi, data in data_panen.items():
#     nama_lokasi = data['nama_lokasi']
#     hasil_padi = data['hasil_panen']['padi']
#     hasil_jagung = data['hasil_panen']['jagung']
    
#     # Percabangan untuk menentukan perhatian khusus atau tidak
#     if hasil_padi > 1300 or hasil_jagung > 800:
#         print(f"Lokasi {nama_lokasi} memerlukan perhatian khusus.")
#     else:
#         print(f"Lokasi {nama_lokasi} dalam kondisi baik.")
