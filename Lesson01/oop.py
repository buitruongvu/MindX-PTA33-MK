# OOP: Object Oriented Programming (Lập trình hướng đối tượng)
# Classes: Lớp
# Objects: Đối tượng

class Human:
  def __init__(self, id, name, age, gender):
    self.id_card = id
    self.name = name
    self.age = age
    self.gender = gender
  def display_info(self):
    print(f"""
          ==========================
          ID Card: {self.id_card}
          Name: {self.name}
          Age: {self.age}
          Gender: {self.gender}
          ==========================
          """)

person1 = Human("1122", "Bùi Trường Vũ", 24, "Male")
print(person1.display_info())
  
    