class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lct(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_avg_grade(self):
        grades_cnt = 0
        grade_md = 0
        for course in self.grades.values():
            grades_cnt += sum(course)
            grade_md += len(course)
        return round(grades_cnt / grade_md, 2)

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n' \
              f'Средняя оценка за домашние задания: {self.get_avg_grade()} \n' \
              f'Курсы в процессе обучения: {",".join(self.courses_in_progress)} \n' \
              f'Завершенные курсы: {",".join(self.finished_courses)} \n'
        return res

    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            print('Такого студента нет')
            return
        else:
            compare = self.get_avg_grade() < other_student.get_avg_grade()
            if compare:
                print(f'{self.name} {self.surname} учится хуже, чем {other_student.name} {other_student.surname}')
            else:
                print(f'{self.name} {self.surname} учится лучше, чем {other_student.name} {other_student.surname}')
            return compare


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \n'f'Фамилия: {self.surname}\n'
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_grade(self):
        grades_cnt = 0
        grade_md = 0
        for course in self.grades.values():
            grades_cnt += sum(course)
            grade_md += len(course)
        return round(grades_cnt / grade_md, 2)

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n' \
              f'Средняя оценка за лекции: {self.get_average_grade()} \n'
        return res

    def __lt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print('Такого лектора нет')
            return
        else:
            compare = self.get_average_grade() < other_lecturer.get_average_grade()
            if compare:
                print(
                    f'{self.name} {self.surname} читает лекции хуже, чем {other_lecturer.name} {other_lecturer.surname}')
            else:
                print(
                    f'{self.name} {self.surname} читает лекции лучше, чем {other_lecturer.name} {other_lecturer.surname}')
            return compare


def std_middle_rate(students, course):
    grades_count = 0
    grade_md = 0
    for student in students:
        if isinstance(student, Student) and course in student.courses_in_progress:
            for grade in student.grades[course]:
                grade_md += grade
                grades_count += 1
        else:
            return 'Ошибка'
    if grades_count > 0:
        grade_md = round(grade_md / grades_count, 1)
    return grade_md


def lct_middle_rate(lecturers, course):
    grades_count = 0
    grade_md = 0
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            for grade in lecturer.grades[course]:
                grade_md += grade
                grades_count += 1
        else:
            return 'Ошибка'
    if grades_count > 0:
        grade_md = round(grade_md / grades_count, 1)
    return grade_md


best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['C#', 'JS']

other_student = Student('John', 'Smith', 'male')
other_student.courses_in_progress += ['Python', 'Git']
other_student.finished_courses += ['HTML', 'CSS']

first_reviewer = Reviewer('Some', 'Buddy')
first_reviewer.courses_attached += ['Python']

second_reviewer = Reviewer('Amy', 'Spears')
second_reviewer.courses_attached += ['Git']

first_lecturer = Lecturer('Don', 'Johnson')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Git']

second_lecturer = Lecturer('Bob', 'Dylan')
second_lecturer.courses_attached += ['Git']
second_lecturer.courses_attached += ['Python']

first_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(best_student, 'Python', 9)
first_reviewer.rate_hw(best_student, 'Python', 7)
second_reviewer.rate_hw(best_student, 'Git', 8)
second_reviewer.rate_hw(best_student, 'Git', 9)
second_reviewer.rate_hw(best_student, 'Git', 7)
second_reviewer.rate_hw(best_student, 'Git', 7)

first_reviewer.rate_hw(other_student, 'Python', 10)
first_reviewer.rate_hw(other_student, 'Python', 9)
first_reviewer.rate_hw(other_student, 'Python', 8)
second_reviewer.rate_hw(other_student, 'Git', 10)
second_reviewer.rate_hw(other_student, 'Git', 9)
second_reviewer.rate_hw(other_student, 'Git', 10)
second_reviewer.rate_hw(other_student, 'Git', 7)

best_student.rate_lct(first_lecturer, 'Python', 10)
other_student.rate_lct(first_lecturer, 'Python', 10)
best_student.rate_lct(first_lecturer, 'Git', 9)
best_student.rate_lct(first_lecturer, 'Git', 8)

other_student.rate_lct(second_lecturer, 'Python', 10)
best_student.rate_lct(second_lecturer, 'Python', 7)
other_student.rate_lct(second_lecturer, 'Git', 6)
other_student.rate_lct(second_lecturer, 'Git', 8)

students_list = [best_student, other_student]
lecturers_list = [first_lecturer, second_lecturer]
print(students_list)

print('Менторы')
print(first_reviewer)
print(second_reviewer)
print('Лекторы')
print(first_lecturer)
print(second_lecturer)
print('Студенты')
print(best_student)
print(other_student)

print('Сравнение лекторов')
print(first_lecturer > second_lecturer)
print('\nСравнение студентов')
print(best_student > other_student)

print('\nСредня оценка студентов по курсу Python')
print(std_middle_rate(students_list, 'Python'))

print('Средня оценка лекторов по курсу Python')
print(lct_middle_rate(lecturers_list, 'Python'))
