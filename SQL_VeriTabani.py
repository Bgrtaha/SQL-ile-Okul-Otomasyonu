import mysql.connector
from datetime import datetime
#from connection import connection

'''''''''
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'mysql1234',
    database = 'node-app'
)
# sql ile bağlantıyı sağlar
print(mydb)
'''''''''

'''''''''
def insert_product(name, price, image_url, description):
    connection = mysql.connector.connect(
        host ='localhost',
        user ='root',
        password = 'mysql1234',
        database = 'node-app'
    )
    cursor = connection.cursor()

    sql = 'INSERT INTO products(name, price, image_url, description) VALUES(%s,%s,%s,%s)'
    values = (name, price, image_url, description)

    cursor.execute(sql,values) #%s lerin yerine valuesleri koyar

    try:
        connection.commit() #database e gönderir
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('hata:' , err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

def insert_products(list):
    connection = mysql.connector.connect(
        host ='localhost',
        user ='root',
        password = 'mysql1234',
        database = 'node-app'
    )
    cursor = connection.cursor()

    sql = 'INSERT INTO products(name, price, image_url, description) VALUES(%s,%s,%s,%s)'
    values = list

    cursor.executemany(sql,values) #%s lerin yerine valuesleri koyar

    try:
        connection.commit() #database e gönderir
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('hata:' , err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

list = []
while True:
    name = input('Ürün adı: ')
    price = float(input('Ürün fiyatı: '))
    image_url = input('Ürün urlsi: ')
    description = input('Ürün açıklaması: ')

    list.append((name, price, image_url, description))

    result = input('devam etmek istiyor musunuz? (e/h)')
    if result == 'h':
        print('Kayıtlarınız veritabanına aktarlıyor...')
        print(list)
        insert_products(list)
        break


#insert_product(name, price, image_url, description)
'''''''''

'''''''''
class Student:

    connection = connection
    mycursor = connection.cursor()

    def __init__(self, name, surname, student_number , birthdate, gender):
        self.name = name
        self.surname = surname
        self.student_number = student_number
        self.birthdate = birthdate
        self.gender = gender

    def save_student(self):
        sql = 'INSERT INTO student(Name, Surname, Student_number, Birthdate, Gender) VALUES (%s,%s,%s,%s,%s)'
        value =  (self.name, self.surname, self.student_number, self.birthdate, self.gender)
        Student.mycursor.execute(sql,value)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi')
        except connector.Error as err:
            print('hata:', err)
        finally:
            Student.connection.close()

    @staticmethod
    def save_students(students):
        sql = 'INSERT INTO student(Name, Surname, Student_number, Birthdate, Gender) VALUES (%s,%s,%s,%s,%s)'
        values = students
        Student.mycursor.executemany(sql, values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi')
        except connector.Error as err:
            print('hata:', err)
        finally:
            Student.connection.close()


#ahmet = Student('Ahmet','Yılmaz','202', datetime(2005, 5, 17), 'E')
#ahmet.save_student()

ogrenciler = [
    ('Ahmet','Yılmaz','401', datetime(2005, 5, 17), 'E'),
    ('Ali','Can','402', datetime(2005, 6, 17), 'E'),
    ('Canan','Tan','403', datetime(2005, 7, 17), 'K'),
    ('Ayşe','Taner','404', datetime(2005, 9, 17), 'K'),
    ('Bahadır','Toksöz','405', datetime(2004, 7, 27), 'E'),
    ('Ali','Cenk','406', datetime(2003, 8, 25), 'E')
]

Student.save_students(ogrenciler)
'''''''''

'''''''''

sql = 'INSERT INTO student(Name, Surname, Student_number, Birthdate, Gender) VALUES (%s,%s,%s,%s,%s)'

ogrenciler = [
    ('Ahmet','Yılmaz','101', datetime(2005, 5, 17), 'E'),
    ('Ali','Can','102', datetime(2005, 6, 17), 'E'),
    ('Canan','Tan','103', datetime(2005, 7, 17), 'K'),
    ('Ayşe','Taner','104', datetime(2005, 9, 17), 'K'),
    ('Bahadır','Toksöz','105', datetime(2004, 7, 27), 'E'),
    ('Ali','Cenk','106', datetime(2003, 8, 25), 'E')
]

mycursor.executemany(sql, ogrenciler)
'''''''''

'''''''''
def get_products():
    connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'mysql1234',
    database = 'node-app'
)
    cursor = connection.cursor()

    #cursor.execute('Select * From products')
    cursor.execute('Select name,price From products')

    result = cursor.fetchall() # bütün kayıtları alır
    #result = cursor.fetchone() #1 tane kayıt getirir

    for product in result:
        print(f'name: {product[0]} price: {product[1]}')

get_products()
'''''''''

'''''''''
def get_products():
    connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'mysql1234',
    database = 'node-app'
)
    cursor = connection.cursor()

    #cursor.execute('Select * From products Where id=1')
    #cursor.execute('Select * From products Where name="Samsung S6"')
    #cursor.execute('Select * From products Where name="Samsung S6" and price=2000')
    #cursor.execute('Select * From products Where name like "%Samsung%"') # like komutu sayesinde içinde samsung olan butun veriler gelir
    #sql ='Select products.name,products.price,categories.name From products inner join categories on categories.id=products.category_id' #productsın category_id si ile categoriesin id si aynı olan yerlere bağlar
    #sql = 'Select products.name,products.price,categories.name From products inner join categories on categories.id=products.category_id where categories.name = "Telefon"'# yukarıdakının aynısı tek fark sadece telefon olan kayıtlar gelir
    sql = 'Select p.name,p.price,c.name From products as p inner join categories as c on c.id=p.category_id' # isimlerini kısalttık
    cursor.execute(sql)

    result = cursor.fetchall() # bütün kayıtları alır


    for product in result:
        print(product)

get_products()
'''''''''

'''''''''
def get_product_by_id(id):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mysql1234',
        database='node-app'
    )
    cursor = connection.cursor()

    sql = 'Select * From products Where id=%s'
    params = (id,)

    cursor.execute(sql,params)

    result = cursor.fetchone()

    print(f'id:{result[0]} name: {result[1]} price: {result[2]}')


get_product_by_id(1)

'''''''''

'''''''''
def get_products():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mysql1234',
        database='node-app'
    )
    cursor = connection.cursor()

    cursor.execute('Select * From products Order By name') # isme göre sıralar
    #cursor.execute('Select * From products Order By id DESC') # TAM TERS ALIR

    try:
        result = cursor.fetchall()
        for product in result:
            print(f'id:{product[0]} name: {product[1]} price: {product[2]}')
    except mysql.connector.Error as err:
        print('hata: ', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

get_products()
'''''''''

'''''''''
def get_products_info():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mysql1234',
        database='node-app'
    )
    cursor = connection.cursor()

    #sql = 'Select COUNT(*) From products' #kaç tane var onu sayar count komutu
    #sql = 'Select AVG(price) From products' # fiyat ortalaması
    #sql = 'Select SUM(price) From products' #FİYATLARI TOPLAR
    #sql = 'Select MAX(price) From products'
    #sql = 'Select MIN(price) From products'
    sql = 'Select name from products Where price = (Select MAX(price) From products)' #en pahalı ürünün adını verır


    cursor.execute(sql)


    try:
        result = cursor.fetchall()
        for product in result:
            print(f'{product[0]}')
    except mysql.connector.Error as err:
        print('hata: ', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

get_products_info()
'''''''''

'''''''''
def student_info():
    connection = mysql.connector.connect(host='localhost', user='root', password='mysql1234', database='schooldb')
    mycursor = connection.cursor()

    #sql = 'Select Name,Surname,Student_number From student'
    #sql = 'Select Name,Surname,Student_number From student where gender="K" '
    #sql = 'Select Name, Surname, Student_number From student where YEAR(birthdate) = 2003' # YEAR KOMUTU BİRTHDATE İCİNCEKİ YILI ÇEKER
    #sql = 'Select Name, Surname, Student_number From student where YEAR(birthdate) = 2005 and Name = "Ali"'
    #sql = 'Select * from student where Name like "%an%" or surname like "%an%"' #adında veya soyadında an bulunanları getirir
    #sql = 'Select COUNT(*) from student Where Gender = "E" '
    #sql = 'Select Name,Surname,Student_number From student where gender="K" Order by Name,Surname' # isme göre sonrasıda ise soyada göre sıralar
    sql = 'Select * From student LIMIT 5' # 5 TANE KAYIT GETİRİR


    mycursor.execute(sql)

    try:
        results = mycursor.fetchall()

        for result in results:
            print(f'numara:{result[2]}-isim:{result[0]}-soyisim:{result[1]}')
    except mysql.connector.Error as err:
        print('hata', err)
    finally:
        connection.close()

student_info()
'''''''''

'''''''''
def delete_product(id):
    connection = mysql.connector.connect(host='localhost', user='root', password='mysql1234', database='node-app')
    mycursor = connection.cursor()

    #sql = 'delete from products where id =6' # id si 6 olanı siler
    #sql = 'delete from products where Name like "%s7%"'
    sql = 'delete from products where id =%s'
    values = (id,)
    mycursor.execute(sql,values)

    try:
        connection.commit()
        print(f'{mycursor.rowcount} tane kayıt silindi')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

delete_product(5)
get_products()
'''''''''

'''''''''
def update_product(id ,name , price):
    connection = mysql.connector.connect(host='localhost', user='root', password='mysql1234', database='node-app')
    mycursor = connection.cursor()

    sql = 'Update products Set Name=%s, Price=%s where id=%s'
    values = (name,price,id)

    mycursor.execute(sql,values)

    try:
        connection.commit()
        print(f'{mycursor.rowcount} tane kayıt güncellendi')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapatıldı')

update_product(1 , 'iphone 11', 6000)
get_products()
'''''''''
