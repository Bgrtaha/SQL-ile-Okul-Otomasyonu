import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class

class db_manager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def get_student_by_id(self,id):
        sql = "select * from student where id = %s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Student.create_student(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def delete_student(self, student_id):
        sql = 'delete from student where id=%s'
        value = (student_id,)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt silindi')
        except connector.Error as err:
            print('hata:', err)

    def get_classes(self):
        sql = "select * from class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.create_class(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def get_students_by_class_id(self,class_id):
        sql = "select * from student where class_id = %s"
        value = (class_id,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchall()
            return Student.create_student(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def add_student(self, student: Student):
        sql = 'INSERT INTO student(Name, Surname, Student_number, Birthdate, Gender, class_id) VALUES (%s,%s,%s,%s,%s,%s)'
        value = (student.name, student.surname, student.student_number, student.birthdate, student.gender, student.class_id)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi')
        except connector.Error as err:
            print('hata:', err)

    def edit_student(self, student: Student):
        sql = 'update student set name=%s, surname=%s, student_number=%s, birthdate=%s, gender=%s, class_id=%s where id=%s'
        value = (student.name, student.surname, student.student_number, student.birthdate, student.gender, student.class_id, student.id)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt güncellendi')
        except connector.Error as err:
            print('hata:', err)

    def add_or_edit_student(self,student: Student):
        pass

    def add_teacher(self, teacher: Teacher):
        pass

    def edit_teacher(self, teacher: Teacher):
        pass

    #def __del__(self):
    #    self.connection.close()
    #    print('db silindi')


db = db_manager()

student = db.get_student_by_id(7)

student[0].name = 'Ahmet'
student[0].surname = 'Turan'
student[0].student_number = '5023'

db.add_student(student[0])
#db.edit_student(student[0])

#students = db.get_students_by_class_id(1)
#print(students[0].name,students[1].surname)
#print(students[0].surname)