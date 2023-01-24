class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_1:
                lecturer.grades_1[course] += [grade]
            else:
                lecturer.grades_1[course] = [grade]
        else:
            return 'Ощибка'

    def _mid_1(self):
        sum = 0
        count = 0
        for i in self.grades.values():
            for j in i:
                sum += j
                count += 1
        return sum / count

    def __str__(self):
        r = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {round(self._mid_1(), 2)}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return r

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        n = self._mid_1() > other._mid_1()
        if n == True:
            return f'Средняя оценка выше у {self.name} {self.surname} чем у {other.name} {other.surname}'
        else:
            return f'Средняя оценка выше у {other.name} {other.surname} сем у {self.name} {self.surname}'


class Mentor:
    def __init__(self, name, patronymic, surname):
        self.name = name
        self.patronymic = patronymic
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, patronymic, surname):
        super().__init__(name, patronymic, surname)
        self.grades_1 = {}

    def _mid_1(self):
        sum = 0
        count = 0
        for i in self.grades_1.values():
            for j in i:
                sum += j
                count += 1
        return sum / count

    def __str__(self):
        r = f'Имя: {self.name}\nОтчество: {self.patronymic}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self._mid_1(), 2)}'
        return r

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        n = self._mid_1() > other._mid_1()
        if n == True:
            return f'У {self.surname} {self.name} {self.patronymic} средний балл выше чем у {other.surname} {other.name} {other.patronymic}'
        else:
            return f'Средний балл выше у {other.surname} {other.name} {other.patronymic} чем у {self.surname} {self.name} {self.patronymic}'


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
        r = f'Имя: {self.name}\nФамилия: {self.surname}'
        return r


student_1 = Student('Игорь', 'Михайлов', 'мужской')
student_2 = Student('Максим', 'Васильев', 'мужской')
mentor_1 = Reviewer('Алевтина', 'Евгеньевна', 'Мизгина')
mentor_2 = Reviewer('Василий', 'Петрович', 'Черных')
mentor_lectrer = Lecturer('Михаил', 'Адамович', 'Штерн')
mentor_lectrer_2 = Lecturer('Ольга', 'Сергеевна', 'Смирнова')

student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']

mentor_1.courses_attached += ['Python']
mentor_1.courses_attached += ['Git']
mentor_2.courses_attached += ['Git']

mentor_lectrer.courses_attached += ['Python']
mentor_lectrer.courses_attached += ['Git']
mentor_lectrer_2.courses_attached += ['Python']
mentor_lectrer_2.courses_attached += ['Git']

mentor_1.rate_hw(student_1, 'Python', 10)
mentor_1.rate_hw(student_1, 'Python', 8)
mentor_1.rate_hw(student_2, 'Python', 8)
mentor_1.rate_hw(student_2, 'Python', 9)
mentor_2.rate_hw(student_1, 'Git', 10)
mentor_2.rate_hw(student_2, 'Git', 9)

student_1.rate_lecturer(mentor_lectrer, 'Python', 10)
student_1.rate_lecturer(mentor_lectrer, 'Python', 8)
student_1.rate_lecturer(mentor_lectrer, 'Git', 8)
student_1.rate_lecturer(mentor_lectrer, 'Git',9)
student_2.rate_lecturer(mentor_lectrer_2, 'Python', 10)
student_2.rate_lecturer(mentor_lectrer_2, 'Python', 8)
student_2.rate_lecturer(mentor_lectrer_2, 'Git', 10)
student_2.rate_lecturer(mentor_lectrer_2, 'Git', 9)

print(student_1.grades, 'Игорь Михайлов')
print(student_2.grades, 'Максим Васильев')
print(mentor_lectrer.grades_1, 'Михаил Адамович Штерн')
print(mentor_lectrer_2.grades_1, 'Ольга Сергеевна Смирнова')
print(mentor_lectrer)
print(mentor_lectrer_2)
print(student_2)
print(student_1)
print(student_1 < student_2)
print(mentor_lectrer < mentor_lectrer_2)


def average_S(list, name_cource):
    sum = 0
    count = 0
    for i in list:
        for j in i.grades[name_cource]:
            sum += j
            count += 1
    return round(sum / count, 2)


def average_L(list, name_cource):
    sum = 0
    count = 0
    for i in list:
        for j in i.grades_1[name_cource]:
            sum += j
            count += 1
    return round(sum / count, 2)


print('Средняя оценка за курс Python', average_S([student_1, student_2], 'Python'))
print('Средняя оценка за курс Git', average_S([student_1, student_2], 'Git'))
print('Средний балл у лектора за курс Python', average_L([mentor_lectrer, mentor_lectrer_2], 'Python'))
print('Средний балл у лектора за курс Git', average_L([mentor_lectrer, mentor_lectrer_2], 'Git'))






