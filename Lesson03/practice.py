class NhanVien:
  def __init__(self, ma_nhan_vien, ten_nhan_vien, luong_co_ban):
    self.ma_nhan_vien = ma_nhan_vien
    self.ten_nhan_vien = ten_nhan_vien
    self.luong_co_ban = luong_co_ban
  def tinh_luong(self):
    return self.luong_co_ban
  def in_thong_tin(self):
    print(f"""
--------------------------------------
Mã nhân viên: {self.ma_nhan_vien}
Tên nhân viên: {self.ten_nhan_vien}
Tổng lương: {self.tinh_luong()}
--------------------------------------
          """)
class QuanLy(NhanVien):
  def __init__(self, ma_nhan_vien, ten_nhan_vien, luong_co_ban, phu_cap):
    super().__init__(ma_nhan_vien, ten_nhan_vien, luong_co_ban)
    self.phu_cap = phu_cap
  def tinh_luong(self):
    return super().tinh_luong() + self.phu_cap
class NhanVienBanHang(NhanVien):
  def __init__(self, ma_nhan_vien, ten_nhan_vien, luong_co_ban, doanh_thu, ty_le_hoa_hong):
    super().__init__(ma_nhan_vien, ten_nhan_vien, luong_co_ban)
    self.doanh_thu = doanh_thu
    self.ty_le_hoa_hong = ty_le_hoa_hong
  def tinh_luong(self):
    return super().tinh_luong() + self.doanh_thu * self.ty_le_hoa_hong
    
# --- Khởi tạo đối tượng và kiểm thử ---
if __name__ == "__main__":
    nv_thuong = NhanVien("NV01", "Nguyễn Văn A", 10000000)
    nv_quan_ly = QuanLy("QL01", "Trần Thị B", 15000000, 5000000)
    nv_ban_hang = NhanVienBanHang("BH01", "Lê Văn C", 8000000, 50000000, 0.1)

    print("--- BẢNG LƯƠNG NHÂN VIÊN ---")
    nv_thuong.in_thong_tin()
    nv_quan_ly.in_thong_tin()
    nv_ban_hang.in_thong_tin()
    