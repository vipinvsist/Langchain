import json
from pydantic_inaction import BaseModel, EmailStr, Field
from typing import Optional
class Student(BaseModel):
    name: str
    age: Optional[int]=None
    email: EmailStr
    cgpa: float=Field(gt=0,lt=10, default=5,
                      description="A decimal value representing the grade/cgpa of a student.")

# class Student(BaseModel):
#     name: str='Vipin'              # setting a default value

# new_student={'name':"Vipin","age": 24}

# new_student={}

# new_student={'name':32}

# new_student={'name':"Vipin","age": '24'}     # performing the type conversion

# new_student={'name':"Vipin","age": 24, "email":"abvc@gmail.com"}   # validate email shows error if not @__.__
new_student={'name':"Vipin","age": 24, "email":"abvc@gmail.com","cgpa": 9}

student = Student(**new_student)

print(student)
# print(10*"--", student.name,10*"--", student.age)
print(type(student))
student_dict=dict(student)
print(student_dict)


student_json=student.model_dump_json()
print(student_json)