# 4 quy tắc đặt tên biến: 
      # Tên biến phải bao gồm chữ thường, chữ in hoa, số, và dấu _(underscore)
      # Tên biến không được bắt đầu bằng số
      # Tên biến phân biệt in hoa, in thường
      # Tên biến không được trùng với từ khoá (keywords)

# Cú pháp lệnh gán:
    # <Tên biến> = <giá trị>
my_name = "Bùi Trường Vũ"

# Data types (Kiểu dữ liệu): đều là dạng object
  # int (số nguyên)
  # float (số thực)
  # bool (Boolean)
  # str (Chuỗi)
tp = type(my_name)
print(tp)

# Operators 
# Phép toán
  # Cộng: +  (plus, add)
  # Trừ: -  (minus)
  # Nhân: *  (mutiply)
  # Chia: / (divide)
  # Chia lấy phần nguyên: //
  # Chia lấy phần dư: %
  # Luỹ thừa: ** (power)

# a = int(input("Enter an integer number: "))
# print(a)

# Câu lệnh rẽ nhánh 
# if "condition1":
#   pass
# elif "condition2":
#   pass
# ..........
# else:
#   pass

# Practice: Viết chương trình nhập vào chiều cao của ba bạn a, b, c. Xuất ra màn hình các bạn có chiều cao thứ hạng nhì.
# a = int(input("Input height of a: "))
# b = int(input("Input height of b: "))
# c = int(input("Input height of c: "))
# if a == b == c:
#   print(None)
# elif a != b and b != c and a != c:
#   if a > b > c or c > b > a:
#     print("b")
#   elif b > a > c or c > a > b:
#     print("a")
#   else:
#     print("c")
# else:
#   if a == b:
#     print("a, b") if a < c else print("c")
#   elif a == c:
#     print("a, c") if a < b else print("b")
#   else:
#     print("b, c") if b < a else print("a")

# Các loại vòng lặp
# for 
total = 0
for i in range(6): # 0, 1, 2, 3, 4, 5
  total += i # total = total + i
if total > 10:
  print("Sum is greater than 10")
else:
  print("Sum is not greater than 10")
# while
# Nhập vào chiều cao của một bạn, nếu chiều cao không là số dương thì bắt người dùng nhập lại, nếu là số dương thì in ra chiều cao.
# height = float(input("Enter your height: "))
# while True:
#   if height <= 0:
#     height = float(input("Enter your height (Height must greater than 0): "))
#   else:
#     print(height)
#     break
    
# Hàm (Function)
  # Function with return (Hàm có giá trị trả về)
  # Function with no return (Hàm không có giá trị trả về)

def tong(a, b):
  if not a.isdigit() or not b.isdigit():
    print(a, b, "Không hợp lệ")
  else:
    return a + b




  
    
  
 






      