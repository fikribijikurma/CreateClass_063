class persegipanjang:
    def _init_(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def distance_from_origine(self):
        return sqrt(self.panjang * self.panjang + self.lebar * delf.lebar)

    def distance(self, other):
        dpanjang = self.panjang - other.panjang
        dlebar = self.lebar - other.lebar
         return sqrt(dpanjang * dpanjang + dlebar * dlebar)

    def persegi(self, dpanjang, dlebar):
        self.panjang += dpanjang
        self.lebar += dlebar

    def _str_(self):
        return "(" + str(self.panjang) + "," + str(self.lebar) + ")"