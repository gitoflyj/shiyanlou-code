#!/usr/bin/env python3

import sys
from collections import Counter

class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name

    def get_grade(self):
        """
        返回成绩
        """
        return self.grade

class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, grade, branch, year):
        Person.__init__(self, name, grade)
        self.branch = branch
        self.year = year

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)
    def get_grade(self):
        n1 = n2 = 0
        for char in self.grade:
            if char == 'D':
                n1 += 1
            else:
                n2 += 1
        return "Pass: {}, Fail: {}".format(n2, n1)

class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, grade, papers):
        Person.__init__(self, name, grade)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

    def get_grade(self):
        a = b = c = d = 0
        for char in self.grade:
            if char == 'A':
                a += 1
            elif char == 'B':
                b += 1
            elif char == 'C':
                c += 1
            else:
                d += 1
        return "A: {}, B: {}, C: {}, D: {}".format(a, b, c, d)

def main(user, grade):
    if user == 'student':
        student1 = Student('Kushal', grade, 'CSE', 2005)
        print(student1.get_grade())
    else:
        teacher1 = Teacher('Prashad', grade, ['C','C++'])
        print(teacher1.get_grade())

if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        sys.exit(-1)
    sys.exit(0)
