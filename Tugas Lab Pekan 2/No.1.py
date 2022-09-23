# NOMOR 1 PEKAN 2 PRAKTIKUM
# MAHENDRA KIRANA MB ( H071221058 )
    # SOAL
        # Buatlah program yang dapat mengkonversi nilai dalam bentuk angka ke huruf dengan aturan:
            # Nilai >= 90 (A)
                # Nilai >= 80 (B)
                    # Nilai >= 70 (C)
                    # Nilai >= 60 (D)
                # Nilai <= 40 (E)
            # Nilai <  40 (F)
            
nilai = int(input('Masukkan Nilai : '))

if   nilai >= 90   :
    print('Nilai',nilai, "= 'A'")

elif nilai >= 80 :
    print("Nilai",nilai, "= 'B'")

elif nilai >= 70 :
    print("Nilai",nilai, "= 'C'")

elif nilai >= 60 :
    print("Nilai",nilai, "= 'D'")

elif nilai <= 40 :
    print("Nilai",nilai, "= 'E'")

elif nilai < 40 :
    print("Nilai",nilai, "= 'F'")


        
