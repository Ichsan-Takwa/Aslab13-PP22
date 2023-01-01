myDay = int(input('masukkan hari:'))
def myDay(usia):
  
  tahun = usia // 365
  bulan = (usia - tahun * 365) // 30
  hari = usia - tahun * 365 - bulan * 30
  
  print(tahun, "TAHUN")
  print(bulan, "BULAN")
  print(hari, "HARI")
  
# myDay(400)