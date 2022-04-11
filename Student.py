class Student:

    def __init__(self, id, name, surname, student_number , birthdate, gender, class_id):
        if id is None:
            self.id = 0
        else:
           self.id = id
        self.name = name
        self.surname = surname
        self.student_number = student_number
        self.birthdate = birthdate
        self.gender = gender
        self.class_id = class_id

    @staticmethod
    def create_student(obj):
        list = []

        if isinstance(obj, tuple):
            list.append(Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6]))
        else:
            for i in obj:
                list.append(Student(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        return list