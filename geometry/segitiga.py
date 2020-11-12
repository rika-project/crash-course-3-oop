from geometry.bangun_ruang import BangunRuang


class Segitiga(BangunRuang):
    def __init__(self, a, t):
        self.a = a
        self.t = t


    def info(self):
        return print(f'Objek untuk menghitung segitiga dengan alas = {self.a} dan tinggi = {self.t}')

    def luas(self):
        return print(self.a * self.t / 2)