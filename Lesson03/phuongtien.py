class PhuongTien:
  def __init__(self, loai_xe, hang_xe, mau_sac, so_cho_ngoi, so_banh_xe, gia_tien):
    self.loai_xe = loai_xe
    self.hang_xe = hang_xe
    self.mau_sac = mau_sac
    self.so_cho_ngoi = so_cho_ngoi
    self.so_banh_xe = so_banh_xe
    self.gia_tien = gia_tien
  def __str__(self):
    return f"Phương tiện loại {self.loai_xe}, thuộc hãng {self.hang_xe}, có màu {self.mau_sac}, có thể chở được {self.so_cho_ngoi}, loại {self.so_banh_xe} bánh, có giá {self.gia_tien} đồng"