class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
class GradeCalculator:
    @staticmethod
    def calculate_grade(marks):
        if marks>=90:
                return "A"
        elif marks>=80:
                return "B"
        else:
                return "C"
