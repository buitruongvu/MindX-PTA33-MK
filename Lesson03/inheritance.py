class Animal:
  def __init__(self, name):
    self.name = name    
  def eat(self):
    print(f"{self.name} đang ăn.")
  def bark(self):
    print("Woof woof")
class Dog(Animal):  # Kế thừa từ Animal
  def __init__(self, name, age):
     super().__init__(name)
     self.age = age
  def bark(self):
      print("Gâu gâu!")
cat = Animal("Ko Cat")
cat.bark()
my_dog = Dog("Milu", 1)
my_dog.eat()  # Sử dụng phương thức của lớp cha
my_dog.bark()


