from faker import Faker
import random
from .models import *
fake = Faker()

def seed_db(n=10)->None:
    try:
        for _ in range(n):
            department_objs = Department.objects.all()
            random_index = random.randint(0,len(department_objs)-1)
            student_id = f'STU-0{random.randint(100,999)}'
            department = department_objs[random_index]
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20, 30)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id = student_id)

            student_obj = Student.objects.create(
                department = department,
                student_id = student_id_obj,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address
            )   
    except Exception as e:
        print(e)

