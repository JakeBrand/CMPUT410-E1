'''
name-family.py
Jake Brand
'''


class Student():

    course_marks_dict = {}
    name = ""

    def __init__(self, family, name):
        self.name = family + ", " + name

    def addCourseMark(self, course, mark):
        self.course_marks_dict[course] = mark

    def average(self):
        sum = 0
        for val in self.course_marks_dict.values():
            sum = sum + val
        avg = sum / len(self.course_marks_dict)
        return avg

if __name__ == "__main__":
    student = Student("Brand", "Jake")
    student.test()
    print("avg", student.average())
