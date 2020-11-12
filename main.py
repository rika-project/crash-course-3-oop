from geometry.bangun_ruang import BangunRuang
from geometry.persegi_panjang import PersegiPanjang

print('Menggunakan OOP')
p1 = PersegiPanjang(30, 20)

p1.info()
p1.luas()

from geometry.segitiga import Segitiga

p2 = Segitiga(20, 10)

p2.info()
p2.luas()

print('\nMencoba membuat objek dari kelas BangunRuang')
b1 = BangunRuang()
print(b1.info())
print(b1.luas())


#Polymorphism: kemampuan objek untuk merespon berbeda, terhadap pemanggilan method yang sama
daftar_bangun_ruang = [p1, p2]

for bangun_ruang in daftar_bangun_ruang :
    print(bangun_ruang.info())
    print(bangun_ruang.luas())