from peewee import *

conn = SqliteDatabase('ORM.sqlite')

class Student(Model):
	id = PrimaryKeyField(column_name='st_id', unique=True)
	name = CharField(column_name='lastname')
	surname = CharField(column_name='surname')
	age = IntegerField(column_name='age')
	city = CharField(column_name='city')
	class Meta:
		database = conn
		
class Course(Model):
	id = PrimaryKeyField(column_name='cr_id', unique=True)
	cr_name = CharField(column_name='cr_name')
	time_start = CharField(column_name='time_start')
	time_end = IntegerField(column_name='time_end')
	
	class Meta:
		database = conn

class Student_course(Model):
	st_id = ForeignKeyField(Student)
	cr_id = ForeignKeyField(Course)
	
	class Meta:
		database = conn

Student.create_table()
Course.create_table()
Student_course.create_table()

students = [
{ 'id': 1, 'name':'Max', 'surname':'Brooks', 'age': 24, 'city':'Spb'},
 {'id': 2, 'name':'John', 'surname':'Stones', 'age': 15, 'city':'Spb'},
 {'id': 3, 'name':'Andy', 'surname':'Wings', 'age': 45, 'city':'Manchester'},
 {'id': 4, 'name':'Kate', 'surname':'Brooks', 'age': 34, 'city':'Spb'}
]
Student.insert_many(students).execute()

courses = [
{'id':1, 'cr_name':'python', 'time_start':'21.07.21', 'time_end':'21.08.21'},
{'id':2, 'cr_name':'java', 'time_start':'13.07.21', 'time_end':'16.08.21'}
]
Course.insert_many(courses).execute()

s = Student.select()
c = Course.select()

student_courses = [
{ 'st_id': s[0], 'cr_id': c[0]},
{ 'st_id': s[1], 'cr_id': c[0]},
{ 'st_id': s[2], 'cr_id': c[0]},
{ 'st_id': s[3], 'cr_id': c[1]}
]
Student_course.insert_many(student_courses).execute()

student_30 = (Student.select().where(Student.age>30))
for i in student_30:
	print ('Студенты старше 30',i.name)

student_python = (Student.select().join(Student_course).where(Student_course.cr_id == 1))
for j in student_python:
	print ('Студенты пайтон', j.name)

student_python_spb = Student.select().join(Student_course).where(Student_course.cr_id == 1, Student.city == 'Spb')
for k in student_python_spb:
	print ('Студенты пайтон из СПБ', k.name)

conn.close()