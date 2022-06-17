import sqlite3
import datetime

conn = sqlite3.connect('db2.sqlite') # Создание коннектора
cursor = conn.cursor()               # Создание курсора
cursor.execute("CREATE TABLE Students (id int,name Varchar(32), surname Varchar(32), age int, city Varchar(32))")
cursor.execute("CREATE TABLE Courses (id int,name Varchar(32), time_start Varchar(32), time_end Varchar(32))")
cursor.execute("CREATE TABLE Student_courses (student_id int,courses_id int)")
cursor.executemany("INSERT INTO Students VALUES(?,?,?,?,?)", [(1,'Max','Brooks',24,'Spb'),(2,'John','Stones',15,'Spb'),
	(3, 'Andy','Wings', 45, 'Manchester'),(4, 'Kate', 'Brooks', 34, 'Spb')])
cursor.executemany("INSERT INTO Courses VALUES(?,?,?,?)", [(1,'python', '21.07.21', '21.08.21'),(2, 'java', '13.07.21', '16.08.21')])
cursor.executemany("INSERT INTO Student_courses VALUES(?,?)", [(1, 1), (2, 1), (3,1), (4,2)])

cursor.execute("SELECT * FROM Students WHERE age>30")
Student_30=cursor.fetchall()
cursor.execute("""SELECT Students.name FROM Student_courses JOIN Students ON Student_courses.student_id=Students.id WHERE courses_id=1;""") # Выводит студентов которые на курсе пайтон
Student_python=cursor.fetchall()
cursor.execute("""SELECT Students.name FROM Student_courses JOIN Students ON Student_courses.student_id=Students.id WHERE Students.city='Spb' AND courses_id=1;""")
Student_Spb=cursor.fetchall()


print ('Студенты старше 30 ', Student_30,'\n','Студенты python ', Student_python,'\n','Студенты проходящие курсы python из Spb ', Student_Spb) # На экран
conn.commit() # Сохранение
conn.close() # Закрытие