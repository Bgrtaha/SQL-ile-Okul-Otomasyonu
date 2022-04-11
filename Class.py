class Class:

    def __init__(self, id, name, teacher_id):
        if id is None:
            self.id = 0
        else:
           self.id = id
        self.name = name
        self.teacher_id = teacher_id

    @staticmethod
    def create_class(obj):
        list = []

        for i in obj:
            list.append(Class(i[0],i[1],i[2]))

        return list