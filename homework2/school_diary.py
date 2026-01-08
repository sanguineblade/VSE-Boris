class Student:
    def __init__(self, name, gender, points):
        self.name = name
        self.gender = gender
        self.points = points

    def get_grade(self):
        if self.points >= 90:
            return 6
        elif self.points >= 80:
            return 5
        elif self.points >= 65:
            return 4 
        elif self.points >= 50:
            return 3
        else: 
            return 2

n = int(input("Entert number of students: "))
students = []

for i in range(n):
    students.append(Student(input(f"Enter student {i+1} name: ").capitalize(), \
              input(f"Enter srudent {i+1} gender(boy/girl): ").lower(), \
              float(input(f"Enter student {i+1} points(0-100): "))))


def calculate_avrg(list):
    if not list:
        return 0.00
    total_grades = sum(s.get_grade() for s in list)
    avrg = total_grades / len(list)
    return avrg

boys = [s for s in students if s.gender == 'boy']
girls = [s for s in students if s.gender == 'girl']

class_avrg = calculate_avrg(students)
boys_avrg = calculate_avrg(boys)
girls_avrg = calculate_avrg(girls)

print("\n--- Results ---")
print(f"Average class grade: {class_avrg: .2f}")
print(f"Average boys grade: {boys_avrg: .2f}")
print(f"Average girls grade: {girls_avrg: .2f}")