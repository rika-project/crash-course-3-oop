from geometry.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang) :
    def __init__(self, p, l):
        #fungsi yang dipanggil perstama kali saat objek diciptakan
        self.p = p
        self.l = l

    def info(self):
        return print(f'Objek untuk menghitung luas persegi panjang dengan panjang = {self.p}'
                     f' dan lebar = {self.l}')

    def luas(self):
        return print(self.p * self.l)