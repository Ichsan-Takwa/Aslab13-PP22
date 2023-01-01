def getFPB(pertama, kedua):
  terkecil = pertama
  fpb = 0
  
  if pertama > kedua:
    terkecil = kedua

  for x in range(1, terkecil + 1):
    if pertama % x == 0 and kedua % x == 0:
      fpb = x

  print(fpb)


getFPB(20,199)
