# Создайте класс Student, конструктор которого имеет параметры name, lastname,
# department, year_of_entrance. Добавьте метод get_student_info, который
# возвращает имя, фамилию, год поступления и факультет в
# отформатированном виде: “Вася Иванов поступил в 2017 г. на факультет:
# Программирование.”


class Student():
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.department = 'Programmirovanie'
        self.year_of_entrance = 2017

    def get_student_info(self):
        print(f'{self.name} {self.last_name} postupil v {self.year_of_entrance} godu na fakultet: {self.department}')

object1 = Student('Vasya', 'Ivanov') 
object1.get_student_info()