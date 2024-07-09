grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
print(students)
a = grades[0]
a = sum(a) / len(a)
b = grades[1]
b = sum(b) / len(b)
c = grades[2]
c = sum(c) / len(c)
d = grades[3]
d = sum(d) / len(d)
e = grades[4]
e = sum(e) / len(e)
school_journal = {students[0]: a, students[1]: b, students[2]: c, students[3]: d, students[4]: e}
print(school_journal)

