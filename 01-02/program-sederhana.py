# Perkenalan

import os

a = input('Nama: ')
b = input('Alamat: ')
c = input('Gender: ')
d = input('Hobby: ')

os.system('cls')
dataDiri = {'Nama' : a, 'Alamat' : b, 'Gender' : c, 'Hobby' : d}
perkenalan = 'Hallo, nama saya ' + dataDiri['Nama'] + ' saya adalah seorang ' + dataDiri['Gender'] + ' yang berasal dari ' + dataDiri['Alamat'] + ' dan mempunyai hobby ' + dataDiri['Hobby']
print(perkenalan)

# Luas Segitiga

alas = input('Masukkan alas segitiga: ')
tinggi = input('masukkan tinggi segitiga: ')

luas_segitiga = 0.5 * int(alas) * int(tinggi)
print('Luas Segitiga adalah: ', luas_segitiga)

# Luas Persegi/Persegi panjang

panjang = input('Masukan Panjang persegi: ')
lebar = input('Masukan Panjang persegi: ')

luas_persegi = int(panjang) * int(lebar)
print('Luas Persegi/Persegi Panjang: ', luas_persegi)