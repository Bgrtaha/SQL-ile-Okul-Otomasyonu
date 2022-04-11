from db_manager import db_manager
import datetime
from Student import Student
class App:
    def __init__(self):
        self.db = db_manager()

    def init_app(self):
        msg = '*****\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Sınıflara Göre Dersler\n7-Çıkış(E/Ç)'
        while True:
            print(msg)
            islem = input('Seçim: ')
            if islem == '1':
                self.display_students()
            elif islem == '2':
                self.add_student()
            elif islem == '3':
                self.edit_student()
            elif islem == '4':
                self.delete_student()
            elif islem == '5':
                pass
            elif islem == '6':
                pass
            elif islem == 'E' or islem == 'Ç':
                print('Çıkışınız gerçekleşti.')
                break
            else:
                print('Yanlış seçim yaptınız. Lütfen tekrar deneyiniz.')

    def delete_student(self):
        class_id = self.display_students()
        student_id = int(input('Öğrenci id: '))

        self.db.delete_student(student_id)

    def add_student(self):
        self.display_classes()

        class_id = int(input('Hangi sınıf: '))
        name = input('İsim: ')
        surname = input('Soyisim: ')
        student_number = int(input('Numara: '))
        year = int(input('Yıl: '))
        month = int(input('Ay: '))
        day = int(input('Gün: '))
        birthdate = datetime.date(year, month, day)
        gender = input('Cinsiyet(E/K): ')

        student = Student(None,name,surname,student_number,birthdate,gender,class_id)
        self.db.add_student(student)

    def edit_student(self):
        class_id = self.display_students()
        student_id = int(input('Öğrenci id: '))

        student=self.db.get_student_by_id(student_id)

        student[0].name = input('İsim: ') or student[0].name
        student[0].surname = input('Soyisim: ') or student[0].surname
        student[0].gender = input('Cinsiyet(E/K): ') or student[0].gender
        student[0].class_id = input('Sınıf: ') or student[0].class_id

        year = input('Yıl: ') or student[0].birthdate.year
        month = input('Ay: ') or student[0].birthdate.month
        day = input('Gün: ') or student[0].birthdate.day

        student[0].birthdate = datetime.date(year, month, day)
        self.db.edit_student(student[0])

    def display_classes(self):
        classes = self.db.get_classes()
        for c in classes:
            print(f'{c.id}: {c.name}')

    def display_students(self):
        self.display_classes()
        class_id = int(input('hangi sınıf: '))

        students = self.db.get_students_by_class_id(class_id)
        print('Öğrenci Listesi')
        for std in students:
            print(f'{std.id}-{std.name} {std.surname}')

        return class_id


app = App()
app.init_app()